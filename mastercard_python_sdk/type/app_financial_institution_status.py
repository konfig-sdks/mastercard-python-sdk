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


class RequiredAppFinancialInstitutionStatus(TypedDict):
    # The ID of a financial institution, represented as a number
    id: int

    # Status of decryption keys for financial institution app registration
    decryptionKeyActivated: bool

    # A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    createdDate: int

    # A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    lastModifiedDate: int

    # \"false\" indicates registration is still pending
    status: bool

class OptionalAppFinancialInstitutionStatus(TypedDict, total=False):
    # The application's abbreviated name
    abbrvName: str

    # An URL to a logo file
    logoUrl: str

class AppFinancialInstitutionStatus(RequiredAppFinancialInstitutionStatus, OptionalAppFinancialInstitutionStatus):
    pass
