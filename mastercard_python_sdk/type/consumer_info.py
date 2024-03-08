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


class RequiredConsumerInfo(TypedDict):
    # The consumer's full SSN without hyphens
    ssn: str

class OptionalConsumerInfo(TypedDict, total=False):
    # The consumer's date of birth in Unix epoch time (in seconds). See: Handling Epoch Dates and Times. The timestamp should be set at the start of day of birth.
    dob: int

class ConsumerInfo(RequiredConsumerInfo, OptionalConsumerInfo):
    pass
