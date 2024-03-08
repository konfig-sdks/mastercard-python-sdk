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


class RequiredMonthlyIncome(TypedDict):
    # Sum of all Mastercard Open Banking estimated monthly pay amounts
    estimatedMonthlyTotalPay: typing.Union[int, float]

class OptionalMonthlyIncome(TypedDict, total=False):
    # Mastercard Open Banking estimated monthly base pay amount for the employment
    estimatedMonthlyBasePay: typing.Union[int, float]

    # Mastercard Open Banking estimated monthly overtime pay amount for the employment
    estimatedMonthlyOvertimePay: typing.Union[int, float]

    # Mastercard Open Banking estimated monthly bonus pay amount for the employment
    estimatedMonthlyBonusPay: typing.Union[int, float]

    # Mastercard Open Banking estimated monthly other pay amount for the employment
    estimatedMonthlyOtherPay: typing.Union[int, float]

    # Mastercard Open Banking estimated monthly commission pay amount for the employment
    estimatedMonthlyCommissionPay: typing.Union[int, float]

class MonthlyIncome(RequiredMonthlyIncome, OptionalMonthlyIncome):
    pass
