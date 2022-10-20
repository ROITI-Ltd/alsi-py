from typing import Union

from gie.mappings.agsi_company import AGSICompany
from gie.mappings.agsi_country import AGSICountry
from gie.mappings.agsi_facility import AGSIFacility
from gie.mappings.alsi_company import ALSICompany
from gie.mappings.alsi_country import ALSICountry
from gie.mappings.alsi_facility import ALSIFacility


def lookup_agsi_company(key: Union[AGSICompany, str]) -> AGSICompany:
    """Key lookup for AGSICompany

    If the key is already of type AGSICompany, returns it immediately.

    Parameters
    ----------
    key : Union[AGSICompany, str]
        The key to use for the lookup.

    Returns
    -------
    AGSICompany
        The corresponding instance of AGSICompany for which
        the value equals the lookup key.

    Raises
    ------
    ValueError
        If `key` does not represent a valid company.
    """

    if isinstance(key, AGSICompany):
        return key
    else:
        try:
            return AGSICompany[key]
        except KeyError:
            try:
                return [obj for obj in AGSICompany if obj.value == key][0]
            except IndexError:
                raise ValueError("The company string provided is invalid!")


# Checking the provided facility string in our base enums
def lookup_facility_agsi(key: Union[AGSIFacility, str]) -> AGSIFacility:
    """Key lookup for AGSIFacility

    If the key is already of type AGSIFacility, returns it immediately.

    Parameters
    ----------
    key : Union[AGSIFacility, str]
        The key to use for the lookup.

    Returns
    -------
    AGSIFacility
        The corresponding instance of AGSIFacility for which
        the value equals the lookup key.

    Raises
    ------
    ValueError
        If `key` does not represent a valid company.
    """

    if isinstance(key, AGSIFacility):
        return key
    else:
        try:
            return AGSIFacility[key]
        except KeyError:

            try:
                return [obj for obj in AGSIFacility if obj.value == key][0]
            except IndexError:
                raise ValueError("The storage string provided is invalid!")


def lookup_country_agsi(key: Union[AGSICountry, str]) -> AGSICountry:
    if isinstance(key, AGSICountry):
        return key
    else:
        try:
            return AGSICountry[key]
        except KeyError:
            try:
                return [obj for obj in AGSICountry if obj.value == key][0]
            except IndexError:
                raise ValueError("The country string provided is invalid!")


def lookup_alsi_company(key: Union[ALSICompany, str]) -> ALSICompany:
    if isinstance(key, ALSICompany):
        return key
    else:
        try:
            return ALSICompany[key]
        except KeyError:
            try:
                return [obj for obj in ALSICompany if obj.value == key][0]
            except IndexError:
                raise ValueError("Invalid lso string")


def lookup_facility_alsi(key: Union[ALSIFacility, str]) -> ALSIFacility:
    if isinstance(key, ALSIFacility):
        return key
    else:
        try:
            return ALSIFacility[key]
        except KeyError:
            try:
                return [obj for obj in ALSIFacility if obj.value == key][0]
            except IndexError:
                raise ValueError("Invalid terminal string")


def lookup_country_alsi(key: Union[ALSICountry, str]) -> ALSICountry:
    if isinstance(key, ALSICountry):
        return key
    else:
        try:
            return ALSICountry[key]
        except KeyError:
            try:
                return [obj for obj in ALSICountry if obj.value == key][0]
            except IndexError:
                raise ValueError("Invalid country string")
