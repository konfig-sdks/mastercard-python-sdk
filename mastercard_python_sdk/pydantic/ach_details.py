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


class ACHDetails(BaseModel):
    # The routing number of the financial institution for specific customer account
    routing_number: str = Field(alias='routingNumber')

    # The account number for initiating ACH transfers for this account
    real_account_number: str = Field(alias='realAccountNumber')
    class Config:
        arbitrary_types_allowed = True
