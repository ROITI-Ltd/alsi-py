from alsi.raw_client import AlsiRawClient
import pytest, asyncio, os

API_KEY = os.getenv("ALSI_KEY")


class TestRawClient:
    @pytest.mark.asyncio
    @pytest.fixture(scope="class")
    async def client(self):
        dummy_client = AlsiRawClient("dummy_key")
        raw_client = AlsiRawClient(API_KEY)

        yield raw_client, dummy_client

        await raw_client.close_session()
        await dummy_client.close_session()

    @pytest.fixture(scope="class")
    def event_loop(self):
        loop = asyncio.get_event_loop_policy().new_event_loop()
        yield loop
        loop.close()

    @pytest.mark.asyncio
    async def test_raw_client(self):

        with pytest.raises(TypeError):
            AlsiRawClient(api_key=None)

    @pytest.mark.asyncio
    async def test_query_for_facility(self, client):
        async for c in client:
            await c[0].query_data_for_facility(
                country_code="FR",
                company_code="21X0000000010679",
                facility_code="63W631527814486R",
            )

            with pytest.raises(TypeError):
                await c[1].query_data_for_facility(
                    facility_code=None,
                    country_code="fr",
                    company_code="21X0000000010679",
                )

            with pytest.raises(TypeError):
                await c[1].query_data_for_facility(
                    facility_code="63W631527814486R",
                    country_code="zzz",
                    company_code="21X0000000010679",
                )

            with pytest.raises(TypeError):
                await c[1].query_data_for_facility(
                    facility_code="63W631527814486R",
                    country_code="fr",
                    company_code=None,
                )

    @pytest.mark.asyncio
    async def test_query_by_country(self, client):
        async for c in client:
            with pytest.raises(TypeError):
                await c[1].query_agg_data_by_country("invalid_country")

            with pytest.raises(TypeError):
                await c[1].query_agg_data_by_country("be", limit="das")

            await c[0].query_agg_data_by_country("be")

    @pytest.mark.asyncio
    async def test_query_by_company_and_country(self, client):
        async for c in client:
            await c[1].query_data_by_company_and_country(
                company_code=None, contry_code=None
            )

            await c[0].query_data_by_company_and_country(
                country_code="be", company_code="21X000000001006T"
            )

    @pytest.mark.asyncio
    async def test_query_eu_or_noneu(self, client):
        async for c in client:
            with pytest.raises(TypeError):
                await c[1].query_agg_data_for_europe_or_noneurope(europe=None)

            with pytest.raises(TypeError):
                await c[1].query_agg_data_for_europe_or_noneurope(
                    "eu", start="1"
                )

            await c[0].query_agg_data_for_europe_or_noneurope("eu")
