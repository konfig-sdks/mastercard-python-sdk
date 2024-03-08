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


class RequiredChildInstitution(TypedDict):
    # The RSSD ID is a unique identifier assigned to financial institutions by the Federal Reserve. While the length of the RSSD ID varies by institution, it cannot exceed 10 numerical digits.
    rssd: int

    # The RSSD ID is a unique identifier assigned to financial institutions by the Federal Reserve. While the length of the RSSD ID varies by institution, it cannot exceed 10 numerical digits.
    parentRSSD: int

    # The name of the institution
    name: str

    # The ID of a financial institution, represented as a number
    institutionId: int

class OptionalChildInstitution(TypedDict, total=False):
    pass

class ChildInstitution(RequiredChildInstitution, OptionalChildInstitution):
    pass
