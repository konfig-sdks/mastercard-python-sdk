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


class ThirdPartyAccessProvenance(BaseModel):
    # Calling client identifier
    client_fingerprint: typing.Optional[str] = Field(None, alias='clientFingerprint')

    # Calling client IP address
    ip_address: typing.Optional[str] = Field(None, alias='ipAddress')

    # Calling client cookie
    token: typing.Optional[str] = Field(None, alias='token')
    class Config:
        arbitrary_types_allowed = True
