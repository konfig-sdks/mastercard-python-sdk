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

from mastercard_python_sdk.pydantic.child_institution import ChildInstitution

class CertifiedInstitution(BaseModel):
    # The ID of a financial institution, represented as a number
    id: int = Field(alias='id')

    # The name of the institution
    name: str = Field(alias='name')

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

    # \"true\": The institution is certified for the Student Loan Data product  \"false\": The institution is decertified for the Student Loan Data product
    student_loan_data: bool = Field(alias='studentLoanData')

    # \"true\": The institution is certified for the Loan Payment Detail product  \"false\": The institution is decertified for the Loan Payment Detail product
    loan_payment_details: bool = Field(alias='loanPaymentDetails')

    # The RSSD ID is a unique identifier assigned to financial institutions by the Federal Reserve. While the length of the RSSD ID varies by institution, it cannot exceed 10 numerical digits.
    rssd: typing.Optional[int] = Field(None, alias='rssd')

    # An array of child financial institutions
    child_institutions: typing.Optional[typing.List[ChildInstitution]] = Field(None, alias='childInstitutions')
    class Config:
        arbitrary_types_allowed = True
