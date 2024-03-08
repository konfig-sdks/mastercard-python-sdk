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

from mastercard_python_sdk.type.cash_flow_monthly_cash_flow_characteristics_summaries import CashFlowMonthlyCashFlowCharacteristicsSummaries

class RequiredCashFlowCashFlowCharacteristicsSummary(TypedDict):
    # Average monthly net amount
    averageMonthlyNet: typing.Union[int, float]

    # Average monthly net less transfers
    averageMonthlyNetLessTransfers: typing.Union[int, float]

    # Sum of all monthly (Total Credits - Total Debits) each month by the account
    twelveMonthTotalNet: typing.Union[int, float]

    # Sum of all monthly (Total Credits - Total Debits) without transfers by the account
    twelveMonthTotalNetLessTransfers: typing.Union[int, float]

    # 6 Month Average (Total Credits - Total Debits) across all accounts
    sixMonthAverageTotalCreditsLessTotalDebits: typing.Union[int, float]

    # 6 Month Average (Total Credits - Total Debits) - (Without Transfers) across all accounts
    sixMonthAverageTotalCreditsLessTotalDebitsLessTransfers: typing.Union[int, float]

    # 2 Month Average (Total Credits - Total Debits) across all accounts
    twoMonthAverageTotalCreditsLessTotalDebits: typing.Union[int, float]

class OptionalCashFlowCashFlowCharacteristicsSummary(TypedDict, total=False):
    # List of attributes for each month
    monthlyCashFlowCharacteristicsSummaries: typing.List[CashFlowMonthlyCashFlowCharacteristicsSummaries]

    # 2 Month Average (Total Credits - Total Debits) - (Without Transfers) across all accounts
    twoMonthAverageTotalCreditsLessTotalDebitsLessTransfers: typing.Union[int, float]

class CashFlowCashFlowCharacteristicsSummary(RequiredCashFlowCashFlowCharacteristicsSummary, OptionalCashFlowCashFlowCharacteristicsSummary):
    pass
