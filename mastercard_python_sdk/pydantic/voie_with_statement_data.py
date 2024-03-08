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


class VOIEWithStatementData(BaseModel):
    # A list of pay statement asset IDs
    asset_ids: typing.List[str] = Field(alias='assetIds')

    # Field to indicate whether to extract the earnings on all pay statements
    extract_earnings: typing.Optional[bool] = Field(None, alias='extractEarnings')

    # Field to indicate whether to extract the deductions on all pay statements
    extract_deductions: typing.Optional[bool] = Field(None, alias='extractDeductions')

    # Field to indicate whether to extract the direct deposits on all pay statements
    extract_direct_deposit: typing.Optional[bool] = Field(None, alias='extractDirectDeposit')
    class Config:
        arbitrary_types_allowed = True
