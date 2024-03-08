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


class PaymentHistoryCustomerMonthlySummary(BaseModel):
    # Date of the month
    month: str = Field(alias='month')

    # Average balance for the month
    average_balance: typing.Union[int, float] = Field(alias='averageBalance')

    # Closing balance for the month
    closing_balance: typing.Union[int, float] = Field(alias='closingBalance')

    # Opening balance for the month
    opening_balance: typing.Union[int, float] = Field(alias='openingBalance')

    # Total of deposit transactions for the month
    total_deposits: typing.Union[int, float] = Field(alias='totalDeposits')

    # Total of withdrawal transactions for the month
    total_withdrawals: typing.Union[int, float] = Field(alias='totalWithdrawals')

    # Total of NSF transactions for the month
    non_sufficient_funds: typing.Union[int, float] = Field(alias='nonSufficientFunds')

    # Total of insurance payment transactions for the month
    insurance_payments: typing.Union[int, float] = Field(alias='insurancePayments')

    # Total of tax payment transactions for the month
    tax_payments: typing.Union[int, float] = Field(alias='taxPayments')

    # Total of recurring expense payment transactions for the month
    recurring_expense_payments: typing.Union[int, float] = Field(alias='recurringExpensePayments')

    # Total of missed recurring expense payment transactions for the month
    missed_recurring_expense_payments: typing.Union[int, float] = Field(alias='missedRecurringExpensePayments')

    # Total of recurring loan payment transactions for the month
    recurring_loan_payments: typing.Union[int, float] = Field(alias='recurringLoanPayments')

    # Total of missed recurring loan payment transactions for the month
    missed_recurring_loan_payments: typing.Union[int, float] = Field(alias='missedRecurringLoanPayments')
    class Config:
        arbitrary_types_allowed = True
