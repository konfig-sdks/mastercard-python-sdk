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


class RequiredPaymentHistoryCustomerMonthlySummary(TypedDict):
    # Date of the month
    month: str

    # Average balance for the month
    averageBalance: typing.Union[int, float]

    # Closing balance for the month
    closingBalance: typing.Union[int, float]

    # Opening balance for the month
    openingBalance: typing.Union[int, float]

    # Total of deposit transactions for the month
    totalDeposits: typing.Union[int, float]

    # Total of withdrawal transactions for the month
    totalWithdrawals: typing.Union[int, float]

    # Total of NSF transactions for the month
    nonSufficientFunds: typing.Union[int, float]

    # Total of insurance payment transactions for the month
    insurancePayments: typing.Union[int, float]

    # Total of tax payment transactions for the month
    taxPayments: typing.Union[int, float]

    # Total of recurring expense payment transactions for the month
    recurringExpensePayments: typing.Union[int, float]

    # Total of missed recurring expense payment transactions for the month
    missedRecurringExpensePayments: typing.Union[int, float]

    # Total of recurring loan payment transactions for the month
    recurringLoanPayments: typing.Union[int, float]

    # Total of missed recurring loan payment transactions for the month
    missedRecurringLoanPayments: typing.Union[int, float]

class OptionalPaymentHistoryCustomerMonthlySummary(TypedDict, total=False):
    pass

class PaymentHistoryCustomerMonthlySummary(RequiredPaymentHistoryCustomerMonthlySummary, OptionalPaymentHistoryCustomerMonthlySummary):
    pass
