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


class PaymentHistoryTransactionsSummary(BaseModel):
    # Total of NSF transactions
    total_non_sufficient_funds: typing.Union[int, float] = Field(alias='totalNonSufficientFunds')

    # Monthly average of NSF transactions
    average_monthly_non_sufficient_funds: typing.Union[int, float] = Field(alias='averageMonthlyNonSufficientFunds')

    # Total of deposit transactions
    total_deposits: typing.Union[int, float] = Field(alias='totalDeposits')

    # Monthly average of deposit transactions
    average_monthly_deposits: typing.Union[int, float] = Field(alias='averageMonthlyDeposits')

    # Total of withdrawals transactions
    total_withdrawals: typing.Union[int, float] = Field(alias='totalWithdrawals')

    # Monthly average of withdrawal transactions
    average_monthly_withdrawals: typing.Union[int, float] = Field(alias='averageMonthlyWithdrawals')

    # ISO-8601 date of earliest transaction
    begin_date: str = Field(alias='beginDate')

    # ISO-8601 date of latest transaction
    end_date: str = Field(alias='endDate')
    class Config:
        arbitrary_types_allowed = True
