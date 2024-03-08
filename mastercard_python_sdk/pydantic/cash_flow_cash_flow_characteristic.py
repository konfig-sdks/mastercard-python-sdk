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

from mastercard_python_sdk.pydantic.cash_flow_monthly_cash_flow_characteristics import CashFlowMonthlyCashFlowCharacteristics

class CashFlowCashFlowCharacteristic(BaseModel):
    # List of attributes for each month
    monthly_cash_flow_characteristics: typing.List[CashFlowMonthlyCashFlowCharacteristics] = Field(alias='monthlyCashFlowCharacteristics')

    # Average (Total Credits - Total Debits) for the account
    average_monthly_net: typing.Union[int, float] = Field(alias='averageMonthlyNet')

    # Average (Total Credits - Total Debits) without transfers for the account
    average_monthly_net_less_transfers: typing.Union[int, float] = Field(alias='averageMonthlyNetLessTransfers')

    # Sum of all monthly (Total Credits - Total Debits) each month for the account
    twelve_month_total_net: typing.Optional[typing.Union[int, float]] = Field(None, alias='twelveMonthTotalNet')

    # Sum of all monthly (Total Credits - Total Debits) without transfers for the account
    twelve_month_total_net_less_transfers: typing.Optional[typing.Union[int, float]] = Field(None, alias='twelveMonthTotalNetLessTransfers')

    # 6 Month Average (Total Credits - Total Debits)
    six_month_average_total_credits_less_total_debits: typing.Optional[typing.Union[int, float]] = Field(None, alias='sixMonthAverageTotalCreditsLessTotalDebits')

    # 6 Month Average (Total Credits - Total Debits) - (Without Transfers)
    six_month_average_total_credits_less_total_debits_less_transfers: typing.Optional[typing.Union[int, float]] = Field(None, alias='sixMonthAverageTotalCreditsLessTotalDebitsLessTransfers')

    # 2 Month Average (Total Credits - Total Debits)
    two_month_average_total_credits_less_total_debits: typing.Optional[typing.Union[int, float]] = Field(None, alias='twoMonthAverageTotalCreditsLessTotalDebits')

    # 2 Month Average (Total Credits - Total Debits) - (Without Transfers)
    two_month_average_total_credits_less_total_debits_less_transfers: typing.Optional[typing.Union[int, float]] = Field(None, alias='twoMonthAverageTotalCreditsLessTotalDebitsLessTransfers')
    class Config:
        arbitrary_types_allowed = True
