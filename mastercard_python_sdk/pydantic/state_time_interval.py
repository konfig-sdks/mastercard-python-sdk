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

from mastercard_python_sdk.pydantic.state_period import StatePeriod

class StateTimeInterval(BaseModel):
    # Periods of the specified time interval type, describing the attribute calculations
    periods: typing.List[StatePeriod] = Field(alias='periods')

    # Possible values for strategies in which attributes may be aggregated and reported across varying time intervals. Allowed Values - MONTHLY_CALENDAR - MONTHLY_ROLLING_30
    time_interval_type: str = Field(alias='timeIntervalType')
    class Config:
        arbitrary_types_allowed = True
