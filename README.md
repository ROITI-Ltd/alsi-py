# alsi-py

Python client for the ALSI API (Aggregated LNG Storage Inventory)

Documentation of the API can be found on: <https://alsi.gie.eu/GIE_API_documentation_v004.pdf>

Documentation of the client API can be found on: <https://roiti-ltd.github.io/alsi-py/>

### Installation

```sh
python3 -m pip3 install alsi-py
```

### Usage

The package is split in two clients:

1. AlsiRawClient: Returns data in raw JSON format.
2. AlsiPandasClient: Returns parsed data in the form of a pandas dataframe.

```python
from alsi.raw_client import AlsiRawClient
from alsi.pandas_client import AlsiPandasClient
from alsi.mappings import Area
from datetime import datetime
import asyncio

API_KEY = "<API_KEY>"

country_code = Area.ES  # Also could be string: 'ES' or 'Spain'
company_code = "21X000000001254A"
facility_code = "21W0000000000370"

async def main():
    client = AlsiRawClient(api_key=API_KEY)
    # Functions that return JSON.
    await client.query_data_for_facility(facility_code, company_code, country_code)
    await client.query_agg_data_for_europe_or_noneurope(europe="eu")
    await client.query_agg_data_by_country(country_code="BE")
    await client.query_data_by_company_and_country(company_code, country_code)

    # Filter results by time
    await client.query_agg_data_by_country(
        country_code,
        start=datetime(2017, 1, 1),
        end=datetime(2018, 1, 1),
        limit=10,
    )

    # Create pandas client. All functions are the same as the raw client.
    pandas_client = AlsiPandasClient(api_key=API_KEY)
    # In the end of the code, make sure to close the client session:
    await client.close_session()
    # or
    await pandas_client.close_session()

loop = asyncio.new_event_loop()
loop.run_until_complete(main())
```

### For more information regarding company codes, facility codes and country codes visit: <https://alsi.gie.eu/#/api>

### Running unit tests

Tell pytest where to look for unit tests and create env for ALSI API key

* On Unix
  
    ```bash
    export PYTHONPATH=./alsi
    export ALSI_KEY='...'
    ```

* On Windows
  
    ```powershell
    $env:PYTHONPATH='./alsi'
    $env:ALSI_KEY='...'
    ```

#### Run unit tests in coverage mode

```sh
python -m pytest ./tests --import-mode=append --cov
```

### Contributing

Pull the repository:

```sh
git clone https://github.com/ROITI-Ltd/alsi-py.git
cd ./alsi-py
```

Set up your working environment:

1. Create virtual environment

    ```sh
    python3 -m venv env
    ```

2. Activate the virtual environment
   * On UNIX

        ```bash
        source env/bin/activate
        ```

   * On Windows
  
        ```sh
        ./env/Scripts/activate
        ```

Install required packages:

```sh
pip3 install -r requirements.txt
pip3 install -r requirements-dev.txt
```

Bumping the package version after making changes:

```sh
bumpversion major|minor|patch|build 
```

For more general guidelines on contributing see: [Contributing to alsi-py](https://github.com/ROITI-Ltd/alsi-py/blob/main/CONTRIBUTING.md).

### Inspiration

Many thanks to the [entsoe-py](https://github.com/EnergieID/entsoe-py) library for serving as inspiration for this library.
