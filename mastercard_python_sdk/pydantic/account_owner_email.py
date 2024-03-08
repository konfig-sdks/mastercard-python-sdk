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


class AccountOwnerEmail(BaseModel):
    # The email is primary.
    is_primary: typing.Optional[bool] = Field(None, alias='isPrimary')

    # An email address
    email: typing.Optional[str] = Field(None, alias='email')

    # The account owner's email type.  * \"Personal\"  * \"Business\"
    email_type: typing.Optional[str] = Field(None, alias='emailType')
    class Config:
        arbitrary_types_allowed = True
