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

from mastercard_python_sdk.pydantic.cash_flow_insufficient_funds_fees import CashFlowInsufficientFundsFees

class CashFlowNegativeTriggers(BaseModel):
    insufficient_fund_fees: typing.Optional[CashFlowInsufficientFundsFees] = Field(None, alias='insufficientFundFees')
    class Config:
        arbitrary_types_allowed = True
