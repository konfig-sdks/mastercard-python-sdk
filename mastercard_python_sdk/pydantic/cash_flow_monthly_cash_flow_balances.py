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


class CashFlowMonthlyCashFlowBalances(BaseModel):
    # One instance for each complete calendar month in the report
    month: int = Field(alias='month')

    # Min Daily Balance for each month
    min_daily_balance: typing.Union[int, float] = Field(alias='minDailyBalance')

    # Max Daily Balance for each month
    max_daily_balance: typing.Union[int, float] = Field(alias='maxDailyBalance')

    # Average Daily Balance for each month
    average_daily_balance: typing.Union[int, float] = Field(alias='averageDailyBalance')

    # Number of Days Negative Balance for each month
    number_of_days_negative_balance: str = Field(alias='numberOfDaysNegativeBalance')

    # Number of Days positive balance for each month
    number_of_days_positive_balance: str = Field(alias='numberOfDaysPositiveBalance')

    # Standard Deviation of Daily Balance for each month
    standard_deviation_of_daily_balance: typing.Optional[str] = Field(None, alias='standardDeviationOfDailyBalance')
    class Config:
        arbitrary_types_allowed = True
