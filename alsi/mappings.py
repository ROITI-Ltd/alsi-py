from enum import Enum
from typing import Union
from .exceptions import InvalidCountryException


def retrieve_country(input: Union["Area", str]) -> "Area":
    if isinstance(input, Area):
        return input
    if isinstance(input, str):
        if Area.has_member(input.upper()):
            return Area[input.upper()]

        check_country = [
            area
            for area in Area
            if area._country_name.lower() == input.lower()
            or area.code.lower() == input.lower()
        ]

        if check_country:
            return check_country[0]
        else:
            raise InvalidCountryException("Invalid Country")

    raise TypeError(
        "Country input parameter can only be of type string or Area."
    )


class Area(Enum):
    def __new__(cls, *args, **kwargs):
        obj = object.__new__(cls)
        obj._value_ = args[0]
        return obj

    def __init__(self, _: str, country_name: str):
        self._country_name = country_name

    @property
    def name(self) -> str:
        return self._country_name

    @property
    def code(self) -> str:
        return self.value

    @classmethod
    def has_member(cls, member) -> bool:
        return member in cls.__members__

    def __str__(self) -> str:
        return self.value

    BE = ("BE", "Belgium")
    ES = ("ES", "Spain")
    ES_ = ("ES*", "Spain*")
    FR = ("FR", "France")
    GB_PRE_BREXIT = ("GB", "Great Britain (Pre Brexit)")
    GB_POST_BREXIT = ("GB*", "Great Britain (Post Brexit)")
    GR = ("GR", "Greece")
    HR = ("HR", "Croatia")
    IT = ("IT", "Italy")
    LT = ("LT", "Lithuania")
    NL = ("NL", "Netherlands")
    PL = ("PL", "Poland")
    PT = ("PT", "Portugal")
