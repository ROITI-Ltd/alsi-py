import asyncio
import sys

import pandas.core.frame
import pytest
import pytest_asyncio
from decouple import config

from roiti.exceptions import ApiError
from roiti.gie_pandas_client import GiePandasClient

API_KEY = config("API_KEY")


class TestPandasGieClient:
    @pytest.mark.asyncio
    @pytest_asyncio.fixture(scope="class")
    async def client(self):
        raw_client = GiePandasClient(api_key=API_KEY)

        yield raw_client

        await raw_client.close_session()

    @pytest_asyncio.fixture(scope="class")
    def event_loop(self):
        if sys.platform == "win32":
            # On Windows we need to set the event loop policy in order to avoid loop error
            asyncio.set_event_loop_policy(
                asyncio.WindowsSelectorEventLoopPolicy()
            )

        loop = asyncio.get_event_loop_policy().new_event_loop()
        yield loop
        loop.close()

    @pytest.mark.asyncio
    async def test_pandas_client(self):
        with pytest.raises(ApiError):
            GiePandasClient(api_key=None)

    @pytest.mark.asyncio
    async def test_query_agsi_eic_listing(self, client):
        result = await client.query_agsi_eic_listing()
        assert isinstance(result, pandas.core.frame.DataFrame)

    @pytest.mark.asyncio
    async def test_query_alsi_eic_listing(self, client):
        result = await client.query_alsi_eic_listing()
        assert isinstance(result, pandas.core.frame.DataFrame)

    @pytest.mark.asyncio
    async def test_query_alsi_news_listing(self, client):
        result = await client.query_alsi_news_listing()
        assert isinstance(result, pandas.core.frame.DataFrame)

    @pytest.mark.asyncio
    async def test_query_agsi_news_listing(self, client):
        result = await client.query_agsi_news_listing()
        assert isinstance(result, pandas.core.frame.DataFrame)

    @pytest.mark.asyncio
    async def test_query_country_agsi_storage_with_correct_country(
        self, client
    ):
        result = await client.query_country_agsi_storage("FR")
        assert isinstance(result, pandas.core.frame.DataFrame)

    @pytest.mark.asyncio
    async def test_query_country_agsi_storage_with_incorrect_country(
        self, client
    ):
        with pytest.raises(ValueError):
            await client.query_country_agsi_storage("Moria")

    @pytest.mark.asyncio
    async def test_query_country_agsi_storage_without_country(self, client):
        result = await client.query_country_agsi_storage()
        assert isinstance(result, pandas.core.frame.DataFrame)

    @pytest.mark.asyncio
    async def test_query_country_alsi_storage_with_correct_country(
        self, client
    ):
        result = await client.query_country_alsi_storage("BE")
        assert isinstance(result, pandas.core.frame.DataFrame)

    @pytest.mark.asyncio
    async def test_query_country_alsi_storage_with_incorrect_country(
        self, client
    ):
        with pytest.raises(ValueError):
            await client.query_country_alsi_storage("Moria")

    @pytest.mark.asyncio
    async def test_query_country_alsi_storage_without_country(self, client):
        result = await client.query_country_agsi_storage()
        assert isinstance(result, pandas.core.frame.DataFrame)

    @pytest.mark.asyncio
    async def test_query_alsi_unavailability_with_country(self, client):
        result = await client.query_alsi_unavailability("FR")
        assert isinstance(result, pandas.core.frame.DataFrame)

    @pytest.mark.asyncio
    async def test_query_alsi_unavailability_without_country(self, client):
        result = await client.query_alsi_unavailability()
        assert isinstance(result, pandas.core.frame.DataFrame)

    @pytest.mark.asyncio
    async def test_query_alsi_unavailability_with_incorrect_country(
        self, client
    ):
        with pytest.raises(ValueError):
            await client.query_alsi_unavailability("Moria")

    @pytest.mark.asyncio
    async def test_query_agsi_unavailability_with_country(self, client):
        result = await client.query_agsi_unavailability("FR")
        assert isinstance(result, pandas.core.frame.DataFrame)

    @pytest.mark.asyncio
    async def test_query_agsi_unavailability_without_country(self, client):
        result = await client.query_agsi_unavailability()
        assert isinstance(result, pandas.core.frame.DataFrame)

    @pytest.mark.asyncio
    async def test_query_agsi_unavailability_with_incorrect_country(
        self, client
    ):
        with pytest.raises(ValueError):
            await client.query_agsi_unavailability("Moria")

    @pytest.mark.asyncio
    async def test_query_agsi_facility_storage_with_correct_facility(
        self, client
    ):
        result = await client.query_agsi_facility_storage("ugs_berlin")
        assert isinstance(result, pandas.core.frame.DataFrame)

    @pytest.mark.asyncio
    async def test_query_agsi_facility_storage_with_incorrect_facility(
        self, client
    ):
        with pytest.raises(ValueError):
            await client.query_agsi_facility_storage("falseStorage")

    @pytest.mark.asyncio
    async def test_query_alsi_facility_storage_with_correct_facility(
        self, client
    ):
        result = await client.query_alsi_facility_storage("zeebrugge")
        assert isinstance(result, pandas.core.frame.DataFrame)

    @pytest.mark.asyncio
    async def test_query_alsi_facility_storage_with_incorrect_facility(
        self, client
    ):
        with pytest.raises(ValueError):
            await client.query_alsi_facility_storage("falseStorage")

    @pytest.mark.asyncio
    async def test_query_agsi_company_with_correct_company(self, client):
        result = await client.query_agsi_company("omv_gas_storage")
        assert isinstance(result, pandas.core.frame.DataFrame)

    @pytest.mark.asyncio
    async def test_query_agsi_company_with_incorrect_company(self, client):
        with pytest.raises(ValueError):
            await client.query_agsi_company("Moria")

    @pytest.mark.asyncio
    async def test_query_alsi_company_with_correct_company(self, client):
        result = await client.query_alsi_company("dunkerque_lng")
        assert isinstance(result, pandas.core.frame.DataFrame)

    @pytest.mark.asyncio
    async def test_query_alsi_company_with_incorrect_company(self, client):
        with pytest.raises(ValueError):
            await client.query_alsi_company("Moria")
