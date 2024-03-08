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


class SubscriptionRecord(BaseModel):
    # ID of a TxPush subscription
    id: int = Field(alias='id')

    # An account ID represented as a number
    account_id: int = Field(alias='accountId')

    # A TxPush subscription type (\"account\" or \"transaction\")
    type: str = Field(alias='type')

    # A callback URL where to receive TxPush notifications
    callback_url: str = Field(alias='callbackUrl')

    # Signing key for events
    signing_key: str = Field(alias='signingKey')
    class Config:
        arbitrary_types_allowed = True
