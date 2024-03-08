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

from mastercard_python_sdk.pydantic.report_transaction import ReportTransaction
from mastercard_python_sdk.pydantic.voi_report_income_stream import VOIReportIncomeStream

class VOIReportAccount(BaseModel):
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

    # The status of the most recent aggregation attempt
    aggregation_status_code: typing.Optional[int] = Field(None, alias='aggregationStatusCode')

    # A list of income stream records
    income_streams: typing.Optional[typing.List[VOIReportIncomeStream]] = Field(None, alias='incomeStreams')

    # The cleared balance of the account as-of `balanceDate`
    balance: typing.Optional[typing.Union[int, float]] = Field(None, alias='balance')

    # The average monthly balance of this account
    average_monthly_balance: typing.Optional[typing.Union[int, float]] = Field(None, alias='averageMonthlyBalance')

    # a list of transaction records
    transactions: typing.Optional[typing.List[ReportTransaction]] = Field(None, alias='transactions')

    # The available balance for the account
    available_balance: typing.Optional[typing.Union[int, float]] = Field(None, alias='availableBalance')

    # Current balance of the account
    current_balance: typing.Optional[typing.Union[int, float]] = Field(None, alias='currentBalance')

    # Beginning balance of account per the time period in the report
    beginning_balance: typing.Optional[typing.Union[int, float]] = Field(None, alias='beginningBalance')

    # A list of miscellaneous deposits
    misc_deposits: typing.Optional[typing.List[ReportTransaction]] = Field(None, alias='miscDeposits')
    class Config:
        arbitrary_types_allowed = True
