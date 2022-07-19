# alsi-py

Python client for the ALSI API (Aggregated LNG Storage Inventory)

Documentation of the API can be found on: https://alsi.gie.eu/GIE_API_documentation_v004.pdf

### Installation
`python3 -m pip3 install alsi-py `

### Usage
The package is split in two clients:
1. AlsiRawClient: Returns data in raw JSON format.
2. AlsiPandasClient: Returns parsed data in the form of a pandas dataframe.

```
from alsi.raw_client import AlsiRawClient
from alsi.pandas_client import AlsiPandasClient
from datetime import datetime
import asyncio

API_KEY = '<API_KEY>'

country_code = 'DE'
company_code = '21X000000001368W'
facility_code = '21W000000000100J'

async def main():
    client = AlsiRawClient(api_key=API_KEY)

    # Functions that return JSON.
    client.query_data_for_facility(facility_code, company_code, country_code)
    client.query_agg_data_for_europe_or_noneurope(europe='eu')
    client.query_agg_data_by_country(contry_code='BE')
    client.query_data_by_company_and_country(company_code, country_code)

    # Filter results by time
    client.query_agg_data_by_country(country_code, start=datetime(2017,1,1), end=datetime(2018,1,1), limit=10)

    # Create pandas client. All functions are the same as the raw client.
    pandas_client = AlsiPandasClient(api_key=API_KEY)

    # In the end of the code, make sure to close the client session:
    await client.close_session()
    # or
    await pandas_client.close_session()

asyncio.run(main())

```

### For more information regarding company codes, facility codes and country codes visit: https://alsi.gie.eu/#/api

### Running unit tests
Tell pytest where to look for unit tests and create env for ALSI API key
```
export PYTHONPATH=./alsi
export ALSI_KEY='...'
```

Run unit tests in coverage mode
```
python -m pytest ./tests --import-mode=append --cov
```

### Contributing

Pull the repository:
```
git clone https://github.com/ROITI-Ltd/alsi-py.git
cd ./alsi-py
```

Set up your working environment:
```
python3 -m venv env
source env/bin/activate
```

Install required packages:
```
pip3 install -r requirements.txt
pip3 install -r requirements-dev.txt
```

Bumping the package version after making changes:
``` 
bumpversion major|minor|patch|build 
``` 

For more general guidelines on contributing see: [Contributing to alsi-py](https://github.com/ROITI-Ltd/alsi-py/blob/main/CONTRIBUTING.md).