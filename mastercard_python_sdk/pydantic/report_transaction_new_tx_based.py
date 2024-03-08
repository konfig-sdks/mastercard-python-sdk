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

from mastercard_python_sdk.pydantic.report_transaction_base1 import ReportTransactionBase1
from mastercard_python_sdk.pydantic.report_transaction_base2 import ReportTransactionBase2

ReportTransactionNewTxBased = typing.Union[ReportTransactionBase1,typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]],ReportTransactionBase2]
ReportTransactionNewTxBased = object
