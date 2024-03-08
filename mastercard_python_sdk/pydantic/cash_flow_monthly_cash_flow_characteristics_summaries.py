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


class CashFlowMonthlyCashFlowCharacteristicsSummaries(BaseModel):
    # One instance for each complete calendar month in the report
    month: int = Field(alias='month')

    # Total Credits - Total Debits by month across all accounts
    total_credits_less_total_debits: typing.Union[int, float] = Field(alias='totalCreditsLessTotalDebits')

    # Total Credits - Total Debits by month (Without Transfers) across all accounts
    total_credits_less_total_debits_less_transfers: typing.Union[int, float] = Field(alias='totalCreditsLessTotalDebitsLessTransfers')

    # Average transaction amount across all accounts
    average_transaction_amount: typing.Union[int, float] = Field(alias='averageTransactionAmount')
    class Config:
        arbitrary_types_allowed = True
