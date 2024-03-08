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


class ObbCurrentReportRequestDetails(BaseModel):
    # The date and time the report was requested
    report_request_date: str = Field(alias='reportRequestDate')

    # Number of days requested for the report
    requested_days_for_report: int = Field(alias='requestedDaysForReport')

    # Date the report would have begun on if enough data was available for which the partner requested
    requested_report_begin_date: str = Field(alias='requestedReportBeginDate')

    # Date from when the requested data is available
    report_begin_date: typing.Optional[str] = Field(None, alias='reportBeginDate')

    # Date to which the requested data is available
    report_end_date: typing.Optional[str] = Field(None, alias='reportEndDate')
    class Config:
        arbitrary_types_allowed = True
