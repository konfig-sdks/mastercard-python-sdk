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


class RequiredAnalyticsReportData(TypedDict):
    # Field to indicate if the requested report is for CRA or NONCRA. For small business lending or other similar business use cases, pass the value as “true” for purposes of this field.
    forCraPurpose: bool

class OptionalAnalyticsReportData(TypedDict, total=False):
    # Field to indicate if the business owner will personally guarantee the loan. If true, a consumer record will be required.
    applicantIsPersonalGuarantor: bool

    # Requested time interval for attribute values.
    timeIntervalTypes: typing.List[str]

class AnalyticsReportData(RequiredAnalyticsReportData, OptionalAnalyticsReportData):
    pass
