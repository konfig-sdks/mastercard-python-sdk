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

from mastercard_python_sdk.type.transactional_attribute_stream_ids import TransactionalAttributeStreamIds
from mastercard_python_sdk.type.transactional_attribute_transaction_ids import TransactionalAttributeTransactionIds
from mastercard_python_sdk.type.transactional_time_interval import TransactionalTimeInterval

class RequiredTransactionalAttribute(TypedDict):
    # List of aggregations by specified Time Interval
    aggregatedByTimePeriods: typing.List[TransactionalTimeInterval]

    # Name of Attribute as mentioned in Data Dictionary
    attributeName: str

    streamIds: TransactionalAttributeStreamIds

    transactionIds: TransactionalAttributeTransactionIds

class OptionalTransactionalAttribute(TypedDict, total=False):
    pass

class TransactionalAttribute(RequiredTransactionalAttribute, OptionalTransactionalAttribute):
    pass
