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


class StatementData(BaseModel):
    # An account ID represented as a number
    account_id: int = Field(alias='accountId')

    # Index of the statement to retrieve
    statement_index: typing.Optional[int] = Field(None, alias='statementIndex')
    class Config:
        arbitrary_types_allowed = True