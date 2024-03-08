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

from mastercard_python_sdk.type.cash_flow_activity_deposits_credits import CashFlowActivityDepositsCredits
from mastercard_python_sdk.type.cash_flow_activity_withdrawals_debits import CashFlowActivityWithdrawalsDebits
from mastercard_python_sdk.type.cash_flow_num_weeks_zeros import CashFlowNumWeeksZeros
from mastercard_python_sdk.type.cash_flow_transaction_analytics_attributes_last_transaction_date import CashFlowTransactionAnalyticsAttributesLastTransactionDate
from mastercard_python_sdk.type.obb_date_range_and_amount import ObbDateRangeAndAmount

class RequiredCashFlowTransactionAnalyticsAttributes(TypedDict):
    # List of all deposit transactions posted to the account during the report period
    activityDepositsCreditsForTheReportTimePeriod: typing.List[CashFlowActivityDepositsCredits]

    # List of all withdrawal transactions posted to the account during the report period
    activityWithdrawalsDebitsForTheReportTimePeriod: typing.List[CashFlowActivityWithdrawalsDebits]

    # Average value of transactions during periods in the report. Values may be positive or negative
    averageTransactionValueByMonthForTheReportTimePeriod: typing.List[ObbDateRangeAndAmount]

class OptionalCashFlowTransactionAnalyticsAttributes(TypedDict, total=False):
    historicWeeksWithZeroTransactions: CashFlowNumWeeksZeros

    lastTransactionDate: CashFlowTransactionAnalyticsAttributesLastTransactionDate

    # Net cash flow for each month during the report period
    netCashFlowByMonthForTheReportTimePeriod: typing.List[ObbDateRangeAndAmount]

    # Net cash flow during the report period (may be positive or negative)
    netCashFlowForTheReportTimePeriod: typing.Union[int, float]

class CashFlowTransactionAnalyticsAttributes(RequiredCashFlowTransactionAnalyticsAttributes, OptionalCashFlowTransactionAnalyticsAttributes):
    pass
