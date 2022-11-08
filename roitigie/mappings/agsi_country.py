import enum


class AGSICountry(enum.Enum):
    """Enum contains 2 things: code and full name"""

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
