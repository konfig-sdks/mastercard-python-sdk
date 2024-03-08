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

class CashFlowInflowAttributes(BaseModel):
    # Count of all deposits during periods in the report
    count_deposits_by_month_for_the_report_time_period: typing.List[ObbDateRangeAndCount] = Field(alias='countDepositsByMonthForTheReportTimePeriod')

    # Count of ALL deposits over entire known history of the account (may exceed requested length of report)
    historic_count_of_deposit_transactions: int = Field(alias='historicCountOfDepositTransactions')

    # Maximum deposit value for different periods in the report
    maximum_deposit_by_month_for_the_report_time_period: typing.List[ObbDateRangeAndAmount] = Field(alias='maximumDepositByMonthForTheReportTimePeriod')

    # Minimum deposit value for different periods in the report
    minimum_deposit_by_month_for_the_report_time_period: typing.List[ObbDateRangeAndAmount] = Field(alias='minimumDepositByMonthForTheReportTimePeriod')

    # Sum of all deposits during periods in the report
    sum_deposits_by_month_for_the_report_time_period: typing.List[ObbDateRangeAndAmount] = Field(alias='sumDepositsByMonthForTheReportTimePeriod')

    # Average value of deposits during periods in the report
    average_deposit_by_month_for_the_report_time_period: typing.Optional[typing.List[ObbDateRangeAndAmount]] = Field(None, alias='averageDepositByMonthForTheReportTimePeriod')

    # Sum of ALL deposits over entire known history of the account (may exceed requested length of report)
    historic_sum_of_deposits: typing.Optional[typing.Union[int, float]] = Field(None, alias='historicSumOfDeposits')
    class Config:
        arbitrary_types_allowed = True
