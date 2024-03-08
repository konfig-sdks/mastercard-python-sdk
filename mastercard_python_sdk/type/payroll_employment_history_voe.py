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

from mastercard_python_sdk.type.payroll_employee_record import PayrollEmployeeRecord
from mastercard_python_sdk.type.payroll_employment_record import PayrollEmploymentRecord
from mastercard_python_sdk.type.payroll_voe_income_record import PayrollVOEIncomeRecord

class RequiredPayrollEmploymentHistoryVOE(TypedDict):
    # The last time the payroll data was updated in the payroll provider's system
    asOfDate: int

    # Name of the employer as stated by the employer in the payroll system
    employerName: str

    # The name of the payroll source where the data was retrieved
    payrollSource: str

    employee: PayrollEmployeeRecord

    employment: PayrollEmploymentRecord

    income: PayrollVOEIncomeRecord

class OptionalPayrollEmploymentHistoryVOE(TypedDict, total=False):
    pass

class PayrollEmploymentHistoryVOE(RequiredPayrollEmploymentHistoryVOE, OptionalPayrollEmploymentHistoryVOE):
    pass
