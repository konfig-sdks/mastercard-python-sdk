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


class RequiredCashFlowMonthlyCashFlowCreditSummaries(TypedDict):
    # One instance for each complete calendar month in the report
    month: int

    # Number of credits by month across all accounts
    numberOfCredits: str

    # Total amount of credits by month across all accounts
    totalCreditsAmount: typing.Union[int, float]

    # Largest credit by month across all accounts
    largestCredit: typing.Union[int, float]

    # Number of credits by month (less transfers) across all accounts
    numberOfCreditsLessTransfers: str

    # Total amount of credits by month (less transfers) across all accounts
    totalCreditsAmountLessTransfers: typing.Union[int, float]

    # The average credit amount
    averageCreditAmount: typing.Union[int, float]

    # The estimated number of loan deposits by month
    estimatedNumberOfLoanDeposits: str

    # The estimated loan deposit amount by month
    estimatedLoanDepositAmount: typing.Union[int, float]

class OptionalCashFlowMonthlyCashFlowCreditSummaries(TypedDict, total=False):
    pass

class CashFlowMonthlyCashFlowCreditSummaries(RequiredCashFlowMonthlyCashFlowCreditSummaries, OptionalCashFlowMonthlyCashFlowCreditSummaries):
    pass
