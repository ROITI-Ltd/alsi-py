import datetime
import urllib.parse
from typing import Any, Dict, Optional, Union

import aiohttp

from roitigie.exceptions import ApiError
from roitigie.mappings.agsi_company import AGSICompany
from roitigie.mappings.agsi_country import AGSICountry
from roitigie.mappings.agsi_facility import AGSIFacility
from roitigie.mappings.alsi_company import ALSICompany
from roitigie.mappings.alsi_country import ALSICountry
from roitigie.mappings.alsi_facility import ALSIFacility
from roitigie.mappings.api_mappings import APIType
from roitigie.lookup_functions import (
    lookup_country_agsi,
    lookup_country_alsi,
    lookup_facility_agsi,
    lookup_facility_alsi,
    lookup_agsi_company,
    lookup_alsi_company,
)


class GieRawClient:
    """AGSI/ALSI Raw Client which queries the API and returns data"""

    def __init__(
        self, api_key: str, session: Optional[aiohttp.ClientSession] = None
    ):
        """Constructor method for our client
        Parameters
        ----------
        api_key : str
            The key needed for accessing the API
        session : Optional[aiohttp.ClientSession], optional
            User supplied aiohttp ClientSession, or create a new one if None, by default None
        """
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

    async def query_agsi_eic_listing(self) -> Dict[str, Any]:
        """Return all the AGSI EIC (Energy Identification Code) listing.

        Returns
        -------
        Dict[str, Any]
            Object holding the data

        """
        return await self.fetch(APIType.AGSI, "about?show=listing")

    async def query_alsi_eic_listing(self) -> Dict[str, Any]:
        """Return all the AGSI EIC (Energy Identification Code) listing.

        Returns
        -------
        Dict[str, Any]
            Object holding the data
        """
        return await self.fetch(APIType.ALSI, "about?show=listing")

    async def query_alsi_news_listing(
        self, news_url_item: Optional[Union[int, str]] = None
    ) -> Dict[str, Any]:
        """Return all the ALSI news or a specific country news listings

        Parameters
        ----------
        news_url_item : Optional[Union[int, str]], optional
           An integer representing a specific country, by default None

        Returns
        -------
        Dict[str, Any]
            Object holding the data
        """
        return await self.fetch(
            APIType.ALSI, "news", news_url_item=news_url_item
        )

    async def query_agsi_news_listing(
        self, news_url_item: Optional[Union[int, str]] = None
    ) -> Dict[str, Any]:
        """Return all the AGSI news or a specific country news listings

        Parameters
        ----------
        news_url_item : Optional[Union[int, str]], optional
           An integer representing a specific country, by default None

        Returns
        -------
        Dict[str, Any]
            Object holding the data
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
    ) -> Dict[str, Any]:
        """Return listing with the AGSI storage data for
           a specific country or all countries

        Parameters
        ----------
        country : Optional[Union[ALSICountry, str]], optional
            Optional country param, by default None
        start : Optional[Union[datetime.datetime, str]], optional
           Optional start date param, by default None
        end : Optional[Union[datetime.datetime, str]], optional
            Optional end date param, by default None
        date : Optional[Union[datetime.datetime, str]], optional
           Optional current date param, by default None
        size : Optional[Union[int, str]], optional
            Optional result size param, by default None

        Returns
        -------
        Dict[str, Any]
            Object holding queried data
        """
        params = None
        if country is not None:
            country_param = lookup_country_agsi(country)
            params = country_param.get_params()

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
    ) -> Dict[str, Any]:
        """Return listing with the ALSI storage data for
           a specific country or all countries

        Parameters
        ----------
        country : Optional[Union[ALSICountry, str]], optional
            Optional country param, by default None
        start : Optional[Union[datetime.datetime, str]], optional
           Optional start date param, by default None
        end : Optional[Union[datetime.datetime, str]], optional
            Optional end date param, by default None
        date : Optional[Union[datetime.datetime, str]], optional
           Optional current date param, by default None
        size : Optional[Union[int, str]], optional
            Optional result size param, by default None

        Returns
        -------
        Dict[str, Any]
            Object holding queried data
        """
        params = None
        if country is not None:
            country_param = lookup_country_alsi(country)
            params = country_param.get_params()

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
    ) -> Dict[str, Any]:
        """Returns the total AGSI unavailability data or
           a specific country unavailability

        Parameters
        ----------
        country : Optional[Union[AGSICountry, str]], optional
            Optional country param, by default None
        start : Optional[Union[datetime.datetime, str]], optional
            Optional start date param, by default None
        end : Optional[Union[datetime.datetime, str]], optional
            Optional end date param, by default None
        size : Optional[Union[int, str]], optional
            Optional result size param, by default None

        Returns
        -------
        Dict[str, Any]
            Object holding queried data
        """
        params = None
        if country is not None:
            country_param = lookup_country_agsi(country)
            params = country_param.get_params()

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
    ) -> Dict[str, Any]:
        """Returns the total ALSI unavailability data or
           a specific country unavailability

        Parameters
        ----------
        country : Optional[Union[AGSICountry, str]], optional
            Optional country param, by default None
        start : Optional[Union[datetime.datetime, str]], optional
            Optional start date param, by default None
        end : Optional[Union[datetime.datetime, str]], optional
            Optional end date param, by default None
        size : Optional[Union[int, str]], optional
            Optional result size param, by default None

        Returns
        -------
        Dict[str, Any]
            Object holding queried data
        """
        params = None
        if country is not None:
            country_param = lookup_country_alsi(country)
            params = country_param.get_params()

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
    ) -> Dict[str, Any]:
        """Return listing with the AGSI data for a specific facility storage

        Parameters
        ----------
        facility_name : Union[ALSIFacility, str]
            The name of the facility to query for
        start : Optional[Union[datetime.datetime, str]], optional
            Optional start date param, by default None
        end : Optional[Union[datetime.datetime, str]], optional
            Optional end date param, by default None
        date : Optional[Union[datetime.datetime, str]], optional
           Optional current date param, by default None
        size : Optional[Union[int, str]], optional
            Optional result size param, by default None

        Returns
        -------
        Dict[str, Any]
            Object holding queried data
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
    ) -> Dict[str, Any]:
        """Return listing with the ALSI data for a specific facility storage

        Parameters
        ----------
        facility_name : Union[ALSIFacility, str]
            The name of the facility to query for
        start : Optional[Union[datetime.datetime, str]], optional
            Optional start date param, by default None
        end : Optional[Union[datetime.datetime, str]], optional
            Optional end date param, by default None
        date : Optional[Union[datetime.datetime, str]], optional
           Optional current date param, by default None
        size : Optional[Union[int, str]], optional
            Optional result size param, by default None

        Returns
        -------
        Dict[str, Any]
            Object holding queried data
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
    ) -> Dict[str, Any]:
        """Returns listing with the AGSI data for a specific company

        Parameters
        ----------
        company_name : Union[AGSICompany, str]
            The name of the company to query for
        start : Optional[Union[datetime.datetime, str]], optional
            Optional start date param, by default None
        end : Optional[Union[datetime.datetime, str]], optional
            Optional end date param, by default None
        date : Optional[Union[datetime.datetime, str]], optional
           Optional current date param, by default None
        size : Optional[Union[int, str]], optional
            Optional result size param, by default None

        Returns
        -------
        Dict[str, Any]
            Object holding queried data
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
    ) -> Dict[str, Any]:
        """Returns listing with the ALSI data for a specific company

        Parameters
        ----------
        company_name : Union[AGSICompany, str]
            The name of the company to query for
        start : Optional[Union[datetime.datetime, str]], optional
            Optional start date param, by default None
        end : Optional[Union[datetime.datetime, str]], optional
            Optional end date param, by default None
        date : Optional[Union[datetime.datetime, str]], optional
           Optional current date param, by default None
        size : Optional[Union[int, str]], optional
            Optional result size param, by default None

        Returns
        -------
        Dict[str, Any]
            Object holding queried data
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
            params: Optional[Dict[str, Any][str, str]] = None,
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
