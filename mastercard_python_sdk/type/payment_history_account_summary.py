# coding: utf-8

"""
    Open Banking

    OpenAPI specification for Finicity APIs.  Open Banking solutions in the US are provided by Finicity, a Mastercard company.

    The version of the OpenAPI document: 1.16.0
    Contact: apisupport@mastercard.com
    Created by: https://developer.mastercard.com/open-banking-us/documentation/support/
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from mastercard_python_sdk.type.payment_history_account_summary_account_owner import PaymentHistoryAccountSummaryAccountOwner

class RequiredPaymentHistoryAccountSummary(TypedDict):
    # Last four digits of the account
    accountNumberDisplay: str

    # Name of the account's institution
    financialInstitution: str

    # URL of institution icon
    institutionIcon: str

    # A currency code
    currency: str

    # An account status
    status: str

    # The account name from the institution
    accountName: str

    accountOwner: PaymentHistoryAccountSummaryAccountOwner

    # The list of supported account types. * \"checking\": Standard checking * \"savings\": Standard savings * \"cd\": Certificates of deposit * \"moneyMarket\": Money Market * \"creditCard\": Standard credit cards * \"lineOfCredit\": Home equity, line of credit * \"investment\": Generic investment (no details) * \"investmentTaxDeferred\": Generic tax-advantaged investment (no details) * \"employeeStockPurchasePlan\": ESPP, Employee Stock Ownership Plans (ESOP), Stock Purchase Plans * \"ira\": Individual Retirement Account (not Rollover or Roth) * \"401k\": 401K Plan * \"roth\": Roth IRA, Roth 401K * \"403b\": 403B Plan * \"529plan\": 529 Plan (True value is 529) * \"rollover\": Rollover IRA * \"ugma\": Uniform Gifts to Minors Act * \"utma\": Uniform Transfers to Minors Act * \"keogh\": Keogh Plan * \"457plan\": 457 Plan (True value is 457) * \"401a\": 401A Plan * \"brokerageAccount\": Brokerage Account * \"educationSavings\": Education Savings Account that is not a 529 * \"healthSavingsAccount\": HSA (Health Savings Accounts) * \"pension\": Pension * \"profitSharingPlan\": Profit Sharing Plan * \"roth401k\": Roth 401K * \"sepIRA\": Simplified Employee Pension IRA * \"simpleIRA\": Simple IRA * \"thriftSavingsPlan\": Thrift Savings Plan * \"variableAnnuity\": Variable Annuity * \"cryptocurrency\": Cryptocurrency Wallet, Cryptocurrency Account * \"mortgage\": Standard Mortgages * \"loan\": Auto loans, equity loans, other loans * \"studentLoan\": Student Loan * \"studentLoanGroup\": Student Loan Group * \"studentLoanAccount\": Student Loan Account
    accountType: str

    # Beginning balance of account
    beginningBalance: typing.Union[int, float]

    # Monthly average balance of account
    averageMonthlyBalance: typing.Union[int, float]

    # Current balance of account
    currentBalance: typing.Union[int, float]

    # Begin date of account
    beginDate: str

    # End date of account
    endDate: str

    # Days since the latest NSF transaction for this account
    daysSinceNonsufficientFunds: int

class OptionalPaymentHistoryAccountSummary(TypedDict, total=False):
    # Total of NSF transactions in this account
    totalNonsufficientFunds: typing.Union[int, float]

class PaymentHistoryAccountSummary(RequiredPaymentHistoryAccountSummary, OptionalPaymentHistoryAccountSummary):
    pass
