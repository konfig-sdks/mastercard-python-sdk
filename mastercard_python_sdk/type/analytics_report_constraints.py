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

from mastercard_python_sdk.type.analytics_report_data import AnalyticsReportData
from mastercard_python_sdk.type.report_custom_fields import ReportCustomFields

class RequiredAnalyticsReportConstraints(TypedDict):
    pass

class OptionalAnalyticsReportConstraints(TypedDict, total=False):
    analyticsReportData: AnalyticsReportData

    # A whitespace-separated list of account IDs to be included in the report (all accounts will be included if not set)
    accountIds: str

    reportCustomFields: ReportCustomFields

    # A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    fromDate: int

class AnalyticsReportConstraints(RequiredAnalyticsReportConstraints, OptionalAnalyticsReportConstraints):
    pass
