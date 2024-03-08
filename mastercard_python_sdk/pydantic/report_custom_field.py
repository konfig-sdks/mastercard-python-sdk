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


class ReportCustomField(BaseModel):
    # The name of the custom field
    label: typing.Optional[str] = Field(None, alias='label')

    # The value of the custom field
    value: typing.Optional[str] = Field(None, alias='value')

    # If the custom field will show on the PDF or not
    shown: typing.Optional[bool] = Field(None, alias='shown')
    class Config:
        arbitrary_types_allowed = True
