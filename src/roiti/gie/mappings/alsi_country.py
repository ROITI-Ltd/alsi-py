import enum


class ALSICountry(enum.Enum):
    """ENUM contains 2 things: code and full name"""

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

    def get_params(self):
        return {
            "country": self.code,
        }

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
