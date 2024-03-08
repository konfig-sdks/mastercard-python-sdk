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

from mastercard_python_sdk.type.stream_model_transaction_ids import StreamModelTransactionIds

class RequiredStreamModel(TypedDict):
    # Number of days that occur between each transaction in the stream
    cadence: int

    # Stream Id assigned to identified Stream
    id: str

    # The party in the transaction that is receiving the funds
    payee: str

    # The party in the transaction that is sending the funds
    payor: str

    # Number of days since the last transaction occurred in the stream
    recency: int

    transactionIds: StreamModelTransactionIds

class OptionalStreamModel(TypedDict, total=False):
    pass

class StreamModel(RequiredStreamModel, OptionalStreamModel):
    pass
