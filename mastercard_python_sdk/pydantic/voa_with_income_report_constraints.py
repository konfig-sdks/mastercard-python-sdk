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

from mastercard_python_sdk.pydantic.report_custom_fields import ReportCustomFields

class VOAWithIncomeReportConstraints(BaseModel):
    # A whitespace-separated list of account IDs to be included in the report (all accounts will be included if not set)
    account_ids: typing.Optional[str] = Field(None, alias='accountIds')

    report_custom_fields: typing.Optional[ReportCustomFields] = Field(None, alias='reportCustomFields')

    # Include the non-sufficient funds (NSF) summary JSON and the NSF summary PDF section in the report. Data included: * Account  * Total number of NSF funds  * Days since the most recent NFS funds fee
    show_nsf: typing.Optional[bool] = Field(None, alias='showNsf')

    # A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    from_date: typing.Optional[int] = Field(None, alias='fromDate')

    # Include income streams in the report, based on the income stream's confidence score. For example, Use the value 50 to include only income streams with a confidence score of 50 or higher.
    income_stream_confidence_minimum: typing.Optional[int] = Field(None, alias='incomeStreamConfidenceMinimum')
    class Config:
        arbitrary_types_allowed = True
