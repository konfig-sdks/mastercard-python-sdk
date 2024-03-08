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


class Receiver(BaseModel):
    # Routing number of receiving bank
    routing_number: str = Field(alias='routingNumber')

    # Micro entries receiving account number of bank
    account_number: str = Field(alias='accountNumber')

    # The list of supported account types. * \"checking\": Standard checking * \"savings\": Standard savings
    account_type: str = Field(alias='accountType')

    # Name of the customer
    name: str = Field(alias='name')

    # Transaction memo to be displayed for transactions
    memo: typing.Optional[str] = Field(None, alias='memo')
    class Config:
        arbitrary_types_allowed = True
