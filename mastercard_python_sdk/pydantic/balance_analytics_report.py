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

from mastercard_python_sdk.pydantic.balance_analytics_account_result import BalanceAnalyticsAccountResult
from mastercard_python_sdk.pydantic.balance_analytics_business_summary import BalanceAnalyticsBusinessSummary
from mastercard_python_sdk.pydantic.obb_report_header import ObbReportHeader

class BalanceAnalyticsReport(BaseModel):
    # Title of the report
    title: str = Field(alias='title')

    # A customer ID represented as a number. See Add Customer API for how to create a customer ID.
    customer_id: int = Field(alias='customerId')

    report_header: ObbReportHeader = Field(alias='reportHeader')

    # Balance results per account
    account_results: typing.Optional[typing.List[BalanceAnalyticsAccountResult]] = Field(None, alias='accountResults')

    # Business ID
    business_id: typing.Optional[int] = Field(None, alias='businessId')

    business_summary: typing.Optional[BalanceAnalyticsBusinessSummary] = Field(None, alias='businessSummary')

    # Name of requester
    requester_name: typing.Optional[str] = Field(None, alias='requesterName')
    class Config:
        arbitrary_types_allowed = True
