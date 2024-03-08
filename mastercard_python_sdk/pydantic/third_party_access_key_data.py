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

class ThirdPartyAccessKeyData(BaseModel):
    # A customer ID. See Add Customer API for how to create a customer ID.
    customer_id: str = Field(alias='customerId')

    # Your Partner ID displayed in the [Developer Dashboard](https://developer.mastercard.com/account/log-in)
    partner_id: str = Field(alias='partnerId')

    # Your Partner ID displayed in the [Developer Dashboard](https://developer.mastercard.com/account/log-in)
    third_party_partner_id: str = Field(alias='thirdPartyPartnerId')

    products: typing.List[ThirdPartyAccessProduct] = Field(alias='products')

    provenance: typing.Optional[ThirdPartyAccessProvenance] = Field(None, alias='provenance')
    class Config:
        arbitrary_types_allowed = True
