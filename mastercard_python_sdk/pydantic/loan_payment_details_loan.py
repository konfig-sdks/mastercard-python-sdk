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


class LoanPaymentDetailsLoan(BaseModel):
    # An account ID
    account_id: str = Field(alias='accountId')

    # Institution's ID of the Student Loan
    loan_number: str = Field(alias='loanNumber')

    # The payment number given by the institution. This number is typically for manual payments. This is not an ACH payment number.
    loan_payment_number: str = Field(alias='loanPaymentNumber')

    # The payment address to which send manual payments should be sent
    loan_payment_address: str = Field(alias='loanPaymentAddress')

    # The payoff amount for the loan
    loan_future_payoff_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='loanFuturePayoffAmount')

    # The date to which the \"Future Payoff Amount\" applies
    loan_future_payoff_date: typing.Optional[datetime] = Field(None, alias='loanFuturePayoffDate')
    class Config:
        arbitrary_types_allowed = True
