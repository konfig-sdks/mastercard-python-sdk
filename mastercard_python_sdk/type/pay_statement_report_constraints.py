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

from mastercard_python_sdk.type.pay_statement_data import PayStatementData
from mastercard_python_sdk.type.report_custom_fields import ReportCustomFields

class RequiredPayStatementReportConstraints(TypedDict):
    paystatementReport: PayStatementData

class OptionalPayStatementReportConstraints(TypedDict, total=False):
    reportCustomFields: ReportCustomFields

class PayStatementReportConstraints(RequiredPayStatementReportConstraints, OptionalPayStatementReportConstraints):
    pass