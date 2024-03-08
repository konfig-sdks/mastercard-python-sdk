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

from mastercard_python_sdk.type.obb_report_header import ObbReportHeader
from mastercard_python_sdk.type.payment_history_analytics import PaymentHistoryAnalytics

class RequiredPaymentHistoryReport(TypedDict):
    # Title of the report
    title: str

    # A customer ID represented as a number. See Add Customer API for how to create a customer ID.
    customerId: int

    # Customer and report metadata
    reportHeader: ObbReportHeader

class OptionalPaymentHistoryReport(TypedDict, total=False):
    # List of account IDs included in the report
    accountIds: typing.List[int]

    # Business ID
    businessId: int

    # Name of requester
    requesterName: str

    analytics: PaymentHistoryAnalytics

class PaymentHistoryReport(RequiredPaymentHistoryReport, OptionalPaymentHistoryReport):
    pass
