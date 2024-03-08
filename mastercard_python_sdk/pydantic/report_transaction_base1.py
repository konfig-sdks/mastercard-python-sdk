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


class ReportTransactionBase1(BaseModel):
    # The description of the transaction, as provided by the institution (often known as `payee`). In the event that this field is left blank by the institution, Finicity will pass a value of \"No description provided by institution\". All other values are provided by the institution.
    description: str = Field(alias='description')

    # A transaction ID
    id: int = Field(alias='id')

    # A timestamp showing when the transaction was posted or cleared by the institution
    posted_date: int = Field(alias='postedDate')

    # The total amount of the transaction. Transactions for deposits are positive values, withdrawals and debits are negative values.
    amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='amount')

    # The memo field of the transaction, as provided by the institution. The institution must provide either a description, a memo, or both. It is recommended to concatenate the two fields into a single value.
    memo: typing.Optional[str] = Field(None, alias='memo')
    class Config:
        arbitrary_types_allowed = True
