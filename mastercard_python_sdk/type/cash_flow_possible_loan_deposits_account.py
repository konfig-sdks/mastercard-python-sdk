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

from mastercard_python_sdk.type.report_transaction import ReportTransaction

class RequiredCashFlowPossibleLoanDepositsAccount(TypedDict):
    # Finicity account ID
    id: str

    # The name(s) of the account owner(s), retrieved from the institution.
    ownerName: str

    # The mailing address of the account owner, retrieved from the institution.
    ownerAddress: str

    # The account name from the institution
    name: str

    # The account number from the institution (obfuscated)
    number: str

    # CFR: `ALL` (`checking` / `savings` / `loan` / `mortgage` / `credit card` / `CD` / `MM` / `investment`...)
    type: str

    # The status of the most recent aggregation attempt for this account (non-zero means the account was not accessed successfully for this report, and additional fields for this account may not be reliable)
    aggregationStatusCode: int

    # The cleared balance of the account as-of `balanceDate`
    currentBalance: typing.Union[int, float]

    # Available balance
    availableBalance: typing.Union[int, float]

    # A timestamp showing when the `balance` was captured
    balanceDate: int

    # a list of transaction records
    transactions: typing.List[ReportTransaction]

class OptionalCashFlowPossibleLoanDepositsAccount(TypedDict, total=False):
    pass

class CashFlowPossibleLoanDepositsAccount(RequiredCashFlowPossibleLoanDepositsAccount, OptionalCashFlowPossibleLoanDepositsAccount):
    pass
