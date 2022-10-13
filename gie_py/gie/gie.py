import enum
from typing import Optional, Union, Any, Coroutine

import aiohttp as aiohttp
import pandas as pd

from gie.agsi_mappings import (
    AGSIStorage,
    lookup_storage_agsi,
    lookup_company,
    AGSICompany,
    AGSICountry,
    lookup_country_agsi,
)
from gie.alsi_mappings import (
    ALSITerminal,
    lookup_terminal,
    ALSILSO,
    lookup_lso,
    ALSICountry,
    lookup_country_alsi,
)
from gie.exceptions import ApiError, NoMatchingDataError


class APIType(str, enum.Enum):
    AGSI = "https://agsi.gie.eu/api/data/"
    ALSI = "https://alsi.gie.eu/api/data/"


class GieRawClient:
    def __init__(self, api_key: str, session: Optional[aiohttp.ClientSession] = None):
        self.api_key = api_key
        self.session = session

        if not self.session:
            self.session = aiohttp.ClientSession(
                raise_for_status=True, headers={"x-key": self.api_key}
            )

    @property
    def api_key(self):
        return self.__api_key

    @api_key.setter
    def api_key(self, value):
        if not value:
            raise ApiError("API token is missing!")
        self.__api_key = value

    async def _fetch(
            self,
            url: str,
            token: APIType,
            start: Union[pd.Timestamp, str],
            end: Union[pd.Timestamp, str],
    ):
        start if type(start) == pd.Timestamp else pd.Timestamp(start)
        end if type(end) == pd.Timestamp else pd.Timestamp(end)

        async with self.session.get(
                token.value + url, params={"from": start, "till": end}
        ) as resp:
            return await resp.json()

    async def query_gas_storage(
            self,
            storage: Union[AGSIStorage, str],
            start: Union[pd.Timestamp, str],
            end: Union[pd.Timestamp, str],
    ) -> Coroutine[Any, Any, None]:
        storage = lookup_storage_agsi(storage)
        return self._fetch(storage.get_url(), APIType.AGSI, start=start, end=end)

    async def query_gas_company(
            self,
            company: Union[AGSICompany, str],
            start: Union[pd.Timestamp, str],
            end: Union[pd.Timestamp, str],
    ) -> Coroutine[Any, Any, None]:
        company = lookup_company(company)
        return self._fetch(company.get_url(), APIType.AGSI, start=start, end=end)

    async def query_gas_country(
            self,
            country: Union[AGSICountry, str],
            start: Union[pd.Timestamp, str],
            end: Union[pd.Timestamp, str],
    ) -> Coroutine[Any, Any, None]:
        country = lookup_country_agsi(country)
        return self._fetch(country.get_url(), APIType.AGSI, start=start, end=end)

    def query_lng_terminal(
            self,
            terminal: Union[ALSITerminal, str],
            start: Union[pd.Timestamp, str],
            end: Union[pd.Timestamp, str],
    ) -> Coroutine[Any, Any, None]:
        terminal = lookup_terminal(terminal)
        return self._fetch(terminal.get_url(), APIType.ALSI, start=start, end=end)

    async def query_lng_lso(
            self,
            lso: Union[ALSILSO, str],
            start: Union[pd.Timestamp, str],
            end: Union[pd.Timestamp, str],
    ) -> Coroutine[Any, Any, None]:
        lso = lookup_lso(lso)
        return self._fetch(lso.get_url(), APIType.ALSI, start=start, end=end)

    async def query_lng_country(
            self,
            country: Union[ALSICountry, str],
            start: Union[pd.Timestamp, str],
            end: Union[pd.Timestamp, str],
    ) -> Coroutine[Any, Any, None]:
        country = lookup_country_alsi(country)
        return self._fetch(country.get_url(), APIType.ALSI, start=start, end=end)

    async def close_session(self) -> None:
        """Close the session."""
        if self.session:
            await self.session.close()


class GiePandasClient(GieRawClient):
    def agsi_to_dataframe(self, data):
        data = data.json()
        df = pd.DataFrame(data=data).drop(columns=['code', 'url', 'info'])

        if not df:
            raise NoMatchingDataError

        df['gasDayStart'] = pd.to_datetime(df['gasDayStart'])
        df = df.set_index('gasDayStart')
        return df

    def query_gas_storage(self, storage: Union[AGSIStorage, str],
                          start: Union[pd.Timestamp, str], end: Union[pd.Timestamp, str]) -> pd.DataFrame:
        return self.agsi_to_dataframe(
            super().query_gas_storage(storage=storage, start=start, end=end)
        )

    def query_gas_company(self, company: Union[AGSIStorage, str],
                          start: Union[pd.Timestamp, str], end: Union[pd.Timestamp, str]) -> pd.DataFrame:
        return self.agsi_to_dataframe(
            super().query_gas_company(company=company, start=start, end=end)
        )

    def query_gas_country(self, country: Union[AGSICountry, str],
                          start: Union[pd.Timestamp, str], end: Union[pd.Timestamp, str]) -> pd.DataFrame:
        return self.agsi_to_dataframe(
            super().query_gas_country(country=country, start=start, end=end)
        )

    def query_lng_terminal(self, terminal: Union[ALSITerminal, str],
                           start: Union[pd.Timestamp, str], end: Union[pd.Timestamp, str]) -> pd.DataFrame:
        return self.agsi_to_dataframe(
            super().query_lng_terminal(terminal=terminal, start=start, end=end)
        )

    def query_lng_lso(self, lso: Union[ALSILSO, str],
                      start: Union[pd.Timestamp, str], end: Union[pd.Timestamp, str]) -> pd.DataFrame:
        return self.agsi_to_dataframe(
            super().query_lng_lso(lso=lso, start=start, end=end)
        )

    def query_lng_country(self, country: Union[ALSICountry, str],
                          start: Union[pd.Timestamp, str], end: Union[pd.Timestamp, str]) -> pd.DataFrame:
        return self.agsi_to_dataframe(
            super().query_lng_country(country=country, start=start, end=end)
        )
