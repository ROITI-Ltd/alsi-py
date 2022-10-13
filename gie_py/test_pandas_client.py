from gie.gie import GiePandasClient
import asyncio


async def main():
    client = GiePandasClient(api_key="b551abbce4194afe648157dd8323c8fe")

    await client.query_lng_terminal("dunkerque", start="2020-01-01", end="2022-07-10")
    await client.close_session()


# set_event_loop_policy method is used in order to avoid EventLoopError from Windows
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())

# TODO FIX COROUTINE OBJECT INTO JSON (IN ORDER TO CAST IT TO DATAFRAME)
