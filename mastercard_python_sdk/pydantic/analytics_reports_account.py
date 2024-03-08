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

from mastercard_python_sdk.pydantic.account_analytics import AccountAnalytics
from mastercard_python_sdk.pydantic.account_details import AccountDetails
from mastercard_python_sdk.pydantic.report_transaction import ReportTransaction

class AnalyticsReportsAccount(BaseModel):
    # The ID of the account
    id: int = Field(alias='id')

    # The account name from the institution
    name: str = Field(alias='name')

    # The account number from the institution (obfuscated)
    number: str = Field(alias='number')

    # One of the values from account types
    type: str = Field(alias='type')

    # a list of transaction records
    transactions: typing.List[ReportTransaction] = Field(alias='transactions')

    # The name(s) of the account owner(s), retrieved from the institution.
    owner_name: typing.Optional[str] = Field(None, alias='ownerName')

    # The mailing address of the account owner, retrieved from the institution.
    owner_address: typing.Optional[str] = Field(None, alias='ownerAddress')

    # The status of the most recent aggregation attempt
    aggregation_status_code: typing.Optional[int] = Field(None, alias='aggregationStatusCode')

    # The cleared balance of the account as-of `balanceDate`
    current_balance: typing.Optional[typing.Union[int, float]] = Field(None, alias='currentBalance')

    # Available balance
    available_balance: typing.Optional[typing.Union[int, float]] = Field(None, alias='availableBalance')

    # A timestamp showing when the `balance` was captured
    balance_date: typing.Optional[int] = Field(None, alias='balanceDate')

    details: typing.Optional[AccountDetails] = Field(None, alias='details')

    account_analytics: typing.Optional[AccountAnalytics] = Field(None, alias='accountAnalytics')
    class Config:
        arbitrary_types_allowed = True
