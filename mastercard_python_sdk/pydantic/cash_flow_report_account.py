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

from mastercard_python_sdk.pydantic.cash_flow_cash_flow_balance import CashFlowCashFlowBalance
from mastercard_python_sdk.pydantic.cash_flow_cash_flow_characteristic import CashFlowCashFlowCharacteristic
from mastercard_python_sdk.pydantic.cash_flow_cash_flow_credit import CashFlowCashFlowCredit
from mastercard_python_sdk.pydantic.cash_flow_cash_flow_debit import CashFlowCashFlowDebit
from mastercard_python_sdk.pydantic.report_transaction import ReportTransaction

class CashFlowReportAccount(BaseModel):
    # Finicity account ID
    id: typing.Optional[int] = Field(None, alias='id')

    # The name(s) of the account owner(s), retrieved from the institution.
    owner_name: typing.Optional[str] = Field(None, alias='ownerName')

    # The mailing address of the account owner, retrieved from the institution.
    owner_address: typing.Optional[str] = Field(None, alias='ownerAddress')

    # The account name from the institution
    name: typing.Optional[str] = Field(None, alias='name')

    # The account number from the institution (obfuscated)
    number: typing.Optional[str] = Field(None, alias='number')

    # CFR: `ALL` (`checking` / `savings` / `loan` / `mortgage` / `credit card` / `CD` / `MM` / `investment`...)
    type: typing.Optional[str] = Field(None, alias='type')

    # The status of the most recent aggregation attempt for this account (non-zero means the account was not accessed successfully for this report, and additional fields for this account may not be reliable)
    aggregation_status_code: typing.Optional[int] = Field(None, alias='aggregationStatusCode')

    # The cleared balance of the account as-of `balanceDate`
    current_balance: typing.Optional[typing.Union[int, float]] = Field(None, alias='currentBalance')

    # Available balance
    available_balance: typing.Optional[typing.Union[int, float]] = Field(None, alias='availableBalance')

    # A timestamp showing when the `balance` was captured
    balance_date: typing.Optional[int] = Field(None, alias='balanceDate')

    # a list of transaction records
    transactions: typing.Optional[typing.List[ReportTransaction]] = Field(None, alias='transactions')

    cash_flow_balance: typing.Optional[CashFlowCashFlowBalance] = Field(None, alias='cashFlowBalance')

    cash_flow_credit: typing.Optional[CashFlowCashFlowCredit] = Field(None, alias='cashFlowCredit')

    cash_flow_debit: typing.Optional[CashFlowCashFlowDebit] = Field(None, alias='cashFlowDebit')

    cash_flow_characteristic: typing.Optional[CashFlowCashFlowCharacteristic] = Field(None, alias='cashFlowCharacteristic')
    class Config:
        arbitrary_types_allowed = True
