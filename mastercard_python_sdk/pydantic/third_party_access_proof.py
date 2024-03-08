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


class ThirdPartyAccessProof(BaseModel):
    # The digital signature for the \"receipt\" portion of the access key
    signature: typing.Optional[str] = Field(None, alias='signature')

    # The Finicity key identifier is used to sign the access key
    key_id: typing.Optional[str] = Field(None, alias='keyId')

    # A date-time with time zone
    timestamp: typing.Optional[datetime] = Field(None, alias='timestamp')
    class Config:
        arbitrary_types_allowed = True
