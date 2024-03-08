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


class RequiredSubscriptionRecord(TypedDict):
    # ID of a TxPush subscription
    id: int

    # An account ID represented as a number
    accountId: int

    # A TxPush subscription type (\"account\" or \"transaction\")
    type: str

    # A callback URL where to receive TxPush notifications
    callbackUrl: str

    # Signing key for events
    signingKey: str

class OptionalSubscriptionRecord(TypedDict, total=False):
    pass

class SubscriptionRecord(RequiredSubscriptionRecord, OptionalSubscriptionRecord):
    pass
