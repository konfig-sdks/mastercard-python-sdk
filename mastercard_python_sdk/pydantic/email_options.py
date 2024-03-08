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

from mastercard_python_sdk.pydantic.email_options_signature import EmailOptionsSignature

class EmailOptions(BaseModel):
    # The email address for the customer receiving the Connect email
    to: str = Field(alias='to')

    # The name of a person or business sending the Connect email
    from_: typing.Optional[str] = Field(None, alias='from')

    # The support phone number listed in the email
    support_phone: typing.Optional[str] = Field(None, alias='supportPhone')

    # The subject line of the email. The default is \"Verify your Financial Information\".
    subject: typing.Optional[str] = Field(None, alias='subject')

    # The first name of the customer or both names of the customers for joint borrowers. Example: \"Marvin and Jenny\".
    first_name: typing.Optional[str] = Field(None, alias='firstName')

    # The name of your company
    institution_name: typing.Optional[str] = Field(None, alias='institutionName')

    # The institution address to appear in the footer of the email
    institution_address: typing.Optional[str] = Field(None, alias='institutionAddress')

    signature: typing.Optional[EmailOptionsSignature] = Field(None, alias='signature')
    class Config:
        arbitrary_types_allowed = True
