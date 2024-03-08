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

from mastercard_python_sdk.pydantic.account_owner_addresses import AccountOwnerAddresses
from mastercard_python_sdk.pydantic.account_owner_documentations import AccountOwnerDocumentations
from mastercard_python_sdk.pydantic.account_owner_emails import AccountOwnerEmails
from mastercard_python_sdk.pydantic.account_owner_identity_insights import AccountOwnerIdentityInsights
from mastercard_python_sdk.pydantic.account_owner_phones import AccountOwnerPhones

class AccountOwnerDetails(BaseModel):
    # The full name of the account owner. Multiple account owners are returned in one string per the source data from the institution.
    owner_name: str = Field(alias='ownerName')

    addresses: AccountOwnerAddresses = Field(alias='addresses')

    # The type of relationship to the account: * \"AUTHORIZED_USER\"  * \"BUSINESS\"  * \"FOR_BENEFIT_OF_PRIMARY\"  * \"FOR_BENEFIT_OF_PRIMARY_JOINT_RESTRICTED\"  * \"FOR_BENEFIT_OF_SECONDARY\"  * \"FOR_BENEFIT_OF_SECONDARY_JOINT_RESTRICTED\"  * \"FOR_BENEFIT_OF_SOLE_OWNER_RESTRICTED\"  * \"POWER_OF_ATTORNEY\"  * \"PRIMARY_JOINT_TENANTS\"  * \"PRIMARY\"  * \"PRIMARY_BORROWER\"  * \"PRIMARY_JOINT\"  * \"SECONDARY\"  * \"SECONDARY_JOINT_TENANTS\"  * \"SECONDARY_BORROWER\"  * \"SECONDARY_JOINT\"  * \"SOLE_OWNER\"  * \"TRUSTEE\"  * \"UNIFORM_TRANSFER_TO_MINOR\"
    relationship: typing.Optional[str] = Field(None, alias='relationship')

    # The first name of the account holder
    first_name: typing.Optional[str] = Field(None, alias='firstName')

    # The middle name of the account holder
    middle_name: typing.Optional[str] = Field(None, alias='middleName')

    # The last name of the account holder
    last_name: typing.Optional[str] = Field(None, alias='lastName')

    # A generational or academic suffix
    suffix: typing.Optional[str] = Field(None, alias='suffix')

    # The classification of the account holder: * \"person / personal / home\" * \"business\" * \"other\"
    name_classification: typing.Optional[str] = Field(None, alias='nameClassification')

    # The confidence score 0-100 of the name classification.
    name_classificationconfidencescore: typing.Optional[typing.Union[int, float]] = Field(None, alias='nameClassificationconfidencescore')

    emails: typing.Optional[AccountOwnerEmails] = Field(None, alias='emails')

    phones: typing.Optional[AccountOwnerPhones] = Field(None, alias='phones')

    documentations: typing.Optional[AccountOwnerDocumentations] = Field(None, alias='documentations')

    identity_insights: typing.Optional[AccountOwnerIdentityInsights] = Field(None, alias='identityInsights')
    class Config:
        arbitrary_types_allowed = True
