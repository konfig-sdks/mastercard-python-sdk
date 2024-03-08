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

from mastercard_python_sdk.type.state_time_interval import StateTimeInterval

class RequiredStateAttribute(TypedDict):
    # Name of Attribute as mentioned in Data Dictionary
    attributeName: str

    # List of state values grouped by specified Time Interval
    reportedByTimePeriods: typing.List[StateTimeInterval]

class OptionalStateAttribute(TypedDict, total=False):
    pass

class StateAttribute(RequiredStateAttribute, OptionalStateAttribute):
    pass
