# coding: utf-8

"""
    Open Banking

    OpenAPI specification for Finicity APIs.  Open Banking solutions in the US are provided by Finicity, a Mastercard company.

    The version of the OpenAPI document: 1.16.0
    Contact: apisupport@mastercard.com
    Created by: https://developer.mastercard.com/open-banking-us/documentation/support/
"""

from mastercard_python_sdk.paths.analytics_cashflow_v1_customer_customer_id.post import GenerateAnalytics
from mastercard_python_sdk.paths.analytics_cashflow_v1_customer_customer_id_fcra.post import GenerateFcraAnalyticsReport
from mastercard_python_sdk.paths.decisioning_v2_customers_customer_id_reports_cashflow_analytics_user_types_user_type.post import GenerateReport
from mastercard_python_sdk.paths.analytics_data_v1_obb_report_id.get import GetReportData
from mastercard_python_sdk.paths.analytics_data_v1_obb_report_id_fcra.get import GetReportDataFcra
from mastercard_python_sdk.apis.tags.cash_flow_analytics_api_raw import CashFlowAnalyticsApiRaw


class CashFlowAnalyticsApi(
    GenerateAnalytics,
    GenerateFcraAnalyticsReport,
    GenerateReport,
    GetReportData,
    GetReportDataFcra,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: CashFlowAnalyticsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = CashFlowAnalyticsApiRaw(api_client)
