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

from mastercard_python_sdk.pydantic.loan_payment_details_loan import LoanPaymentDetailsLoan

class LoanPaymentDetailsGroup(BaseModel):
    # An account ID
    account_id: str = Field(alias='accountId')

    # Institution's ID of the Student Loan Group
    group_number: str = Field(alias='groupNumber')

    # The payment number given by the institution. This number is typically for manual payments. This is not an ACH payment number.
    group_payment_number: str = Field(alias='groupPaymentNumber')

    # The payment address to which send manual payments should be sent
    group_payment_address: str = Field(alias='groupPaymentAddress')

    group_loan_detail: typing.List[LoanPaymentDetailsLoan] = Field(alias='groupLoanDetail')

    # The payoff amount for the group
    group_future_payoff_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='groupFuturePayoffAmount')

    # The date to which the \"Future Payoff Amount\" applies
    group_future_payoff_date: typing.Optional[datetime] = Field(None, alias='groupFuturePayoffDate')
    class Config:
        arbitrary_types_allowed = True
