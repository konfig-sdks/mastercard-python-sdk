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

from mastercard_python_sdk.pydantic.payroll_data_out import PayrollDataOut
from mastercard_python_sdk.pydantic.report_custom_fields import ReportCustomFields

class PayrollReportConstraintsOut(BaseModel):
    payroll_data: PayrollDataOut = Field(alias='payrollData')

    report_custom_fields: typing.Optional[ReportCustomFields] = Field(None, alias='reportCustomFields')

    # A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    pay_statements_from_date: typing.Optional[int] = Field(None, alias='payStatementsFromDate')
    class Config:
        arbitrary_types_allowed = True
