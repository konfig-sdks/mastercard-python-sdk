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

from mastercard_python_sdk.type.new_address import NewAddress
from mastercard_python_sdk.type.phone_number_format import PhoneNumberFormat

class RequiredNewBusiness(TypedDict):
    # The legal name of the business
    name: str

    # Indicates whether a business owner is personally liable for a loan
    personallyLiable: bool

    address: NewAddress

    phoneNumber: PhoneNumberFormat

class OptionalNewBusiness(TypedDict, total=False):
    # A URL for the business website
    url: str

    # An email address
    email: str

    # The business type eg LLC, Corp, S Corp, C Corp, B Corp, Sole Propriertorship, Nonprofit, etc.
    type: str

    # Provide details of the tax id for the business
    taxId: str

class NewBusiness(RequiredNewBusiness, OptionalNewBusiness):
    pass
