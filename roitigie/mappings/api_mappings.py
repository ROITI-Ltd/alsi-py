"""An API type enumerator"""
import enum


class APIType(str, enum.Enum):
    """Enumerator class for the two API types"""

    AGSI = "https://agsi.gie.eu/api/"
    ALSI = "https://alsi.gie.eu/api/"
