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


class ChildInstitution(BaseModel):
    # The RSSD ID is a unique identifier assigned to financial institutions by the Federal Reserve. While the length of the RSSD ID varies by institution, it cannot exceed 10 numerical digits.
    rssd: int = Field(alias='rssd')

    # The RSSD ID is a unique identifier assigned to financial institutions by the Federal Reserve. While the length of the RSSD ID varies by institution, it cannot exceed 10 numerical digits.
    parent_r_s_s_d: int = Field(alias='parentRSSD')

    # The name of the institution
    name: str = Field(alias='name')

    # The ID of a financial institution, represented as a number
    institution_id: int = Field(alias='institutionId')
    class Config:
        arbitrary_types_allowed = True
