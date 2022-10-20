import enum


class APIType(str, enum.Enum):
    AGSI = "https://agsi.gie.eu/api"
    ALSI = "https://alsi.gie.eu/api"
