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


class CashFlowMonthlyCashFlowCredits(BaseModel):
    # One instance for each complete calendar month in the report
    month: int = Field(alias='month')

    # Number of credits by month
    number_of_credits: str = Field(alias='numberOfCredits')

    # Total amount of credits by month
    total_credits_amount: typing.Union[int, float] = Field(alias='totalCreditsAmount')

    # Largest credit by month
    largest_credit: typing.Union[int, float] = Field(alias='largestCredit')

    # Number of credits by month (less transfers)
    number_of_credits_less_transfers: str = Field(alias='numberOfCreditsLessTransfers')

    # Total amount of credits by month (less transfers)
    total_credits_amount_less_transfers: typing.Union[int, float] = Field(alias='totalCreditsAmountLessTransfers')

    # The average credit amount
    average_credit_amount: typing.Union[int, float] = Field(alias='averageCreditAmount')

    # The estimated number of loan deposits
    estimated_number_of_loan_deposits: str = Field(alias='estimatedNumberOfLoanDeposits')

    # The estimated loan deposit amount
    estimated_loan_deposit_amount: typing.Union[int, float] = Field(alias='estimatedLoanDepositAmount')
    class Config:
        arbitrary_types_allowed = True
