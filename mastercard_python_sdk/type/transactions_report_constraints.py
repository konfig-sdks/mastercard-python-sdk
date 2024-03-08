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

class RequiredTransactionsReportConstraints(TypedDict):
    pass

class OptionalTransactionsReportConstraints(TypedDict, total=False):
    # A whitespace-separated list of account IDs to be included in the report (all accounts will be included if not set)
    accountIds: str

    # A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    fromDate: int

    reportCustomFields: ReportCustomFields

class TransactionsReportConstraints(RequiredTransactionsReportConstraints, OptionalTransactionsReportConstraints):
    pass
