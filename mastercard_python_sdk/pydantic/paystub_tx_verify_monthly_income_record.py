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


class PaystubTxVerifyMonthlyIncomeRecord(BaseModel):
    # The estimated monthly base pay amount for the employment from the paystub, calculated by Finicity
    estimated_monthly_base_pay: typing.Optional[typing.Union[int, float]] = Field(None, alias='estimatedMonthlyBasePay')

    # The estimated monthly overtime pay amount for the employment from the paystub, calculated by Finicity
    estimated_monthly_overtime_pay: typing.Optional[typing.Union[int, float]] = Field(None, alias='estimatedMonthlyOvertimePay')

    # The estimated monthly bonus pay amount for the employment from the paystub, calculated by Finicity
    estimated_monthly_bonus_pay: typing.Optional[typing.Union[int, float]] = Field(None, alias='estimatedMonthlyBonusPay')

    # The estimated commission bonus pay amount for the employment from the paystub, calculated by Finicity
    estimated_monthly_commission_pay: typing.Optional[typing.Union[int, float]] = Field(None, alias='estimatedMonthlyCommissionPay')

    # The estimated monthly other pay amount for the employment from the paystub, calculated by Finicity
    estimated_monthly_other_pay: typing.Optional[typing.Union[int, float]] = Field(None, alias='estimatedMonthlyOtherPay')

    # The estimated monthly total pay amount for the employment from the paystub, calculated by Finicity
    estimated_monthly_total_pay: typing.Optional[typing.Union[int, float]] = Field(None, alias='estimatedMonthlyTotalPay')
    class Config:
        arbitrary_types_allowed = True
