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


class ObbInstitution(BaseModel):
    # ID of the financial institution
    institution_id: int = Field(alias='institutionId')

    # URL of the institution logo icon for reporting
    institution_icon_url: typing.Optional[str] = Field(None, alias='institutionIconUrl')

    # Name of the financial institution
    institution_name: typing.Optional[str] = Field(None, alias='institutionName')

    # Primary branding color of the institution, in hex color format
    institution_primary_color: typing.Optional[str] = Field(None, alias='institutionPrimaryColor')
    class Config:
        arbitrary_types_allowed = True
