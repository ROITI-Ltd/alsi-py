import datetime
import urllib.parse
from typing import Dict, Optional, Union

import aiohttp as aiohttp

from gie.exceptions import ApiError
from gie.mappings.agsi_company import AGSICompany
from gie.mappings.agsi_country import AGSICountry
from gie.mappings.agsi_facility import AGSIFacility
from gie.mappings.alsi_company import ALSICompany
from gie.mappings.alsi_country import ALSICountry
from gie.mappings.alsi_facility import ALSIFacility
from gie.mappings.api_mappings import APIType
from gie.lookup_functions import (
    lookup_country_agsi,
    lookup_country_alsi,
    lookup_facility_agsi,
    lookup_facility_alsi,
    lookup_agsi_company,
    lookup_alsi_company,
)


class GieRawClient:
    """
    AGSI/ALSI Raw Client which queries the API and returns data.
    """

    def __init__(
        self, api_key: str, session: Optional[aiohttp.ClientSession] = None
    ):
        self.api_key = api_key
        self.session = (
            session
            if session is not None
            else aiohttp.ClientSession(
                raise_for_status=True, headers={"x-key": self.api_key}
            )
        )

    @property
    def api_key(self):
        return self.__api_key

    @api_key.setter
    def api_key(self, value):
        if not value:
            raise ApiError("API api_type is invalid or missing!")
        self.__api_key = value

    async def query_agsi_eic_listing(self) -> object:
        """Return all the AGSI EIC (Energy Identification Code) listing.

        Returns
        -------
            Queries the API and returns the specific data in a json format.

        """
        return await self.fetch(APIType.AGSI, "about?show=listing")

    async def query_alsi_eic_listing(self) -> object:
        """Return all the AGSI EIC (Energy Identification Code) listing.

        Returns
        -------
            Queries the API and returns the specific data in a json format.

        """
        return await self.fetch(APIType.ALSI, "about?show=listing")

    async def query_alsi_news_listing(
        self, news_url_item: Optional[Union[int, str]] = None
    ) -> object:
        """Return a listing with all the ALSI countries news or a specific country.

        Parameters
        ----------
            news_url_item: Optional[Union[int, str]] = None
            optional parameter for a specific country

        Returns
        -------
           Queries the API and returns the specific data in a json format.

        """
        return await self.fetch(
            APIType.ALSI, "news", news_url_item=news_url_item
        )

    async def query_agsi_news_listing(
        self, news_url_item: Optional[Union[int, str]] = None
    ) -> object:
        """Return a listing with all the AGSI countries news or a specific country.

        Parameters
        ----------
            news_url_item: Optional[Union[int, str]] = None
            optional country url parameter

        Returns
        -------
            Queries the API and returns the specific data in a json format.

        """
        return await self.fetch(
            APIType.AGSI, "news", news_url_item=news_url_item
        )

    async def query_country_agsi_storage(
        self,
        country: Optional[Union[AGSICountry, str]] = None,
        start: Optional[Union[datetime.datetime, str]] = None,
        end: Optional[Union[datetime.datetime, str]] = None,
        date: Optional[Union[datetime.datetime, str]] = None,
        size: Optional[Union[int, str]] = None,
    ) -> object:
        """Return listing with the AGSI storage data for a specific country or all countries.

        Parameters
        ----------
            country: Optional[Union[AGSICountry, str]] = None,
            start: Optional[Union[datetime.datetime, str]] = None,
            end: Optional[Union[datetime.datetime, str]] = None,
            date: Optional[Union[datetime.datetime, str]] = None,
            size: Optional[Union[int, str]] = None,

        Returns
        -------
            Queries the API and returns the specific data in a json format.
        """
        country_param = (
            lookup_country_agsi(country) if country is not None else ""
        )

        params = country_param.get_params() if country_param else ""

        return await self.fetch(
            APIType.AGSI,
            params=params,
            start=start,
            end=end,
            date=date,
            size=size,
        )

    async def query_country_alsi_storage(
        self,
        country: Optional[Union[ALSICountry, str]] = None,
        start: Optional[Union[datetime.datetime, str]] = None,
        end: Optional[Union[datetime.datetime, str]] = None,
        date: Optional[Union[datetime.datetime, str]] = None,
        size: Optional[Union[int, str]] = None,
    ) -> object:
        """Return listing with the ALSI storage data for a specific country or all countries.

        Parameters
        ----------
            country: Optional[Union[AGSICountry, str]] = None,
            start: Optional[Union[datetime.datetime, str]] = None,
            end: Optional[Union[datetime.datetime, str]] = None,
            date: Optional[Union[datetime.datetime, str]] = None,
            size: Optional[Union[int, str]] = None,

        Returns
        -------
            Queries the API and returns the specific data in a json format.
        """
        country_param = (
            lookup_country_alsi(country) if country is not None else ""
        )

        params = country_param.get_params() if country_param else ""

        return await self.fetch(
            APIType.AGSI,
            params=params,
            start=start,
            end=end,
            date=date,
            size=size,
        )

    async def query_agsi_unavailability(
        self,
        country: Optional[Union[AGSICountry, str]] = None,
        start: Optional[Union[datetime.datetime, str]] = None,
        end: Optional[Union[datetime.datetime, str]] = None,
        size: Optional[Union[int, str]] = None,
    ) -> object:
        """Return all the AGSI unavailability data or the unavailability data for a country.

        Parameters
        ----------
            country: Optional[Union[AGSICountry, str]] = None,
            start: Optional[Union[datetime.datetime, str]] = None,
            end: Optional[Union[datetime.datetime, str]] = None,
            size: Optional[Union[int, str]] = None,
            Returns
        -------
            Queries the API and returns the specific data in a json format.
        """
        country_param = (
            lookup_country_agsi(country) if country is not None else ""
        )

        params = country_param.get_params() if country_param else ""

        return await self.fetch(
            APIType.AGSI,
            endpoint="unavailability",
            params=params,
            start=start,
            end=end,
            size=size,
        )

    async def query_alsi_unavailability(
        self,
        country: Optional[Union[ALSICountry, str]] = None,
        start: Optional[Union[datetime.datetime, str]] = None,
        end: Optional[Union[datetime.datetime, str]] = None,
        size: Optional[Union[int, str]] = None,
    ) -> object:
        """Return all the ALSI unavailability data or the unavailability data for a country.

        Parameters
        ----------
            country: Optional[Union[AGSICountry, str]] = None,
            start: Optional[Union[datetime.datetime, str]] = None,
            end: Optional[Union[datetime.datetime, str]] = None,
            size: Optional[Union[int, str]] = None,
            Returns
        -------
            Queries the API and returns the specific data in a json format.
        """
        country_param = (
            lookup_country_alsi(country) if country is not None else ""
        )

        params = country_param.get_params() if country_param else ""

        return await self.fetch(
            APIType.ALSI,
            endpoint="unavailability",
            params=params,
            start=start,
            end=end,
            size=size,
        )

    async def query_agsi_facility_storage(
        self,
        facility_name: Union[AGSIFacility, str],
        start: Optional[Union[datetime.datetime, str]] = None,
        end: Optional[Union[datetime.datetime, str]] = None,
        date: Optional[Union[datetime.datetime, str]] = None,
        size: Optional[Union[int, str]] = None,
    ) -> object:
        """Return the data for a specific AGSI facility.

        Parameters
        ----------
            facility_name: Union[AGSIFacility, str],
            start: Optional[Union[datetime.datetime, str]] = None,
            end: Optional[Union[datetime.datetime, str]] = None,
            date: Optional[Union[datetime.datetime, str]] = None,
            size: Optional[Union[int, str]] = None,

        Returns
        -------
            Queries the API and returns the specific data in a json format.
        """
        facility_param = lookup_facility_agsi(facility_name)

        params = facility_param.get_params()

        return await self.fetch(
            APIType.AGSI,
            params=params,
            start=start,
            end=end,
            date=date,
            size=size,
        )

    async def query_alsi_facility_storage(
        self,
        facility_name: Union[ALSIFacility, str],
        start: Optional[Union[datetime.datetime, str]] = None,
        end: Optional[Union[datetime.datetime, str]] = None,
        date: Optional[Union[datetime.datetime, str]] = None,
        size: Optional[Union[int, str]] = None,
    ) -> object:
        """Return the data for a specific ALSI facility.

        Parameters
        ----------
            facility_name: Union[AGSIFacility, str],
            start: Optional[Union[datetime.datetime, str]] = None,
            end: Optional[Union[datetime.datetime, str]] = None,
            date: Optional[Union[datetime.datetime, str]] = None,
            size: Optional[Union[int, str]] = None,

        Returns
        -------
            Queries the API and returns the specific data in a json format.
        """
        facility_param = lookup_facility_alsi(facility_name)
        params = facility_param.get_params()
        return await self.fetch(
            APIType.ALSI,
            params=params,
            start=start,
            end=end,
            date=date,
            size=size,
        )

    async def query_agsi_company(
        self,
        company_name: Union[AGSICompany, str],
        start: Optional[Union[datetime.datetime, str]] = None,
        end: Optional[Union[datetime.datetime, str]] = None,
        date: Optional[Union[datetime.datetime, str]] = None,
        size: Optional[Union[int, str]] = None,
    ) -> object:
        """Return all the data for a specific AGSI company

        Parameters
        ----------
            company_name: Union[AGSICompany, str],
            start: Optional[Union[datetime.datetime, str]] = None,
            end: Optional[Union[datetime.datetime, str]] = None,
            date: Optional[Union[datetime.datetime, str]] = None,
            size: Optional[Union[int, str]] = None,

        Returns
        -------
            Queries the API and returns the specific data in a json format.
        """
        company_param = lookup_agsi_company(company_name)
        params = company_param.get_params()

        return await self.fetch(
            APIType.AGSI,
            params=params,
            start=start,
            end=end,
            date=date,
            size=size,
        )

    async def query_alsi_company(
        self,
        company_name: Union[ALSICompany, str],
        start: Optional[Union[datetime.datetime, str]] = None,
        end: Optional[Union[datetime.datetime, str]] = None,
        date: Optional[Union[datetime.datetime, str]] = None,
        size: Optional[Union[int, str]] = None,
    ) -> object:
        """Return all the data for a specific ALSI company

        Parameters
        ----------
            company_name: Union[AGSICompany, str],
            start: Optional[Union[datetime.datetime, str]] = None,
            end: Optional[Union[datetime.datetime, str]] = None,
            date: Optional[Union[datetime.datetime, str]] = None,
            size: Optional[Union[int, str]] = None,

        Returns
        -------
            Queries the API and returns the specific data in a json format.
        """
        company_param = lookup_alsi_company(company_name)
        params = company_param.get_params()
        return await self.fetch(
            APIType.ALSI,
            params=params,
            start=start,
            end=end,
            date=date,
            size=size,
        )

    async def fetch(
        self,
        api_type: Union[APIType, str],
        endpoint: Optional[str] = None,
        params: Optional[Dict[str, str]] = None,
        news_url_item: Optional[Union[int, str]] = None,
        start: Optional[Union[datetime.datetime, str]] = None,
        end: Optional[Union[datetime.datetime, str]] = None,
        date: Optional[Union[datetime.datetime, str]] = None,
        size: Optional[Union[int, str]] = None,
    ):
        """Builds the URL and sends requests to the API.

        Parameters
        ----------
            api_type: Union[APIType, str],
            endpoint: Optional[str] = None,
            params: Optional[Dict[str, str]] = None,
            news_url_item: Optional[Union[int, str]] = None,
            start: Optional[Union[datetime.datetime, str]] = None,
            end: Optional[Union[datetime.datetime, str]] = None,
            date: Optional[Union[datetime.datetime, str]] = None,
            size: Optional[Union[int, str]] = None,

        Returns
        -------
            Returns the desired data according to the pointed params.
        """
        _params = {
            "url": news_url_item,
            "from": start,
            "to": end,
            "date": date,
            "size": size,
        }

        if params is not None:
            _params.update(params)

        root_url = (
            api_type.value if isinstance(api_type, APIType) else api_type
        )

        final_url = urllib.parse.urljoin(root_url, endpoint)
        final_params = {k: v for k, v in _params.items() if v is not None}

        async with self.session.get(
            final_url,
            params=final_params,
        ) as resp:
            return await resp.json()

    async def close_session(self) -> None:
        """Close the session."""
        if self.session:
            await self.session.close()
