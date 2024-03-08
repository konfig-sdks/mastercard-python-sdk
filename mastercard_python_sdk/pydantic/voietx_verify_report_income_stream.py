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

from mastercard_python_sdk.pydantic.cadence_details import CadenceDetails
from mastercard_python_sdk.pydantic.net_monthly import NetMonthly
from mastercard_python_sdk.pydantic.report_transaction import ReportTransaction

class VOIETXVerifyReportIncomeStream(BaseModel):
    # Finicity's income stream ID
    id: str = Field(alias='id')

    # A human-readable name based on the `normalizedPayee` name of the transactions for this income stream
    name: str = Field(alias='name')

    # Possible values: \"ACTIVE\", \"INACTIVE\"
    status: str = Field(alias='status')

    # Level of confidence that the deposit stream represents income (example: 85%)
    confidence: int = Field(alias='confidence')

    cadence: CadenceDetails = Field(alias='cadence')

    # A list of transaction records
    transactions: typing.List[ReportTransaction] = Field(alias='transactions')

    # A list of net monthly records. One instance for each complete calendar month in the report.
    net_monthly: typing.Optional[typing.List[NetMonthly]] = Field(None, alias='netMonthly')

    # Sum of all values in `netMonthlyIncome` over the previous 12 months
    net_annual: typing.Optional[typing.Union[int, float]] = Field(None, alias='netAnnual')

    # Projected net income over the next 12 months, across all income streams, based on `netAnnualIncome`
    projected_net_annual: typing.Optional[typing.Union[int, float]] = Field(None, alias='projectedNetAnnual')

    # Before-tax gross annual income (estimated from `netAnnual`) across all income stream in the past 12 months
    estimated_gross_annual: typing.Optional[typing.Union[int, float]] = Field(None, alias='estimatedGrossAnnual')

    # Projected gross income over the next 12 months, across all active income streams, based on `projectedNetAnnual`
    projected_gross_annual: typing.Optional[typing.Union[int, float]] = Field(None, alias='projectedGrossAnnual')

    # Monthly average amount over the previous 24 months
    average_monthly_income_net: typing.Optional[typing.Union[int, float]] = Field(None, alias='averageMonthlyIncomeNet')

    # The number of months the income transactions are observed
    income_stream_months: typing.Optional[int] = Field(None, alias='incomeStreamMonths')
    class Config:
        arbitrary_types_allowed = True
