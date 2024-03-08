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

from mastercard_python_sdk.type.third_party_access_product import ThirdPartyAccessProduct
from mastercard_python_sdk.type.third_party_access_provenance import ThirdPartyAccessProvenance

class RequiredThirdPartyAccessKeyData(TypedDict):
    # A customer ID. See Add Customer API for how to create a customer ID.
    customerId: str

    # Your Partner ID displayed in the [Developer Dashboard](https://developer.mastercard.com/account/log-in)
    partnerId: str

    # Your Partner ID displayed in the [Developer Dashboard](https://developer.mastercard.com/account/log-in)
    thirdPartyPartnerId: str

    products: typing.List[ThirdPartyAccessProduct]

class OptionalThirdPartyAccessKeyData(TypedDict, total=False):
    provenance: ThirdPartyAccessProvenance

class ThirdPartyAccessKeyData(RequiredThirdPartyAccessKeyData, OptionalThirdPartyAccessKeyData):
    pass
