from typing import Optional
from typing_extensions import Literal
from .raw_client import AlsiRawClient
import pandas as pd
from datetime import datetime


class AlsiPandasClient(AlsiRawClient):
    """Client to perform API calls and return dataframes for ALSI API: https://alsi.gie.eu/#/api"""

    async def query_agg_data_for_europe_or_noneurope(
        self,
        europe: Literal["ne", "eu"],
        start: Optional[datetime] = None,
        end: Optional[datetime] = None,
        limit: Optional[int] = 0,
    ) -> pd.DataFrame:
        """Aggregated historical data export for Europe or Non Europe

        Parameters
        ----------
        europe : Literal['ne', 'eu']
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
        >>> from alsi.raw_client import AlsiPandasClient
        >>> from datetime import datetime
        >>> API_KEY='...'
        >>> client = AlsiPandasClient(api_key=API_KEY)
        >>> result = await client.query_agg_data_for_europe_or_noneurope(europe='eu', start=datetime(2017,3,3), end=datetime(2019, 1,1), limit=10)
        """
        json_result = await super().query_agg_data_for_europe_or_noneurope(
            europe, start, end, limit
        )

        return pd.DataFrame(json_result)

    async def query_agg_data_by_country(
        self,
        country_code: str,
        start: Optional[datetime] = None,
        end: Optional[datetime] = None,
        limit: Optional[int] = 0,
    ) -> pd.DataFrame:
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
        >>> from alsi.raw_client import AlsiPandasClient
        >>> API_KEY='...'
        >>> client = AlsiPandasClient(api_key=API_KEY)
        >>> result = await client.query_agg_data_by_country(country_code='be')
        """
        json_result = await super().query_agg_data_by_country(
            country_code, start, end, limit
        )

        return pd.DataFrame(json_result)

    async def query_data_by_company_and_country(
        self,
        company_code: str,
        country_code: str,
        start: Optional[datetime] = None,
        end: Optional[datetime] = None,
        limit: Optional[int] = 0,
    ) -> pd.DataFrame:
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
        >>> from alsi.raw_client import AlsiPandasClient
        >>> from datetime import datetime
        >>> API_KEY='...'
        >>> client = AlsiPandasClient(api_key=API_KEY)
        >>> result = await client.query_data_by_company_and_country(company_code='21X000000001006T', country_code='be', start=datetime(2017, 3, 3))
        """
        json_result = await super().query_data_by_company_and_country(
            company_code, country_code, start, end, limit
        )

        return pd.DataFrame(json_result)

    async def query_data_for_facility(
        self,
        facility_code: str,
        company_code: str,
        country_code: str,
        start: Optional[datetime] = None,
        end: Optional[datetime] = None,
        limit: Optional[int] = 0,
    ) -> pd.DataFrame:
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
        >>> from alsi.raw_client import AlsiPandasClient
        >>> API_KEY='...'
        >>> client = AlsiPandasClient(api_key=API_KEY)
        >>> result = await client.query_data_for_facility(facility_code='18W000000000GVMT', company_code='21X0000000013368', country_code='es*')
        """
        json_result = await super().query_data_for_facility(
            facility_code, company_code, country_code, start, end, limit
        )

        return pd.DataFrame(json_result)
