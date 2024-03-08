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

from mastercard_python_sdk.pydantic.transactional_attribute_stream_ids import TransactionalAttributeStreamIds
from mastercard_python_sdk.pydantic.transactional_attribute_transaction_ids import TransactionalAttributeTransactionIds
from mastercard_python_sdk.pydantic.transactional_time_interval import TransactionalTimeInterval

class TransactionalAttribute(BaseModel):
    # List of aggregations by specified Time Interval
    aggregated_by_time_periods: typing.List[TransactionalTimeInterval] = Field(alias='aggregatedByTimePeriods')

    # Name of Attribute as mentioned in Data Dictionary
    attribute_name: str = Field(alias='attributeName')

    stream_ids: TransactionalAttributeStreamIds = Field(alias='streamIds')

    transaction_ids: TransactionalAttributeTransactionIds = Field(alias='transactionIds')
    class Config:
        arbitrary_types_allowed = True
