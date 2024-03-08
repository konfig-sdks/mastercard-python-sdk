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

from mastercard_python_sdk.pydantic.obb_week_of_year import ObbWeekOfYear

class CashFlowNumWeeksZeros(BaseModel):
    # Number of weeks during known history of account in which data was available
    historic_number_of_weeks_with_data_available: int = Field(alias='historicNumberOfWeeksWithDataAvailable')

    # Number of weeks during known history of account where zero transactions were posted
    historic_number_of_weeks_zero_transactions: int = Field(alias='historicNumberOfWeeksZeroTransactions')

    # List of weeks with zero reported transactions
    historic_weeks_with_zero_transactions: typing.List[ObbWeekOfYear] = Field(alias='historicWeeksWithZeroTransactions')
    class Config:
        arbitrary_types_allowed = True
