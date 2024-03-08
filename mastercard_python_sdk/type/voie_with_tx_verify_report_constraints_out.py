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

from mastercard_python_sdk.type.report_account_ids import ReportAccountIds
from mastercard_python_sdk.type.report_custom_fields import ReportCustomFields
from mastercard_python_sdk.type.voie_with_interview_data import VOIEWithInterviewData

class RequiredVOIEWithTXVerifyReportConstraintsOut(TypedDict):
    voieWithInterviewData: VOIEWithInterviewData

class OptionalVOIEWithTXVerifyReportConstraintsOut(TypedDict, total=False):
    accountIds: ReportAccountIds

    reportCustomFields: ReportCustomFields

    # A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    fromDate: int

    # Include income streams in the report, based on the income stream's confidence score. For example, Use the value 50 to include only income streams with a confidence score of 50 or higher.
    incomeStreamConfidenceMinimum: int

class VOIEWithTXVerifyReportConstraintsOut(RequiredVOIEWithTXVerifyReportConstraintsOut, OptionalVOIEWithTXVerifyReportConstraintsOut):
    pass
