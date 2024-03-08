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


class StatePeriod(BaseModel):
    # Value on the first date in the period
    beginning_value: typing.Union[int, float] = Field(alias='beginningValue')

    # Count of data points during the period
    count: int = Field(alias='count')

    # End date for the period being reported
    end_date: date = Field(alias='endDate')

    # Value on the last date in the period
    ending_value: typing.Union[int, float] = Field(alias='endingValue')

    # Start date for the period being reported
    start_date: date = Field(alias='startDate')

    # Maximum amount during the period
    max: typing.Optional[typing.Union[int, float]] = Field(None, alias='max')

    # Mean of amounts during the period
    mean: typing.Optional[typing.Union[int, float]] = Field(None, alias='mean')

    # Median of amounts during the period
    median: typing.Optional[typing.Union[int, float]] = Field(None, alias='median')

    # Minimum amount during the period
    min: typing.Optional[typing.Union[int, float]] = Field(None, alias='min')

    # Standard deviation of amounts during the period
    standard_deviation: typing.Optional[typing.Union[int, float]] = Field(None, alias='standardDeviation')

    # Sum of amounts during the period
    sum: typing.Optional[typing.Union[int, float]] = Field(None, alias='sum')
    class Config:
        arbitrary_types_allowed = True
