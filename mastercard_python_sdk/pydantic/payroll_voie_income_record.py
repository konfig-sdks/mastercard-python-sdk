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

from mastercard_python_sdk.pydantic.annual_income import AnnualIncome
from mastercard_python_sdk.pydantic.direct_pay_statements import DirectPayStatements
from mastercard_python_sdk.pydantic.monthly_income import MonthlyIncome

class PayrollVOIEIncomeRecord(BaseModel):
    # The current pay frequency or how often a regular pay check is:  * `Daily`  * `Weekly`  * `Bi-Weekly`  * `Semi-Monthly`  * `Monthly`  * `Quarterly`  * `Semi-Annual`  * `Annual`  * `Every 2.6 wks`  * `Every 4 wks`  * `Every 5.2 wks`  * `Other` 
    pay_frequency: typing.Optional[str] = Field(None, alias='payFrequency')

    # The current pay type:  * `Salary`  * `Hourly`  * `Daily` 
    pay_type: typing.Optional[str] = Field(None, alias='payType')

    # The current base or regular pay rate. Please use in conjunction with the `basePayRateUnit` field.
    base_pay_rate: typing.Optional[typing.Union[int, float]] = Field(None, alias='basePayRate')

    # Unit for the base pay rate:  * `Hourly`  * `Daily`  * `Weekly`  * `Bi-Weekly`  * `Semi-Monthly`  * `Monthly`  * `Quarterly`  * `Semi-Annual`  * `Annual`  * `Every 2.6 wks`  * `Every 5.2 wks`  * `Other` 
    base_pay_rate_unit: typing.Optional[str] = Field(None, alias='basePayRateUnit')

    # The date of the oldest direct pay statement available from the payroll source, as measured by the oldest `payDate` from all the pay statements delivered.
    oldest_pay_statement_available: typing.Optional[str] = Field(None, alias='oldestPayStatementAvailable')

    # The annual pay for the current year, through prior year 2 (as available)  This is a mandatory field only for VOIE-payroll report type.
    annual_income: typing.Optional[typing.List[AnnualIncome]] = Field(None, alias='annualIncome')

    monthly_income: typing.Optional[MonthlyIncome] = Field(None, alias='monthlyIncome')

    # An array of payment histories for each available paycheck
    direct_pay_statements: typing.Optional[typing.List[DirectPayStatements]] = Field(None, alias='directPayStatements')
    class Config:
        arbitrary_types_allowed = True
