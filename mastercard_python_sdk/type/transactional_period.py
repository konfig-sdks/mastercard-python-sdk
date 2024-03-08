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


class RequiredTransactionalPeriod(TypedDict):
    # Count of data points during the period
    count: int

    # End date for the period being reported
    endDate: date

    # Start date for the period being reported
    startDate: date

class OptionalTransactionalPeriod(TypedDict, total=False):
    # Maximum amount during the period
    max: typing.Union[int, float]

    # Mean of amounts during the period
    mean: typing.Union[int, float]

    # Median of amounts during the period
    median: typing.Union[int, float]

    # Minimum amount during the period
    min: typing.Union[int, float]

    # Standard deviation of amounts during the period
    standardDeviation: typing.Union[int, float]

    # Sum of amounts during the period
    sum: typing.Union[int, float]

class TransactionalPeriod(RequiredTransactionalPeriod, OptionalTransactionalPeriod):
    pass
