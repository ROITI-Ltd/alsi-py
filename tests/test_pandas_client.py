from alsi.pandas_client import AlsiPandasClient
import pytest, asyncio, os, pytest_asyncio

API_KEY = os.getenv("ALSI_KEY")


class TestPandasClient:
    @pytest.mark.asyncio
    @pytest_asyncio.fixture(scope="class", autouse=True)
    async def client(self):
        dummy_client = AlsiPandasClient("dummy_key")
        pandas_client = AlsiPandasClient(API_KEY)

        yield pandas_client, dummy_client

        await pandas_client.close_session()
        await dummy_client.close_session()

    @pytest_asyncio.fixture(scope="class")
    def event_loop(self):
        loop = asyncio.get_event_loop_policy().new_event_loop()
        yield loop
        loop.close()

    @pytest.mark.asyncio
    async def test_pandas_client(
        self,
    ):
        with pytest.raises(TypeError):
            AlsiPandasClient()

    @pytest.mark.asyncio
    async def test_query_eu_or_noneu(self, client):
        with pytest.raises(TypeError):
            await client[1].query_agg_data_for_europe_or_noneurope()

        with pytest.raises(TypeError):
            await client[1].query_agg_data_for_europe_or_noneurope(
                "eu", start="1"
            )

        await client[0].query_agg_data_for_europe_or_noneurope("eu")

    @pytest.mark.asyncio
    async def test_query_by_country(self, client):

        with pytest.raises(TypeError):
            await client[1].query_agg_data_by_country("invalid_country")

        with pytest.raises(TypeError):
            await client[1].query_agg_data_by_country("be", limit="das")

        await client[0].query_agg_data_by_country("be")

    @pytest.mark.asyncio
    async def test_query_by_company_and_country(self, client):
        with pytest.raises(TypeError):
            await client[1].query_data_by_company_and_country()

        await client[0].query_data_by_company_and_country(
            country_code="be", company_code="21X000000001006T"
        )

    @pytest.mark.asyncio
    async def test_query_for_facility(self, client):
        with pytest.raises(TypeError):
            await client[1].query_data_for_facility()

        await client[0].query_data_for_facility(
            country_code="FR",
            company_code="21X0000000010679",
            facility_code="63W631527814486R",
        )
