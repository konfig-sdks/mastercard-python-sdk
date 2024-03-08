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


class MainPayStatementFields(BaseModel):
    # Pay date for the pay period
    pay_date: int = Field(alias='payDate')

    # Gross pay amount for the pay period
    gross_pay_amount: typing.Union[int, float] = Field(alias='grossPayAmount')

    # Start date for the pay period
    start_date: typing.Optional[int] = Field(None, alias='startDate')

    # End date for the pay period
    end_date: typing.Optional[int] = Field(None, alias='endDate')

    # Sum of all hours worked each week for the pay period
    pay_period_hours: typing.Optional[typing.Union[int, float]] = Field(None, alias='payPeriodHours')

    # The current pay frequency, or how often a regular pay check is distributed:  * `Daily`  * `Weekly`  * `Bi-Weekly`  * `Semi-Monthly`  * `Monthly`  * `Quarterly`  * `Semi-Annual`  * `Annual`  * `Every 2.6 wks`  * `Every 4 wks`  * `Every 5.2 wks`  * `Other` 
    pay_frequency: typing.Optional[str] = Field(None, alias='payFrequency')

    # Current pay type:  * `Salary`  * `Hourly`  * `Daily` 
    pay_type: typing.Optional[str] = Field(None, alias='payType')

    # Year to date (YTD) gross pay amount at the time of payment
    gross_pay_amount_y_t_d: typing.Optional[typing.Union[int, float]] = Field(None, alias='grossPayAmountYTD')

    # Net pay amount for a pay period
    net_pay_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='netPayAmount')

    # Year to date (YTD) net pay amount at the time of payment
    net_pay_amount_y_t_d: typing.Optional[typing.Union[int, float]] = Field(None, alias='netPayAmountYTD')
    class Config:
        arbitrary_types_allowed = True
