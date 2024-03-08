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

from mastercard_python_sdk.type.cadence_details import CadenceDetails
from mastercard_python_sdk.type.net_monthly import NetMonthly
from mastercard_python_sdk.type.report_transaction import ReportTransaction

class RequiredVOIETXVerifyReportIncomeStream(TypedDict):
    # Finicity's income stream ID
    id: str

    # A human-readable name based on the `normalizedPayee` name of the transactions for this income stream
    name: str

    # Possible values: \"ACTIVE\", \"INACTIVE\"
    status: str

    # Level of confidence that the deposit stream represents income (example: 85%)
    confidence: int

    cadence: CadenceDetails

    # A list of transaction records
    transactions: typing.List[ReportTransaction]

class OptionalVOIETXVerifyReportIncomeStream(TypedDict, total=False):
    # A list of net monthly records. One instance for each complete calendar month in the report.
    netMonthly: typing.List[NetMonthly]

    # Sum of all values in `netMonthlyIncome` over the previous 12 months
    netAnnual: typing.Union[int, float]

    # Projected net income over the next 12 months, across all income streams, based on `netAnnualIncome`
    projectedNetAnnual: typing.Union[int, float]

    # Before-tax gross annual income (estimated from `netAnnual`) across all income stream in the past 12 months
    estimatedGrossAnnual: typing.Union[int, float]

    # Projected gross income over the next 12 months, across all active income streams, based on `projectedNetAnnual`
    projectedGrossAnnual: typing.Union[int, float]

    # Monthly average amount over the previous 24 months
    averageMonthlyIncomeNet: typing.Union[int, float]

    # The number of months the income transactions are observed
    incomeStreamMonths: int

class VOIETXVerifyReportIncomeStream(RequiredVOIETXVerifyReportIncomeStream, OptionalVOIETXVerifyReportIncomeStream):
    pass
