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

from mastercard_python_sdk.pydantic.cash_flow_activity_deposits_credits import CashFlowActivityDepositsCredits
from mastercard_python_sdk.pydantic.cash_flow_activity_withdrawals_debits import CashFlowActivityWithdrawalsDebits
from mastercard_python_sdk.pydantic.cash_flow_num_weeks_zeros import CashFlowNumWeeksZeros
from mastercard_python_sdk.pydantic.cash_flow_transaction_analytics_attributes_last_transaction_date import CashFlowTransactionAnalyticsAttributesLastTransactionDate
from mastercard_python_sdk.pydantic.obb_date_range_and_amount import ObbDateRangeAndAmount

class CashFlowTransactionAnalyticsAttributes(BaseModel):
    # List of all deposit transactions posted to the account during the report period
    activity_deposits_credits_for_the_report_time_period: typing.List[CashFlowActivityDepositsCredits] = Field(alias='activityDepositsCreditsForTheReportTimePeriod')

    # List of all withdrawal transactions posted to the account during the report period
    activity_withdrawals_debits_for_the_report_time_period: typing.List[CashFlowActivityWithdrawalsDebits] = Field(alias='activityWithdrawalsDebitsForTheReportTimePeriod')

    # Average value of transactions during periods in the report. Values may be positive or negative
    average_transaction_value_by_month_for_the_report_time_period: typing.List[ObbDateRangeAndAmount] = Field(alias='averageTransactionValueByMonthForTheReportTimePeriod')

    historic_weeks_with_zero_transactions: typing.Optional[CashFlowNumWeeksZeros] = Field(None, alias='historicWeeksWithZeroTransactions')

    last_transaction_date: typing.Optional[CashFlowTransactionAnalyticsAttributesLastTransactionDate] = Field(None, alias='lastTransactionDate')

    # Net cash flow for each month during the report period
    net_cash_flow_by_month_for_the_report_time_period: typing.Optional[typing.List[ObbDateRangeAndAmount]] = Field(None, alias='netCashFlowByMonthForTheReportTimePeriod')

    # Net cash flow during the report period (may be positive or negative)
    net_cash_flow_for_the_report_time_period: typing.Optional[typing.Union[int, float]] = Field(None, alias='netCashFlowForTheReportTimePeriod')
    class Config:
        arbitrary_types_allowed = True
