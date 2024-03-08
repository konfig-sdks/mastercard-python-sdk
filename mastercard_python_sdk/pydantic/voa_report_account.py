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
from pydantic import BaseModel, Field, RootModel

from mastercard_python_sdk.pydantic.account_details_tx_based import AccountDetailsTxBased
from mastercard_python_sdk.pydantic.prequalification_report_asset_summary import PrequalificationReportAssetSummary
from mastercard_python_sdk.pydantic.report_account_position import ReportAccountPosition
from mastercard_python_sdk.pydantic.report_transaction_new_tx_based import ReportTransactionNewTxBased

class VOAReportAccount(BaseModel):
    # The ID of the account
    id: typing.Optional[int] = Field(None, alias='id')

    # The account number from the institution (all digits except the last four are obfuscated)
    number: typing.Optional[str] = Field(None, alias='number')

    # The name(s) of the account owner(s). This field is optional. If no owner information is available, this field will not appear in the report.
    owner_name: typing.Optional[str] = Field(None, alias='ownerName')

    # The mailing address of the account owner(s). This field is optional. If no owner information is available, this field will not appear in the report.
    owner_address: typing.Optional[str] = Field(None, alias='ownerAddress')

    # The account name from the institution
    name: typing.Optional[str] = Field(None, alias='name')

    # One of the values from account types
    type: typing.Optional[str] = Field(None, alias='type')

    # The available balance for the account
    available_balance: typing.Optional[typing.Union[int, float]] = Field(None, alias='availableBalance')

    # The status of the most recent aggregation attempt
    aggregation_status_code: typing.Optional[int] = Field(None, alias='aggregationStatusCode')

    # The cleared balance of the account as-of balanceDate
    balance: typing.Optional[typing.Union[int, float]] = Field(None, alias='balance')

    # A timestamp showing when the balance was captured
    balance_date: typing.Optional[int] = Field(None, alias='balanceDate')

    # The average monthly balance of this account
    average_monthly_balance: typing.Optional[typing.Union[int, float]] = Field(None, alias='averageMonthlyBalance')

    # The count for the total number of insufficient funds transactions, based on the `fromDate` of the report.
    tot_number_insufficient_funds_fee_debit_tx_account: typing.Optional[int] = Field(None, alias='totNumberInsufficientFundsFeeDebitTxAccount')

    # The count for the total number of insufficient funds transactions for the last two months, based on the `fromDate` of the report.
    tot_number_insufficient_funds_fee_debit_tx_over2_months_account: typing.Optional[int] = Field(None, alias='totNumberInsufficientFundsFeeDebitTxOver2MonthsAccount')

    # The number of days since the most recent insufficient funds transaction, based on the `fromDate` of the report.
    tot_number_days_since_most_recent_insufficient_funds_fee_debit_tx_account: typing.Optional[int] = Field(None, alias='totNumberDaysSinceMostRecentInsufficientFundsFeeDebitTxAccount')

    # a list of transaction records
    transactions: typing.Optional[typing.List[ReportTransactionNewTxBased]] = Field(None, alias='transactions')

    details: typing.Optional[AccountDetailsTxBased] = Field(None, alias='details')

    position: typing.Optional[ReportAccountPosition] = Field(None, alias='position')

    asset: typing.Optional[PrequalificationReportAssetSummary] = Field(None, alias='asset')
    class Config:
        arbitrary_types_allowed = True
