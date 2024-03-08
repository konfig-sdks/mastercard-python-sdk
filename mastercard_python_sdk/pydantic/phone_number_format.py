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
from pydantic import BaseModel, Field, RootModel

from mastercard_python_sdk.pydantic.country_code_number import CountryCodeNumber
from mastercard_python_sdk.pydantic.new_phone_number import NewPhoneNumber

class PhoneNumberFormat(BaseModel):
    country_code: typing.Optional[CountryCodeNumber] = Field(None, alias='countryCode')

    phone_no: typing.Optional[NewPhoneNumber] = Field(None, alias='phoneNo')
    class Config:
        arbitrary_types_allowed = True
