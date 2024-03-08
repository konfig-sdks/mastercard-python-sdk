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

from mastercard_python_sdk.pydantic.balance_analytics_metrics import BalanceAnalyticsMetrics
from mastercard_python_sdk.pydantic.obb_current_report_request_details import ObbCurrentReportRequestDetails
from mastercard_python_sdk.pydantic.obb_data_availability import ObbDataAvailability

class BalanceAnalyticsBusinessSummary(BaseModel):
    balance_analytics_metrics: typing.Optional[BalanceAnalyticsMetrics] = Field(None, alias='balanceAnalyticsMetrics')

    current_report_request: typing.Optional[ObbCurrentReportRequestDetails] = Field(None, alias='currentReportRequest')

    historic_data_availability: typing.Optional[ObbDataAvailability] = Field(None, alias='historicDataAvailability')
    class Config:
        arbitrary_types_allowed = True
