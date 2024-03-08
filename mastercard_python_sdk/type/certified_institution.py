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

from mastercard_python_sdk.type.child_institution import ChildInstitution

class RequiredCertifiedInstitution(TypedDict):
    # The ID of a financial institution, represented as a number
    id: int

    # The name of the institution
    name: str

    # \"true\": The institution is certified for the Transaction Aggregation product \"false\": The institution is decertified for the Transaction Aggregation product
    transAgg: bool

    # \"true\": The institution is certified for the ACH product \"false\": The institution is decertified for the ACH product
    ach: bool

    # \"true\": The institution is certified for the Statement Aggregation product \"false\": The institution is decertified for the Statement Aggregation product
    stateAgg: bool

    # \"true\": The institution is certified for the VOI product \"false\": The institution is decertified for the VOI product
    voi: bool

    # \"true\": The institution is certified for the VOA product \"false\": The institution is decertified for the VOA product
    voa: bool

    # \"true\": The institution is certified for the Account History Aggregation product \"false\": The institution is decertified for the Account History Aggregation product
    aha: bool

    # \"true\": The institution is certified for the Account Balance Check (ABC) product \"false\": The institution is decertified for the Account Balance Check (ABC) product
    availBalance: bool

    # \"true\": The institution is certified for the Account Owner product \"false\": The institution is decertified for the Account Owner product
    accountOwner: bool

    # \"true\": The institution is certified for the Student Loan Data product  \"false\": The institution is decertified for the Student Loan Data product
    studentLoanData: bool

    # \"true\": The institution is certified for the Loan Payment Detail product  \"false\": The institution is decertified for the Loan Payment Detail product
    loanPaymentDetails: bool

class OptionalCertifiedInstitution(TypedDict, total=False):
    # The RSSD ID is a unique identifier assigned to financial institutions by the Federal Reserve. While the length of the RSSD ID varies by institution, it cannot exceed 10 numerical digits.
    rssd: int

    # An array of child financial institutions
    childInstitutions: typing.List[ChildInstitution]

class CertifiedInstitution(RequiredCertifiedInstitution, OptionalCertifiedInstitution):
    pass
