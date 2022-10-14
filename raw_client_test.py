from gie.gie_raw_client import GieRawClient
import asyncio


async def main():
    client = GieRawClient(api_key="b551abbce4194afe648157dd8323c8fe")

    # res = await client.query_lng_terminal(
    #     "fos_cavaou", start="2020-01-01", end="2022-07-10"
    # )
    # res2 = await client.query_agsi_eic_listing()
    # res3 = await client.query_alsi_eic_listing()
    # res4 = await client.query_alsi_news_listing(4581)
    # res5 = await client.query_agsi_news_listing()
    # res6 = await client.query_country_agsi_storage(country="DE", date="2022-03-31", size=60)
    # res7 = await client.query_country_agsi_storage()
    # result8 = await client.query_agsi_facility_storage("vgs_omv_tallesbrunn")
    # result9 = await client.query_alsi_facility_storage("dunkerque")
    # result10 = await client.query_agsi_company("astora")
    # result11 = await client.query_alsi_company("dunkerque_lng")

    await client.close_session()


# set_event_loop_policy method is used in order to avoid EventLoopError from Windows
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())
