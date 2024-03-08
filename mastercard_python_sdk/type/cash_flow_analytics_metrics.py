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

from mastercard_python_sdk.type.cash_flow_inflow_attributes import CashFlowInflowAttributes
from mastercard_python_sdk.type.cash_flow_negative_triggers import CashFlowNegativeTriggers
from mastercard_python_sdk.type.cash_flow_outflow_attributes import CashFlowOutflowAttributes
from mastercard_python_sdk.type.cash_flow_transaction_analytics_attributes import CashFlowTransactionAnalyticsAttributes
from mastercard_python_sdk.type.obb_date_range_and_amount import ObbDateRangeAndAmount

class RequiredCashFlowAnalyticsMetrics(TypedDict):
    pass

class OptionalCashFlowAnalyticsMetrics(TypedDict, total=False):
    inflow: CashFlowInflowAttributes

    negativeTriggers: CashFlowNegativeTriggers

    outflow: CashFlowOutflowAttributes

    # Sum of all transactions categorized as revenue, split by months
    revenueByMonthForTheReportTimePeriod: typing.List[ObbDateRangeAndAmount]

    # Sum of all transactions categorized as revenue
    revenueForTheReportTimePeriod: typing.Union[int, float]

    transactionAnalytics: CashFlowTransactionAnalyticsAttributes

class CashFlowAnalyticsMetrics(RequiredCashFlowAnalyticsMetrics, OptionalCashFlowAnalyticsMetrics):
    pass
