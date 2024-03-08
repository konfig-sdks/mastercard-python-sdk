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

from mastercard_python_sdk.pydantic.new_address import NewAddress
from mastercard_python_sdk.pydantic.phone_number_format import PhoneNumberFormat

class NewBusiness(BaseModel):
    # The legal name of the business
    name: str = Field(alias='name')

    # Indicates whether a business owner is personally liable for a loan
    personally_liable: bool = Field(alias='personallyLiable')

    address: NewAddress = Field(alias='address')

    phone_number: PhoneNumberFormat = Field(alias='phoneNumber')

    # A URL for the business website
    url: typing.Optional[str] = Field(None, alias='url')

    # An email address
    email: typing.Optional[str] = Field(None, alias='email')

    # The business type eg LLC, Corp, S Corp, C Corp, B Corp, Sole Propriertorship, Nonprofit, etc.
    type: typing.Optional[str] = Field(None, alias='type')

    # Provide details of the tax id for the business
    tax_id: typing.Optional[str] = Field(None, alias='taxId')
    class Config:
        arbitrary_types_allowed = True
