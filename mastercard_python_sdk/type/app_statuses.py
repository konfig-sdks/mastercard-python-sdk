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

from mastercard_python_sdk.type.app_status import AppStatus

class RequiredAppStatuses(TypedDict):
    # The total number of results
    totalRecords: int

    # The total number of pages
    totalPages: int

    # The current page number
    pageNumber: int

    # The number of results per page
    numberOfRecordsPerPage: int

    # A list of applications with their statuses
    applications: typing.List[AppStatus]

class OptionalAppStatuses(TypedDict, total=False):
    pass

class AppStatuses(RequiredAppStatuses, OptionalAppStatuses):
    pass
