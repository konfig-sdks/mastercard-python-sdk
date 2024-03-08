import typing_extensions

from mastercard_python_sdk.apis.tags import TagValues
from mastercard_python_sdk.apis.tags.accounts_api import AccountsApi
from mastercard_python_sdk.apis.tags.connect_api import ConnectApi
from mastercard_python_sdk.apis.tags.customers_api import CustomersApi
from mastercard_python_sdk.apis.tags.verify_income_and_employment_api import VerifyIncomeAndEmploymentApi
from mastercard_python_sdk.apis.tags.payments_api import PaymentsApi
from mastercard_python_sdk.apis.tags.app_registration_api import AppRegistrationApi
from mastercard_python_sdk.apis.tags.balance_analytics_api import BalanceAnalyticsApi
from mastercard_python_sdk.apis.tags.cash_flow_analytics_api import CashFlowAnalyticsApi
from mastercard_python_sdk.apis.tags.institutions_api import InstitutionsApi
from mastercard_python_sdk.apis.tags.transactions_api import TransactionsApi
from mastercard_python_sdk.apis.tags.accounts_simple_api import AccountsSimpleApi
from mastercard_python_sdk.apis.tags.consumers_api import ConsumersApi
from mastercard_python_sdk.apis.tags.payment_history_api import PaymentHistoryApi
from mastercard_python_sdk.apis.tags.reports_api import ReportsApi
from mastercard_python_sdk.apis.tags.tx_push_api import TxPushApi
from mastercard_python_sdk.apis.tags.verify_assets_api import VerifyAssetsApi
from mastercard_python_sdk.apis.tags.businesses_api_api import BusinessesAPIApi
from mastercard_python_sdk.apis.tags.account_validation_assistance_api import AccountValidationAssistanceApi
from mastercard_python_sdk.apis.tags.bank_statements_api import BankStatementsApi
from mastercard_python_sdk.apis.tags.third_party_access_api import ThirdPartyAccessApi
from mastercard_python_sdk.apis.tags.authentication_api import AuthenticationApi
from mastercard_python_sdk.apis.tags.cash_flow_api import CashFlowApi
from mastercard_python_sdk.apis.tags.portfolios_api import PortfoliosApi
from mastercard_python_sdk.apis.tags.assets_api import AssetsApi
from mastercard_python_sdk.apis.tags.pay_statements_api import PayStatementsApi
from mastercard_python_sdk.apis.tags.customer_authorization_details_api import CustomerAuthorizationDetailsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ACCOUNTS: AccountsApi,
        TagValues.CONNECT_: ConnectApi,
        TagValues.CUSTOMERS: CustomersApi,
        TagValues.VERIFY_INCOME_AND_EMPLOYMENT: VerifyIncomeAndEmploymentApi,
        TagValues.PAYMENTS: PaymentsApi,
        TagValues.APP_REGISTRATION: AppRegistrationApi,
        TagValues.BALANCE_ANALYTICS: BalanceAnalyticsApi,
        TagValues.CASH_FLOW_ANALYTICS: CashFlowAnalyticsApi,
        TagValues.INSTITUTIONS: InstitutionsApi,
        TagValues.TRANSACTIONS: TransactionsApi,
        TagValues.ACCOUNTS_SIMPLE: AccountsSimpleApi,
        TagValues.CONSUMERS: ConsumersApi,
        TagValues.PAYMENT_HISTORY: PaymentHistoryApi,
        TagValues.REPORTS: ReportsApi,
        TagValues.TX_PUSH: TxPushApi,
        TagValues.VERIFY_ASSETS: VerifyAssetsApi,
        TagValues.BUSINESSES_API: BusinessesAPIApi,
        TagValues.ACCOUNT_VALIDATION_ASSISTANCE: AccountValidationAssistanceApi,
        TagValues.BANK_STATEMENTS: BankStatementsApi,
        TagValues.THIRD_PARTY_ACCESS: ThirdPartyAccessApi,
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.CASH_FLOW: CashFlowApi,
        TagValues.PORTFOLIOS: PortfoliosApi,
        TagValues.ASSETS: AssetsApi,
        TagValues.PAY_STATEMENTS: PayStatementsApi,
        TagValues.CUSTOMER_AUTHORIZATION_DETAILS: CustomerAuthorizationDetailsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ACCOUNTS: AccountsApi,
        TagValues.CONNECT_: ConnectApi,
        TagValues.CUSTOMERS: CustomersApi,
        TagValues.VERIFY_INCOME_AND_EMPLOYMENT: VerifyIncomeAndEmploymentApi,
        TagValues.PAYMENTS: PaymentsApi,
        TagValues.APP_REGISTRATION: AppRegistrationApi,
        TagValues.BALANCE_ANALYTICS: BalanceAnalyticsApi,
        TagValues.CASH_FLOW_ANALYTICS: CashFlowAnalyticsApi,
        TagValues.INSTITUTIONS: InstitutionsApi,
        TagValues.TRANSACTIONS: TransactionsApi,
        TagValues.ACCOUNTS_SIMPLE: AccountsSimpleApi,
        TagValues.CONSUMERS: ConsumersApi,
        TagValues.PAYMENT_HISTORY: PaymentHistoryApi,
        TagValues.REPORTS: ReportsApi,
        TagValues.TX_PUSH: TxPushApi,
        TagValues.VERIFY_ASSETS: VerifyAssetsApi,
        TagValues.BUSINESSES_API: BusinessesAPIApi,
        TagValues.ACCOUNT_VALIDATION_ASSISTANCE: AccountValidationAssistanceApi,
        TagValues.BANK_STATEMENTS: BankStatementsApi,
        TagValues.THIRD_PARTY_ACCESS: ThirdPartyAccessApi,
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.CASH_FLOW: CashFlowApi,
        TagValues.PORTFOLIOS: PortfoliosApi,
        TagValues.ASSETS: AssetsApi,
        TagValues.PAY_STATEMENTS: PayStatementsApi,
        TagValues.CUSTOMER_AUTHORIZATION_DETAILS: CustomerAuthorizationDetailsApi,
    }
)
