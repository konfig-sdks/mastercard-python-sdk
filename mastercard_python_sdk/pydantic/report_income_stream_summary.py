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

from mastercard_python_sdk.pydantic.net_monthly import NetMonthly
from mastercard_python_sdk.pydantic.report_income_estimate import ReportIncomeEstimate

class ReportIncomeStreamSummary(BaseModel):
    # Possible values: \"HIGH\", \"MODERATE\", \"LOW\", \"NO\"
    confidence_type: str = Field(alias='confidenceType')

    # A list of net monthly records. One instance for each complete calendar month in the report.
    net_monthly: typing.List[NetMonthly] = Field(alias='netMonthly')

    income_estimate: ReportIncomeEstimate = Field(alias='incomeEstimate')
    class Config:
        arbitrary_types_allowed = True
