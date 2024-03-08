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

from mastercard_python_sdk.type.annual_income import AnnualIncome
from mastercard_python_sdk.type.direct_pay_statements import DirectPayStatements
from mastercard_python_sdk.type.monthly_income import MonthlyIncome

class RequiredPayrollVOIEIncomeRecord(TypedDict):
    pass

class OptionalPayrollVOIEIncomeRecord(TypedDict, total=False):
    # The current pay frequency or how often a regular pay check is:  * `Daily`  * `Weekly`  * `Bi-Weekly`  * `Semi-Monthly`  * `Monthly`  * `Quarterly`  * `Semi-Annual`  * `Annual`  * `Every 2.6 wks`  * `Every 4 wks`  * `Every 5.2 wks`  * `Other` 
    payFrequency: str

    # The current pay type:  * `Salary`  * `Hourly`  * `Daily` 
    payType: str

    # The current base or regular pay rate. Please use in conjunction with the `basePayRateUnit` field.
    basePayRate: typing.Union[int, float]

    # Unit for the base pay rate:  * `Hourly`  * `Daily`  * `Weekly`  * `Bi-Weekly`  * `Semi-Monthly`  * `Monthly`  * `Quarterly`  * `Semi-Annual`  * `Annual`  * `Every 2.6 wks`  * `Every 5.2 wks`  * `Other` 
    basePayRateUnit: str

    # The date of the oldest direct pay statement available from the payroll source, as measured by the oldest `payDate` from all the pay statements delivered.
    oldestPayStatementAvailable: str

    # The annual pay for the current year, through prior year 2 (as available)  This is a mandatory field only for VOIE-payroll report type.
    annualIncome: typing.List[AnnualIncome]

    monthlyIncome: MonthlyIncome

    # An array of payment histories for each available paycheck
    directPayStatements: typing.List[DirectPayStatements]

class PayrollVOIEIncomeRecord(RequiredPayrollVOIEIncomeRecord, OptionalPayrollVOIEIncomeRecord):
    pass
