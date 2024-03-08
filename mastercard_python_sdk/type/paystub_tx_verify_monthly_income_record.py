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


class RequiredPaystubTxVerifyMonthlyIncomeRecord(TypedDict):
    pass

class OptionalPaystubTxVerifyMonthlyIncomeRecord(TypedDict, total=False):
    # The estimated monthly base pay amount for the employment from the paystub, calculated by Finicity
    estimatedMonthlyBasePay: typing.Union[int, float]

    # The estimated monthly overtime pay amount for the employment from the paystub, calculated by Finicity
    estimatedMonthlyOvertimePay: typing.Union[int, float]

    # The estimated monthly bonus pay amount for the employment from the paystub, calculated by Finicity
    estimatedMonthlyBonusPay: typing.Union[int, float]

    # The estimated commission bonus pay amount for the employment from the paystub, calculated by Finicity
    estimatedMonthlyCommissionPay: typing.Union[int, float]

    # The estimated monthly other pay amount for the employment from the paystub, calculated by Finicity
    estimatedMonthlyOtherPay: typing.Union[int, float]

    # The estimated monthly total pay amount for the employment from the paystub, calculated by Finicity
    estimatedMonthlyTotalPay: typing.Union[int, float]

class PaystubTxVerifyMonthlyIncomeRecord(RequiredPaystubTxVerifyMonthlyIncomeRecord, OptionalPaystubTxVerifyMonthlyIncomeRecord):
    pass
