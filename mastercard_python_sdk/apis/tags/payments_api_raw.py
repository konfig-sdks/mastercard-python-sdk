# coding: utf-8

"""
    Open Banking

    OpenAPI specification for Finicity APIs.  Open Banking solutions in the US are provided by Finicity, a Mastercard company.

    The version of the OpenAPI document: 1.16.0
    Contact: apisupport@mastercard.com
    Created by: https://developer.mastercard.com/open-banking-us/documentation/support/
"""

from mastercard_python_sdk.paths.aggregation_v1_customers_customer_id_accounts_account_id_owner.get import GetAccountOwnerDetailsRaw
from mastercard_python_sdk.paths.aggregation_v3_customers_customer_id_accounts_account_id_owner.get import GetAccountOwnerDetails0Raw
from mastercard_python_sdk.paths.aggregation_v1_customers_customer_id_accounts_account_id_details.get import GetAchDetailsRaw
from mastercard_python_sdk.paths.aggregation_v1_customers_customer_id_accounts_account_id_available_balance_live.get import GetAvailableBalanceLiveRaw
from mastercard_python_sdk.paths.aggregation_v1_customers_customer_id_accounts_account_id_available_balance.get import GetLatestCachedBalanceRaw
from mastercard_python_sdk.paths.aggregation_v2_customers_customer_id_accounts_account_id_loan_details.get import GetLoanPaymentDetailsRaw


class PaymentsApiRaw(
    GetAccountOwnerDetailsRaw,
    GetAccountOwnerDetails0Raw,
    GetAchDetailsRaw,
    GetAvailableBalanceLiveRaw,
    GetLatestCachedBalanceRaw,
    GetLoanPaymentDetailsRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
