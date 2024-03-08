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


class NewCustomer(BaseModel):
    # The customer's username, assigned by the partner (a unique identifier), following these rules: minimum 6 characters maximum 255 characters any mix of uppercase, lowercase, numeric, and non-alphabet special characters ! @ . # $ % & * _ - + the use of email in this field is discouraged it is recommended to use a unique non-email identifier. Use of special characters may result in an error (e.g. í, ü, etc.). Usernames are unique. A username used in Test Drive can't be reused in other plans.
    username: str = Field(alias='username')

    # The first name of the account holder
    first_name: typing.Optional[str] = Field(None, alias='firstName')

    # The last name of the account holder
    last_name: typing.Optional[str] = Field(None, alias='lastName')

    # `applicationId` value returned from the Get App Registration Status API and the partner assign the customers to. This cannot be changed once set. Only applicable in cases of partners with multiple registered applications. If the partner only has one app, this can usually be omitted. This field is populated after the app is in a status approved.
    application_id: typing.Optional[str] = Field(None, alias='applicationId')

    # A phone number (max length 15).
    phone: typing.Optional[str] = Field(None, alias='phone')

    # An email address
    email: typing.Optional[str] = Field(None, alias='email')
    class Config:
        arbitrary_types_allowed = True
