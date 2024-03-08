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


class CashFlowMonthlyCashFlowDebitSummaries(BaseModel):
    # One instance for each complete calendar month in the report
    month: int = Field(alias='month')

    # Number of Debits by month across all accounts
    number_of_debits: str = Field(alias='numberOfDebits')

    # Total Amount of Debits by month across all accounts
    total_debits_amount: typing.Union[int, float] = Field(alias='totalDebitsAmount')

    # Largest Debit by month
    largest_debit: typing.Union[int, float] = Field(alias='largestDebit')

    # Number of Debits by month (less transfers)
    number_of_debits_less_transfers: str = Field(alias='numberOfDebitsLessTransfers')

    # Total amount of debits by month (less transfers)
    total_debits_amount_less_transfers: typing.Union[int, float] = Field(alias='totalDebitsAmountLessTransfers')

    # The average debit amount
    average_debit_amount: typing.Union[int, float] = Field(alias='averageDebitAmount')
    class Config:
        arbitrary_types_allowed = True
