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

from mastercard_python_sdk.type.account_details_tx_based import AccountDetailsTxBased
from mastercard_python_sdk.type.prequalification_report_asset_summary import PrequalificationReportAssetSummary
from mastercard_python_sdk.type.report_account_position import ReportAccountPosition
from mastercard_python_sdk.type.report_transaction_new_tx_based import ReportTransactionNewTxBased

class RequiredVOAReportAccount(TypedDict):
    pass

class OptionalVOAReportAccount(TypedDict, total=False):
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

    # The available balance for the account
    availableBalance: typing.Union[int, float]

    # The status of the most recent aggregation attempt
    aggregationStatusCode: int

    # The cleared balance of the account as-of balanceDate
    balance: typing.Union[int, float]

    # A timestamp showing when the balance was captured
    balanceDate: int

    # The average monthly balance of this account
    averageMonthlyBalance: typing.Union[int, float]

    # The count for the total number of insufficient funds transactions, based on the `fromDate` of the report.
    totNumberInsufficientFundsFeeDebitTxAccount: int

    # The count for the total number of insufficient funds transactions for the last two months, based on the `fromDate` of the report.
    totNumberInsufficientFundsFeeDebitTxOver2MonthsAccount: int

    # The number of days since the most recent insufficient funds transaction, based on the `fromDate` of the report.
    totNumberDaysSinceMostRecentInsufficientFundsFeeDebitTxAccount: int

    # a list of transaction records
    transactions: typing.List[ReportTransactionNewTxBased]

    details: AccountDetailsTxBased

    position: ReportAccountPosition

    asset: PrequalificationReportAssetSummary

class VOAReportAccount(RequiredVOAReportAccount, OptionalVOAReportAccount):
    pass
