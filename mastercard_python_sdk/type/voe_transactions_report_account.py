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

from mastercard_python_sdk.type.voe_transactions_report_income_stream import VOETransactionsReportIncomeStream

class RequiredVOETransactionsReportAccount(TypedDict):
    pass

class OptionalVOETransactionsReportAccount(TypedDict, total=False):
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
    incomeStreams: typing.List[VOETransactionsReportIncomeStream]

class VOETransactionsReportAccount(RequiredVOETransactionsReportAccount, OptionalVOETransactionsReportAccount):
    pass
