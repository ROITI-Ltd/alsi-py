import datetime
from typing import Union, Optional

import pandas as pd

from gie.agsi_mappings import AGSIFacility, AGSICountry, AGSICompany
from gie.alsi_mappings import ALSIFacility, ALSICompany, ALSICountry
from gie.gie_raw_client import GieRawClient


class GiePandasClient(GieRawClient):
    # query for all the AGSI EIC provided from the API
    async def query_agsi_eic_listing(self):
        json_result = await super().query_agsi_eic_listing()
        return pd.DataFrame(json_result)

    # query for all the ALSI EIC provided from the API
    async def query_alsi_eic_listing(self):
        json_result = await super().query_alsi_eic_listing()
        return pd.DataFrame(json_result)

    # query which provide us all ALSI news OR a specific item (news for a concrete country)
    async def query_alsi_news_listing(
            self, news_url_item: Optional[Union[int, str]] = None
    ):
        json_result = await super().query_alsi_news_listing(news_url_item=news_url_item)
        return pd.DataFrame(json_result["data"])

    # query which provide us all ALSI news OR a specific item (news for a concrete country)
    async def query_agsi_news_listing(
            self, news_url_item: Optional[Union[int, str]] = None
    ):
        json_result = await super().query_agsi_news_listing(news_url_item=news_url_item)
        return pd.DataFrame(json_result["data"])

    # AGSI query which provides data for a specific country
    async def query_country_agsi_storage(
            self,
            country: Optional[Union[AGSICountry, str]] = None,
            start: Optional[Union[datetime.datetime, str]] = None,
            end: Optional[Union[datetime.datetime, str]] = None,
            date: Optional[Union[datetime.datetime, str]] = None,
            size: Optional[Union[int, str]] = None,
    ):
        json_result = await super().query_country_agsi_storage(
            country=country, start=start, end=end, date=date, size=size
        )
        df = pd.DataFrame(json_result["data"])
        return df

    # ALSI query which provides data for a specific country
    async def query_country_alsi_storage(
            self,
            country: Optional[Union[AGSICountry, str]] = None,
            start: Optional[Union[datetime.datetime, str]] = None,
            end: Optional[Union[datetime.datetime, str]] = None,
            date: Optional[Union[datetime.datetime, str]] = None,
            size: Optional[Union[int, str]] = None,
    ):
        json_result = await super().query_country_alsi_storage(
            country=country, start=start, end=end, date=date, size=size
        )
        df = pd.DataFrame(json_result["data"])
        return df

    # AGSI query which provides all the data for a specific facility
    async def query_agsi_facility_storage(
            self,
            facility_name: Union[AGSIFacility, str],
            start: Optional[Union[datetime.datetime, str]] = None,
            end: Optional[Union[datetime.datetime, str]] = None,
            date: Optional[Union[datetime.datetime, str]] = None,
            size: Optional[Union[int, str]] = None,
    ):
        json_result = await super().query_agsi_facility_storage(
            facility_name=facility_name, start=start, end=end, date=date, size=size
        )
        df = pd.DataFrame(json_result["data"])
        return df

    # ALSI query which provides all the data for a specific facility
    async def query_alsi_facility_storage(
            self,
            facility_name: Union[ALSIFacility, str],
            start: Optional[Union[datetime.datetime, str]] = None,
            end: Optional[Union[datetime.datetime, str]] = None,
            date: Optional[Union[datetime.datetime, str]] = None,
            size: Optional[Union[int, str]] = None,
    ):
        json_result = await super().query_alsi_facility_storage(
            facility_name=facility_name, start=start, end=end, date=date, size=size
        )
        df = pd.DataFrame(json_result["data"])
        return df

    # AGSI query which provides data for a specific company
    async def query_agsi_company(
            self,
            company_name: Union[AGSICompany, str],
            start: Optional[Union[datetime.datetime, str]] = None,
            end: Optional[Union[datetime.datetime, str]] = None,
            date: Optional[Union[datetime.datetime, str]] = None,
            size: Optional[Union[int, str]] = None,
    ):
        json_result = await super().query_agsi_company(
            company_name=company_name, start=start, end=end, date=date, size=size
        )
        df = pd.DataFrame(json_result["data"])
        return df

    # ALSI query which provides data for a specific company
    async def query_alsi_company(
            self,
            company_name: Union[ALSICompany, str],
            start: Optional[Union[datetime.datetime, str]] = None,
            end: Optional[Union[datetime.datetime, str]] = None,
            date: Optional[Union[datetime.datetime, str]] = None,
            size: Optional[Union[int, str]] = None,
    ):
        json_result = await super().query_alsi_company(
            company_name=company_name, start=start, end=end, date=date, size=size
        )
        df = pd.DataFrame(json_result["data"])
        return df

    async def query_agsi_unavailability(self, country: Optional[Union[AGSICountry, str]] = None,
                                        start: Optional[Union[datetime.datetime, str]] = None,
                                        end: Optional[Union[datetime.datetime, str]] = None,
                                        size: Optional[Union[int, str]] = None):
        json_result = await super().query_agsi_unavailability(country=country, start=start, end=end, size=size)
        df = pd.DataFrame(json_result["data"])
        return df

    async def query_alsi_unavailability(self, country: Optional[Union[ALSICountry, str]] = None,
                                        start: Optional[Union[datetime.datetime, str]] = None,
                                        end: Optional[Union[datetime.datetime, str]] = None,
                                        size: Optional[Union[int, str]] = None):
        json_result = await super().query_alsi_unavailability(country=country, start=start, end=end, size=size)
        df = pd.DataFrame(json_result["data"])
        return df

    # async def query_gas_storage(
    #     self,
    #     storage: Union[AGSIFacility, str],
    #     start: Optional[Union[datetime.datetime, str]] = None,
    #     end: Optional[Union[datetime.datetime, str]] = None,
    # ):
    #
    #     json_result = await super().query_gas_storage(
    #         storage=storage, start=start, end=end
    #     )
    #     return pd.DataFrame(json_result["data"])
    #
    # async def query_gas_company(
    #     self,
    #     company: Union[AGSIFacility, str],
    #     start: Union[datetime.datetime, str],
    #     end: Union[datetime.datetime, str],
    # ) -> pd.DataFrame:
    #     json_result = await super().query_gas_company(
    #         company=company, start=start, end=end
    #     )
    #     return pd.DataFrame(json_result["data"])
    #
    # async def query_gas_country(
    #     self,
    #     country: Union[AGSICountry, str],
    #     start: Union[datetime.datetime, str],
    #     end: Union[datetime.datetime, str],
    # ) -> pd.DataFrame:
    #     json_result = await super().query_gas_country(
    #         country=country, start=start, end=end
    #     )
    #     return pd.DataFrame(json_result["data"])
    #
    # async def query_lng_terminal(
    #     self,
    #     terminal: Union[ALSIFacility, str],
    #     start: Union[datetime.datetime, str],
    #     end: Union[datetime.datetime, str],
    # ) -> pd.DataFrame:
    #     json_result = await super().query_lng_terminal(
    #         terminal=terminal, start=start, end=end
    #     )
    #     df = pd.DataFrame(json_result["data"])
    #     return df
    #
    # async def query_lng_lso(
    #     self,
    #     lso: Union[ALSICompany, str],
    #     start: Union[datetime.datetime, str],
    #     end: Union[datetime.datetime, str],
    # ) -> pd.DataFrame:
    #     json_result = await super().query_lng_lso(lso=lso, start=start, end=end)
    #     return pd.DataFrame(json_result["data"])
    #
    # async def query_lng_country(
    #     self,
    #     country: Union[ALSICountry, str],
    #     start: Union[datetime.datetime, str],
    #     end: Union[datetime.datetime, str],
    # ) -> pd.DataFrame:
    #     json_result = await super().query_lng_country(
    #         country=country, start=start, end=end
    #     )
    #     return pd.DataFrame(json_result["data"])
