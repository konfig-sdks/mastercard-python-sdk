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

from mastercard_python_sdk.pydantic.cash_flow_analytics_metrics import CashFlowAnalyticsMetrics
from mastercard_python_sdk.pydantic.obb_account_details import ObbAccountDetails
from mastercard_python_sdk.pydantic.obb_current_report_request_details import ObbCurrentReportRequestDetails
from mastercard_python_sdk.pydantic.obb_data_availability import ObbDataAvailability

class CashFlowAnalyticsAccountResult(BaseModel):
    account_details: ObbAccountDetails = Field(alias='accountDetails')

    # An account ID represented as a number
    account_id: int = Field(alias='accountId')

    current_report_request: ObbCurrentReportRequestDetails = Field(alias='currentReportRequest')

    historic_data_availability: ObbDataAvailability = Field(alias='historicDataAvailability')

    cashflow_analytics_metrics: typing.Optional[CashFlowAnalyticsMetrics] = Field(None, alias='cashflowAnalyticsMetrics')
    class Config:
        arbitrary_types_allowed = True
