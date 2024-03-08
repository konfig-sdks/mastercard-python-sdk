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

from mastercard_python_sdk.pydantic.obb_account_owner import ObbAccountOwner
from mastercard_python_sdk.pydantic.obb_institution import ObbInstitution

class ObbAccountDetails(BaseModel):
    account_owner: ObbAccountOwner = Field(alias='accountOwner')

    # An account ID represented as a number
    id: int = Field(alias='id')

    institution: ObbInstitution = Field(alias='institution')

    # The account number from a financial institution in truncated format
    account_number_display: typing.Optional[str] = Field(None, alias='accountNumberDisplay')

    # A timestamp showing the last aggregation attempt. This will not be present until you have run your first aggregation for the account.
    aggregation_attempt_date: typing.Optional[str] = Field(None, alias='aggregationAttemptDate')

    # The status of the most recent aggregation attempt. This will not be present until you have run your first aggregation for the account
    aggregation_status_code: typing.Optional[int] = Field(None, alias='aggregationStatusCode')

    # A timestamp showing the last successful aggregation of the account. This will not be present until you have run your first aggregation for the account.
    aggregation_success_date: typing.Optional[str] = Field(None, alias='aggregationSuccessDate')

    # The currency of the account
    currency: typing.Optional[str] = Field(None, alias='currency')

    # Current reported balance of the account
    current_balance: typing.Optional[typing.Union[int, float]] = Field(None, alias='currentBalance')

    # An institution login ID (from the account record), represented as a number
    institution_login_id: typing.Optional[int] = Field(None, alias='institutionLoginId')

    # The account name from the institution
    name: typing.Optional[str] = Field(None, alias='name')

    # The last 4 digits of the ACH account number
    real_account_number_last4: typing.Optional[int] = Field(None, alias='realAccountNumberLast4')

    # pending during account discovery, always active following successful account activation
    status: typing.Optional[str] = Field(None, alias='status')

    # Account type, e.g. checking/saving
    type: typing.Optional[str] = Field(None, alias='type')
    class Config:
        arbitrary_types_allowed = True
