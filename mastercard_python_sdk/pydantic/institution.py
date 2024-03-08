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

from mastercard_python_sdk.pydantic.branding import Branding
from mastercard_python_sdk.pydantic.institution_address import InstitutionAddress
from mastercard_python_sdk.pydantic.institution_special_instructions import InstitutionSpecialInstructions

class Institution(BaseModel):
    # The ID of a financial institution, represented as a number
    id: int = Field(alias='id')

    # \"true\": The institution is certified for the Transaction Aggregation product \"false\": The institution is decertified for the Transaction Aggregation product
    trans_agg: bool = Field(alias='transAgg')

    # \"true\": The institution is certified for the ACH product \"false\": The institution is decertified for the ACH product
    ach: bool = Field(alias='ach')

    # \"true\": The institution is certified for the Statement Aggregation product \"false\": The institution is decertified for the Statement Aggregation product
    state_agg: bool = Field(alias='stateAgg')

    # \"true\": The institution is certified for the VOI product \"false\": The institution is decertified for the VOI product
    voi: bool = Field(alias='voi')

    # \"true\": The institution is certified for the VOA product \"false\": The institution is decertified for the VOA product
    voa: bool = Field(alias='voa')

    # \"true\": The institution is certified for the Account History Aggregation product \"false\": The institution is decertified for the Account History Aggregation product
    aha: bool = Field(alias='aha')

    # \"true\": The institution is certified for the Account Balance Check (ABC) product \"false\": The institution is decertified for the Account Balance Check (ABC) product
    avail_balance: bool = Field(alias='availBalance')

    # \"true\": The institution is certified for the Account Owner product \"false\": The institution is decertified for the Account Owner product
    account_owner: bool = Field(alias='accountOwner')

    # \"true\": The institution is an OAuth connection  \"false\": The institution isn't an OAuth connection
    oauth_enabled: bool = Field(alias='oauthEnabled')

    # A currency code
    currency: str = Field(alias='currency')

    # Status for the institution: \"online\", \"offline\", \"maintenance\", \"testing\"
    status: str = Field(alias='status')

    # The name of the institution
    name: typing.Optional[str] = Field(None, alias='name')

    # \"true\": The institution is certified for the Student Loan Data product  \"false\": The institution is decertified for the Student Loan Data product
    student_loan_data: typing.Optional[bool] = Field(None, alias='studentLoanData')

    # \"true\": The institution is certified for the Loan Payment Detail product  \"false\": The institution is decertified for the Loan Payment Detail product
    loan_payment_details: typing.Optional[bool] = Field(None, alias='loanPaymentDetails')

    # Values: Banking, Investments, Credit Cards/Accounts, Workplace Retirement, Mortgages and Loans, Insurance
    account_type_description: typing.Optional[str] = Field(None, alias='accountTypeDescription')

    # A phone number (max length 15).
    phone: typing.Optional[str] = Field(None, alias='phone')

    # The URL of the institution's primary home page
    url_home_app: typing.Optional[str] = Field(None, alias='urlHomeApp')

    # The URL of the institution's login page
    url_logon_app: typing.Optional[str] = Field(None, alias='urlLogonApp')

    # Institution's forgot password page
    url_forgot_password: typing.Optional[str] = Field(None, alias='urlForgotPassword')

    # Institution's signup page
    url_online_registration: typing.Optional[str] = Field(None, alias='urlOnlineRegistration')

    # Institution's class
    class_: typing.Optional[str] = Field(None, alias='class')

    # Special instructions given to customers for login
    special_text: typing.Optional[str] = Field(None, alias='specialText')

    # The time zone of the institution.
    time_zone: typing.Optional[str] = Field(None, alias='timeZone')

    special_instructions: typing.Optional[InstitutionSpecialInstructions] = Field(None, alias='specialInstructions')

    # The title of the special instructions, if one exists or is required.
    special_instutions_title: typing.Optional[str] = Field(None, alias='specialInstutionsTitle')

    address: typing.Optional[InstitutionAddress] = Field(None, alias='address')

    # An email address
    email: typing.Optional[str] = Field(None, alias='email')

    # The ID of a financial institution, represented as a number
    new_institution_id: typing.Optional[int] = Field(None, alias='newInstitutionId')

    branding: typing.Optional[Branding] = Field(None, alias='branding')

    # The ID of a financial institution, represented as a number
    oauth_institution_id: typing.Optional[int] = Field(None, alias='oauthInstitutionId')
    class Config:
        arbitrary_types_allowed = True
