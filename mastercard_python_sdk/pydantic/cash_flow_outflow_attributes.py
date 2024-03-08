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

from mastercard_python_sdk.pydantic.obb_date_range_and_amount import ObbDateRangeAndAmount
from mastercard_python_sdk.pydantic.obb_date_range_and_count import ObbDateRangeAndCount

class CashFlowOutflowAttributes(BaseModel):
    # Count of all withdrawals during periods in the report
    count_withdrawals_by_month_for_the_report_time_period: typing.List[ObbDateRangeAndCount] = Field(alias='countWithdrawalsByMonthForTheReportTimePeriod')

    # Count of ALL withdrawals over entire known history of the account (may exceed requested length of report)
    historic_count_of_withdrawal_transactions: int = Field(alias='historicCountOfWithdrawalTransactions')

    # Maximum withdrawal value for different periods in the report
    maximum_withdrawal_by_month_for_the_report_time_period: typing.List[ObbDateRangeAndAmount] = Field(alias='maximumWithdrawalByMonthForTheReportTimePeriod')

    # Minimum withdrawal value for different periods in the report
    minimum_withdrawal_by_month_for_the_report_time_period: typing.List[ObbDateRangeAndAmount] = Field(alias='minimumWithdrawalByMonthForTheReportTimePeriod')

    # Sum of all withdrawals during periods in the report
    sum_withdrawals_by_month_for_the_report_time_period: typing.List[ObbDateRangeAndAmount] = Field(alias='sumWithdrawalsByMonthForTheReportTimePeriod')

    # Average value of withdrawals during periods in the report
    average_withdrawal_by_month_for_the_report_time_period: typing.Optional[typing.List[ObbDateRangeAndAmount]] = Field(None, alias='averageWithdrawalByMonthForTheReportTimePeriod')

    # Sum of ALL withdrawals over entire known history of the account (may exceed requested length of report)
    historic_sum_of_withdrawals: typing.Optional[typing.Union[int, float]] = Field(None, alias='historicSumOfWithdrawals')
    class Config:
        arbitrary_types_allowed = True
