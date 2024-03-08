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


class RequiredThirdPartyAccessProof(TypedDict):
    pass

class OptionalThirdPartyAccessProof(TypedDict, total=False):
    # The digital signature for the \"receipt\" portion of the access key
    signature: str

    # The Finicity key identifier is used to sign the access key
    keyId: str

    # A date-time with time zone
    timestamp: datetime

class ThirdPartyAccessProof(RequiredThirdPartyAccessProof, OptionalThirdPartyAccessProof):
    pass
