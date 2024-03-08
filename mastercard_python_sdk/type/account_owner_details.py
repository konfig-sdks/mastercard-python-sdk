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

from mastercard_python_sdk.type.account_owner_addresses import AccountOwnerAddresses
from mastercard_python_sdk.type.account_owner_documentations import AccountOwnerDocumentations
from mastercard_python_sdk.type.account_owner_emails import AccountOwnerEmails
from mastercard_python_sdk.type.account_owner_identity_insights import AccountOwnerIdentityInsights
from mastercard_python_sdk.type.account_owner_phones import AccountOwnerPhones

class RequiredAccountOwnerDetails(TypedDict):
    # The full name of the account owner. Multiple account owners are returned in one string per the source data from the institution.
    ownerName: str

    addresses: AccountOwnerAddresses

class OptionalAccountOwnerDetails(TypedDict, total=False):
    # The type of relationship to the account: * \"AUTHORIZED_USER\"  * \"BUSINESS\"  * \"FOR_BENEFIT_OF_PRIMARY\"  * \"FOR_BENEFIT_OF_PRIMARY_JOINT_RESTRICTED\"  * \"FOR_BENEFIT_OF_SECONDARY\"  * \"FOR_BENEFIT_OF_SECONDARY_JOINT_RESTRICTED\"  * \"FOR_BENEFIT_OF_SOLE_OWNER_RESTRICTED\"  * \"POWER_OF_ATTORNEY\"  * \"PRIMARY_JOINT_TENANTS\"  * \"PRIMARY\"  * \"PRIMARY_BORROWER\"  * \"PRIMARY_JOINT\"  * \"SECONDARY\"  * \"SECONDARY_JOINT_TENANTS\"  * \"SECONDARY_BORROWER\"  * \"SECONDARY_JOINT\"  * \"SOLE_OWNER\"  * \"TRUSTEE\"  * \"UNIFORM_TRANSFER_TO_MINOR\"
    relationship: str

    # The first name of the account holder
    firstName: str

    # The middle name of the account holder
    middleName: str

    # The last name of the account holder
    lastName: str

    # A generational or academic suffix
    suffix: str

    # The classification of the account holder: * \"person / personal / home\" * \"business\" * \"other\"
    nameClassification: str

    # The confidence score 0-100 of the name classification.
    nameClassificationconfidencescore: typing.Union[int, float]

    emails: AccountOwnerEmails

    phones: AccountOwnerPhones

    documentations: AccountOwnerDocumentations

    identityInsights: AccountOwnerIdentityInsights

class AccountOwnerDetails(RequiredAccountOwnerDetails, OptionalAccountOwnerDetails):
    pass
