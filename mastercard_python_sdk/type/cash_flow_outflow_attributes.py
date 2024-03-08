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

class RequiredCashFlowOutflowAttributes(TypedDict):
    # Count of all withdrawals during periods in the report
    countWithdrawalsByMonthForTheReportTimePeriod: typing.List[ObbDateRangeAndCount]

    # Count of ALL withdrawals over entire known history of the account (may exceed requested length of report)
    historicCountOfWithdrawalTransactions: int

    # Maximum withdrawal value for different periods in the report
    maximumWithdrawalByMonthForTheReportTimePeriod: typing.List[ObbDateRangeAndAmount]

    # Minimum withdrawal value for different periods in the report
    minimumWithdrawalByMonthForTheReportTimePeriod: typing.List[ObbDateRangeAndAmount]

    # Sum of all withdrawals during periods in the report
    sumWithdrawalsByMonthForTheReportTimePeriod: typing.List[ObbDateRangeAndAmount]

class OptionalCashFlowOutflowAttributes(TypedDict, total=False):
    # Average value of withdrawals during periods in the report
    averageWithdrawalByMonthForTheReportTimePeriod: typing.List[ObbDateRangeAndAmount]

    # Sum of ALL withdrawals over entire known history of the account (may exceed requested length of report)
    historicSumOfWithdrawals: typing.Union[int, float]

class CashFlowOutflowAttributes(RequiredCashFlowOutflowAttributes, OptionalCashFlowOutflowAttributes):
    pass
