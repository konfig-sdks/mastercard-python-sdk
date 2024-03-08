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


class RequiredReportAccountPosition(TypedDict):
    pass

class OptionalReportAccountPosition(TypedDict, total=False):
    # The id of the investment position
    id: typing.Union[int, float]

    # What currency the account operates in
    currency: str

    # The investment position’s market ticker symbol
    symbol: str

    # The security name for the investment holding
    securityName: str

    # The number of units of the holding
    units: typing.Union[int, float]

    # Market value of an investment position at the time of retrieval
    marketValue: typing.Union[int, float]

    # The current price of the investment holding
    currentPrice: typing.Union[int, float]

    # Type of security of the investment position
    securityType: typing.Union[int, float]

class ReportAccountPosition(RequiredReportAccountPosition, OptionalReportAccountPosition):
    pass
