# coding: utf-8

"""
    Open Banking

    OpenAPI specification for Finicity APIs.  Open Banking solutions in the US are provided by Finicity, a Mastercard company.

    The version of the OpenAPI document: 1.16.0
    Contact: apisupport@mastercard.com
    Created by: https://developer.mastercard.com/open-banking-us/documentation/support/
"""

from mastercard_python_sdk.paths.decisioning_v2_customers_customer_id_transactions.post import Get24MonthsHistoryAndGenerateReportRaw
from mastercard_python_sdk.paths.aggregation_v3_customers_customer_id_transactions.get import GetAllCustomerTransactionsRaw
from mastercard_python_sdk.paths.aggregation_v2_customers_customer_id_transactions_transaction_id.get import GetByIdRaw
from mastercard_python_sdk.paths.aggregation_v4_customers_customer_id_accounts_account_id_transactions.get import GetCustomerAccountTransactionsRaw
from mastercard_python_sdk.paths.aggregation_v1_customers_customer_id_accounts_account_id_transactions_historic.post import LoadHistoricTransactionsForCustomerAccountRaw


class TransactionsApiRaw(
    Get24MonthsHistoryAndGenerateReportRaw,
    GetAllCustomerTransactionsRaw,
    GetByIdRaw,
    GetCustomerAccountTransactionsRaw,
    LoadHistoricTransactionsForCustomerAccountRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass