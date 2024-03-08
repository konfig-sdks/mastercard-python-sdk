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


class RequiredObbAnalyticsReportAck(TypedDict):
    # Title of the report
    title: str

    # List of account IDs included in the report
    accountIds: typing.List[int]

    # Created date of balance analytics request
    createdDate: str

    # A customer ID represented as a number. See Add Customer API for how to create a customer ID.
    customerId: int

    # A report ID
    reportId: str

    # PIN that may be used to access the report
    reportPin: str

class OptionalObbAnalyticsReportAck(TypedDict, total=False):
    # Business ID associated with the requested customer
    businessId: int

    # Name of requester
    requesterName: str

class ObbAnalyticsReportAck(RequiredObbAnalyticsReportAck, OptionalObbAnalyticsReportAck):
    pass
