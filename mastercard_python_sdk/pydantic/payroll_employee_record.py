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

from mastercard_python_sdk.pydantic.payroll_employee_address import PayrollEmployeeAddress

class PayrollEmployeeRecord(BaseModel):
    # Full name of the employee: first, middle (if stated), and last name
    name: str = Field(alias='name')

    # First name of employee
    given_name: typing.Optional[str] = Field(None, alias='givenName')

    # Middle name of employee, if stated
    middle_name: typing.Optional[str] = Field(None, alias='middleName')

    # Last name of employee
    family_name: typing.Optional[str] = Field(None, alias='familyName')

    # Array of addresses
    address: typing.Optional[typing.List[PayrollEmployeeAddress]] = Field(None, alias='address')
    class Config:
        arbitrary_types_allowed = True
