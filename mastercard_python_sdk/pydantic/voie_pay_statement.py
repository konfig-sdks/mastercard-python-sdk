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

from mastercard_python_sdk.pydantic.deduction import Deduction
from mastercard_python_sdk.pydantic.direct_deposit import DirectDeposit
from mastercard_python_sdk.pydantic.employee import Employee
from mastercard_python_sdk.pydantic.employer import Employer
from mastercard_python_sdk.pydantic.pay_stat import PayStat

class VOIEPayStatement(BaseModel):
    # The pay period of the pay statement
    pay_period: typing.Optional[str] = Field(None, alias='payPeriod')

    # Designates whether the pay statement is billable
    billable: typing.Optional[bool] = Field(None, alias='billable')

    # The asset ID of the stored pay statement
    asset_id: typing.Optional[str] = Field(None, alias='assetId')

    # The listed pay date for the pay statement
    pay_date: typing.Optional[int] = Field(None, alias='payDate')

    # The beginning of the pay period
    start_date: typing.Optional[int] = Field(None, alias='startDate')

    # The end of the pay period
    end_date: typing.Optional[int] = Field(None, alias='endDate')

    # The total pay after deductions for the employee for the current pay period
    net_pay_current: typing.Optional[typing.Union[int, float]] = Field(None, alias='netPayCurrent')

    # The total accumulation of pay after deductions for the employee for the current pay year
    net_pay_y_t_d: typing.Optional[typing.Union[int, float]] = Field(None, alias='netPayYTD')

    # The total pay before deductions for the employee for the current pay period
    gross_pay_current: typing.Optional[typing.Union[int, float]] = Field(None, alias='grossPayCurrent')

    # The total accumulation of pay before deductions for the employee for the current pay year
    gross_pay_y_t_d: typing.Optional[typing.Union[int, float]] = Field(None, alias='grossPayYTD')

    # The company that provides the pay stub.
    payroll_provider: typing.Optional[str] = Field(None, alias='payrollProvider')

    employer: typing.Optional[Employer] = Field(None, alias='employer')

    employee: typing.Optional[Employee] = Field(None, alias='employee')

    # Information pertaining to the earnings on the pay statement
    pay_stat: typing.Optional[typing.List[PayStat]] = Field(None, alias='payStat')

    # Information pertaining to deductions on the pay statement
    deductions: typing.Optional[typing.List[Deduction]] = Field(None, alias='deductions')

    # Information pertaining to direct deposits on the pay statement
    direct_deposits: typing.Optional[typing.List[DirectDeposit]] = Field(None, alias='directDeposits')
    class Config:
        arbitrary_types_allowed = True
