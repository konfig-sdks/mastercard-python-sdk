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


class RequiredReportIncomeEstimate(TypedDict):
    # Sum of all values in `netMonthlyIncome` over the previous 12 months
    netAnnual: typing.Union[int, float]

    # Projected net income over the next 12 months, across all income streams, based on `netAnnualIncome`
    projectedNetAnnual: typing.Union[int, float]

    # Before-tax gross annual income (estimated from `netAnnual`) across all income stream in the past 12 months
    estimatedGrossAnnual: typing.Union[int, float]

    # Projected gross income over the next 12 months, across all active income streams, based on `projectedNetAnnual`
    projectedGrossAnnual: typing.Union[int, float]

class OptionalReportIncomeEstimate(TypedDict, total=False):
    pass

class ReportIncomeEstimate(RequiredReportIncomeEstimate, OptionalReportIncomeEstimate):
    pass
