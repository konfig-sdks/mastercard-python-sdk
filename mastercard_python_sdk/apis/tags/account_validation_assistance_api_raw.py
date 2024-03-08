# coding: utf-8

"""
    Open Banking

    OpenAPI specification for Finicity APIs.  Open Banking solutions in the US are provided by Finicity, a Mastercard company.

    The version of the OpenAPI document: 1.16.0
    Contact: apisupport@mastercard.com
    Created by: https://developer.mastercard.com/open-banking-us/documentation/support/
"""

from mastercard_python_sdk.paths.microentry_v1_customers_customer_id_accounts_account_id.get import GetMicroEntriesDetailsRaw
from mastercard_python_sdk.paths.microentry_v1_customers_customer_id.post import InitiateMicroEntriesRaw
from mastercard_python_sdk.paths.microentry_v1_customers_customer_id_accounts_account_id_amounts.post import VerifyMicroEntriesRaw


class AccountValidationAssistanceApiRaw(
    GetMicroEntriesDetailsRaw,
    InitiateMicroEntriesRaw,
    VerifyMicroEntriesRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass