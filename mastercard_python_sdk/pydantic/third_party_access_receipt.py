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

from mastercard_python_sdk.pydantic.third_party_access_product import ThirdPartyAccessProduct
from mastercard_python_sdk.pydantic.third_party_access_provenance import ThirdPartyAccessProvenance

class ThirdPartyAccessReceipt(BaseModel):
    # A schema version of receipt
    version: typing.Optional[str] = Field(None, alias='version')

    # Representation of the type of consent receipt
    profile: typing.Optional[int] = Field(None, alias='profile')

    # This is officially the Consent Receipt ID, but is aliased as the Access Key ID. This is a unique identifier managed by Finicity that points to the contents of this JSON document.
    receipt_id: typing.Optional[str] = Field(None, alias='receiptId')

    # This is recipient's customerId represented as a pseudo identifier
    customer_id: typing.Optional[str] = Field(None, alias='customerId')

    # Your Partner ID displayed in the [Developer Dashboard](https://developer.mastercard.com/account/log-in)
    partner_id: typing.Optional[str] = Field(None, alias='partnerId')

    products: typing.Optional[typing.List[ThirdPartyAccessProduct]] = Field(None, alias='products')

    provenance: typing.Optional[ThirdPartyAccessProvenance] = Field(None, alias='provenance')

    # A date-time with time zone
    timestamp: typing.Optional[datetime] = Field(None, alias='timestamp')
    class Config:
        arbitrary_types_allowed = True
