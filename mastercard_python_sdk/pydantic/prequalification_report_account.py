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

from mastercard_python_sdk.pydantic.account_details import AccountDetails
from mastercard_python_sdk.pydantic.prequalification_report_asset_summary import PrequalificationReportAssetSummary
from mastercard_python_sdk.pydantic.report_transaction import ReportTransaction

class PrequalificationReportAccount(BaseModel):
    # The ID of the account
    id: typing.Optional[int] = Field(None, alias='id')

    # The account number from the institution (all digits except the last four are obfuscated)
    number: typing.Optional[str] = Field(None, alias='number')

    # The name of the account owner. If no owner information is available, this field won't appear in the report.
    owner_name: typing.Optional[str] = Field(None, alias='ownerName')

    # The mailing address of the account owner. If no owner information is available, this field won't appear in the report.
    owner_address: typing.Optional[str] = Field(None, alias='ownerAddress')

    # The account name from the institution
    name: typing.Optional[str] = Field(None, alias='name')

    # One of the values from account types
    type: typing.Optional[str] = Field(None, alias='type')

    # The status of the most recent aggregation attempt
    aggregation_status_code: typing.Optional[int] = Field(None, alias='aggregationStatusCode')

    # The cleared balance of the account as-of `balanceDate`
    balance: typing.Optional[typing.Union[int, float]] = Field(None, alias='balance')

    # A timestamp of the balance
    balance_date: typing.Optional[int] = Field(None, alias='balanceDate')

    # Available balance
    available_balance: typing.Optional[typing.Union[int, float]] = Field(None, alias='availableBalance')

    # The average monthly balance of the account
    average_monthly_balance: typing.Optional[typing.Union[int, float]] = Field(None, alias='averageMonthlyBalance')

    # The count for the total number of insufficient funds transactions, based on the `fromDate` of the report
    tot_number_insufficient_funds_fee_debit_tx_account: typing.Optional[int] = Field(None, alias='totNumberInsufficientFundsFeeDebitTxAccount')

    # The total number of  insufficient funds fees for the account over six months
    tot_number_insufficient_funds_fee_debit_tx_over6_months_account: typing.Optional[int] = Field(None, alias='totNumberInsufficientFundsFeeDebitTxOver6MonthsAccount')

    # The total number of days since the most recent insufficient funds fee for the account
    tot_number_days_since_most_recent_insufficient_funds_fee_debit_tx_account: typing.Optional[int] = Field(None, alias='totNumberDaysSinceMostRecentInsufficientFundsFeeDebitTxAccount')

    # a list of transaction records
    transactions: typing.Optional[typing.List[ReportTransaction]] = Field(None, alias='transactions')

    asset: typing.Optional[PrequalificationReportAssetSummary] = Field(None, alias='asset')

    details: typing.Optional[AccountDetails] = Field(None, alias='details')
    class Config:
        arbitrary_types_allowed = True
