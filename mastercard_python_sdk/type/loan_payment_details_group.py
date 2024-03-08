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

from mastercard_python_sdk.type.loan_payment_details_loan import LoanPaymentDetailsLoan

class RequiredLoanPaymentDetailsGroup(TypedDict):
    # An account ID
    accountId: str

    # Institution's ID of the Student Loan Group
    groupNumber: str

    # The payment number given by the institution. This number is typically for manual payments. This is not an ACH payment number.
    groupPaymentNumber: str

    # The payment address to which send manual payments should be sent
    groupPaymentAddress: str

    groupLoanDetail: typing.List[LoanPaymentDetailsLoan]

class OptionalLoanPaymentDetailsGroup(TypedDict, total=False):
    # The payoff amount for the group
    groupFuturePayoffAmount: typing.Union[int, float]

    # The date to which the \"Future Payoff Amount\" applies
    groupFuturePayoffDate: datetime

class LoanPaymentDetailsGroup(RequiredLoanPaymentDetailsGroup, OptionalLoanPaymentDetailsGroup):
    pass
