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


class CashFlowTransactionAnalyticsAttributesLastTransactionDateItem(BaseModel):
    # Date the deposit transaction was posted
    date: str = Field(alias='date')

    # Amount of transaction if deposit, otherwise null
    deposits_credits: typing.Optional[typing.Union[int, float]] = Field(None, alias='depositsCredits')

    # Amount of transaction if withdrawal, otherwise null
    withdrawals_debits: typing.Optional[typing.Union[int, float]] = Field(None, alias='withdrawalsDebits')

    # Amount of transaction if zero, otherwise null
    zero_amount_transaction: typing.Optional[typing.Union[int, float]] = Field(None, alias='zeroAmountTransaction')

    # Description of transaction
    transaction_description: typing.Optional[str] = Field(None, alias='transactionDescription')
    class Config:
        arbitrary_types_allowed = True
