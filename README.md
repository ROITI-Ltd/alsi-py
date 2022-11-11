# ROITI LTD GIE APP 

Python client for the ALSI/AGSI APIs

Documentation of the API can be found on: <https://www.gie.eu/transparency-platform/GIE_API_documentation_v007.pdf>

Documentation of the client API can be found on: <https://petrofff93.github.io/agsi-py/>

### Installation

```sh
python -m pip install -i https://test.pypi.org/simple/ roiti-gie
```

### Usage

The package is split in two clients:

1. GieRawClient: Returns data in raw Python Dict.
2. GiePandasClient: Returns parsed data in the form of a pandas DataFrame.

```python
import asyncio

from roiti.gie.gie_pandas_client import GiePandasClient
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

```python
"""All possible use cases of the AGSI/ALSI queries.
Each query from our service could be triggered only with the simple variable (below)
passed as an argument (and of course you could add dates, size and other query params)
"""


# All AGSI companies (please use the variable names for your queries)

astora = "21X000000001160J", "AT"
gsa = "25X-GSALLC-----E", "AT"
omv_gas_storage = "25X-OMVGASSTORA5", "AT"
rag_energy_storage = "23X----100225-1C", "AT"
uniper_energy_storage_at = "21X000000001127H", "AT"
fluxys = "21X-BE-A-A0A0A-Y", "BE"
bulgartransgaz = "21X-BG-A-A0A0A-C", "BG"
psp = "31X-PSP-OSS-HR-D", "HR"
mnd_energy_storage = "27XG-MNDGS-CZ--R", "CZ"
moravia_gas_storage = "27X-MORAVIAGS--E", "CZ"
rwe_gas_storage_cz = "27XG-RWE-GAS-STI", "CZ"
spp_storage = "27X-SPPSTORAGE-R", "CZ"
gsd = "21X000000001104T", "DK"
storengy = "21X000000001083B", "FR"
terega = "21X-FR-B-A0A0A-J", "FR"
astora_germany = "21X000000001160J", "DE"
bayernugs = "37X0000000000151", "DE"
bes = "37X0000000000224", "DE"
edf_gas_deutschland = "37X000000000152S", "DE"
enbw_etzel_speicher = "11X0-0000-0667-8", "DE"
eneco_gasspeicher = "21X0000000010849", "DE"
enovos_storage = "**TOBEPROVIDED**", "DE"
equinor_storage_deutschland = "21X000000001368W", "DE"
erdgasspeicher_peissen = "21X000000001297T", "DE"
ekb = "21X000000001080H", "DE"
ewe_gasspeicher = "21X0000000011756", "DE"
hansewerk = "21X0000000013805", "DE"
kge = "21X000000001140P", "DE"
met_speicher = "37X000000000047P", "DE"
mnd_energy_storage_germany = "37X000000000042Z", "DE"
n_ergie = "11XNERGIE------1", "DE"
nafta_speicher_inzenham = "21X0000000011748", "DE"
nuon_epe_gasspeicher = "37X0000000000119", "DE"
omv_gas_storage_germany = "25X-OMVGASSTORA5", "DE"
rwe_gas_storage_west = "21X000000001262B", "DE"
stadtwerke_hannover = "11XSWHANNOVERAG3", "DE"
storengy_deutschland = "21X000000001072G", "DE"
swb_vertrieb_bremen = "11XSWB-BREMEN--I", "DE"
swkiel_speicher = "37X000000000051Y", "DE"
tep = "21X000000001307F", "DE"
total_etzel_gaslager = "**TOBEPROVIDED**", "DE"
trianel_gasspeicher_epe = "21X000000001310Q", "DE"
uniper_energy_storage = "21X000000001127H", "DE"
vng_gasspeicher_gmbh = "21X000000001138C", "DE"
hexum = "21X0000000013643", "HU"
hgs = "21X0000000013635", "HU"
kinsale_energy = "47X0000000000584", "IE"
edison_stoccaggio = "21X0000000013651", "IT"
igs = "59X4-IGSTORAGE-T", "IT"
stogit = "21X000000001250I", "IT"
conexus_baltic_grid = "21X000000001379R", "LV"
energystock = "21X000000001057C", "NL"
ewe_gasspeicher_nl = "21X0000000011756", "NL"
nam = "21X000000001075A", "NL"
taqa_gas_storage = "21X000000001120V", "NL"
taqa_piek_gas = "21X0000000013732", "NL"
gsp = "53XPL000000OSMP5", "PL"
ren_armazenagem = "21X0000000013627", "PT"
depomures = "21X000000001300T", "RO"
depogaz_ploiesti = "21X-DEPOGAZ-AGSI", "RO"
nafta = "42X-NAFTA-SK---U", "SK"
pozagas = "42X-POZAGAS-SK-V", "SK"
enagas_gts = "21X0000000013368", "ES"
swedegas = "21X-SE-A-A0A0A-F", "SE"
centrica_storage = "21X000000001022V", "GB"
edf = "23X-EDFE-------W", "GB"
humbly_grove_energy = "55XHUMBLYGROVE1H", "GB"
scottish_power = "23XSCOTTISHPOWEF", "GB"
sse_gas_storage = "23X--140207-SSE9", "GB"
storengy_uk = "48XSTORENGYUK01P", "GB"
uniper_energy_storage_ltd = "21X0000000013716", "GB"

# All AGSI countries (please use the variable names for your queries)

AT = "AT", "Austria"
BE = "BE", "Belgium"
BG = "BG", "Bulgaria"
HR = "HR", "Croatia"
CZ = "CZ", "Czech Republic"
DK = "DK", "Denmark"
FR = "FR", "France"
DE = "DE", "Germany"
HU = "HU", "Hungary"
IE = "IE", "Ireland"
IT = "IT", "Italy"
LV = "LV", "Latvia"
NL = "NL", "Netherlands"
PL = "PL", "Poland"
PT = "PT", "Portugal"
RO = "RO", "Romania"
SK = "SK", "Slovakia"
ES = "ES", "Spain"
SE = "SE", "Sweden"
GB_pre = "GB", "United Kingdom (Pre-Brexit)"
RS = "RS", "Serbia"
UA = "UA", "Ukraine"
GB = "GB*", "United Kingdom (Post-Brexit)"

# ALL AGSI facilities (please use the variable names for your queries)

ugs_haidach_astora = "21W000000000078N", "AT", "21X000000001160J"
ugs_haidach_gsa = "25W-SPHAID-GAZ-M", "AT", "25X-GSALLC-----E"
vgs_omv_tallesbrunn = "21W000000000081Y", "AT", "25X-OMVGASSTORA5"
rag_puchkirchen_haag = "21W000000000079L", "AT", "23X----100225-1C"
ugs_7_fields_uniper = "21W000000000057V", "AT", "21X000000001127H"
ugs_loenhout = "21Z000000000102A", "BE", "21X-BE-A-A0A0A-Y"
ugs_chiren = "21W000000000031C", "BG", "21X-BG-A-A0A0A-C"
ugs_okoli = "21W000000000077P", "HR", "31X-PSP-OSS-HR-D"
ugs_uhrice = "21W000000000075T", "CZ", "27XG-MNDGS-CZ--R"
ugs_damborice = "21W000000000102F", "CZ", "27X-MORAVIAGS--E"
vgs_rwe_haje = "21W000000000076R", "CZ", "27XG-RWE-GAS-STI"
ugs_dolni_bojanovice = "21W000000000074V", "CZ", "27X-SPPSTORAGE-R"
vgs_gsd_lille_torup_stenlille = (
        "45W000000000112V",
        "DK",
        "21X000000001104T",
    )
vgs_saline_tersanne_etrez_manosque = (
        "21W000000000084S",
        "FR",
        "21X000000001083B",
    )
vgs_sediane_saintilliers = "21W0000000000710", "FR", "21X000000001083B"
vgs_sediane_b_gournay = "21W0000000000702", "FR", "21X000000001083B"
vgs_serene_atlantique_chemery = (
        "63W197197128864M",
        "FR",
        "21X000000001083B",
    )
vgs_serene_nord_trois_fontaines_labbaye = (
        "21W000000000073X",
        "FR",
        "21X000000001083B",
    )
vgs_lussagnet_terega = "21W000000000068Q", "FR", "21X-FR-B-A0A0A-J"
ugs_jemgum_h_astora = "21W0000000001148", "DE", "21X000000001160J"
ugs_rehden = "21Z000000000271O", "DE", "21X000000001160J"
vsp_nord_rehden_jemgum = "21W0000000001261", "DE", "21X000000001160J"
ugs_wolfersberg = "21W0000000000184", "DE", "37X0000000000151"
ugs_berlin = "21W0000000001083", "DE", "37X0000000000224"
vgs_ugs_etzel_edf = "37W000000000003M", "DE", "37X000000000152S"
vgs_ugs_etzel_enbw = "11W0-0000-0432-M", "DE", "11X0-0000-0667-8"
ugs_enschede_epe_eneco = "21W000000000012G", "DE", "21X0000000010849"
ugs_frankenthal = "37Z0000000034538", "DE", "**TOBEPROVIDED**"
ugs_etzel_egl_equinor_storage_deutschland = (
        "21W000000000100J",
        "DE",
        "21X000000001368W",
    )
ugs_katharina = "21W0000000000281", "DE", "21X000000001297T"
ugs_etzel_ekb = "21Z000000000291I", "DE", "21X000000001080H"
ewe_h = "37W000000000002O", "DE", "21X0000000011756"
ugs_ewe_l = "21W0000000001075", "DE", "21X0000000011756"
ugs_jemgum_h_ewe = "21W0000000000508", "DE", "21X0000000011756"
ugs_nuttermoor_h_2 = "21W000000000104B", "DE", "21X0000000011756"
ugs_nuttermoor_h_3 = "21W000000000103D", "DE", "21X0000000011756"
ugs_nuttermoor_l_gud = "21W0000000001067", "DE", "21X0000000011756"
ugs_rudersdorf_h = "21W000000000048W", "DE", "21X0000000011756"
ugs_kraak = "21W000000000020H", "DE", "21X0000000013805"
ugs_epe_kge = "21W000000000097J", "DE", "21X000000001140P"
ugs_etzel_ese_met = "21W000000000055Z", "DE", "37X000000000047P"
ugs_reckrod = "21W0000000000540", "DE", "37X000000000047P"
vgs_zone_mnd_esg_ugs_stockstadt = (
        "37Y000000000386Q",
        "DE",
        "37X000000000042Z",
    )
ugs_eschenfelden_nergie = "21Z000000000321Z", "DE", "11XNERGIE------1"
ugs_inzenham_west = "21W0000000000192", "DE", "21X0000000011748"
ugs_enschede_epe_nuon = "21W000000000005D", "DE", "37X0000000000119"
ugs_etzel_ese_omv = "21W000000000056X", "DE", "25X-OMVGASSTORA5"
innexpool_rwegsw = "21W000000000121B", "DE", "21X000000001262B"
ugs_epe_l_rwegsw = "21W0000000000532", "DE", "21X000000001262B"
ugs_epe_nl_rwegswest = "21W000000000003H", "DE", "21X000000001262B"
ugs_kalle_rwegswest = "21W000000000004F", "DE", "21X000000001262B"
ugs_stassfurt_rwegswest = "21W0000000000265", "DE", "21X000000001262B"
ugs_ronnenberg_empelde = "21Z0000000004002", "DE", "11XSWHANNOVERAG3"
ugs_fronhofen = "21W000000000091V", "DE", "21X000000001072G"
ugs_harsefeld = "21W000000000092T", "DE", "21X000000001072G"
ugs_lesum = "21W000000000090X", "DE", "21X000000001072G"
ugs_peckensen = "21W0000000000273", "DE", "21X000000001072G"
ugs_schmidhausen = "21W000000000089I", "DE", "21X000000001072G"
ugs_uelsen = "21W000000000093R", "DE", "21X000000001072G"
ugs_bremen_lesum_swb = "21W000000000090X", "DE", "11XSWB-BREMEN--I"
ugs_kiel_ronne = "21W0000000001164", "DE", "37X000000000051Y"
ugs_allmenhausen = "21W000000000030E", "DE", "21X000000001307F"
ugs_etzel_egl_total_etzel_gaslager = (
        "**TOBEPROVIDED**",
        "DE",
        "**TOBEPROVIDED**",
    )
ugs_epe_trianel = "21W000000000085Q", "DE", "21X000000001310Q"
ugs_bierwang = "21W0000000000613", "DE", "21X000000001127H"
ugs_breitbrunn = "21W0000000000605", "DE", "21X000000001127H"
ugs_epe_uniper_h = "21W000000000066U", "DE", "21X000000001127H"
ugs_epe_uniper_l = "21W000000000065W", "DE", "21X000000001127H"
ugs_eschenfelden_uniper = "21W000000000083U", "DE", "21X000000001127H"
ugs_etzel_erdgas_lager_egl = "21W000000000059R", "DE", "21X000000001127H"
ugs_etzel_ese_uniper_energy_storage = (
        "21W0000000000168",
        "DE",
        "21X000000001127H",
    )
ugs_krummhorn = "21W000000000067S", "DE", "21X000000001127H"
ugs_etzel_ese_vgs = "21W000000000120D", "DE", "21X000000001138C"
ugs_jemgum_h_vgs = "21W000000000128Y", "DE", "21X000000001138C"
vgs_storage_hub_bernburg = "21W0000000000427", "DE", "21X000000001138C"
vgs_vtp_storage_gpl = "21W0000000001091", "DE", "21X000000001138C"
ugs_szoreg_1 = "21W000000000086O", "HU", "21X0000000013643"
vgs_mfgt_pusztaederics = "21W000000000087M", "HU", "21X0000000013635"
ugs_kinsale_southwest = "47W000000000245J", "IE", "47X0000000000584"
vgs_edison_stoccaggio_collalto = (
        "21W000000000095N",
        "IT",
        "21X0000000013651",
    )
ugs_cornegliano = "59W-IGSTORAGE-0Q", "IT", "59X4-IGSTORAGE-T"
vgs_stogit_fiume_treste = "21Z000000000274I", "IT", "21X000000001250I"
ugs_incukalns = "21W000000000113A", "LV", "21X000000001379R"
ugs_energystock = "21W000000000006B", "NL", "21X000000001057C"
ugs_nuttermoor_h_1 = "21W0000000001059", "NL", "21X0000000011756"
ugs_grijpskerk = "21W000000000001L", "NL", "21X000000001075A"
ugs_norg_langelo = "21W000000000015A", "NL", "21X000000001075A"
ugs_bergermeer = "21W0000000000087", "NL", "21X000000001120V"
ugs_alkmaar = "21W000000000002J", "NL", "21X0000000013732"
gsp_historical_data_prior_to_4_feb_2014 = (
        "PRIOR_OSM_000001",
        "PL",
        "53XPL000000OSMP5",
    )
ugs_wierzchowice = "21Z000000000381H", "PL", "53XPL000000OSMP5"
vgs_gim_kawerna_kosakowo = "21Z000000000383D", "PL", "53XPL000000OSMP5"
vgs_gim_sanok_brzeznica = "21Z000000000382F", "PL", "53XPL000000OSMP5"
ugs_carrico = "16ZAS01--------8", "PT", "21X0000000013627"
ugs_targu_mures = "21Z000000000309P", "RO", "21X000000001300T"
ugs_balaceanca = "21Z0000000003111", "RO", "21X-DEPOGAZ-AGSI"
ugs_bilciuresti = "21Z000000000313Y", "RO", "21X-DEPOGAZ-AGSI"
ugs_cetatea_de_balta = "21Z000000000316S", "RO", "21X-DEPOGAZ-AGSI"
ugs_ghercesti = "21Z000000000315U", "RO", "21X-DEPOGAZ-AGSI"
ugs_sarmasel = "21Z000000000314W", "RO", "21X-DEPOGAZ-AGSI"
ugs_urziceni = "21Z0000000003103", "RO", "21X-DEPOGAZ-AGSI"
ugs_lab_incl_gajary_baden = "21W000000000088K", "SK", "42X-NAFTA-SK---U"
ugs_lab_iv_pozagas = "21W000000000047Y", "SK", "42X-POZAGAS-SK-V"
vgs_enagas_serrablo = "21W000000000032A", "ES", "21X0000000013368"
ugs_skallen = "21W0000000000435", "SE", "21X-SE-A-A0A0A-F"
ugs_rough = "21W000000000094P", "GB", "21X000000001022V"
ugs_holehouse_farm_storage = "21Z000000000227R", "GB", "23X-EDFE-------W"
ugs_humbly_grove = "55WHUMBLY1GROVER", "GB", "55XHUMBLYGROVE1H"
ugs_hatfield_moors_storage = "21Z000000000229N", "GB", "23XSCOTTISHPOWEF"
ugs_aldbrough_i = "55WALDBOROUGH00H", "GB", "23X--140207-SSE9"
ugs_atwick = "55WATWICK-SSE00J", "GB", "23X--140207-SSE9"
ugs_stublach = "21W000000000101H", "GB", "48XSTORENGYUK01P"
ugs_holford = "21W000000000112C", "GB", "21X0000000013716"

# ALL ALSI companies (please use the variable names for your queries)

fluxys_lng = "21X000000001006T", "BE"
lng_croatia = "31X-LNG-HR-----7", "HR"
elengy = "21X0000000010679", "FR"
dunkerque_lng = "21X000000001331I", "FR"
fosmax_lng = "21X000000001070K", "FR"
desfa = "21X-GR-A-A0A0A-G", "GR"
gnl_italia = "26X00000117915-0", "IT"
olt_offshore_lng_toscana = "21X000000001109G", "IT"
adriatic_lng = "21X000000001360B", "IT"
klaipedos_nafta = "21X0000000013740", "LT"
eemsenergy_terminal = "52X000000000088H", "NL"
gate_terminal = "21X000000001063H", "NL"
gaz_system = "21X-PL-A-A0A0A-B", "PT"
ren_atlantico = "21X0000000013619", "PT"
bbg = "21X000000001352A", "ES"
enagas_transporte = "21X000000001254A", "ES"
saggas = "18XTGPRS-12345-G", "ES"
reganosa = "18XRGNSA-12345-V", "ES"
national_grid_grain_lng = "21X-GB-A-A0A0A-7", "GB"
south_hook_lng = "21X0000000013554", "GB"
all_spanish_terminals = "21X0000000013368", "ES*"
national_grid_grain_lng_post_brexit = "21X-GB-A-A0A0A-7", "GB*"
south_hook_lng_post_brexit = "21X0000000013554", "GB*"

# ALL ALSI countries (pelase use the variable names for your queries)

BE = "BE", "Belgium"
HR = "HR", "Croatia"
FR = "FR", "France"
GR = "GR", "Greece"
IT = "IT", "Italy"
LT = "LT", "Lithuania"
NL = "NL", "Netherlands"
PL = "PL", "Poland"
PT = "PT", "Portugal"
ES = "ES", "Spain"

# ALL ALSI facilities (pelase use the variable names for your queries)

zeebrugge = "21W0000000001245", "BE", "21X000000001006T"
bilbao = "21W0000000000362", "ES", "21X000000001352A"
barcelona = "21W000000000039X", "ES", "21X000000001254A"
cartagena = "21W000000000038Z", "ES", "21X000000001254A"
huelva = "21W0000000000370", "ES", "21X000000001254A"
sagunto = "21W0000000000354", "ES", "18XTGPRS-12345-G"
mugardos = "21W0000000000338", "ES", "18XRGNSA-12345-V"
tvb_virtual_balancing_lng_tank = (
        "18W000000000GVMT",
        "ES",
        "21X0000000013368",
    )
fos_tonkin = "63W179356656691A", "FR", "21X0000000010679"
montoir_de_bretagne = "63W631527814486R", "FR", "21X0000000010679"
dunkerque = "21W0000000000451", "FR", "21X000000001331I"
fos_cavaou = "63W943693783886F", "FR", "21X000000001070K"
isle_of_grain = "21W000000000099F", "GB", "21X-GB-A-A0A0A-7"
south_hook = "21W0000000000419", "GB", "21X0000000013554"
revythoussa = "21W000000000040B", "GR", "21X-GR-A-A0A0A-G"
krk_fsru = "31W-0000-G-000-Z", "HR", "31X-LNG-HR-----7"
panigaglia = "59W0000000000011", "IT", "26X00000117915-0"
fsru_olt_offshore_lng_toscana = (
        "21W0000000000443",
        "IT",
        "21X000000001109G",
    )
porto_levante = "21W000000000082W", "IT", "21X000000001360B"
fsru_independence = "21W0000000001253", "LT", "21X0000000013740"
rotterdam_gate = "21W0000000000079", "NL", "21X000000001063H"
swinoujscie = "21W000000000096L", "PL", "21X-PL-A-A0A0A-B"
sines = "16WTGNL01------O", "PT", "21X0000000013619"
eemsenergy_lng = "52W000000000001W", "LT", "52X000000000088H"
```

### For more information regarding company codes, facility codes and country codes visit: <https://alsi.gie.eu/#/api>

### Running unit tests

Tell pytest where to look for unit tests and create env for ALSI API key

- On Unix

  ```sh
  export PYTHONPATH=./roiti
  export API_KEY='<API_KEY>'
  ```

- On Windows

  ```powershell
  $env:PYTHONPATH='./roitigie'
  $env:API_KEY='<API_KEY>'
  ```

Run unit tests in coverage mode

```sh
python -m pytest ./tests --import-mode=append --cov
```

### Contributing

Pull the repository:

```sh
git clone https://github.com/Petrofff93/agsi-py.git
cd ./roiti
```

Set up your working environment:

1. Create virtual environment

   ```sh
   python -m venv venv
   ```

2. Activate the virtual environment

   - On UNIX system

     ```sh
     source venv/bin/activate
     ```

   - On Windows system

     ```powershell
     ./venv/Scripts/activate
     ```

Install required packages:

```sh
python -m pip install -r requirements.txt
```

Bumping the package version after making changes:

```sh
bumpversion major|minor|patch|build
```
