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


class AvailableBalance(BaseModel):
    # A customer ID represented as a number. See Add Customer API for how to create a customer ID.
    id: int = Field(alias='id')

    # The last 4 digits of the ACH account number
    real_account_number_last4: str = Field(alias='realAccountNumberLast4')

    # The available balance of the account
    available_balance: typing.Union[int, float] = Field(alias='availableBalance')

    # A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    available_balance_date: int = Field(alias='availableBalanceDate')

    # The cleared balance of the account. Also referred as posted balance, current balance, ledger balance
    cleared_balance: typing.Union[int, float] = Field(alias='clearedBalance')

    # A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    cleared_balance_date: int = Field(alias='clearedBalanceDate')

    # The status of the most recent aggregation attempt (see [Aggregation Status Codes](https://developer.mastercard.com/open-banking-us/documentation/products/manage/account-aggregation/#aggregation-status-codes)). Won't be present until you have run your first aggregation for the account.
    aggregation_status_code: int = Field(alias='aggregationStatusCode')

    # A currency code
    currency: str = Field(alias='currency')
    class Config:
        arbitrary_types_allowed = True
