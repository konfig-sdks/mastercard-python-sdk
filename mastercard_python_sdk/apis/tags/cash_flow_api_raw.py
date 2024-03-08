# coding: utf-8

"""
    Open Banking

    OpenAPI specification for Finicity APIs.  Open Banking solutions in the US are provided by Finicity, a Mastercard company.

    The version of the OpenAPI document: 1.16.0
    Contact: apisupport@mastercard.com
    Created by: https://developer.mastercard.com/open-banking-us/documentation/support/
"""

from mastercard_python_sdk.paths.decisioning_v2_customers_customer_id_cash_flow_personal.post import GeneratePersonalReportRaw
from mastercard_python_sdk.paths.decisioning_v2_customers_customer_id_cash_flow_business.post import GenerateReportBusinessRaw


class CashFlowApiRaw(
    GeneratePersonalReportRaw,
    GenerateReportBusinessRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass