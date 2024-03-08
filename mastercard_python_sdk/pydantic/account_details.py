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


class AccountDetails(BaseModel):
    # Only available for investment accounts. Net interest earned after deducting interest paid out.
    interest_margin_balance: typing.Optional[typing.Union[int, float]] = Field(None, alias='interestMarginBalance')

    # Only available for investment accounts. Amount available for cash withdrawal.
    available_cash_balance: typing.Optional[typing.Union[int, float]] = Field(None, alias='availableCashBalance')

    # Only available for investment accounts. Vested amount in account.
    vested_balance: typing.Optional[typing.Union[int, float]] = Field(None, alias='vestedBalance')

    # Only available for investment accounts. Current loan balance.
    current_loan_balance: typing.Optional[typing.Union[int, float]] = Field(None, alias='currentLoanBalance')

    # The available balance for the account
    available_balance_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='availableBalanceAmount')
    class Config:
        arbitrary_types_allowed = True
