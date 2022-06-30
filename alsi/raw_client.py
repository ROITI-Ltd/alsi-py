from typing import Optional
from typing_extensions import Literal
import aiohttp
from datetime import datetime
from .exceptions import AccessDeniedException
from .timefilter import Timefilter


class AlsiRawClient:
    """Client to perform API calls and return JSON data for ALSI API: https://alsi.gie.eu/#/api"""

    BASE_URL = "https://alsi.gie.eu/api/data"

    def __init__(
        self,
        api_key: str,
        session: Optional[aiohttp.ClientSession] = None,
    ) -> None:

        if not api_key:
            raise TypeError("No API key provided.")

        self.__api_key = api_key

        self.__session = (
            aiohttp.ClientSession(
                raise_for_status=True,
                headers={"x-key": self.__api_key},
            )
            if not session
            else session
        )

    async def query_data_for_facility(
        self,
        facility_code: str,
        company_code: str,
        country_code: str,
        start: Optional[datetime] = None,
        end: Optional[datetime] = None,
        limit: Optional[int] = 0,
    ) -> list:
        """Query historical data export for a specific facility from a company within a country

        Parameters
        ----------
        facility_code : str
            21 digit EIC code of the facility
        company_code : str
            21 digit EIC code of the company
        country_code : str
            2 digit country code
        start: Optional[datetime]
            start date
        end: Optional[datetime]
            end date
        limit: Optional[int]
            limit the number of results

        Raises
        ------
        TypeError
            if country code, company code or facility code is invalid

        Examples
        --------
        >>> from alsi.raw_client import AlsiRawClient
        >>> API_KEY='...'
        >>> client = AlsiRawClient(api_key=API_KEY)
        >>> result = await client.query_data_for_facility(facility_code='18W000000000GVMT', company_code='21X0000000013368', country_code='es*')
        """

        if not facility_code:
            raise TypeError("Facility code not provided.")

        if not company_code:
            raise TypeError("Company code not provided.")

        if AlsiRawClient.__invalid_country_code(country_code):
            raise TypeError("Invalid country code format.")

        timefilter = Timefilter(start, end, limit)

        return await self.__base_request(
            facility_code.upper(),
            country_code.upper(),
            company_code.upper(),
            timefilter=timefilter,
        )

    async def query_agg_data_for_europe_or_noneurope(
        self,
        europe: Literal["eu", "ne"],
        start: Optional[datetime] = None,
        end: Optional[datetime] = None,
        limit: Optional[int] = 0,
    ) -> list:
        """Aggregated historical data export for Europe or Non Europe

        Parameters
        ----------
        europe : Literal['eu', 'ne']
            'ne' for noneurope, eu for europe
        start: Optional[datetime]
            start date
        end: Optional[datetime]
            end date
        limit: Optional[int]
            limit the number of results

        Raises
        ------
        TypeError
            if europe: str parameter is not provided or invalid

        Examples
        --------
        >>> from alsi.raw_client import AlsiRawClient
        >>> from datetime import datetime
        >>> API_KEY='...'
        >>> client = AlsiRawClient(api_key=API_KEY)
        >>> result = await client.query_agg_data_for_europe_or_noneurope(europe='eu', start=datetime(2017,3,3), end=datetime(2019, 1,1), limit=10)
        """

        invalid_param = not europe or europe not in ("eu", "ne")

        if invalid_param:
            raise TypeError("Invalid parameter.")

        timefilter = Timefilter(start, end, limit)

        return await self.__base_request(europe.lower(), timefilter=timefilter)

    async def query_agg_data_by_country(
        self,
        country_code: str,
        start: Optional[datetime] = None,
        end: Optional[datetime] = None,
        limit: Optional[int] = 0,
    ) -> list:
        """Aggregated historical data export for a specific country

        Parameters
        ----------
        country_code : str
            2 digit country code
        start: Optional[datetime]
            start date
        end: Optional[datetime]
            end date
        limit: Optional[int]
            limit the number of results

        Raises
        ------
        TypeError
            if country code is invalid

        Examples
        --------
        >>> from alsi.raw_client import AlsiRawClient
        >>> API_KEY='...'
        >>> client = AlsiRawClient(api_key=API_KEY)
        >>> result = await client.query_agg_data_by_country(country_code='be')
        """

        if AlsiRawClient.__invalid_country_code(country_code):
            raise TypeError("Invalid country code format.")

        timefilter = Timefilter(start, end, limit)

        return await self.__base_request(
            country_code.upper(),
            timefilter=timefilter,
        )

    async def query_data_by_company_and_country(
        self,
        company_code: str,
        country_code: str,
        start: Optional[datetime] = None,
        end: Optional[datetime] = None,
        limit: Optional[int] = 0,
    ):
        """Historical data export for a specific company within a country

        Parameters
        ----------
        company_code : str
            21 digic EIC company code
        country_code : str
            2 digit country code
        start: Optional[datetime]
            start date
        end: Optional[datetime]
            end date
        limit: Optional[int]
            limit the number of results

        Raises
        ------
        TypeError
            if country code or company code is invalid

        Examples
        --------
        >>> from alsi.raw_client import AlsiRawClient
        >>> from datetime import datetime
        >>> API_KEY='...'
        >>> client = AlsiRawClient(api_key=API_KEY)
        >>> result = await client.query_data_by_company_and_country(company_code='21X000000001006T', country_code='be', start=datetime(2017, 3, 3))
        """

        if not company_code:
            raise TypeError("Company code not provided.")

        if AlsiRawClient.__invalid_country_code(country_code):
            raise TypeError("Invalid country code format.")

        timefilter = Timefilter(start, end, limit)

        return await self.__base_request(
            company_code.upper(),
            country_code.upper(),
            timefilter=timefilter,
        )

    async def __base_request(
        self, *path_segments: str, timefilter: Timefilter
    ):

        if AlsiRawClient.__invalid_timefilter(timefilter):
            raise TypeError("Invalid timefilter.")

        params = {}

        if any(timefilter):
            start, end, limit = timefilter
            if start:
                params["from"] = start.strftime("%Y-%m-%d")
            if end:
                params["till"] = end.strftime("%Y-%m-%d")
            if limit:
                params["limit"] = str(limit)

        url = f"{AlsiRawClient.BASE_URL}/{'/'.join(path_segments)}"

        async with self.__session.get(url, params=params) as res:
            if res.status < 400:
                if "access denied" in (await res.text()):
                    raise AccessDeniedException("Check if API key is invalid.")

                return await res.json()

    @staticmethod
    def __invalid_country_code(country_code: str) -> bool:

        return (
            not country_code
            or len(country_code.strip("*")) > 2
            or any(not char.isalpha() for char in country_code.strip("*"))
        )

    @staticmethod
    def __invalid_timefilter(timefilter: tuple) -> bool:
        start, end, limit = timefilter

        return (
            len(timefilter) > 3
            or (limit and (not isinstance(limit, int) or limit < 0))
            or ((start and end) and (start > end))
            or (start and (not isinstance(start, datetime)))
            or (end and (not isinstance(end, datetime)))
        )

    async def close_session(self) -> None:
        """Close the session."""
        if self.__session:
            await self.__session.close()
