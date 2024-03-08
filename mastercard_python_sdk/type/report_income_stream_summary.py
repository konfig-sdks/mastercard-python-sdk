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

from mastercard_python_sdk.type.net_monthly import NetMonthly
from mastercard_python_sdk.type.report_income_estimate import ReportIncomeEstimate

class RequiredReportIncomeStreamSummary(TypedDict):
    # Possible values: \"HIGH\", \"MODERATE\", \"LOW\", \"NO\"
    confidenceType: str

    # A list of net monthly records. One instance for each complete calendar month in the report.
    netMonthly: typing.List[NetMonthly]

    incomeEstimate: ReportIncomeEstimate

class OptionalReportIncomeStreamSummary(TypedDict, total=False):
    pass

class ReportIncomeStreamSummary(RequiredReportIncomeStreamSummary, OptionalReportIncomeStreamSummary):
    pass
