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

from mastercard_python_sdk.type.cash_flow_monthly_cash_flow_characteristics import CashFlowMonthlyCashFlowCharacteristics

class RequiredCashFlowCashFlowCharacteristic(TypedDict):
    # List of attributes for each month
    monthlyCashFlowCharacteristics: typing.List[CashFlowMonthlyCashFlowCharacteristics]

    # Average (Total Credits - Total Debits) for the account
    averageMonthlyNet: typing.Union[int, float]

    # Average (Total Credits - Total Debits) without transfers for the account
    averageMonthlyNetLessTransfers: typing.Union[int, float]

class OptionalCashFlowCashFlowCharacteristic(TypedDict, total=False):
    # Sum of all monthly (Total Credits - Total Debits) each month for the account
    twelveMonthTotalNet: typing.Union[int, float]

    # Sum of all monthly (Total Credits - Total Debits) without transfers for the account
    twelveMonthTotalNetLessTransfers: typing.Union[int, float]

    # 6 Month Average (Total Credits - Total Debits)
    sixMonthAverageTotalCreditsLessTotalDebits: typing.Union[int, float]

    # 6 Month Average (Total Credits - Total Debits) - (Without Transfers)
    sixMonthAverageTotalCreditsLessTotalDebitsLessTransfers: typing.Union[int, float]

    # 2 Month Average (Total Credits - Total Debits)
    twoMonthAverageTotalCreditsLessTotalDebits: typing.Union[int, float]

    # 2 Month Average (Total Credits - Total Debits) - (Without Transfers)
    twoMonthAverageTotalCreditsLessTotalDebitsLessTransfers: typing.Union[int, float]

class CashFlowCashFlowCharacteristic(RequiredCashFlowCashFlowCharacteristic, OptionalCashFlowCashFlowCharacteristic):
    pass
