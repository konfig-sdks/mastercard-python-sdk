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


class RequiredPartnerCredentials(TypedDict):
    # Your Partner ID displayed in the [Developer Dashboard](https://developer.mastercard.com/account/log-in)
    partnerId: str

    # Your Partner Secret displayed in the [Developer Dashboard](https://developer.mastercard.com/account/log-in)
    partnerSecret: str

class OptionalPartnerCredentials(TypedDict, total=False):
    pass

class PartnerCredentials(RequiredPartnerCredentials, OptionalPartnerCredentials):
    pass
