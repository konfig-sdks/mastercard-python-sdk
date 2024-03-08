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

from mastercard_python_sdk.type.report_custom_fields import ReportCustomFields

class RequiredPrequalificationReportConstraints(TypedDict):
    pass

class OptionalPrequalificationReportConstraints(TypedDict, total=False):
    # A whitespace-separated list of account IDs to be included in the report (all accounts will be included if not set)
    accountIds: str

    reportCustomFields: ReportCustomFields

    # Include the non-sufficient funds (NSF) summary JSON and the NSF summary PDF section in the report. Data included: * Account  * Total number of NSF funds  * Days since the most recent NFS funds fee
    showNsf: bool

    # A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    fromDate: int

class PrequalificationReportConstraints(RequiredPrequalificationReportConstraints, OptionalPrequalificationReportConstraints):
    pass
