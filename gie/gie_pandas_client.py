import datetime
from typing import Union, Optional

import pandas as pd

from gie.gie_raw_client import GieRawClient
from gie.mappings.agsi_company import AGSICompany
from gie.mappings.agsi_country import AGSICountry
from gie.mappings.agsi_facility import AGSIFacility
from gie.mappings.alsi_company import ALSICompany
from gie.mappings.alsi_country import ALSICountry
from gie.mappings.alsi_facility import ALSIFacility


class GiePandasClient(GieRawClient):
    # query for all the AGSI EIC provided from the API
    async def query_agsi_eic_listing(self):
        """

        Returns
        -------
            Inherits GieRawClient's method and
            parses the output as pandas DataFrame

        """
        json_result = await super().query_agsi_eic_listing()
        return pd.DataFrame(json_result)

    async def query_alsi_eic_listing(self):
        """

        Returns
        -------
            Inherits GieRawClient's method and
            parses the output as pandas DataFrame

        """
        json_result = await super().query_alsi_eic_listing()
        return pd.DataFrame(json_result)

    async def query_alsi_news_listing(
        self, news_url_item: Optional[Union[int, str]] = None
    ):
        """

        Returns
        -------
            Inherits GieRawClient's method and
            parses the output as pandas DataFrame

        """
        json_result = await super().query_alsi_news_listing(
            news_url_item=news_url_item
        )
        df = pd.DataFrame(json_result["data"])
        df = df.astype("float", copy=False, errors="ignore")
        return df

    async def query_agsi_news_listing(
        self, news_url_item: Optional[Union[int, str]] = None
    ):
        """

        Returns
        -------
            Inherits GieRawClient's method and
            parses the output as pandas DataFrame

        """
        json_result = await super().query_agsi_news_listing(
            news_url_item=news_url_item
        )
        df = pd.DataFrame(json_result["data"])
        df = df.astype("float", copy=False, errors="ignore")
        return df

    async def query_country_agsi_storage(
        self,
        country: Optional[Union[AGSICountry, str]] = None,
        start: Optional[Union[datetime.datetime, str]] = None,
        end: Optional[Union[datetime.datetime, str]] = None,
        date: Optional[Union[datetime.datetime, str]] = None,
        size: Optional[Union[int, str]] = None,
    ):
        """

        Returns
        -------
            Inherits GieRawClient's method and
            parses the output as pandas DataFrame

        """
        json_result = await super().query_country_agsi_storage(
            country=country, start=start, end=end, date=date, size=size
        )
        df = pd.DataFrame(json_result["data"])
        df = df.astype("float", copy=False, errors="ignore")
        return df

    async def query_country_alsi_storage(
        self,
        country: Optional[Union[ALSICountry, str]] = None,
        start: Optional[Union[datetime.datetime, str]] = None,
        end: Optional[Union[datetime.datetime, str]] = None,
        date: Optional[Union[datetime.datetime, str]] = None,
        size: Optional[Union[int, str]] = None,
    ):
        """

        Returns
        -------
            Inherits GieRawClient's method and
            parses the output as pandas DataFrame

        """
        json_result = await super().query_country_alsi_storage(
            country=country, start=start, end=end, date=date, size=size
        )
        df = pd.DataFrame(json_result["data"])
        df = df.astype("float", copy=False, errors="ignore")
        return df

    async def query_agsi_facility_storage(
        self,
        facility_name: Union[AGSIFacility, str],
        start: Optional[Union[datetime.datetime, str]] = None,
        end: Optional[Union[datetime.datetime, str]] = None,
        date: Optional[Union[datetime.datetime, str]] = None,
        size: Optional[Union[int, str]] = None,
    ):
        """

        Returns
        -------
            Inherits GieRawClient's method and
            parses the output as pandas DataFrame

        """
        json_result = await super().query_agsi_facility_storage(
            facility_name=facility_name,
            start=start,
            end=end,
            date=date,
            size=size,
        )
        gas_df = pd.DataFrame(json_result)
        df = pd.DataFrame(json_result["data"])
        df.insert(0, "gas_day", gas_df["gas_day"], True)
        df = df.astype("float", copy=False, errors="ignore")
        return df

    async def query_alsi_facility_storage(
        self,
        facility_name: Union[ALSIFacility, str],
        start: Optional[Union[datetime.datetime, str]] = None,
        end: Optional[Union[datetime.datetime, str]] = None,
        date: Optional[Union[datetime.datetime, str]] = None,
        size: Optional[Union[int, str]] = None,
    ):
        """

        Returns
        -------
            Inherits GieRawClient's method and
            parses the output as pandas DataFrame

        """
        json_result = await super().query_alsi_facility_storage(
            facility_name=facility_name,
            start=start,
            end=end,
            date=date,
            size=size,
        )
        gas_df = pd.DataFrame(json_result)
        df = pd.DataFrame(json_result["data"])
        df.insert(0, "gas_day", gas_df["gas_day"], True)
        df = df.astype("float", copy=False, errors="ignore")
        return df

    async def query_agsi_company(
        self,
        company_name: Union[AGSICompany, str],
        start: Optional[Union[datetime.datetime, str]] = None,
        end: Optional[Union[datetime.datetime, str]] = None,
        date: Optional[Union[datetime.datetime, str]] = None,
        size: Optional[Union[int, str]] = None,
    ):
        """

        Returns
        -------
            Inherits GieRawClient's method and
            parses the output as pandas DataFrame

        """
        json_result = await super().query_agsi_company(
            company_name=company_name,
            start=start,
            end=end,
            date=date,
            size=size,
        )
        df = pd.DataFrame(json_result["data"])
        df = df.astype("float", copy=False, errors="ignore")
        return df

    async def query_alsi_company(
        self,
        company_name: Union[ALSICompany, str],
        start: Optional[Union[datetime.datetime, str]] = None,
        end: Optional[Union[datetime.datetime, str]] = None,
        date: Optional[Union[datetime.datetime, str]] = None,
        size: Optional[Union[int, str]] = None,
    ):
        """

        Returns
        -------
            Inherits GieRawClient's method and
            parses the output as pandas DataFrame

        """
        json_result = await super().query_alsi_company(
            company_name=company_name,
            start=start,
            end=end,
            date=date,
            size=size,
        )
        df = pd.DataFrame(json_result["data"])
        df = df.astype("float", copy=False, errors="ignore")
        return df

    async def query_agsi_unavailability(
        self,
        country: Optional[Union[AGSICountry, str]] = None,
        start: Optional[Union[datetime.datetime, str]] = None,
        end: Optional[Union[datetime.datetime, str]] = None,
        size: Optional[Union[int, str]] = None,
    ):
        """

        Returns
        -------
            Inherits GieRawClient's method and
            parses the output as pandas DataFrame

        """
        json_result = await super().query_agsi_unavailability(
            country=country, start=start, end=end, size=size
        )
        df = pd.DataFrame(json_result["data"])
        df = df.astype("float", copy=False, errors="ignore")
        return df

    async def query_alsi_unavailability(
        self,
        country: Optional[Union[ALSICountry, str]] = None,
        start: Optional[Union[datetime.datetime, str]] = None,
        end: Optional[Union[datetime.datetime, str]] = None,
        size: Optional[Union[int, str]] = None,
    ):
        """

        Returns
        -------
            Inherits GieRawClient's method and
            parses the output as pandas DataFrame

        """
        json_result = await super().query_alsi_unavailability(
            country=country, start=start, end=end, size=size
        )
        df = pd.DataFrame(json_result["data"])
        df = df.astype("float", copy=False, errors="ignore")
        return df
