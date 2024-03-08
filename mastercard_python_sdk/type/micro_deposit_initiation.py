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

from mastercard_python_sdk.type.receiver import Receiver

class RequiredMicroDepositInitiation(TypedDict):
    receiver: Receiver

class OptionalMicroDepositInitiation(TypedDict, total=False):
    # An institution login ID (from the account record)
    institutionLoginId: str

    # A callback URL where to receive micro deposit notifications
    callbackUrl: str

class MicroDepositInitiation(RequiredMicroDepositInitiation, OptionalMicroDepositInitiation):
    pass
