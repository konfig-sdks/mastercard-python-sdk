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
from mastercard_python_sdk.pydantic.report_account_position import ReportAccountPosition
from mastercard_python_sdk.pydantic.report_transaction_new_tx_based import ReportTransactionNewTxBased
from mastercard_python_sdk.pydantic.voietx_verify_report_income_stream import VOIETXVerifyReportIncomeStream

class VOIETXVerifyReportAccount(BaseModel):
    # The ID of the account
    id: int = Field(alias='id')

    # The account number from the institution (all digits except the last four are obfuscated)
    number: str = Field(alias='number')

    # The account name from the institution
    name: str = Field(alias='name')

    # One of the values from account types
    type: str = Field(alias='type')

    # The status of the most recent aggregation attempt
    aggregation_status_code: int = Field(alias='aggregationStatusCode')

    # a list of transaction records
    transactions: typing.List[ReportTransactionNewTxBased] = Field(alias='transactions')

    # The name(s) of the account owner(s). This field is optional. If no owner information is available, this field will not appear in the report.
    owner_name: typing.Optional[str] = Field(None, alias='ownerName')

    # The mailing address of the account owner(s). This field is optional. If no owner information is available, this field will not appear in the report.
    owner_address: typing.Optional[str] = Field(None, alias='ownerAddress')

    # A list of income stream records
    income_streams: typing.Optional[typing.List[VOIETXVerifyReportIncomeStream]] = Field(None, alias='incomeStreams')

    # The cleared balance of the account as-of `balanceDate`
    balance: typing.Optional[typing.Union[int, float]] = Field(None, alias='balance')

    # The average monthly balance of this account
    average_monthly_balance: typing.Optional[typing.Union[int, float]] = Field(None, alias='averageMonthlyBalance')

    details: typing.Optional[AccountDetailsTxBased] = Field(None, alias='details')

    position: typing.Optional[ReportAccountPosition] = Field(None, alias='position')

    # The available balance for the account
    available_balance: typing.Optional[typing.Union[int, float]] = Field(None, alias='availableBalance')
    class Config:
        arbitrary_types_allowed = True
