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

from mastercard_python_sdk.type.loan_payment_details_account import LoanPaymentDetailsAccount

class RequiredLoanPaymentDetails(TypedDict):
    # The number of the specific loan under the account.
    loanNumber: str

    # The payment number given by the institution. This number is typically for manual payments. This is not an ACH payment number.
    loanPaymentNumber: str

    # The payment address to send manual payments to
    loanPaymentAddress: str

class OptionalLoanPaymentDetails(TypedDict, total=False):
    accountDetail: LoanPaymentDetailsAccount

class LoanPaymentDetails(RequiredLoanPaymentDetails, OptionalLoanPaymentDetails):
    pass
