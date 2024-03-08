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

from mastercard_python_sdk.type.deduction import Deduction
from mastercard_python_sdk.type.direct_deposit import DirectDeposit
from mastercard_python_sdk.type.employee import Employee
from mastercard_python_sdk.type.employer import Employer
from mastercard_python_sdk.type.pay_stat import PayStat

class RequiredVOIEPayStatement(TypedDict):
    pass

class OptionalVOIEPayStatement(TypedDict, total=False):
    # The pay period of the pay statement
    payPeriod: str

    # Designates whether the pay statement is billable
    billable: bool

    # The asset ID of the stored pay statement
    assetId: str

    # The listed pay date for the pay statement
    payDate: int

    # The beginning of the pay period
    startDate: int

    # The end of the pay period
    endDate: int

    # The total pay after deductions for the employee for the current pay period
    netPayCurrent: typing.Union[int, float]

    # The total accumulation of pay after deductions for the employee for the current pay year
    netPayYTD: typing.Union[int, float]

    # The total pay before deductions for the employee for the current pay period
    grossPayCurrent: typing.Union[int, float]

    # The total accumulation of pay before deductions for the employee for the current pay year
    grossPayYTD: typing.Union[int, float]

    # The company that provides the pay stub.
    payrollProvider: str

    employer: Employer

    employee: Employee

    # Information pertaining to the earnings on the pay statement
    payStat: typing.List[PayStat]

    # Information pertaining to deductions on the pay statement
    deductions: typing.List[Deduction]

    # Information pertaining to direct deposits on the pay statement
    directDeposits: typing.List[DirectDeposit]

class VOIEPayStatement(RequiredVOIEPayStatement, OptionalVOIEPayStatement):
    pass
