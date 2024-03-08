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

from mastercard_python_sdk.type.account_details import AccountDetails
from mastercard_python_sdk.type.prequalification_report_asset_summary import PrequalificationReportAssetSummary
from mastercard_python_sdk.type.report_transaction import ReportTransaction

class RequiredPrequalificationReportAccount(TypedDict):
    pass

class OptionalPrequalificationReportAccount(TypedDict, total=False):
    # The ID of the account
    id: int

    # The account number from the institution (all digits except the last four are obfuscated)
    number: str

    # The name of the account owner. If no owner information is available, this field won't appear in the report.
    ownerName: str

    # The mailing address of the account owner. If no owner information is available, this field won't appear in the report.
    ownerAddress: str

    # The account name from the institution
    name: str

    # One of the values from account types
    type: str

    # The status of the most recent aggregation attempt
    aggregationStatusCode: int

    # The cleared balance of the account as-of `balanceDate`
    balance: typing.Union[int, float]

    # A timestamp of the balance
    balanceDate: int

    # Available balance
    availableBalance: typing.Union[int, float]

    # The average monthly balance of the account
    averageMonthlyBalance: typing.Union[int, float]

    # The count for the total number of insufficient funds transactions, based on the `fromDate` of the report
    totNumberInsufficientFundsFeeDebitTxAccount: int

    # The total number of  insufficient funds fees for the account over six months
    totNumberInsufficientFundsFeeDebitTxOver6MonthsAccount: int

    # The total number of days since the most recent insufficient funds fee for the account
    totNumberDaysSinceMostRecentInsufficientFundsFeeDebitTxAccount: int

    # a list of transaction records
    transactions: typing.List[ReportTransaction]

    asset: PrequalificationReportAssetSummary

    details: AccountDetails

class PrequalificationReportAccount(RequiredPrequalificationReportAccount, OptionalPrequalificationReportAccount):
    pass
