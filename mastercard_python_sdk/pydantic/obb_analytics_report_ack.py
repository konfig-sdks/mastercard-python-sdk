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


class ObbAnalyticsReportAck(BaseModel):
    # Title of the report
    title: str = Field(alias='title')

    # List of account IDs included in the report
    account_ids: typing.List[int] = Field(alias='accountIds')

    # Created date of balance analytics request
    created_date: str = Field(alias='createdDate')

    # A customer ID represented as a number. See Add Customer API for how to create a customer ID.
    customer_id: int = Field(alias='customerId')

    # A report ID
    report_id: str = Field(alias='reportId')

    # PIN that may be used to access the report
    report_pin: str = Field(alias='reportPin')

    # Business ID associated with the requested customer
    business_id: typing.Optional[int] = Field(None, alias='businessId')

    # Name of requester
    requester_name: typing.Optional[str] = Field(None, alias='requesterName')
    class Config:
        arbitrary_types_allowed = True
