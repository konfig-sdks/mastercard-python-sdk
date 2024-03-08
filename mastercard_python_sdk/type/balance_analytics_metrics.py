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

from mastercard_python_sdk.type.obb_daily_balance import ObbDailyBalance
from mastercard_python_sdk.type.obb_date_range_and_amount import ObbDateRangeAndAmount
from mastercard_python_sdk.type.obb_date_range_and_count import ObbDateRangeAndCount
from mastercard_python_sdk.type.obb_num_weeks_average_balance_increasing import ObbNumWeeksAverageBalanceIncreasing

class RequiredBalanceAnalyticsMetrics(TypedDict):
    pass

class OptionalBalanceAnalyticsMetrics(TypedDict, total=False):
    # Available Balance
    availableBalance: typing.Union[int, float]

    # Available Balance date
    availableBalanceDate: str

    # Average daily ending balance each month over the report time period
    averageDailyBalanceByMonthForTheReportTimePeriod: typing.List[ObbDateRangeAndAmount]

    # Average Daily Balance
    averageDailyBalanceForTheReportTimePeriod: typing.Union[int, float]

    # Average Weekday Balance
    averageWeekdayBalanceForTheReportTimePeriod: typing.Union[int, float]

    # Number of negative daily ending balances each month over the report time period
    countDailyNegativeBalancesByMonthForTheReportTimePeriod: typing.List[ObbDateRangeAndCount]

    # Current Running Balance Date
    currentRunningBalance: typing.Union[int, float]

    # Current Running Balance date
    currentRunningBalanceDate: str

    # Daily balance of the account during weekdays over the length of the report
    dailyBalancesByWeekdayForTheReportTimePeriod: typing.List[ObbDailyBalance]

    # Daily balance of the account over the length of the report
    dailyBalancesForTheReportTimePeriod: typing.List[ObbDailyBalance]

    historicNumberOfWeeksAverageBalanceIncreasing: ObbNumWeeksAverageBalanceIncreasing

    # Maximum daily ending balance each month over the report time period
    maximumDailyBalanceByMonthForTheReportTimePeriod: typing.List[ObbDateRangeAndAmount]

    # Maximum Running Balance
    maximumRunningBalanceForTheReportTimePeriod: typing.Union[int, float]

    # Minimum daily ending balance each month over the report time period
    minimumDailyBalanceByMonthForTheReportTimePeriod: typing.List[ObbDateRangeAndAmount]

    # Minimum Running Balance
    minimumRunningBalanceForTheReportTimePeriod: typing.Union[int, float]

class BalanceAnalyticsMetrics(RequiredBalanceAnalyticsMetrics, OptionalBalanceAnalyticsMetrics):
    pass
