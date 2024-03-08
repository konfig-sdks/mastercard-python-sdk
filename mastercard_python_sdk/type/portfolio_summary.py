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

from mastercard_python_sdk.type.portfolio_report import PortfolioReport

class RequiredPortfolioSummary(TypedDict):
    # A unique identifier that will be consistent across all reports created for the same customer
    portfolioId: str

    # A list of reports in the portfolio
    reports: typing.List[PortfolioReport]

class OptionalPortfolioSummary(TypedDict, total=False):
    pass

class PortfolioSummary(RequiredPortfolioSummary, OptionalPortfolioSummary):
    pass
