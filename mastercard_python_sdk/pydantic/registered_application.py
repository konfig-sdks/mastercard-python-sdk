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


class RegisteredApplication(BaseModel):
    # Identifier to track the application registration from the App Registration and Get App Registration Status APIs, represented as a number
    pre_app_id: int = Field(alias='preAppId')

    # The status of an app registration request. \"A\" means approved. \"P\" means pending which is the status when initially submitted or when the app is modified and awaiting approval. \"R\" means rejected. If it is rejected there will be a note with the rejected reason.
    status: str = Field(alias='status')
    class Config:
        arbitrary_types_allowed = True
