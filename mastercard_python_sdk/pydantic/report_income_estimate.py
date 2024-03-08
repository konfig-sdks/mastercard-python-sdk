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


class ReportIncomeEstimate(BaseModel):
    # Sum of all values in `netMonthlyIncome` over the previous 12 months
    net_annual: typing.Union[int, float] = Field(alias='netAnnual')

    # Projected net income over the next 12 months, across all income streams, based on `netAnnualIncome`
    projected_net_annual: typing.Union[int, float] = Field(alias='projectedNetAnnual')

    # Before-tax gross annual income (estimated from `netAnnual`) across all income stream in the past 12 months
    estimated_gross_annual: typing.Union[int, float] = Field(alias='estimatedGrossAnnual')

    # Projected gross income over the next 12 months, across all active income streams, based on `projectedNetAnnual`
    projected_gross_annual: typing.Union[int, float] = Field(alias='projectedGrossAnnual')
    class Config:
        arbitrary_types_allowed = True
