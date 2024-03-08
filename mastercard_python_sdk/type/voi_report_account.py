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
from mastercard_python_sdk.type.voi_report_income_stream import VOIReportIncomeStream

class RequiredVOIReportAccount(TypedDict):
    pass

class OptionalVOIReportAccount(TypedDict, total=False):
    # The ID of the account
    id: int

    # The account number from the institution (all digits except the last four are obfuscated)
    number: str

    # The name(s) of the account owner(s). This field is optional. If no owner information is available, this field will not appear in the report.
    ownerName: str

    # The mailing address of the account owner(s). This field is optional. If no owner information is available, this field will not appear in the report.
    ownerAddress: str

    # The account name from the institution
    name: str

    # One of the values from account types
    type: str

    # The status of the most recent aggregation attempt
    aggregationStatusCode: int

    # A list of income stream records
    incomeStreams: typing.List[VOIReportIncomeStream]

    # The cleared balance of the account as-of `balanceDate`
    balance: typing.Union[int, float]

    # The average monthly balance of this account
    averageMonthlyBalance: typing.Union[int, float]

    # a list of transaction records
    transactions: typing.List[ReportTransaction]

    # The available balance for the account
    availableBalance: typing.Union[int, float]

    # Current balance of the account
    currentBalance: typing.Union[int, float]

    # Beginning balance of account per the time period in the report
    beginningBalance: typing.Union[int, float]

    # A list of miscellaneous deposits
    miscDeposits: typing.List[ReportTransaction]

class VOIReportAccount(RequiredVOIReportAccount, OptionalVOIReportAccount):
    pass
