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


class ObbReportHeader(BaseModel):
    # Date the report was requested
    report_date: str = Field(alias='reportDate')

    # Generated unique report ID
    report_id: str = Field(alias='reportId')

    # Business address line 1
    business_address: typing.Optional[str] = Field(None, alias='businessAddress')

    # Business address city
    business_city: typing.Optional[str] = Field(None, alias='businessCity')

    # Name of the business
    business_name: typing.Optional[str] = Field(None, alias='businessName')

    # Business address state
    business_state: typing.Optional[str] = Field(None, alias='businessState')

    # Business address zip
    business_zip: typing.Optional[str] = Field(None, alias='businessZip')

    # Partner-provided reference number
    reference_number: typing.Optional[str] = Field(None, alias='referenceNumber')
    class Config:
        arbitrary_types_allowed = True
