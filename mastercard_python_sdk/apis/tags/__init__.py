# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from mastercard_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    ACCOUNTS = "Accounts"
    CONNECT_ = "Connect 🔗"
    CUSTOMERS = "Customers"
    VERIFY_INCOME_AND_EMPLOYMENT = "Verify Income and Employment"
    PAYMENTS = "Payments"
    APP_REGISTRATION = "App Registration"
    BALANCE_ANALYTICS = "Balance Analytics"
    CASH_FLOW_ANALYTICS = "Cash Flow Analytics"
    INSTITUTIONS = "Institutions"
    TRANSACTIONS = "Transactions"
    ACCOUNTS_SIMPLE = "Accounts (Simple)"
    CONSUMERS = "Consumers"
    PAYMENT_HISTORY = "Payment History"
    REPORTS = "Reports"
    TX_PUSH = "TxPush"
    VERIFY_ASSETS = "Verify Assets"
    BUSINESSES_API = "Businesses API"
    ACCOUNT_VALIDATION_ASSISTANCE = "Account Validation Assistance"
    BANK_STATEMENTS = "Bank Statements"
    THIRD_PARTY_ACCESS = "Third Party Access"
    AUTHENTICATION = "Authentication"
    CASH_FLOW = "Cash Flow"
    PORTFOLIOS = "Portfolios"
    ASSETS = "Assets"
    PAY_STATEMENTS = "Pay Statements"
    CUSTOMER_AUTHORIZATION_DETAILS = "Customer Authorization Details"
