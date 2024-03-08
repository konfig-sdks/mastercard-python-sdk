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


class DirectDeposits(BaseModel):
    # Bank account type:  * `Checking`  * `Savings`  * `Loan`: Loan account employee choose to direct a portion of their net pay to help pay off a loan 
    account_type_code: typing.Optional[str] = Field(None, alias='accountTypeCode')

    # Direct deposit amount
    amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='amount')

    # Last four digits of the deposit account number
    account_last_four: typing.Optional[str] = Field(None, alias='accountLastFour')

    # Routing number for the deposit account
    routing_number: typing.Optional[str] = Field(None, alias='routingNumber')
    class Config:
        arbitrary_types_allowed = True
