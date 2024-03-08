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


class ReportAccountPosition(BaseModel):
    # The id of the investment position
    id: typing.Optional[typing.Union[int, float]] = Field(None, alias='id')

    # What currency the account operates in
    currency: typing.Optional[str] = Field(None, alias='currency')

    # The investment position’s market ticker symbol
    symbol: typing.Optional[str] = Field(None, alias='symbol')

    # The security name for the investment holding
    security_name: typing.Optional[str] = Field(None, alias='securityName')

    # The number of units of the holding
    units: typing.Optional[typing.Union[int, float]] = Field(None, alias='units')

    # Market value of an investment position at the time of retrieval
    market_value: typing.Optional[typing.Union[int, float]] = Field(None, alias='marketValue')

    # The current price of the investment holding
    current_price: typing.Optional[typing.Union[int, float]] = Field(None, alias='currentPrice')

    # Type of security of the investment position
    security_type: typing.Optional[typing.Union[int, float]] = Field(None, alias='securityType')
    class Config:
        arbitrary_types_allowed = True
