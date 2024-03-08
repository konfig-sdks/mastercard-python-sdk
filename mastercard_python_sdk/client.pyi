# coding: utf-8
"""
    Open Banking

    OpenAPI specification for Finicity APIs.  Open Banking solutions in the US are provided by Finicity, a Mastercard company.

    The version of the OpenAPI document: 1.16.0
    Contact: apisupport@mastercard.com
    Created by: https://developer.mastercard.com/open-banking-us/documentation/support/
"""

import typing
import inspect
from datetime import date, datetime
from mastercard_python_sdk.client_custom import ClientCustom
from mastercard_python_sdk.configuration import Configuration
from mastercard_python_sdk.api_client import ApiClient
from mastercard_python_sdk.type_util import copy_signature
from mastercard_python_sdk.apis.tags.account_validation_assistance_api import AccountValidationAssistanceApi
from mastercard_python_sdk.apis.tags.accounts_api import AccountsApi
from mastercard_python_sdk.apis.tags.accounts_simple_api import AccountsSimpleApi
from mastercard_python_sdk.apis.tags.app_registration_api import AppRegistrationApi
from mastercard_python_sdk.apis.tags.assets_api import AssetsApi
from mastercard_python_sdk.apis.tags.authentication_api import AuthenticationApi
from mastercard_python_sdk.apis.tags.balance_analytics_api import BalanceAnalyticsApi
from mastercard_python_sdk.apis.tags.bank_statements_api import BankStatementsApi
from mastercard_python_sdk.apis.tags.businesses_api_api import BusinessesAPIApi
from mastercard_python_sdk.apis.tags.cash_flow_api import CashFlowApi
from mastercard_python_sdk.apis.tags.cash_flow_analytics_api import CashFlowAnalyticsApi
from mastercard_python_sdk.apis.tags.connect_api import ConnectApi
from mastercard_python_sdk.apis.tags.consumers_api import ConsumersApi
from mastercard_python_sdk.apis.tags.customer_authorization_details_api import CustomerAuthorizationDetailsApi
from mastercard_python_sdk.apis.tags.customers_api import CustomersApi
from mastercard_python_sdk.apis.tags.institutions_api import InstitutionsApi
from mastercard_python_sdk.apis.tags.pay_statements_api import PayStatementsApi
from mastercard_python_sdk.apis.tags.payment_history_api import PaymentHistoryApi
from mastercard_python_sdk.apis.tags.payments_api import PaymentsApi
from mastercard_python_sdk.apis.tags.portfolios_api import PortfoliosApi
from mastercard_python_sdk.apis.tags.reports_api import ReportsApi
from mastercard_python_sdk.apis.tags.third_party_access_api import ThirdPartyAccessApi
from mastercard_python_sdk.apis.tags.transactions_api import TransactionsApi
from mastercard_python_sdk.apis.tags.tx_push_api import TxPushApi
from mastercard_python_sdk.apis.tags.verify_assets_api import VerifyAssetsApi
from mastercard_python_sdk.apis.tags.verify_income_and_employment_api import VerifyIncomeAndEmploymentApi



class Mastercard(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.account_validation_assistance: AccountValidationAssistanceApi = AccountValidationAssistanceApi(api_client)
        self.accounts: AccountsApi = AccountsApi(api_client)
        self.accounts_(simple): AccountsSimpleApi = AccountsSimpleApi(api_client)
        self.app_registration: AppRegistrationApi = AppRegistrationApi(api_client)
        self.assets: AssetsApi = AssetsApi(api_client)
        self.authentication: AuthenticationApi = AuthenticationApi(api_client)
        self.balance_analytics: BalanceAnalyticsApi = BalanceAnalyticsApi(api_client)
        self.bank_statements: BankStatementsApi = BankStatementsApi(api_client)
        self.businesses_api: BusinessesAPIApi = BusinessesAPIApi(api_client)
        self.cash_flow: CashFlowApi = CashFlowApi(api_client)
        self.cash_flow_analytics: CashFlowAnalyticsApi = CashFlowAnalyticsApi(api_client)
        self.connect_🔗: ConnectApi = ConnectApi(api_client)
        self.consumers: ConsumersApi = ConsumersApi(api_client)
        self.customer_authorization_details: CustomerAuthorizationDetailsApi = CustomerAuthorizationDetailsApi(api_client)
        self.customers: CustomersApi = CustomersApi(api_client)
        self.institutions: InstitutionsApi = InstitutionsApi(api_client)
        self.pay_statements: PayStatementsApi = PayStatementsApi(api_client)
        self.payment_history: PaymentHistoryApi = PaymentHistoryApi(api_client)
        self.payments: PaymentsApi = PaymentsApi(api_client)
        self.portfolios: PortfoliosApi = PortfoliosApi(api_client)
        self.reports: ReportsApi = ReportsApi(api_client)
        self.third_party_access: ThirdPartyAccessApi = ThirdPartyAccessApi(api_client)
        self.transactions: TransactionsApi = TransactionsApi(api_client)
        self.tx_push: TxPushApi = TxPushApi(api_client)
        self.verify_assets: VerifyAssetsApi = VerifyAssetsApi(api_client)
        self.verify_income_and_employment: VerifyIncomeAndEmploymentApi = VerifyIncomeAndEmploymentApi(api_client)
