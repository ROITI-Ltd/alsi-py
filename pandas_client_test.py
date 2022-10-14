import asyncio

from gie.gie_pandas_client import GiePandasClient


async def main():
    client = GiePandasClient(api_key="b551abbce4194afe648157dd8323c8fe")

    # res = await client.query_gas_country("BG", start="2020-01-01", end="2022-07-10")
    # res2 = await client.query_agsi_eic_listing()
    # res3 = await client.query_alsi_eic_listing()
    # res4 = await client.query_alsi_news_listing(43419)
    # res5 = await client.query_alsi_news_listing()
    # res6 = await client.query_agsi_news_listing()
    # res7 = await client.query_agsi_news_listing(9318)
    # res8 = await client.query_country_agsi_storage(country="DE")
    # res9 = await client.query_country_agsi_storage()
    # res10 = await client.query_country_alsi_storage(country="BE")
    # res11 = await client.query_country_alsi_storage()
    # res12 = await client.query_agsi_facility_storage("ugs_haidach_astora", start="2022-10-10")
    # res13 = await client.query_alsi_facility_storage("dunkerque")
    # result14 = await client.query_agsi_company("astora", size=60)
    # result15 = await client.query_alsi_company("dunkerque_lng")
    result16 = await client.query_alsi_company("dunkerque_lng", size=200)

    await client.close_session()


# set_event_loop_policy method is used in order to avoid EventLoopError from Windows
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())
