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


class PayrollVOEIncomeRecord(BaseModel):
    # The current pay frequency or how often a regular pay check is:  * `Daily`  * `Weekly`  * `Bi-Weekly`  * `Semi-Monthly`  * `Monthly`  * `Quarterly`  * `Semi-Annual`  * `Annual`  * `Every 2.6 wks`  * `Every 4 wks`  * `Every 5.2 wks`  * `Other` 
    pay_frequency: typing.Optional[str] = Field(None, alias='payFrequency')
    class Config:
        arbitrary_types_allowed = True
