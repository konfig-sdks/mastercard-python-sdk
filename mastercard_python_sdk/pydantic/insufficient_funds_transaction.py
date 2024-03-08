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


class InsufficientFundsTransaction(BaseModel):
    # Amount of the NSF transaction
    amount: typing.Union[int, float] = Field(alias='amount')

    # Posted date of the NSF transaction
    posted_date: str = Field(alias='postedDate')

    # Finicity transaction ID
    transaction_id: int = Field(alias='transactionId')

    # Description of the transaction
    description: typing.Optional[str] = Field(None, alias='description')

    # Transaction memo
    memo: typing.Optional[str] = Field(None, alias='memo')
    class Config:
        arbitrary_types_allowed = True
