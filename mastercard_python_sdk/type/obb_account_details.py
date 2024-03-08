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

from mastercard_python_sdk.type.obb_account_owner import ObbAccountOwner
from mastercard_python_sdk.type.obb_institution import ObbInstitution

class RequiredObbAccountDetails(TypedDict):
    accountOwner: ObbAccountOwner

    # An account ID represented as a number
    id: int

    institution: ObbInstitution

class OptionalObbAccountDetails(TypedDict, total=False):
    # The account number from a financial institution in truncated format
    accountNumberDisplay: str

    # A timestamp showing the last aggregation attempt. This will not be present until you have run your first aggregation for the account.
    aggregationAttemptDate: str

    # The status of the most recent aggregation attempt. This will not be present until you have run your first aggregation for the account
    aggregationStatusCode: int

    # A timestamp showing the last successful aggregation of the account. This will not be present until you have run your first aggregation for the account.
    aggregationSuccessDate: str

    # The currency of the account
    currency: str

    # Current reported balance of the account
    currentBalance: typing.Union[int, float]

    # An institution login ID (from the account record), represented as a number
    institutionLoginId: int

    # The account name from the institution
    name: str

    # The last 4 digits of the ACH account number
    realAccountNumberLast4: int

    # pending during account discovery, always active following successful account activation
    status: str

    # Account type, e.g. checking/saving
    type: str

class ObbAccountDetails(RequiredObbAccountDetails, OptionalObbAccountDetails):
    pass
