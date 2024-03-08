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

from mastercard_python_sdk.type.obb_date_range_and_amount import ObbDateRangeAndAmount
from mastercard_python_sdk.type.obb_date_range_and_count import ObbDateRangeAndCount

class RequiredCashFlowInflowAttributes(TypedDict):
    # Count of all deposits during periods in the report
    countDepositsByMonthForTheReportTimePeriod: typing.List[ObbDateRangeAndCount]

    # Count of ALL deposits over entire known history of the account (may exceed requested length of report)
    historicCountOfDepositTransactions: int

    # Maximum deposit value for different periods in the report
    maximumDepositByMonthForTheReportTimePeriod: typing.List[ObbDateRangeAndAmount]

    # Minimum deposit value for different periods in the report
    minimumDepositByMonthForTheReportTimePeriod: typing.List[ObbDateRangeAndAmount]

    # Sum of all deposits during periods in the report
    sumDepositsByMonthForTheReportTimePeriod: typing.List[ObbDateRangeAndAmount]

class OptionalCashFlowInflowAttributes(TypedDict, total=False):
    # Average value of deposits during periods in the report
    averageDepositByMonthForTheReportTimePeriod: typing.List[ObbDateRangeAndAmount]

    # Sum of ALL deposits over entire known history of the account (may exceed requested length of report)
    historicSumOfDeposits: typing.Union[int, float]

class CashFlowInflowAttributes(RequiredCashFlowInflowAttributes, OptionalCashFlowInflowAttributes):
    pass
