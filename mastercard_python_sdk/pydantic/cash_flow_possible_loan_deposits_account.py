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

from mastercard_python_sdk.pydantic.report_transaction import ReportTransaction

class CashFlowPossibleLoanDepositsAccount(BaseModel):
    # Finicity account ID
    id: str = Field(alias='id')

    # The name(s) of the account owner(s), retrieved from the institution.
    owner_name: str = Field(alias='ownerName')

    # The mailing address of the account owner, retrieved from the institution.
    owner_address: str = Field(alias='ownerAddress')

    # The account name from the institution
    name: str = Field(alias='name')

    # The account number from the institution (obfuscated)
    number: str = Field(alias='number')

    # CFR: `ALL` (`checking` / `savings` / `loan` / `mortgage` / `credit card` / `CD` / `MM` / `investment`...)
    type: str = Field(alias='type')

    # The status of the most recent aggregation attempt for this account (non-zero means the account was not accessed successfully for this report, and additional fields for this account may not be reliable)
    aggregation_status_code: int = Field(alias='aggregationStatusCode')

    # The cleared balance of the account as-of `balanceDate`
    current_balance: typing.Union[int, float] = Field(alias='currentBalance')

    # Available balance
    available_balance: typing.Union[int, float] = Field(alias='availableBalance')

    # A timestamp showing when the `balance` was captured
    balance_date: int = Field(alias='balanceDate')

    # a list of transaction records
    transactions: typing.List[ReportTransaction] = Field(alias='transactions')
    class Config:
        arbitrary_types_allowed = True
