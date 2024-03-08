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

from mastercard_python_sdk.pydantic.obb_report_header import ObbReportHeader
from mastercard_python_sdk.pydantic.payment_history_analytics import PaymentHistoryAnalytics

class PaymentHistoryReport(BaseModel):
    # Title of the report
    title: str = Field(alias='title')

    # A customer ID represented as a number. See Add Customer API for how to create a customer ID.
    customer_id: int = Field(alias='customerId')

    # Customer and report metadata
    report_header: ObbReportHeader = Field(alias='reportHeader')

    # List of account IDs included in the report
    account_ids: typing.Optional[typing.List[int]] = Field(None, alias='accountIds')

    # Business ID
    business_id: typing.Optional[int] = Field(None, alias='businessId')

    # Name of requester
    requester_name: typing.Optional[str] = Field(None, alias='requesterName')

    analytics: typing.Optional[PaymentHistoryAnalytics] = Field(None, alias='analytics')
    class Config:
        arbitrary_types_allowed = True
