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

class RequiredThirdPartyAccessReceipt(TypedDict):
    pass

class OptionalThirdPartyAccessReceipt(TypedDict, total=False):
    # A schema version of receipt
    version: str

    # Representation of the type of consent receipt
    profile: int

    # This is officially the Consent Receipt ID, but is aliased as the Access Key ID. This is a unique identifier managed by Finicity that points to the contents of this JSON document.
    receiptId: str

    # This is recipient's customerId represented as a pseudo identifier
    customerId: str

    # Your Partner ID displayed in the [Developer Dashboard](https://developer.mastercard.com/account/log-in)
    partnerId: str

    products: typing.List[ThirdPartyAccessProduct]

    provenance: ThirdPartyAccessProvenance

    # A date-time with time zone
    timestamp: datetime

class ThirdPartyAccessReceipt(RequiredThirdPartyAccessReceipt, OptionalThirdPartyAccessReceipt):
    pass
