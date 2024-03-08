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


class AppFinancialInstitutionStatus(BaseModel):
    # The ID of a financial institution, represented as a number
    id: int = Field(alias='id')

    # Status of decryption keys for financial institution app registration
    decryption_key_activated: bool = Field(alias='decryptionKeyActivated')

    # A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    created_date: int = Field(alias='createdDate')

    # A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    last_modified_date: int = Field(alias='lastModifiedDate')

    # \"false\" indicates registration is still pending
    status: bool = Field(alias='status')

    # The application's abbreviated name
    abbrv_name: typing.Optional[str] = Field(None, alias='abbrvName')

    # An URL to a logo file
    logo_url: typing.Optional[str] = Field(None, alias='logoUrl')
    class Config:
        arbitrary_types_allowed = True
