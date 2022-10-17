import enum
from typing import Union


# Checking the provided company string in our base enums
def lookup_alsi_company(input_string: Union["ALSICompany", str]) -> "ALSICompany":
    if isinstance(input_string, ALSICompany):
        return input_string
    else:
        try:
            return ALSICompany[input_string]
        except KeyError:
            try:
                return [obj for obj in ALSICompany if obj.value == input_string][0]
            except IndexError:
                raise ValueError("Invalid lso string")


# Checking the provided facility string in our base enums
def lookup_facility_alsi(input_string: Union["ALSIFacility", str]) -> "ALSIFacility":
    if isinstance(input_string, ALSIFacility):
        return input_string
    else:
        try:
            return ALSIFacility[input_string]
        except KeyError:
            try:
                return [obj for obj in ALSIFacility if obj.value == input_string][0]
            except IndexError:
                raise ValueError("Invalid terminal string")


# Checking the provided country string in our base enums
def lookup_country_alsi(input_string: Union["ALSICountry", str]) -> "ALSICountry":
    if isinstance(input_string, ALSICountry):
        return input_string
    else:
        try:
            return ALSICountry[input_string]
        except KeyError:
            try:
                return [obj for obj in ALSICountry if obj.value == input_string][0]
            except IndexError:
                raise ValueError("Invalid country string")


class ALSICountry(enum.Enum):
    """
    ENUM contains 2 things: code and full name
    """

    def __new__(cls, *args, **kwargs):
        obj = object.__new__(cls)
        obj._value_ = args[0]
        return obj

    def __init__(self, _: str, full_name: str):
        self._full_name = full_name

    def __str__(self):
        return self.value

    @property
    def full_name(self):
        return self._full_name

    @property
    def code(self):
        return self.value

    def get_url(self):
        return "?" + "country=" + self.code

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


class ALSICompany(enum.Enum):
    """
    ENUM containing 2 things about an Area: code, country
    """

    def __new__(cls, *args, **kwargs):
        obj = object.__new__(cls)
        obj._value_ = args[0]
        return obj

    def __init__(self, _: str, country: str):
        self._country = country

    def __str__(self):
        return self.value

    @property
    def country(self):
        return self._country

    @property
    def code(self):
        return self.value

    def get_url(self):
        return "?country=" + self.country + "&company=" + self.code

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


class ALSIFacility(enum.Enum):
    """
    ENUM containing 3 things about an Area: code, country, code company
    """

    def __new__(cls, *args, **kwargs):
        obj = object.__new__(cls)
        obj._value_ = args[0]
        return obj

    def __init__(self, _: str, country: str, company: str):
        self._country = country
        self._company = company

    def __str__(self):
        return self.value

    @property
    def company(self):
        return self._company

    @property
    def country(self):
        return self._country

    @property
    def code(self):
        return self.value

    def get_url(self):
        return (
            "?"
            + "country="
            + self.country
            + "&company="
            + self.company
            + "&facility="
            + self.code
        )

    zeebrugge = "21W0000000001245", "BE", "21X000000001006T"
    bilbao = "21W0000000000362", "ES", "21X000000001352A"
    barcelona = "21W000000000039X", "ES", "21X000000001254A"
    cartagena = "21W000000000038Z", "ES", "21X000000001254A"
    huelva = "21W0000000000370", "ES", "21X000000001254A"
    sagunto = "21W0000000000354", "ES", "18XTGPRS-12345-G"
    mugardos = "21W0000000000338", "ES", "18XRGNSA-12345-V"
    tvb_virtual_balancing_lng_tank = "18W000000000GVMT", "ES", "21X0000000013368"
    fos_tonkin = "63W179356656691A", "FR", "21X0000000010679"
    montoir_de_bretagne = "63W631527814486R", "FR", "21X0000000010679"
    dunkerque = "21W0000000000451", "FR", "21X000000001331I"
    fos_cavaou = "63W943693783886F", "FR", "21X000000001070K"
    isle_of_grain = "21W000000000099F", "GB", "21X-GB-A-A0A0A-7"
    south_hook = "21W0000000000419", "GB", "21X0000000013554"
    revythoussa = "21W000000000040B", "GR", "21X-GR-A-A0A0A-G"
    krk_fsru = "31W-0000-G-000-Z", "HR", "31X-LNG-HR-----7"
    panigaglia = "59W0000000000011", "IT", "26X00000117915-0"
    fsru_olt_offshore_lng_toscana = "21W0000000000443", "IT", "21X000000001109G"
    porto_levante = "21W000000000082W", "IT", "21X000000001360B"
    fsru_independence = "21W0000000001253", "LT", "21X0000000013740"
    rotterdam_gate = "21W0000000000079", "NL", "21X000000001063H"
    swinoujscie = "21W000000000096L", "PL", "21X-PL-A-A0A0A-B"
    sines = "16WTGNL01------O", "PT", "21X0000000013619"
    eemsenergy_lng = "52W000000000001W", "LT", "52X000000000088H"
