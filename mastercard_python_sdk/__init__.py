# coding: utf-8

# flake8: noqa

"""
    Open Banking

    OpenAPI specification for Finicity APIs.  Open Banking solutions in the US are provided by Finicity, a Mastercard company.

    The version of the OpenAPI document: 1.16.0
    Contact: apisupport@mastercard.com
    Created by: https://developer.mastercard.com/open-banking-us/documentation/support/
"""

__version__ = "1.16.0"

# import ApiClient
from mastercard_python_sdk.api_client import ApiClient

# import Configuration
from mastercard_python_sdk.configuration import Configuration

# import exceptions
from mastercard_python_sdk.exceptions import OpenApiException
from mastercard_python_sdk.exceptions import ApiAttributeError
from mastercard_python_sdk.exceptions import ApiTypeError
from mastercard_python_sdk.exceptions import ApiValueError
from mastercard_python_sdk.exceptions import ApiKeyError
from mastercard_python_sdk.exceptions import ApiException

from mastercard_python_sdk.client import Mastercard
