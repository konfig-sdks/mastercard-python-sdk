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

class RequiredPortfolioConsumer(TypedDict):
    # A consumer ID. See Create Consumer API for how to create a consumer ID.
    id: str

    # The first name of the account holder
    firstName: str

    # The last name of the account holder
    lastName: str

    # A customer ID represented as a number. See Add Customer API for how to create a customer ID.
    customerId: int

    # A full SSN with or without hyphens
    ssn: str

    birthday: Birthday

class OptionalPortfolioConsumer(TypedDict, total=False):
    # A generational or academic suffix
    suffix: str

class PortfolioConsumer(RequiredPortfolioConsumer, OptionalPortfolioConsumer):
    pass
