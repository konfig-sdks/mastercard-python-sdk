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

from mastercard_python_sdk.pydantic.cadence_details import CadenceDetails
from mastercard_python_sdk.pydantic.report_transaction import ReportTransaction

class VOETransactionsReportIncomeStream(BaseModel):
    # Income stream ID
    id: str = Field(alias='id')

    # A human-readable name based on the `normalizedPayee` name of the transactions for this income stream
    name: str = Field(alias='name')

    # Possible values: \"ACTIVE\", \"INACTIVE\"
    status: str = Field(alias='status')

    # Possible values: \"HIGH\", \"MODERATE\", \"LOW\", \"NO\"
    estimate_inclusion: str = Field(alias='estimateInclusion')

    # Level of confidence that the deposit stream represents income (example: 85%)
    confidence: int = Field(alias='confidence')

    cadence: CadenceDetails = Field(alias='cadence')

    # The number of days since the last credit transaction for the particular income stream
    days_since_last_transaction: int = Field(alias='daysSinceLastTransaction')

    # The next expected credit transaction date for the particular income stream, based on the cadence
    next_expected_transaction_date: int = Field(alias='nextExpectedTransactionDate')

    # A list of transaction records
    transactions: typing.List[ReportTransaction] = Field(alias='transactions')

    # The number of months the income transactions are observed
    income_stream_months: typing.Optional[int] = Field(None, alias='incomeStreamMonths')
    class Config:
        arbitrary_types_allowed = True
