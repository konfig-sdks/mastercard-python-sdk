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


class RequiredMicroDepositDetails(TypedDict):
    pass

class OptionalMicroDepositDetails(TypedDict, total=False):
    # The following values may be returned in the field of a status:  * \"Pending\" : Micro entries not yet deposited to customer's account * \"Completed\": Micro entries deposited to customer's account * \"Verified\": Micro entries got successfully verified * \"Rejected\": Micro entries got rejected due to some reason * \"Returned\": Micro entries got returned back * \"Failed\": Micro entries got failed due to some reason * \"Expired\": Micro entries got expired as they remains unverified for certain defined days
    status: str

    # Micro entries status description
    statusDescription: str

    # A date-time without time zone
    creationDate: str

    # Routing number of receiving bank
    routingNumber: str

    # The last 4 digits of the ACH account number
    accountNumberLast4: str

class MicroDepositDetails(RequiredMicroDepositDetails, OptionalMicroDepositDetails):
    pass
