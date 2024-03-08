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

from mastercard_python_sdk.pydantic.state_attribute import StateAttribute
from mastercard_python_sdk.pydantic.stream_model import StreamModel
from mastercard_python_sdk.pydantic.transactional_attribute import TransactionalAttribute

class AccountAnalytics(BaseModel):
    # List of calculated transactional attributes
    transactional_attributes: typing.List[TransactionalAttribute] = Field(alias='transactionalAttributes')

    # List of calculated state attributes
    state_attributes: typing.List[StateAttribute] = Field(alias='stateAttributes')

    # List of generated streams
    streams: typing.List[StreamModel] = Field(alias='streams')
    class Config:
        arbitrary_types_allowed = True
