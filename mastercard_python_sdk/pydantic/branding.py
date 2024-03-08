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


class Branding(BaseModel):
    # File path of the institution's logo. For white backgrounds designed at 375 x 72, has built in spacing around it to normalize brand sizing.
    logo: typing.Optional[str] = Field(None, alias='logo')

    # File path of the institution's alternate logo. For colored backgrounds designed at 375 x 72 has built in spacing around it to normalize brand sizing.
    alternate_logo: typing.Optional[str] = Field(None, alias='alternateLogo')

    # File path of the institution's icon. For search results designed at 40 x 40.
    icon: typing.Optional[str] = Field(None, alias='icon')

    # Hex code for the institution's primary color
    primary_color: typing.Optional[str] = Field(None, alias='primaryColor')

    # File path of institution name logo. For popular banks designed at 160 x 72.
    tile: typing.Optional[str] = Field(None, alias='tile')
    class Config:
        arbitrary_types_allowed = True
