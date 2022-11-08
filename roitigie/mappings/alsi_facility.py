import enum


class ALSIFacility(enum.Enum):
    """Enum containing 3 things about an Area: code, country, code company"""

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

    def get_params(self):
        return {
            "country": self.country,
            "company": self.company,
            "facility": self.code,
        }

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
