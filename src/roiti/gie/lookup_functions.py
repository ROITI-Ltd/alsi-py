from typing import Union

from .mappings.agsi_company import AGSICompany
from .mappings.agsi_country import AGSICountry
from .mappings.agsi_facility import AGSIFacility
from .mappings.alsi_company import ALSICompany
from .mappings.alsi_country import ALSICountry
from .mappings.alsi_facility import ALSIFacility


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
            except IndexError as err:
                raise ValueError(
                    "The company string provided is invalid!"
                ) from err


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
            except IndexError as err:
                raise ValueError("The facility provided is invalid!") from err


def lookup_country_agsi(key: Union[AGSICountry, str]) -> AGSICountry:
    """Key lookup for AGSICountry

    Parameters
    ----------
    key: Union[AGSICountry, str]
        The key to use for the lookup.

    Returns
    -------
    AGSICountry
        The corresponding instance of AGSICountry for which
        the value equals the lookup key.

    Raises
    ------
    ValueError
        If 'key' does not represent a valid country.

    """
    if isinstance(key, AGSICountry):
        return key
    else:
        try:
            return AGSICountry[key]
        except KeyError:
            try:
                return [obj for obj in AGSICountry if obj.value == key][0]
            except IndexError as err:
                raise ValueError(
                    "The country string provided is invalid!"
                ) from err


def lookup_alsi_company(key: Union[ALSICompany, str]) -> ALSICompany:
    """Key lookup for ALSICompany

    Parameters
    ----------
    key: Union[ALSICompany, str]
        The key to use for the lookup.

    Returns
    -------
    AGSICompany
        The corresponding instance of ALSICompany for which
        the value equals the lookup key.

    Raises
    ------
    ValueError
        If 'key' does not represent a valid company.

    """
    if isinstance(key, ALSICompany):
        return key
    else:
        try:
            return ALSICompany[key]
        except KeyError:
            try:
                return [obj for obj in ALSICompany if obj.value == key][0]
            except IndexError as err:
                raise ValueError(
                    "The company string provided is invalid!"
                ) from err


def lookup_facility_alsi(key: Union[ALSIFacility, str]) -> ALSIFacility:
    """Key lookup for ALSIFacility

    If the key is already of type ALSIFacility, returns it immediately.

    Parameters
    ----------
    key : Union[ALSIFacility, str]
        The key to use for the lookup.

    Returns
    -------
    ALSIFacility
        The corresponding instance of ALSIFacility for which
        the value equals the lookup key.

    Raises
    ------
    ValueError
        If `key` does not represent a valid company.
    """
    if isinstance(key, ALSIFacility):
        return key
    else:
        try:
            return ALSIFacility[key]
        except KeyError:
            try:
                return [obj for obj in ALSIFacility if obj.value == key][0]
            except IndexError as err:
                raise ValueError(
                    "The facility string provided is invalid!"
                ) from err


def lookup_country_alsi(key: Union[ALSICountry, str]) -> ALSICountry:
    """Key lookup for ALSICountry

    Parameters
    ----------
    key: Union[ALSICountry, str]
        The key to use for the lookup.

    Returns
    -------
    ALSICountry
        The corresponding instance of ALSICountry for which
        the value equals the lookup key.

    Raises
    ------
    ValueError
        If 'key' does not represent a valid country.

    """
    if isinstance(key, ALSICountry):
        return key
    else:
        try:
            return ALSICountry[key]
        except KeyError:
            try:
                return [obj for obj in ALSICountry if obj.value == key][0]
            except IndexError as err:
                raise ValueError(
                    "The country string provided is invalid!"
                ) from err
