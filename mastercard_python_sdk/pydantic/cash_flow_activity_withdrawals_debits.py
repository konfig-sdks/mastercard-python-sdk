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


class CashFlowActivityWithdrawalsDebits(BaseModel):
    # Date the withdrawal transaction was posted
    date: str = Field(alias='date')

    # Amount of the withdrawal
    withdrawals_debits: typing.Union[int, float] = Field(alias='withdrawalsDebits')

    # Description of transaction
    transaction_description: typing.Optional[str] = Field(None, alias='transactionDescription')
    class Config:
        arbitrary_types_allowed = True
