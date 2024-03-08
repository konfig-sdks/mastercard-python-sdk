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

from mastercard_python_sdk.pydantic.cash_flow_inflow_attributes import CashFlowInflowAttributes
from mastercard_python_sdk.pydantic.cash_flow_negative_triggers import CashFlowNegativeTriggers
from mastercard_python_sdk.pydantic.cash_flow_outflow_attributes import CashFlowOutflowAttributes
from mastercard_python_sdk.pydantic.cash_flow_transaction_analytics_attributes import CashFlowTransactionAnalyticsAttributes
from mastercard_python_sdk.pydantic.obb_date_range_and_amount import ObbDateRangeAndAmount

class CashFlowAnalyticsMetrics(BaseModel):
    inflow: typing.Optional[CashFlowInflowAttributes] = Field(None, alias='inflow')

    negative_triggers: typing.Optional[CashFlowNegativeTriggers] = Field(None, alias='negativeTriggers')

    outflow: typing.Optional[CashFlowOutflowAttributes] = Field(None, alias='outflow')

    # Sum of all transactions categorized as revenue, split by months
    revenue_by_month_for_the_report_time_period: typing.Optional[typing.List[ObbDateRangeAndAmount]] = Field(None, alias='revenueByMonthForTheReportTimePeriod')

    # Sum of all transactions categorized as revenue
    revenue_for_the_report_time_period: typing.Optional[typing.Union[int, float]] = Field(None, alias='revenueForTheReportTimePeriod')

    transaction_analytics: typing.Optional[CashFlowTransactionAnalyticsAttributes] = Field(None, alias='transactionAnalytics')
    class Config:
        arbitrary_types_allowed = True
