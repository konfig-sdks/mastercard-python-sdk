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

from mastercard_python_sdk.pydantic.insufficient_funds_transaction import InsufficientFundsTransaction

class CashFlowInsufficientFundsFees(BaseModel):
    # Count of all NSF transactions during the report
    count_of_transactions_for_the_report_time_period: typing.Optional[int] = Field(None, alias='countOfTransactionsForTheReportTimePeriod')

    # Sum of all NSF transactions during the report
    sum_of_transactions_for_the_report_time_period: typing.Optional[typing.Union[int, float]] = Field(None, alias='sumOfTransactionsForTheReportTimePeriod')

    # Transactions categorized as NSF
    transactions: typing.Optional[typing.List[InsufficientFundsTransaction]] = Field(None, alias='transactions')
    class Config:
        arbitrary_types_allowed = True
