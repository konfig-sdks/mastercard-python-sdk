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

from mastercard_python_sdk.type.app_financial_institution_status import AppFinancialInstitutionStatus

class RequiredAppStatus(TypedDict):
    # Your Partner ID displayed in the [Developer Dashboard](https://developer.mastercard.com/account/log-in)
    partnerId: str

    # Identifier to track the application registration from the App Registration and Get App Registration Status APIs
    preAppId: str

    # The name of the application assigned to the customer
    appName: str

    # A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    submittedDate: int

    # A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    modifiedDate: int

    # The status of an app registration request. \"A\" means approved. \"P\" means pending which is the status when initially submitted or when the app is modified and awaiting approval. \"R\" means rejected. If it is rejected there will be a note with the rejected reason.
    status: str

class OptionalAppStatus(TypedDict, total=False):
    # A note on the registration. Typically used to indicate reasons for rejected apps.
    note: str

    # `applicationId` value returned from the Get App Registration Status API and the partner assign the customers to. This cannot be changed once set. Only applicable in cases of partners with multiple registered applications. If the partner only has one app, this can usually be omitted. This field is populated after the app is in a status approved.
    applicationId: str

    # Indicates scopes of data accessible to the app
    scopes: str

    # A list of the registration status for each FI for the application
    institutionDetails: typing.List[AppFinancialInstitutionStatus]

class AppStatus(RequiredAppStatus, OptionalAppStatus):
    pass
