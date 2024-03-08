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

from mastercard_python_sdk.type.loan_payment_details_group import LoanPaymentDetailsGroup
from mastercard_python_sdk.type.loan_payment_details_loan import LoanPaymentDetailsLoan

class RequiredLoanPaymentDetailsAccount(TypedDict):
    # An account ID
    accountId: str

    # Institution's ID of the Student Loan Account
    accountNumber: str

    # The payment number given by the institution. This number is typically for manual payments. This is not an ACH payment number.
    accountPaymentNumber: str

    # The payment address to which send manual payments should be sent
    accountPaymentAddress: str

class OptionalLoanPaymentDetailsAccount(TypedDict, total=False):
    # The payoff amount for the account
    accountFuturePayoffAmount: typing.Union[int, float]

    # The date to which the \"Future Payoff Amount\" applies
    accountFuturePayoffDate: datetime

    # Group details
    groupDetail: typing.List[LoanPaymentDetailsGroup]

    # Loan details
    loanDetail: typing.List[LoanPaymentDetailsLoan]

class LoanPaymentDetailsAccount(RequiredLoanPaymentDetailsAccount, OptionalLoanPaymentDetailsAccount):
    pass
