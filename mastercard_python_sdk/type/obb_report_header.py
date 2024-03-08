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


class RequiredObbReportHeader(TypedDict):
    # Date the report was requested
    reportDate: str

    # Generated unique report ID
    reportId: str

class OptionalObbReportHeader(TypedDict, total=False):
    # Business address line 1
    businessAddress: str

    # Business address city
    businessCity: str

    # Name of the business
    businessName: str

    # Business address state
    businessState: str

    # Business address zip
    businessZip: str

    # Partner-provided reference number
    referenceNumber: str

class ObbReportHeader(RequiredObbReportHeader, OptionalObbReportHeader):
    pass
