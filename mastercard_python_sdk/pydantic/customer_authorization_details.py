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


class CustomerAuthorizationDetails(BaseModel):
    # Institution login id of the customer.
    institution_login_id: int = Field(alias='institutionLoginId')

    # Authorization start date and time in ISO 8601 format.
    authorization_start_date: str = Field(alias='authorizationStartDate')

    # Authorization end date and time in ISO 8601 format.
    authorization_end_date: str = Field(alias='authorizationEndDate')
    class Config:
        arbitrary_types_allowed = True
