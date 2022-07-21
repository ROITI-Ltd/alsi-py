import asyncio
from alsi.raw_client import AlsiRawClient
from alsi.mappings import Area


API_KEY = "30556fadc754d7ecb5604290cccc5eb2"


async def main():

    client = AlsiRawClient(api_key=API_KEY)

    result = await client.query_data_by_company_and_country(
        company_code="21X000000001006T", country_code="bElGiUm", limit=5
    )

    print(result)

    await client.close_session()


asyncio.run(main())
