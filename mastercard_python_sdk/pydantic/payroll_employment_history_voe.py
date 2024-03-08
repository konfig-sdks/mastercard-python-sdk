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

from mastercard_python_sdk.pydantic.payroll_employee_record import PayrollEmployeeRecord
from mastercard_python_sdk.pydantic.payroll_employment_record import PayrollEmploymentRecord
from mastercard_python_sdk.pydantic.payroll_voe_income_record import PayrollVOEIncomeRecord

class PayrollEmploymentHistoryVOE(BaseModel):
    # The last time the payroll data was updated in the payroll provider's system
    as_of_date: int = Field(alias='asOfDate')

    # Name of the employer as stated by the employer in the payroll system
    employer_name: str = Field(alias='employerName')

    # The name of the payroll source where the data was retrieved
    payroll_source: str = Field(alias='payrollSource')

    employee: PayrollEmployeeRecord = Field(alias='employee')

    employment: PayrollEmploymentRecord = Field(alias='employment')

    income: PayrollVOEIncomeRecord = Field(alias='income')
    class Config:
        arbitrary_types_allowed = True
