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
from pydantic import BaseModel, Field, RootModel

from mastercard_python_sdk.pydantic.app_status import AppStatus

class AppStatuses(BaseModel):
    # The total number of results
    total_records: int = Field(alias='totalRecords')

    # The total number of pages
    total_pages: int = Field(alias='totalPages')

    # The current page number
    page_number: int = Field(alias='pageNumber')

    # The number of results per page
    number_of_records_per_page: int = Field(alias='numberOfRecordsPerPage')

    # A list of applications with their statuses
    applications: typing.List[AppStatus] = Field(alias='applications')
    class Config:
        arbitrary_types_allowed = True
