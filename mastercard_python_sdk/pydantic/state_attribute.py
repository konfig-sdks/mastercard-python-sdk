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

from mastercard_python_sdk.pydantic.state_time_interval import StateTimeInterval

class StateAttribute(BaseModel):
    # Name of Attribute as mentioned in Data Dictionary
    attribute_name: str = Field(alias='attributeName')

    # List of state values grouped by specified Time Interval
    reported_by_time_periods: typing.List[StateTimeInterval] = Field(alias='reportedByTimePeriods')
    class Config:
        arbitrary_types_allowed = True
