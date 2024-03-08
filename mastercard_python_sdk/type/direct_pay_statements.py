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

from mastercard_python_sdk.type.deductions import Deductions
from mastercard_python_sdk.type.direct_deposits import DirectDeposits
from mastercard_python_sdk.type.earnings import Earnings
from mastercard_python_sdk.type.main_pay_statement_fields import MainPayStatementFields

class RequiredDirectPayStatements(TypedDict):
    # An ID for the income and employment details for the given pay period
    payrollPayHistoryId: str

    # Most recent available pay check
    lastPayPeriodIndicator: bool

    mainPayStatementFields: MainPayStatementFields

    # Categorization of pay, for the pay period
    earnings: typing.List[Earnings]

class OptionalDirectPayStatements(TypedDict, total=False):
    # Deductions from the pay check
    deductions: typing.List[Deductions]

    # Direct deposit information for the paycheck
    directDeposits: typing.List[DirectDeposits]

class DirectPayStatements(RequiredDirectPayStatements, OptionalDirectPayStatements):
    pass
