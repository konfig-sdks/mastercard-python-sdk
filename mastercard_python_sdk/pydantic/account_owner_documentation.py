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


class AccountOwnerDocumentation(BaseModel):
    # Country specific tax ID associated with the customer. * **United Stated**: Social Security number (SSN) or Taxpayer Identification Number (TIN)    * Format: 123-45-7890  * **Canada**: Social Insurance Number (SIM) or Numero d'assurance sociale (NAS)    * Format: 123-456-789
    tax_id: typing.Optional[str] = Field(None, alias='taxId')

    # Country code is Iso3166-1 Alpha-2 code and Alpha 3 standard (max length 3).
    tax_id_country: typing.Optional[str] = Field(None, alias='taxIdCountry')

    # A federal or state issued identification number in alphanumeric characters. * **United States**:    * Passport: 6-9 digits.    * US Visa: 8 digits.    * Driver's license: 1-19 digits * **Canada**:    * Passport: 8 digits    * Driver: 6-9 digits
    government_id: typing.Optional[str] = Field(None, alias='governmentId')
    class Config:
        arbitrary_types_allowed = True
