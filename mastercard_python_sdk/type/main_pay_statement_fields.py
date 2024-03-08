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


class RequiredMainPayStatementFields(TypedDict):
    # Pay date for the pay period
    payDate: int

    # Gross pay amount for the pay period
    grossPayAmount: typing.Union[int, float]

class OptionalMainPayStatementFields(TypedDict, total=False):
    # Start date for the pay period
    startDate: int

    # End date for the pay period
    endDate: int

    # Sum of all hours worked each week for the pay period
    payPeriodHours: typing.Union[int, float]

    # The current pay frequency, or how often a regular pay check is distributed:  * `Daily`  * `Weekly`  * `Bi-Weekly`  * `Semi-Monthly`  * `Monthly`  * `Quarterly`  * `Semi-Annual`  * `Annual`  * `Every 2.6 wks`  * `Every 4 wks`  * `Every 5.2 wks`  * `Other` 
    payFrequency: str

    # Current pay type:  * `Salary`  * `Hourly`  * `Daily` 
    payType: str

    # Year to date (YTD) gross pay amount at the time of payment
    grossPayAmountYTD: typing.Union[int, float]

    # Net pay amount for a pay period
    netPayAmount: typing.Union[int, float]

    # Year to date (YTD) net pay amount at the time of payment
    netPayAmountYTD: typing.Union[int, float]

class MainPayStatementFields(RequiredMainPayStatementFields, OptionalMainPayStatementFields):
    pass
