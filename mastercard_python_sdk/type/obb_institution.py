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


class RequiredObbInstitution(TypedDict):
    # ID of the financial institution
    institutionId: int

class OptionalObbInstitution(TypedDict, total=False):
    # URL of the institution logo icon for reporting
    institutionIconUrl: str

    # Name of the financial institution
    institutionName: str

    # Primary branding color of the institution, in hex color format
    institutionPrimaryColor: str

class ObbInstitution(RequiredObbInstitution, OptionalObbInstitution):
    pass
