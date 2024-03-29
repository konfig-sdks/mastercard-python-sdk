# coding: utf-8

"""
    Open Banking

    OpenAPI specification for Finicity APIs.  Open Banking solutions in the US are provided by Finicity, a Mastercard company.

    The version of the OpenAPI document: 1.16.0
    Contact: apisupport@mastercard.com
    Created by: https://developer.mastercard.com/open-banking-us/documentation/support/
"""

from mastercard_python_sdk.paths.institution_v2_institutions_institution_id_branding.get import GetBrandingByIdRaw
from mastercard_python_sdk.paths.institution_v2_institutions_institution_id.get import GetByIdDetailsRaw
from mastercard_python_sdk.paths.institution_v2_certified_institutions_rssd.get import GetCertifiedInstitutionsWithRssdRaw
from mastercard_python_sdk.paths.institution_v2_certified_institutions.get import ListCertifiedInstitutionsRaw
from mastercard_python_sdk.paths.institution_v2_institutions.get import SearchFinancialInstitutionsRaw


class InstitutionsApiRaw(
    GetBrandingByIdRaw,
    GetByIdDetailsRaw,
    GetCertifiedInstitutionsWithRssdRaw,
    ListCertifiedInstitutionsRaw,
    SearchFinancialInstitutionsRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
