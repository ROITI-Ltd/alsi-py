import datetime
from typing import Union, Optional, Any

import pandas as pd
import pandas.core.frame

from roitigie.gie_raw_client import GieRawClient
from roitigie.mappings.agsi_company import AGSICompany
from roitigie.mappings.agsi_country import AGSICountry
from roitigie.mappings.agsi_facility import AGSIFacility
from roitigie.mappings.alsi_company import ALSICompany
from roitigie.mappings.alsi_country import ALSICountry
from roitigie.mappings.alsi_facility import ALSIFacility


class GiePandasClient(GieRawClient):
    """
    AGSI/ALSI Pandas Client which queries the API and returns data.
    """

    _FLOATING_COLS = [
        "gasInStorage",
        "consumption",
        "consumptionFull",
        "injection",
        "withdrawal",
        "netWithdrawal",
        "workingGasVolume",
        "injectionCapacity",
        "withdrawalCapacity",
        "trend",
        "full",
        "inventory",
        "sendOut",
        "dtmi",
        "dtrs",
        "volume",
    ]

    async def query_agsi_eic_listing(self) -> pandas.core.frame.DataFrame:
        """Return all the AGSI EIC(Energy Identification Code) listing.

        Returns
        -------
        pd.DataFrame
            DataFrame holding the EIC listings.

        """
        json_result = await super().query_agsi_eic_listing()
        return self._pandas_df_format(json_result)

    async def query_alsi_eic_listing(self) -> pandas.core.frame.DataFrame:
        """Return all the ALSI EIC(Energy Identification Code) listing.

        Returns
        -------
        pd.DataFrame
            DataFrame holding the EIC listings.

        """
        json_result = await super().query_alsi_eic_listing()
        return self._pandas_df_format(json_result)

    async def query_alsi_news_listing(
        self, news_url_item: Optional[Union[int, str]] = None
    ) -> pandas.core.frame.DataFrame:
        """Return all the ALSI news or a specific country news listings.

        Returns
        -------
        pd.DataFrame
            DataFrame holding the NEWS listings.

        """
        json_result = await super().query_alsi_news_listing(
            news_url_item=news_url_item
        )
        return self._pandas_df_format(json_result)

    async def query_agsi_news_listing(
        self, news_url_item: Optional[Union[int, str]] = None
    ) -> pandas.core.frame.DataFrame:
        """Return all the AGSI news or a specific country news listings.

        Returns
        -------
        pd.DataFrame
            DataFrame holding the NEWS listings.

        """
        json_result = await super().query_agsi_news_listing(
            news_url_item=news_url_item
        )
        return self._pandas_df_format(json_result)

    async def query_country_agsi_storage(
        self,
        country: Optional[Union[AGSICountry, str]] = None,
        start: Optional[Union[datetime.datetime, str]] = None,
        end: Optional[Union[datetime.datetime, str]] = None,
        date: Optional[Union[datetime.datetime, str]] = None,
        size: Optional[Union[int, str]] = None,
    ) -> pandas.core.frame.DataFrame:
        """Return listing with the AGSI storage data for a specific country or all countries.

        Returns
        -------
        pd.DataFrame
            DataFrame holding data for a specific country or all countries listing.

        """
        json_result = await super().query_country_agsi_storage(
            country=country, start=start, end=end, date=date, size=size
        )
        return self._pandas_df_format(json_result, self._FLOATING_COLS)

    async def query_country_alsi_storage(
        self,
        country: Optional[Union[ALSICountry, str]] = None,
        start: Optional[Union[datetime.datetime, str]] = None,
        end: Optional[Union[datetime.datetime, str]] = None,
        date: Optional[Union[datetime.datetime, str]] = None,
        size: Optional[Union[int, str]] = None,
    ) -> pandas.core.frame.DataFrame:
        """Return listing with the ALSI storage data for a specific country or all countries.

        Returns
        -------
        pd.DataFrame
            DataFrame holding data for a specific country or all countries listing.

        """
        json_result = await super().query_country_alsi_storage(
            country=country, start=start, end=end, date=date, size=size
        )
        return self._pandas_df_format(json_result, self._FLOATING_COLS)

    async def query_agsi_facility_storage(
        self,
        facility_name: Union[AGSIFacility, str],
        start: Optional[Union[datetime.datetime, str]] = None,
        end: Optional[Union[datetime.datetime, str]] = None,
        date: Optional[Union[datetime.datetime, str]] = None,
        size: Optional[Union[int, str]] = None,
    ) -> pandas.core.frame.DataFrame:
        """Return listing with the AGSI data for a specific facility storage.

        Returns
        -------
        pd.DataFrame
            DataFrame holding the AGSI facility data.

        """
        json_result = await super().query_agsi_facility_storage(
            facility_name=facility_name,
            start=start,
            end=end,
            date=date,
            size=size,
        )
        return self._pandas_df_format(json_result, self._FLOATING_COLS)

    async def query_alsi_facility_storage(
        self,
        facility_name: Union[ALSIFacility, str],
        start: Optional[Union[datetime.datetime, str]] = None,
        end: Optional[Union[datetime.datetime, str]] = None,
        date: Optional[Union[datetime.datetime, str]] = None,
        size: Optional[Union[int, str]] = None,
    ) -> pandas.core.frame.DataFrame:
        """Return listing with the ALSI data for a specific facility storage.

        Returns
        -------
        pd.DataFrame
            DataFrame holding the ALSI facility data.

        """
        json_result = await super().query_alsi_facility_storage(
            facility_name=facility_name,
            start=start,
            end=end,
            date=date,
            size=size,
        )
        return self._pandas_df_format(json_result, self._FLOATING_COLS)

    async def query_agsi_company(
        self,
        company_name: Union[AGSICompany, str],
        start: Optional[Union[datetime.datetime, str]] = None,
        end: Optional[Union[datetime.datetime, str]] = None,
        date: Optional[Union[datetime.datetime, str]] = None,
        size: Optional[Union[int, str]] = None,
    ) -> pandas.core.frame.DataFrame:
        """Returns listing with the AGSI data for a specific company

        Returns
        -------
            pd.DataFrame
            DataFrame holding the AGSI company data.

        """
        json_result = await super().query_agsi_company(
            company_name=company_name,
            start=start,
            end=end,
            date=date,
            size=size,
        )
        return self._pandas_df_format(json_result, self._FLOATING_COLS)

    async def query_alsi_company(
        self,
        company_name: Union[ALSICompany, str],
        start: Optional[Union[datetime.datetime, str]] = None,
        end: Optional[Union[datetime.datetime, str]] = None,
        date: Optional[Union[datetime.datetime, str]] = None,
        size: Optional[Union[int, str]] = None,
    ) -> pandas.core.frame.DataFrame:
        """Returns listing with the ALSI data for a specific company

        Returns
        -------
            pd.DataFrame
            DataFrame holding the ALSI company data.

        """
        json_result = await super().query_alsi_company(
            company_name=company_name,
            start=start,
            end=end,
            date=date,
            size=size,
        )
        return self._pandas_df_format(json_result, self._FLOATING_COLS)

    async def query_agsi_unavailability(
        self,
        country: Optional[Union[AGSICountry, str]] = None,
        start: Optional[Union[datetime.datetime, str]] = None,
        end: Optional[Union[datetime.datetime, str]] = None,
        size: Optional[Union[int, str]] = None,
    ) -> pandas.core.frame.DataFrame:
        """Returns the total AGSI unavailability data or a specific country unavailability.

        Returns
        -------
            pd.DataFrame
            DataFrame holding the AGSI unavailability data.

        """
        json_result = await super().query_agsi_unavailability(
            country=country, start=start, end=end, size=size
        )
        return self._pandas_df_format(json_result, self._FLOATING_COLS)

    async def query_alsi_unavailability(
        self,
        country: Optional[Union[ALSICountry, str]] = None,
        start: Optional[Union[datetime.datetime, str]] = None,
        end: Optional[Union[datetime.datetime, str]] = None,
        size: Optional[Union[int, str]] = None,
    ) -> pandas.core.frame.DataFrame:
        """Returns the total ALSI unavailability data or a specific country unavailability.

        Returns
        -------
            pd.DataFrame
            DataFrame holding the ALSI unavailability data.

        """
        json_result = await super().query_alsi_unavailability(
            country=country, start=start, end=end, size=size
        )
        return self._pandas_df_format(json_result, self._FLOATING_COLS)

    def _pandas_df_format(
        self, json_res: Any, float_cols: Optional[list] = None
    ) -> pandas.core.frame.DataFrame:
        df = (
            pd.DataFrame(json_res["data"])
            if "data" in json_res
            else pd.DataFrame(json_res)
        )

        if "gas_day" in json_res:
            df.insert(0, "gas_day", json_res["gas_day"], allow_duplicates=True)

        if float_cols is not None:
            df_cols = [x for x in float_cols if x in df.columns]
            if df_cols:
                df[df_cols] = df[df_cols].astype("float", errors="ignore")

        return df
