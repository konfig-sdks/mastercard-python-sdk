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

from mastercard_python_sdk.pydantic.loan_payment_details_account import LoanPaymentDetailsAccount

class LoanPaymentDetails(BaseModel):
    # The number of the specific loan under the account.
    loan_number: str = Field(alias='loanNumber')

    # The payment number given by the institution. This number is typically for manual payments. This is not an ACH payment number.
    loan_payment_number: str = Field(alias='loanPaymentNumber')

    # The payment address to send manual payments to
    loan_payment_address: str = Field(alias='loanPaymentAddress')

    account_detail: typing.Optional[LoanPaymentDetailsAccount] = Field(None, alias='accountDetail')
    class Config:
        arbitrary_types_allowed = True
