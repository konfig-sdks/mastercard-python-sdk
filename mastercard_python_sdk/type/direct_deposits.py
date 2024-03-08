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


class RequiredDirectDeposits(TypedDict):
    pass

class OptionalDirectDeposits(TypedDict, total=False):
    # Bank account type:  * `Checking`  * `Savings`  * `Loan`: Loan account employee choose to direct a portion of their net pay to help pay off a loan 
    accountTypeCode: str

    # Direct deposit amount
    amount: typing.Union[int, float]

    # Last four digits of the deposit account number
    accountLastFour: str

    # Routing number for the deposit account
    routingNumber: str

class DirectDeposits(RequiredDirectDeposits, OptionalDirectDeposits):
    pass
