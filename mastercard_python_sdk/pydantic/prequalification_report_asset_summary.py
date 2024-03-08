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


class PrequalificationReportAssetSummary(BaseModel):
    # The current balance of the account
    current_balance: typing.Union[int, float] = Field(alias='currentBalance')

    # The two month average daily balance of the account
    two_month_average: typing.Union[int, float] = Field(alias='twoMonthAverage')

    # The beginning balance of the account per the time period of the report
    beginning_balance: typing.Union[int, float] = Field(alias='beginningBalance')

    # The asset type: \"checking\", \"savings\", \"moneyMarket\", \"cd\", \"investment\"
    type: typing.Optional[str] = Field(None, alias='type')

    # The available balance for the account
    available_balance: typing.Optional[typing.Union[int, float]] = Field(None, alias='availableBalance')

    # The six month average daily balance of the account
    six_month_average: typing.Optional[typing.Union[int, float]] = Field(None, alias='sixMonthAverage')
    class Config:
        arbitrary_types_allowed = True
