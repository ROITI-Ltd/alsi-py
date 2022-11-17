import enum


class ALSICompany(enum.Enum):
    """ENUM containing 2 things about an Area: code, country"""

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

    def get_params(self):
        return {
            "country": self.country,
            "company": self.code,
        }

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
