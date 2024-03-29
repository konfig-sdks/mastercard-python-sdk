# coding: utf-8

"""
    Open Banking

    OpenAPI specification for Finicity APIs.  Open Banking solutions in the US are provided by Finicity, a Mastercard company.

    The version of the OpenAPI document: 1.16.0
    Contact: apisupport@mastercard.com
    Created by: https://developer.mastercard.com/open-banking-us/documentation/support/
"""

from mastercard_python_sdk.paths.business_services_customers_customer_id_businesses.post import CreateNewBusinessRaw
from mastercard_python_sdk.paths.business_services_customers_customer_id_businesses.get import GetDetailsByCustomerIdRaw
from mastercard_python_sdk.paths.business_services_businesses_business_id.get import GetDetailsByIdRaw
from mastercard_python_sdk.paths.business_services_businesses_business_id.put import UpdateByIdRaw


class BusinessesAPIApiRaw(
    CreateNewBusinessRaw,
    GetDetailsByCustomerIdRaw,
    GetDetailsByIdRaw,
    UpdateByIdRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
