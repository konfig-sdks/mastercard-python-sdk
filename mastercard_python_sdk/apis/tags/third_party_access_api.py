# coding: utf-8

"""
    Open Banking

    OpenAPI specification for Finicity APIs.  Open Banking solutions in the US are provided by Finicity, a Mastercard company.

    The version of the OpenAPI document: 1.16.0
    Contact: apisupport@mastercard.com
    Created by: https://developer.mastercard.com/open-banking-us/documentation/support/
"""

from mastercard_python_sdk.paths.aggregation_v1_partners_access_key.post import GenerateKey
from mastercard_python_sdk.paths.aggregation_v1_partners_access_key_consent_receipt_id.delete import RevokePartnersAccess
from mastercard_python_sdk.paths.aggregation_v1_partners_access_key_consent_receipt_id.put import UpdateAccess
from mastercard_python_sdk.apis.tags.third_party_access_api_raw import ThirdPartyAccessApiRaw


class ThirdPartyAccessApi(
    GenerateKey,
    RevokePartnersAccess,
    UpdateAccess,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ThirdPartyAccessApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ThirdPartyAccessApiRaw(api_client)
