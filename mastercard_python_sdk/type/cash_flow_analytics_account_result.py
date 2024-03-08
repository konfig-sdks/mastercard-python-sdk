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

from mastercard_python_sdk.type.cash_flow_analytics_metrics import CashFlowAnalyticsMetrics
from mastercard_python_sdk.type.obb_account_details import ObbAccountDetails
from mastercard_python_sdk.type.obb_current_report_request_details import ObbCurrentReportRequestDetails
from mastercard_python_sdk.type.obb_data_availability import ObbDataAvailability

class RequiredCashFlowAnalyticsAccountResult(TypedDict):
    accountDetails: ObbAccountDetails

    # An account ID represented as a number
    accountId: int

    currentReportRequest: ObbCurrentReportRequestDetails

    historicDataAvailability: ObbDataAvailability

class OptionalCashFlowAnalyticsAccountResult(TypedDict, total=False):
    cashflowAnalyticsMetrics: CashFlowAnalyticsMetrics

class CashFlowAnalyticsAccountResult(RequiredCashFlowAnalyticsAccountResult, OptionalCashFlowAnalyticsAccountResult):
    pass
