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

from mastercard_python_sdk.pydantic.loan_payment_details_group import LoanPaymentDetailsGroup
from mastercard_python_sdk.pydantic.loan_payment_details_loan import LoanPaymentDetailsLoan

class LoanPaymentDetailsAccount(BaseModel):
    # An account ID
    account_id: str = Field(alias='accountId')

    # Institution's ID of the Student Loan Account
    account_number: str = Field(alias='accountNumber')

    # The payment number given by the institution. This number is typically for manual payments. This is not an ACH payment number.
    account_payment_number: str = Field(alias='accountPaymentNumber')

    # The payment address to which send manual payments should be sent
    account_payment_address: str = Field(alias='accountPaymentAddress')

    # The payoff amount for the account
    account_future_payoff_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='accountFuturePayoffAmount')

    # The date to which the \"Future Payoff Amount\" applies
    account_future_payoff_date: typing.Optional[datetime] = Field(None, alias='accountFuturePayoffDate')

    # Group details
    group_detail: typing.Optional[typing.List[LoanPaymentDetailsGroup]] = Field(None, alias='groupDetail')

    # Loan details
    loan_detail: typing.Optional[typing.List[LoanPaymentDetailsLoan]] = Field(None, alias='loanDetail')
    class Config:
        arbitrary_types_allowed = True
