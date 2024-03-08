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

from mastercard_python_sdk.type.branding import Branding
from mastercard_python_sdk.type.institution_address import InstitutionAddress
from mastercard_python_sdk.type.institution_special_instructions import InstitutionSpecialInstructions

RequiredInstitution = TypedDict("RequiredInstitution", {
    # The ID of a financial institution, represented as a number
    "id": int,

    # \"true\": The institution is certified for the Transaction Aggregation product \"false\": The institution is decertified for the Transaction Aggregation product
    "transAgg": bool,

    # \"true\": The institution is certified for the ACH product \"false\": The institution is decertified for the ACH product
    "ach": bool,

    # \"true\": The institution is certified for the Statement Aggregation product \"false\": The institution is decertified for the Statement Aggregation product
    "stateAgg": bool,

    # \"true\": The institution is certified for the VOI product \"false\": The institution is decertified for the VOI product
    "voi": bool,

    # \"true\": The institution is certified for the VOA product \"false\": The institution is decertified for the VOA product
    "voa": bool,

    # \"true\": The institution is certified for the Account History Aggregation product \"false\": The institution is decertified for the Account History Aggregation product
    "aha": bool,

    # \"true\": The institution is certified for the Account Balance Check (ABC) product \"false\": The institution is decertified for the Account Balance Check (ABC) product
    "availBalance": bool,

    # \"true\": The institution is certified for the Account Owner product \"false\": The institution is decertified for the Account Owner product
    "accountOwner": bool,

    # \"true\": The institution is an OAuth connection  \"false\": The institution isn't an OAuth connection
    "oauthEnabled": bool,

    # A currency code
    "currency": str,

    # Status for the institution: \"online\", \"offline\", \"maintenance\", \"testing\"
    "status": str,
    })

OptionalInstitution = TypedDict("OptionalInstitution", {
    # The name of the institution
    "name": str,

    # \"true\": The institution is certified for the Student Loan Data product  \"false\": The institution is decertified for the Student Loan Data product
    "studentLoanData": bool,

    # \"true\": The institution is certified for the Loan Payment Detail product  \"false\": The institution is decertified for the Loan Payment Detail product
    "loanPaymentDetails": bool,

    # Values: Banking, Investments, Credit Cards/Accounts, Workplace Retirement, Mortgages and Loans, Insurance
    "accountTypeDescription": str,

    # A phone number (max length 15).
    "phone": str,

    # The URL of the institution's primary home page
    "urlHomeApp": str,

    # The URL of the institution's login page
    "urlLogonApp": str,

    # Institution's forgot password page
    "urlForgotPassword": str,

    # Institution's signup page
    "urlOnlineRegistration": str,

    # Institution's class
    "class": str,

    # Special instructions given to customers for login
    "specialText": str,

    # The time zone of the institution.
    "timeZone": str,

    "specialInstructions": InstitutionSpecialInstructions,

    # The title of the special instructions, if one exists or is required.
    "specialInstutionsTitle": str,

    "address": InstitutionAddress,

    # An email address
    "email": str,

    # The ID of a financial institution, represented as a number
    "newInstitutionId": int,

    "branding": Branding,

    # The ID of a financial institution, represented as a number
    "oauthInstitutionId": int,
    }, total=False)

class Institution(RequiredInstitution, OptionalInstitution):
    pass
