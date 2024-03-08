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

from mastercard_python_sdk.pydantic.stream_model_transaction_ids import StreamModelTransactionIds

class StreamModel(BaseModel):
    # Number of days that occur between each transaction in the stream
    cadence: int = Field(alias='cadence')

    # Stream Id assigned to identified Stream
    id: str = Field(alias='id')

    # The party in the transaction that is receiving the funds
    payee: str = Field(alias='payee')

    # The party in the transaction that is sending the funds
    payor: str = Field(alias='payor')

    # Number of days since the last transaction occurred in the stream
    recency: int = Field(alias='recency')

    transaction_ids: StreamModelTransactionIds = Field(alias='transactionIds')
    class Config:
        arbitrary_types_allowed = True
