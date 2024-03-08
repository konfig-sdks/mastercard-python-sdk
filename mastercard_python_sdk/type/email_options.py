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

from mastercard_python_sdk.type.email_options_signature import EmailOptionsSignature

RequiredEmailOptions = TypedDict("RequiredEmailOptions", {
    # The email address for the customer receiving the Connect email
    "to": str,
    })

OptionalEmailOptions = TypedDict("OptionalEmailOptions", {
    # The name of a person or business sending the Connect email
    "from": str,

    # The support phone number listed in the email
    "supportPhone": str,

    # The subject line of the email. The default is \"Verify your Financial Information\".
    "subject": str,

    # The first name of the customer or both names of the customers for joint borrowers. Example: \"Marvin and Jenny\".
    "firstName": str,

    # The name of your company
    "institutionName": str,

    # The institution address to appear in the footer of the email
    "institutionAddress": str,

    "signature": EmailOptionsSignature,
    }, total=False)

class EmailOptions(RequiredEmailOptions, OptionalEmailOptions):
    pass
