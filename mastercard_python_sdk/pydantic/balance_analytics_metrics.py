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

from mastercard_python_sdk.pydantic.obb_daily_balance import ObbDailyBalance
from mastercard_python_sdk.pydantic.obb_date_range_and_amount import ObbDateRangeAndAmount
from mastercard_python_sdk.pydantic.obb_date_range_and_count import ObbDateRangeAndCount
from mastercard_python_sdk.pydantic.obb_num_weeks_average_balance_increasing import ObbNumWeeksAverageBalanceIncreasing

class BalanceAnalyticsMetrics(BaseModel):
    # Available Balance
    available_balance: typing.Optional[typing.Union[int, float]] = Field(None, alias='availableBalance')

    # Available Balance date
    available_balance_date: typing.Optional[str] = Field(None, alias='availableBalanceDate')

    # Average daily ending balance each month over the report time period
    average_daily_balance_by_month_for_the_report_time_period: typing.Optional[typing.List[ObbDateRangeAndAmount]] = Field(None, alias='averageDailyBalanceByMonthForTheReportTimePeriod')

    # Average Daily Balance
    average_daily_balance_for_the_report_time_period: typing.Optional[typing.Union[int, float]] = Field(None, alias='averageDailyBalanceForTheReportTimePeriod')

    # Average Weekday Balance
    average_weekday_balance_for_the_report_time_period: typing.Optional[typing.Union[int, float]] = Field(None, alias='averageWeekdayBalanceForTheReportTimePeriod')

    # Number of negative daily ending balances each month over the report time period
    count_daily_negative_balances_by_month_for_the_report_time_period: typing.Optional[typing.List[ObbDateRangeAndCount]] = Field(None, alias='countDailyNegativeBalancesByMonthForTheReportTimePeriod')

    # Current Running Balance Date
    current_running_balance: typing.Optional[typing.Union[int, float]] = Field(None, alias='currentRunningBalance')

    # Current Running Balance date
    current_running_balance_date: typing.Optional[str] = Field(None, alias='currentRunningBalanceDate')

    # Daily balance of the account during weekdays over the length of the report
    daily_balances_by_weekday_for_the_report_time_period: typing.Optional[typing.List[ObbDailyBalance]] = Field(None, alias='dailyBalancesByWeekdayForTheReportTimePeriod')

    # Daily balance of the account over the length of the report
    daily_balances_for_the_report_time_period: typing.Optional[typing.List[ObbDailyBalance]] = Field(None, alias='dailyBalancesForTheReportTimePeriod')

    historic_number_of_weeks_average_balance_increasing: typing.Optional[ObbNumWeeksAverageBalanceIncreasing] = Field(None, alias='historicNumberOfWeeksAverageBalanceIncreasing')

    # Maximum daily ending balance each month over the report time period
    maximum_daily_balance_by_month_for_the_report_time_period: typing.Optional[typing.List[ObbDateRangeAndAmount]] = Field(None, alias='maximumDailyBalanceByMonthForTheReportTimePeriod')

    # Maximum Running Balance
    maximum_running_balance_for_the_report_time_period: typing.Optional[typing.Union[int, float]] = Field(None, alias='maximumRunningBalanceForTheReportTimePeriod')

    # Minimum daily ending balance each month over the report time period
    minimum_daily_balance_by_month_for_the_report_time_period: typing.Optional[typing.List[ObbDateRangeAndAmount]] = Field(None, alias='minimumDailyBalanceByMonthForTheReportTimePeriod')

    # Minimum Running Balance
    minimum_running_balance_for_the_report_time_period: typing.Optional[typing.Union[int, float]] = Field(None, alias='minimumRunningBalanceForTheReportTimePeriod')
    class Config:
        arbitrary_types_allowed = True
