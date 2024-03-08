# coding: utf-8

"""
    Open Banking

    OpenAPI specification for Finicity APIs.  Open Banking solutions in the US are provided by Finicity, a Mastercard company.

    The version of the OpenAPI document: 1.16.0
    Contact: apisupport@mastercard.com
    Created by: https://developer.mastercard.com/open-banking-us/documentation/support/
"""

from mastercard_python_sdk.paths.institution_v2_institutions_institution_id_branding.get import GetBrandingById
from mastercard_python_sdk.paths.institution_v2_institutions_institution_id.get import GetByIdDetails
from mastercard_python_sdk.paths.institution_v2_certified_institutions_rssd.get import GetCertifiedInstitutionsWithRssd
from mastercard_python_sdk.paths.institution_v2_certified_institutions.get import ListCertifiedInstitutions
from mastercard_python_sdk.paths.institution_v2_institutions.get import SearchFinancialInstitutions
from mastercard_python_sdk.apis.tags.institutions_api_raw import InstitutionsApiRaw


class InstitutionsApi(
    GetBrandingById,
    GetByIdDetails,
    GetCertifiedInstitutionsWithRssd,
    ListCertifiedInstitutions,
    SearchFinancialInstitutions,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: InstitutionsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = InstitutionsApiRaw(api_client)
