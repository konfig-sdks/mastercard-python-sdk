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

from mastercard_python_sdk.type.af_business_address import AFBusinessAddress

class RequiredAFBusiness(TypedDict):
    # The name of a business
    name: str

    address: AFBusinessAddress

class OptionalAFBusiness(TypedDict, total=False):
    pass

class AFBusiness(RequiredAFBusiness, OptionalAFBusiness):
    pass
