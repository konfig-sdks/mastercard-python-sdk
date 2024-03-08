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

from mastercard_python_sdk.pydantic.deductions import Deductions
from mastercard_python_sdk.pydantic.direct_deposits import DirectDeposits
from mastercard_python_sdk.pydantic.earnings import Earnings
from mastercard_python_sdk.pydantic.main_pay_statement_fields import MainPayStatementFields

class DirectPayStatements(BaseModel):
    # An ID for the income and employment details for the given pay period
    payroll_pay_history_id: str = Field(alias='payrollPayHistoryId')

    # Most recent available pay check
    last_pay_period_indicator: bool = Field(alias='lastPayPeriodIndicator')

    main_pay_statement_fields: MainPayStatementFields = Field(alias='mainPayStatementFields')

    # Categorization of pay, for the pay period
    earnings: typing.List[Earnings] = Field(alias='earnings')

    # Deductions from the pay check
    deductions: typing.Optional[typing.List[Deductions]] = Field(None, alias='deductions')

    # Direct deposit information for the paycheck
    direct_deposits: typing.Optional[typing.List[DirectDeposits]] = Field(None, alias='directDeposits')
    class Config:
        arbitrary_types_allowed = True
