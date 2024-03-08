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

from mastercard_python_sdk.type.business_id import BusinessId
from mastercard_python_sdk.type.new_business import NewBusiness

Business = typing.Union[NewBusiness,typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]
