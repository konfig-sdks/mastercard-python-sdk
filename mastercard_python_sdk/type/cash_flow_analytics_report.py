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

from mastercard_python_sdk.type.cash_flow_analytics_account_result import CashFlowAnalyticsAccountResult
from mastercard_python_sdk.type.cash_flow_analytics_business_summary import CashFlowAnalyticsBusinessSummary
from mastercard_python_sdk.type.obb_report_header import ObbReportHeader

class RequiredCashFlowAnalyticsReport(TypedDict):
    # Title of the report
    title: str

    # A customer ID represented as a number. See Add Customer API for how to create a customer ID.
    customerId: int

    reportHeader: ObbReportHeader

class OptionalCashFlowAnalyticsReport(TypedDict, total=False):
    # Cash flow results per account
    accountResults: typing.List[CashFlowAnalyticsAccountResult]

    # Business ID
    businessId: int

    businessSummary: CashFlowAnalyticsBusinessSummary

    # Name of requester
    requesterName: str

    # The total revenue
    totalRevenue: typing.Union[int, float]

class CashFlowAnalyticsReport(RequiredCashFlowAnalyticsReport, OptionalCashFlowAnalyticsReport):
    pass
