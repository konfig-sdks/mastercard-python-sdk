# coding: utf-8

"""
    Open Banking

    OpenAPI specification for Finicity APIs.  Open Banking solutions in the US are provided by Finicity, a Mastercard company.

    The version of the OpenAPI document: 1.16.0
    Contact: apisupport@mastercard.com
    Created by: https://developer.mastercard.com/open-banking-us/documentation/support/
"""

from mastercard_python_sdk.paths.aggregation_v1_customers_customer_id_subscriptions_subscription_id.delete import DeleteSubscription
from mastercard_python_sdk.paths.aggregation_v1_customers_customer_id_accounts_account_id_txpush.delete import DisableNotifications
from mastercard_python_sdk.paths.aggregation_v1_customers_customer_id_accounts_account_id_transactions.post import InjectTestTransaction
from mastercard_python_sdk.paths.aggregation_v1_customers_customer_id_accounts_account_id_txpush.post import SubscribeNotifications
from mastercard_python_sdk.apis.tags.tx_push_api_raw import TxPushApiRaw


class TxPushApi(
    DeleteSubscription,
    DisableNotifications,
    InjectTestTransaction,
    SubscribeNotifications,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: TxPushApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = TxPushApiRaw(api_client)