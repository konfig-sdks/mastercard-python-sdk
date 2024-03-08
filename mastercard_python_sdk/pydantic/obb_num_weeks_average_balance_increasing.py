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

from mastercard_python_sdk.pydantic.obb_average_weekly_balance import ObbAverageWeeklyBalance

class ObbNumWeeksAverageBalanceIncreasing(BaseModel):
    # Average weekly balances over the known history
    historic_average_weekly_balances: typing.List[ObbAverageWeeklyBalance] = Field(alias='historicAverageWeeklyBalances')

    # Number of weeks during the known history where the average balance of the account increased week over week
    historic_number_of_weeks_average_balance_increasing: int = Field(alias='historicNumberOfWeeksAverageBalanceIncreasing')

    # Number of weeks during the history in which data was available
    historic_number_of_weeks_with_data_available: int = Field(alias='historicNumberOfWeeksWithDataAvailable')
    class Config:
        arbitrary_types_allowed = True
