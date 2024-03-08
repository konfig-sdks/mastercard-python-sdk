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

from mastercard_python_sdk.pydantic.cash_flow_possible_loan_deposits_account import CashFlowPossibleLoanDepositsAccount

class CashFlowPossibleLoanDepositsInstitutions(BaseModel):
    # Finicity institution ID
    id: str = Field(alias='id')

    # Finicity institution name
    name: str = Field(alias='name')

    # The URL of the Financial Institution
    url_home_app: str = Field(alias='urlHomeApp')

    # A list of account records
    accounts: typing.List[CashFlowPossibleLoanDepositsAccount] = Field(alias='accounts')
    class Config:
        arbitrary_types_allowed = True
