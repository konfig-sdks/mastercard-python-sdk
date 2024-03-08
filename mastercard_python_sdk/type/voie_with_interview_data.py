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

from mastercard_python_sdk.type.tx_verify_interview import TxVerifyInterview

class RequiredVOIEWithInterviewData(TypedDict):
    # An array of `TxVerifyInterview` objects
    txVerifyInterview: typing.List[TxVerifyInterview]

class OptionalVOIEWithInterviewData(TypedDict, total=False):
    # Field to indicate whether to extract the earnings on all pay statements
    extractEarnings: bool

    # Field to indicate whether to extract the deductions on all pay statements
    extractDeductions: bool

    # Field to indicate whether to extract the direct deposits on all pay statements
    extractDirectDeposit: bool

class VOIEWithInterviewData(RequiredVOIEWithInterviewData, OptionalVOIEWithInterviewData):
    pass
