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

from mastercard_python_sdk.pydantic.cash_flow_monthly_cash_flow_balances import CashFlowMonthlyCashFlowBalances

class CashFlowCashFlowBalance(BaseModel):
    # List of attributes for each month
    monthly_cash_flow_balances: typing.List[CashFlowMonthlyCashFlowBalances] = Field(alias='monthlyCashFlowBalances')

    # Min daily balance across entire transaction history
    min_daily_balance: typing.Union[int, float] = Field(alias='minDailyBalance')

    # Max Daily Balance across entire transaction history
    max_daily_balance: typing.Union[int, float] = Field(alias='maxDailyBalance')

    # Average Daily Balance across twelve months for the account
    twelve_month_average_daily_balance: typing.Union[int, float] = Field(alias='twelveMonthAverageDailyBalance')

    # Average Daily Balance across six months for the account
    six_month_average_daily_balance: typing.Union[int, float] = Field(alias='sixMonthAverageDailyBalance')

    # Average Daily Balance across two months for the account
    two_month_average_daily_balance: typing.Union[int, float] = Field(alias='twoMonthAverageDailyBalance')

    # Standard Deviation of Daily Balance across twelve months for the account
    twelve_month_standard_deviation_of_daily_balance: str = Field(alias='twelveMonthStandardDeviationOfDailyBalance')

    # Standard Deviation of Daily Balance across two months for the account
    two_month_standard_deviation_of_daily_balance: str = Field(alias='twoMonthStandardDeviationOfDailyBalance')

    # Number of Days positive balance over entire transaction history
    number_of_days_positive_balance: str = Field(alias='numberOfDaysPositiveBalance')

    # Standard Deviation of Daily Balance across six months for the account
    six_month_standard_deviation_of_daily_balance: typing.Optional[str] = Field(None, alias='sixMonthStandardDeviationOfDailyBalance')

    # Number of Days Negative Balance over entire transaction history
    number_days_negative_balance: typing.Optional[str] = Field(None, alias='numberDaysNegativeBalance')
    class Config:
        arbitrary_types_allowed = True
