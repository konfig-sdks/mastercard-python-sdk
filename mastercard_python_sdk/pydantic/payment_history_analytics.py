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

from mastercard_python_sdk.pydantic.payment_history_account_summary import PaymentHistoryAccountSummary
from mastercard_python_sdk.pydantic.payment_history_customer_monthly_summary import PaymentHistoryCustomerMonthlySummary
from mastercard_python_sdk.pydantic.payment_history_transactions_summary import PaymentHistoryTransactionsSummary

class PaymentHistoryAnalytics(BaseModel):
    # Report status
    status: typing.Optional[str] = Field(None, alias='status')

    # Calculated risk score
    risk_score: typing.Optional[typing.Union[int, float]] = Field(None, alias='riskScore')

    # Months of transactions
    transaction_history: typing.Optional[int] = Field(None, alias='transactionHistory')

    transactions_summary: typing.Optional[PaymentHistoryTransactionsSummary] = Field(None, alias='transactionsSummary')

    # Account-level summary of transactions
    account_summaries: typing.Optional[typing.List[PaymentHistoryAccountSummary]] = Field(None, alias='accountSummaries')

    # Customer-level summary of transactions per month
    customer_summary_by_months: typing.Optional[typing.List[PaymentHistoryCustomerMonthlySummary]] = Field(None, alias='customerSummaryByMonths')
    class Config:
        arbitrary_types_allowed = True
