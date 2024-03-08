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


class RequiredLoanPaymentDetailsLoan(TypedDict):
    # An account ID
    accountId: str

    # Institution's ID of the Student Loan
    loanNumber: str

    # The payment number given by the institution. This number is typically for manual payments. This is not an ACH payment number.
    loanPaymentNumber: str

    # The payment address to which send manual payments should be sent
    loanPaymentAddress: str

class OptionalLoanPaymentDetailsLoan(TypedDict, total=False):
    # The payoff amount for the loan
    loanFuturePayoffAmount: typing.Union[int, float]

    # The date to which the \"Future Payoff Amount\" applies
    loanFuturePayoffDate: datetime

class LoanPaymentDetailsLoan(RequiredLoanPaymentDetailsLoan, OptionalLoanPaymentDetailsLoan):
    pass
