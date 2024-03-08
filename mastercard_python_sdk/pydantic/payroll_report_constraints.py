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

from mastercard_python_sdk.pydantic.payroll_data import PayrollData
from mastercard_python_sdk.pydantic.report_custom_fields import ReportCustomFields

class PayrollReportConstraints(BaseModel):
    payroll_data: PayrollData = Field(alias='payrollData')

    report_custom_fields: typing.Optional[ReportCustomFields] = Field(None, alias='reportCustomFields')

    # Limits the pay statement history in the VOIE - Payroll report income record. Pay statements are only included if the payDate of the statement is equal to or greater than the start date requested. Date should be in Unix epoch time (in seconds). See: Handling Epoch Dates and Times.
    pay_statements_from_date: typing.Optional[int] = Field(None, alias='payStatementsFromDate')

    # Use case for requesting the consumer's data. Current supported enumerations are \"Mortgage\" and \"KYC\". If your use case doesn't match one of these please reach out to your technical point of contact.
    market_segment: typing.Optional[str] = Field(None, alias='marketSegment')

    # Only used on an exception basis for clients that need to exclude EmpInfo data from the VOE-Payroll or VOIE-Payroll report. If true is passed EmpInfo payroll provider's data will not be searched or returned.
    exclude_emp_info: typing.Optional[bool] = Field(None, alias='excludeEmpInfo')

    # FCRA required 2-digit Permissible Purpose Code, specifying the reason for retrieving this report.
    purpose: typing.Optional[str] = Field(None, alias='purpose')
    class Config:
        arbitrary_types_allowed = True
