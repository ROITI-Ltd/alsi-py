# gie-py

Python client for the ALSI/AGSI APIs

Documentation of the API can be found on: <https://www.gie.eu/transparency-platform/GIE_API_documentation_v007.pdf>

Documentation of the client API can be found on: <https://roiti-ltd.github.io/gie-py/>

### Installation

```sh
python -m pip install gie-py
```

### Usage

The package is split in two clients:

1. GieRawClient: Returns data in raw JSON format.
2. GiePandasClient: Returns parsed data in the form of a pandas DataFrame.

```python
import asyncio

from gie.gie_pandas_client import GiePandasClient
from decouple import config


async def main():
    """
    The following methods return pandas DataFrame, however you can use the
    raw client "raw_client = GieRawClient(api_key=Your API key)" and you will get the results as
    JSON parsed to a Python Object
    
    NOTE that every method available for AGSI is also available for ALSI
    """
    pandas_client = GiePandasClient(api_key=config("API_KEY"))

    # You can specify the country, start date, end date, size (the number of results) in order to get country storage
    await pandas_client.query_country_agsi_storage("AT", start="2020-01-01", end="2022-07-10", size=60)

    # You can run the query without any parameters (in order to get all countries result)
    await pandas_client.query_country_alsi_storage()

    # You can use this query in order to get all AGSI/ALSI EICs (Energy Identification Code)
    await pandas_client.query_alsi_eic_listing()
    
    # Query which lists all the ALSI/AGSI news (without params)
    await pandas_client.query_alsi_news_listing()
    
    # Query which lists the news for a specific country (using the url code)
    await pandas_client.query_alsi_news_listing(43419)
    
    # Query which lists the data for a current facility storage (provide the storage name and params)
    await pandas_client.query_agsi_facility_storage("ugs_haidach_astora", start="2022-10-10")
    
    # You can list the data for a current storage only using its name
    await pandas_client.query_alsi_facility_storage("dunkerque")
    
    # Query which lists the data for a current company (also date and size are by choice)
    await pandas_client.query_agsi_company("astora", size=60)
    await pandas_client.query_alsi_company("dunkerque_lng", size=200)
    
    # Query which lists the unavailability for a current country (country name, date, size are optional)
    await pandas_client.query_agsi_unavailability("GB", size=60)
    await pandas_client.query_agsi_unavailability()
    await pandas_client.query_alsi_unavailability("FR")

    await pandas_client.close_session()


# set_event_loop_policy method is used in order to avoid EventLoopError for Windows
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())
```