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

from mastercard_python_sdk.type.payroll_employee_address import PayrollEmployeeAddress

class RequiredPayrollEmployeeRecord(TypedDict):
    # Full name of the employee: first, middle (if stated), and last name
    name: str

class OptionalPayrollEmployeeRecord(TypedDict, total=False):
    # First name of employee
    givenName: str

    # Middle name of employee, if stated
    middleName: str

    # Last name of employee
    familyName: str

    # Array of addresses
    address: typing.List[PayrollEmployeeAddress]

class PayrollEmployeeRecord(RequiredPayrollEmployeeRecord, OptionalPayrollEmployeeRecord):
    pass
