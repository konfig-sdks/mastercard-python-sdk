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


class PayrollDataOut(BaseModel):
    # An ID to identify the data retrieved from the payroll providers for the report.
    payroll_data_retrieval_id: typing.Optional[str] = Field(None, alias='payrollDataRetrievalId')

    # An array of employmentIds
    employment_ids: typing.Optional[typing.List[str]] = Field(None, alias='employmentIds')

    # An array of payrollAccountIds
    payroll_account_ids: typing.Optional[typing.List[str]] = Field(None, alias='payrollAccountIds')

    # A report ID
    report_id: typing.Optional[str] = Field(None, alias='reportId')
    class Config:
        arbitrary_types_allowed = True
