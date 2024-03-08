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


class PayrollEmployerAddress(BaseModel):
    # Employer address as stated by the employer in the payroll system
    address1: typing.Optional[str] = Field(None, alias='address1')

    # Employer city as stated by the employer in the payroll system
    city: typing.Optional[str] = Field(None, alias='city')

    # Employer state as stated by the employer in the payroll system
    state: typing.Optional[str] = Field(None, alias='state')

    # Employer zip code as stated by the employer in the payroll system
    zip: typing.Optional[str] = Field(None, alias='zip')
    class Config:
        arbitrary_types_allowed = True
