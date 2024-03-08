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

from mastercard_python_sdk.pydantic.cash_flow_monthly_cash_flow_characteristics_summaries import CashFlowMonthlyCashFlowCharacteristicsSummaries

class CashFlowCashFlowCharacteristicsSummary(BaseModel):
    # Average monthly net amount
    average_monthly_net: typing.Union[int, float] = Field(alias='averageMonthlyNet')

    # Average monthly net less transfers
    average_monthly_net_less_transfers: typing.Union[int, float] = Field(alias='averageMonthlyNetLessTransfers')

    # Sum of all monthly (Total Credits - Total Debits) each month by the account
    twelve_month_total_net: typing.Union[int, float] = Field(alias='twelveMonthTotalNet')

    # Sum of all monthly (Total Credits - Total Debits) without transfers by the account
    twelve_month_total_net_less_transfers: typing.Union[int, float] = Field(alias='twelveMonthTotalNetLessTransfers')

    # 6 Month Average (Total Credits - Total Debits) across all accounts
    six_month_average_total_credits_less_total_debits: typing.Union[int, float] = Field(alias='sixMonthAverageTotalCreditsLessTotalDebits')

    # 6 Month Average (Total Credits - Total Debits) - (Without Transfers) across all accounts
    six_month_average_total_credits_less_total_debits_less_transfers: typing.Union[int, float] = Field(alias='sixMonthAverageTotalCreditsLessTotalDebitsLessTransfers')

    # 2 Month Average (Total Credits - Total Debits) across all accounts
    two_month_average_total_credits_less_total_debits: typing.Union[int, float] = Field(alias='twoMonthAverageTotalCreditsLessTotalDebits')

    # List of attributes for each month
    monthly_cash_flow_characteristics_summaries: typing.Optional[typing.List[CashFlowMonthlyCashFlowCharacteristicsSummaries]] = Field(None, alias='monthlyCashFlowCharacteristicsSummaries')

    # 2 Month Average (Total Credits - Total Debits) - (Without Transfers) across all accounts
    two_month_average_total_credits_less_total_debits_less_transfers: typing.Optional[typing.Union[int, float]] = Field(None, alias='twoMonthAverageTotalCreditsLessTotalDebitsLessTransfers')
    class Config:
        arbitrary_types_allowed = True
