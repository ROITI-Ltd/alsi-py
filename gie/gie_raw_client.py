import datetime
from turtle import end_poly
from typing import Dict, Optional, Union
from urllib.parse import urljoin

import aiohttp as aiohttp

from gie.exceptions import ApiError
from gie.mappings import (
    AGSICompany,
    AGSICountry,
    AGSIFacility,
    ALSICompany,
    ALSICountry,
    ALSIFacility,
    APIType,
    lookup_agsi_company,
    lookup_alsi_company,
    lookup_country_agsi,
    lookup_country_alsi,
    lookup_facility_agsi,
    lookup_facility_alsi,
)


class GieRawClient:
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

    async def query_agsi_eic_listing(self):
        return await self.fetch(APIType.AGSI, "/about?show=listing")

    async def query_alsi_eic_listing(self):
        return await self.fetch(APIType.ALSI, "/about?show=listing")

    async def query_alsi_news_listing(
        self, news_url_item: Optional[Union[int, str]] = None
    ):
        return await self.fetch(
            APIType.ALSI, "/news", news_url_item=news_url_item
        )

    async def query_agsi_news_listing(
        self, news_url_item: Optional[Union[int, str]] = None
    ):
        return await self.fetch(
            APIType.AGSI, "/news", news_url_item=news_url_item
        )

    async def query_country_agsi_storage(
        self,
        country: Optional[Union[AGSICountry, str]] = None,
        start: Optional[Union[datetime.datetime, str]] = None,
        end: Optional[Union[datetime.datetime, str]] = None,
        date: Optional[Union[datetime.datetime, str]] = None,
        size: Optional[Union[int, str]] = None,
    ):
        country_param = (
            lookup_country_agsi(country) if country is not None else ""
        )

        params = (
            country_param.get_params()
            if isinstance(country_param, AGSICountry)
            else None
        )
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
    ):
        country_param = (
            lookup_country_alsi(country) if country is not None else ""
        )

        params = (
            country_param.get_params()
            if isinstance(country_param, ALSICountry)
            else None
        )
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
    ):
        country_param = (
            lookup_country_agsi(country) if country is not None else ""
        )

        params = (
            country_param.get_params()
            if isinstance(country_param, AGSICountry)
            else None
        )
        return await self.fetch(
            APIType.AGSI,
            endpoint="/unavailability",
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
    ):
        country_param = (
            lookup_country_alsi(country) if country is not None else ""
        )
        return await self.fetch(
            "/unavailability" + country_param.get_url()
            if isinstance(country_param, ALSICountry)
            else "/unavailability",
            APIType.ALSI,
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
    ):
        facility_param = lookup_facility_agsi(facility_name)

        return await self.fetch(
            facility_param.get_url(),
            APIType.AGSI,
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
    ):
        facility_param = lookup_facility_alsi(facility_name)
        return await self.fetch(
            facility_param.get_url(),
            APIType.ALSI,
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
    ):
        company_param = lookup_agsi_company(company_name)
        return await self.fetch(
            company_param.get_url(),
            APIType.AGSI,
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
    ):
        company_param = lookup_alsi_company(company_name)
        return await self.fetch(
            "",
            APIType.ALSI,
            company_param.get_params(),
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
        # Our Abstract FETCH method which helps us request the API with series
        # of optional query params

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

        final_url = urljoin(root_url, endpoint)
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
