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

from mastercard_python_sdk.type.cadence_details import CadenceDetails
from mastercard_python_sdk.type.report_transaction import ReportTransaction

class RequiredVOETransactionsReportIncomeStream(TypedDict):
    # Income stream ID
    id: str

    # A human-readable name based on the `normalizedPayee` name of the transactions for this income stream
    name: str

    # Possible values: \"ACTIVE\", \"INACTIVE\"
    status: str

    # Possible values: \"HIGH\", \"MODERATE\", \"LOW\", \"NO\"
    estimateInclusion: str

    # Level of confidence that the deposit stream represents income (example: 85%)
    confidence: int

    cadence: CadenceDetails

    # The number of days since the last credit transaction for the particular income stream
    daysSinceLastTransaction: int

    # The next expected credit transaction date for the particular income stream, based on the cadence
    nextExpectedTransactionDate: int

    # A list of transaction records
    transactions: typing.List[ReportTransaction]

class OptionalVOETransactionsReportIncomeStream(TypedDict, total=False):
    # The number of months the income transactions are observed
    incomeStreamMonths: int

class VOETransactionsReportIncomeStream(RequiredVOETransactionsReportIncomeStream, OptionalVOETransactionsReportIncomeStream):
    pass
