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


class ThirdPartyAccessPeriod(BaseModel):
    # Multiple types will be supported. Presently below types are supported. * \"timeframe\": Specifies a timeframe bounded by a startTime and endTime.   The startTime is the time at which the access was granted and the access key generated,   and the endTime is the time at which the access was revoked. Times are represented in ISO 8601 format(\"2022-03-10T06:06:20Z\")
    type: str = Field(alias='type')

    # A date-time with time zone
    start_time: datetime = Field(alias='startTime')

    # A date-time with time zone
    end_time: datetime = Field(alias='endTime')
    class Config:
        arbitrary_types_allowed = True
