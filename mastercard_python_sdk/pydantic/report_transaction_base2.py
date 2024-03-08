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


class ReportTransactionBase2(BaseModel):
    # A normalized payee, derived from the transaction's `description` and `memo` fields
    normalized_payee: typing.Optional[str] = Field(None, alias='normalizedPayee')

    # The unique identifier given by the FI for each transaction
    institution_transaction_id: typing.Optional[str] = Field(None, alias='institutionTransactionId')

    # One of the values from Categories (assigned based on the payee name)
    category: typing.Optional[str] = Field(None, alias='category')

    # One of the values from transaction types
    type: typing.Optional[str] = Field(None, alias='type')

    # The type of investment security (VOA only)
    security_type: typing.Optional[str] = Field(None, alias='securityType')

    # Investment symbol (VOA only)
    symbol: typing.Optional[str] = Field(None, alias='symbol')

    # A commission amount
    commission: typing.Optional[typing.Union[int, float]] = Field(None, alias='commission')
    class Config:
        arbitrary_types_allowed = True
