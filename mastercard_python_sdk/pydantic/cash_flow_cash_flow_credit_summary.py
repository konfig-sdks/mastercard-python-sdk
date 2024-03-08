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

from mastercard_python_sdk.pydantic.cash_flow_monthly_cash_flow_credit_summaries import CashFlowMonthlyCashFlowCreditSummaries

class CashFlowCashFlowCreditSummary(BaseModel):
    # List of attributes for each month
    monthly_cash_flow_credit_summaries: typing.List[CashFlowMonthlyCashFlowCreditSummaries] = Field(alias='monthlyCashFlowCreditSummaries')

    # Sum of all credit transactions for each month for all accounts
    twelve_month_credit_total: typing.Union[int, float] = Field(alias='twelveMonthCreditTotal')

    # Sum of all monthly credit transactions without transfers for all accounts
    twelve_month_credit_total_less_transfers: typing.Union[int, float] = Field(alias='twelveMonthCreditTotalLessTransfers')

    # Six month sum of all credit transactions
    six_month_credit_total: typing.Union[int, float] = Field(alias='sixMonthCreditTotal')

    # Six month sum of all monthly credit transactions without transfers for all accounts
    six_month_credit_total_less_transfers: typing.Union[int, float] = Field(alias='sixMonthCreditTotalLessTransfers')

    # Two month sum of all credit transactions
    two_month_credit_total: typing.Union[int, float] = Field(alias='twoMonthCreditTotal')

    # Two month sum of all monthly credit transactions without transfers for all accounts
    two_month_credit_total_less_transfers: typing.Union[int, float] = Field(alias='twoMonthCreditTotalLessTransfers')
    class Config:
        arbitrary_types_allowed = True
