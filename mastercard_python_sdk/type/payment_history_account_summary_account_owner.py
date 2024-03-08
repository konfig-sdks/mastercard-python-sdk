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


class RequiredPaymentHistoryAccountSummaryAccountOwner(TypedDict):
    # The full name of the account owner. Multiple account owners are returned in one string per the source data from the institution.
    name: str

    # A street address
    address: str

class OptionalPaymentHistoryAccountSummaryAccountOwner(TypedDict, total=False):
    # City
    city: str

    # State
    state: str

    # A ZIP code
    zip: str

class PaymentHistoryAccountSummaryAccountOwner(RequiredPaymentHistoryAccountSummaryAccountOwner, OptionalPaymentHistoryAccountSummaryAccountOwner):
    pass
