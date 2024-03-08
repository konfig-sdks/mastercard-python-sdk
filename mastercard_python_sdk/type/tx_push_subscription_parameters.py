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


class RequiredTxPushSubscriptionParameters(TypedDict):
    # A callback URL where to receive TxPush notifications
    callbackUrl: str

class OptionalTxPushSubscriptionParameters(TypedDict, total=False):
    pass

class TxPushSubscriptionParameters(RequiredTxPushSubscriptionParameters, OptionalTxPushSubscriptionParameters):
    pass
