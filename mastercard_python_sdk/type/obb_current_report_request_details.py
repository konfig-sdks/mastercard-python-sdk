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


class RequiredObbCurrentReportRequestDetails(TypedDict):
    # The date and time the report was requested
    reportRequestDate: str

    # Number of days requested for the report
    requestedDaysForReport: int

    # Date the report would have begun on if enough data was available for which the partner requested
    requestedReportBeginDate: str

class OptionalObbCurrentReportRequestDetails(TypedDict, total=False):
    # Date from when the requested data is available
    reportBeginDate: str

    # Date to which the requested data is available
    reportEndDate: str

class ObbCurrentReportRequestDetails(RequiredObbCurrentReportRequestDetails, OptionalObbCurrentReportRequestDetails):
    pass
