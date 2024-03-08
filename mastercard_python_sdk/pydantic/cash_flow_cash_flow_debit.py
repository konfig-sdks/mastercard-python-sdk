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

from mastercard_python_sdk.pydantic.cash_flow_monthlycashflow_debits import CashFlowMonthlycashflowDebits

class CashFlowCashFlowDebit(BaseModel):
    # List of attributes for each month
    monthly_cash_flow_debits: typing.List[CashFlowMonthlycashflowDebits] = Field(alias='monthlyCashFlowDebits')

    # Sum of all monthly debit transactions for each month by account
    twelve_month_debit_total: typing.Optional[typing.Union[int, float]] = Field(None, alias='twelveMonthDebitTotal')

    # Sum of all monthly debit transactions without transfers for the account
    twelve_month_debit_total_less_transfers: typing.Optional[typing.Union[int, float]] = Field(None, alias='twelveMonthDebitTotalLessTransfers')

    # Six month sum of all debit transactions
    six_month_debit_total: typing.Optional[typing.Union[int, float]] = Field(None, alias='sixMonthDebitTotal')

    # Six month sum of all debit transactions without transfers for the account
    six_month_debit_total_less_transfers: typing.Optional[typing.Union[int, float]] = Field(None, alias='sixMonthDebitTotalLessTransfers')

    # Two month sum of all debit transactions
    two_month_debit_total: typing.Optional[typing.Union[int, float]] = Field(None, alias='twoMonthDebitTotal')

    # Two month sum of all debit transactions without transfers for the account
    two_month_debit_total_less_transfers: typing.Optional[typing.Union[int, float]] = Field(None, alias='twoMonthDebitTotalLessTransfers')
    class Config:
        arbitrary_types_allowed = True
