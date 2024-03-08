# coding: utf-8

"""
    Open Banking

    OpenAPI specification for Finicity APIs.  Open Banking solutions in the US are provided by Finicity, a Mastercard company.

    The version of the OpenAPI document: 1.16.0
    Contact: apisupport@mastercard.com
    Created by: https://developer.mastercard.com/open-banking-us/documentation/support/
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from mastercard_python_sdk.type.birthday import Birthday

class RequiredConsumerUpdate(TypedDict):
    pass

class OptionalConsumerUpdate(TypedDict, total=False):
    # The first name of the account holder
    firstName: str

    # The last name of the account holder
    lastName: str

    # A street address
    address: str

    # City
    city: str

    # State
    state: str

    # A ZIP code
    zip: str

    # A phone number (max length 15).
    phone: str

    # A full SSN with or without hyphens
    ssn: str

    birthday: Birthday

    # An email address
    email: str

    # A generational or academic suffix
    suffix: str

class ConsumerUpdate(RequiredConsumerUpdate, OptionalConsumerUpdate):
    pass
