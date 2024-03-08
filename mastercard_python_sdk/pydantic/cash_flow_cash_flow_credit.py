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

from mastercard_python_sdk.pydantic.cash_flow_monthly_cash_flow_credits import CashFlowMonthlyCashFlowCredits

class CashFlowCashFlowCredit(BaseModel):
    # List of attributes for each month
    monthly_cash_flow_credits: typing.List[CashFlowMonthlyCashFlowCredits] = Field(alias='monthlyCashFlowCredits')

    # Sum of all credit transactions for each month by account
    twelve_month_credit_total: typing.Optional[typing.Union[int, float]] = Field(None, alias='twelveMonthCreditTotal')

    # Sum of all monthly credit transactions without transfers for the account
    twelve_month_credit_total_less_transfers: typing.Optional[typing.Union[int, float]] = Field(None, alias='twelveMonthCreditTotalLessTransfers')

    # Sum of six month credit transactions
    six_month_credit_total: typing.Optional[typing.Union[int, float]] = Field(None, alias='sixMonthCreditTotal')

    # Sum of six month credit transactions without transfers
    six_month_credit_total_less_transfers: typing.Optional[typing.Union[int, float]] = Field(None, alias='sixMonthCreditTotalLessTransfers')

    # Sum of two month credit transactions
    two_month_credit_total: typing.Optional[typing.Union[int, float]] = Field(None, alias='twoMonthCreditTotal')

    # Sum of two month credit transactions without transfers
    two_month_credit_total_less_transfers: typing.Optional[typing.Union[int, float]] = Field(None, alias='twoMonthCreditTotalLessTransfers')
    class Config:
        arbitrary_types_allowed = True
