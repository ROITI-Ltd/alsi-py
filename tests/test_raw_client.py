import asyncio
import pytest
import pytest_asyncio
import aiohttp
from aiohttp import ClientResponseError
from decouple import config

from gie.exceptions import ApiError
from gie.gie_raw_client import GieRawClient

API_KEY = config("API_KEY")


class TestRawGieClient:
    @pytest.mark.asyncio
    @pytest_asyncio.fixture(scope="class")
    async def client(self):
        dummy_client = GieRawClient(api_key="WTF_THIS_KEY_SHOULDN'T_WORK")
        raw_client = GieRawClient(api_key=API_KEY)

        yield raw_client, dummy_client

        await raw_client.close_session()
        await dummy_client.close_session()

    @pytest_asyncio.fixture(scope="class")
    def event_loop(self):
        # On Windows we need to set the event loop policy in order to avoid loop error
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        loop = asyncio.get_event_loop_policy().new_event_loop()
        yield loop
        loop.close()

    @pytest.mark.asyncio
    async def test_raw_client(self):
        with pytest.raises(ApiError):
            GieRawClient(api_key=None)

    @pytest.mark.asyncio
    async def test_query_agsi_eic_listing(self, client):
        await client[0].query_agsi_eic_listing()

    @pytest.mark.asyncio
    async def test_query_alsi_eic_listing(self, client):
        await client[0].query_alsi_eic_listing()

    @pytest.mark.asyncio
    async def test_query_alsi_news_listing(self, client):
        await client[0].query_alsi_news_listing()

    @pytest.mark.asyncio
    async def test_query_agsi_news_listing(self, client):
        await client[0].query_agsi_news_listing()

    @pytest.mark.asyncio
    async def test_query_country_agsi_storage_with_correct_country(self, client):
        await client[0].query_country_agsi_storage("FR")

    @pytest.mark.asyncio
    async def test_query_country_agsi_storage_with_incorrect_country(self, client):
        with pytest.raises(ValueError):
            await client[0].query_country_agsi_storage("Moria")

    @pytest.mark.asyncio
    async def test_query_country_agsi_storage_without_country(self, client):
        await client[0].query_country_agsi_storage()

    @pytest.mark.asyncio
    async def test_query_country_alsi_storage_with_correct_country(self, client):
        await client[0].query_country_alsi_storage("BE")

    @pytest.mark.asyncio
    async def test_query_country_alsi_storage_with_incorrect_country(self, client):
        with pytest.raises(ValueError):
            await client[0].query_country_alsi_storage("Moria")

    @pytest.mark.asyncio
    async def test_query_country_alsi_storage_without_country(self, client):
        await client[0].query_country_agsi_storage()

    @pytest.mark.asyncio
    async def test_query_alsi_unavailability_with_country(self, client):
        await client[0].query_alsi_unavailability("FR")

    @pytest.mark.asyncio
    async def test_query_alsi_unavailability_without_country(self, client):
        await client[0].query_alsi_unavailability()

    @pytest.mark.asyncio
    async def test_query_alsi_unavailability_with_incorrect_country(self, client):
        with pytest.raises(ValueError):
            await client[0].query_alsi_unavailability("Moria")

    @pytest.mark.asyncio
    async def test_query_agsi_unavailability_with_country(self, client):
        await client[0].query_agsi_unavailability("FR")

    @pytest.mark.asyncio
    async def test_query_agsi_unavailability_without_country(self, client):
        await client[0].query_agsi_unavailability()

    @pytest.mark.asyncio
    async def test_query_agsi_unavailability_with_incorrect_country(self, client):
        with pytest.raises(ValueError):
            await client[0].query_agsi_unavailability("Moria")

    @pytest.mark.asyncio
    async def test_query_agsi_facility_storage_with_correct_facility(self, client):
        await client[0].query_agsi_facility_storage("ugs_berlin")

    @pytest.mark.asyncio
    async def test_query_agsi_facility_storage_with_incorrect_facility(self, client):
        with pytest.raises(ValueError):
            await client[0].query_agsi_facility_storage("falseStorage")

    @pytest.mark.asyncio
    async def test_query_alsi_facility_storage_with_correct_facility(self, client):
        await client[0].query_alsi_facility_storage("zeebrugge")

    @pytest.mark.asyncio
    async def test_query_alsi_facility_storage_with_incorrect_facility(self, client):
        with pytest.raises(ValueError):
            await client[0].query_alsi_facility_storage("falseStorage")

    @pytest.mark.asyncio
    async def test_query_agsi_company_with_correct_company(self, client):
        await client[0].query_agsi_company("omv_gas_storage")

    @pytest.mark.asyncio
    async def test_query_agsi_company_with_incorrect_company(self, client):
        with pytest.raises(ValueError):
            await client[0].query_agsi_company("Moria")

    @pytest.mark.asyncio
    async def test_query_alsi_company_with_correct_company(self, client):
        await client[0].query_alsi_company("dunkerque_lng")

    @pytest.mark.asyncio
    async def test_query_alsi_company_with_incorrect_company(self, client):
        with pytest.raises(ValueError):
            await client[0].query_alsi_company("Moria")

    @pytest.mark.asyncio
    async def test_gie_raw_client_session_request_with_correct_url(self, client):
        resp = await client[0].session.get("https://agsi.gie.eu/api")
        assert resp.status == 200

    @pytest.mark.asyncio
    async def test_gie_raw_client_session_request_with_incorrect_url(self, client):
        with pytest.raises(ClientResponseError):
            await client[0].session.get("https://agsi.gie.eu/api8888")

    @pytest.mark.asyncio
    async def test_gie_raw_client_session_request_with_incorrect_api_token(self, client):
        resp = await client[1].session.get("https://alsi.gie.eu/api/news?")
        assert resp.status == 200
