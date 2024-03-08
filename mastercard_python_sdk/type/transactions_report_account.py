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

from mastercard_python_sdk.type.report_transaction import ReportTransaction

class RequiredTransactionsReportAccount(TypedDict):
    pass

class OptionalTransactionsReportAccount(TypedDict, total=False):
    # The Finicity account ID
    id: int

    # The account name from the financial institution.
    name: str

    # The account number from the financial institution (obfuscated)
    number: str

    # The list of supported account types. * \"checking\": Standard checking * \"savings\": Standard savings * \"cd\": Certificates of deposit * \"moneyMarket\": Money Market * \"creditCard\": Standard credit cards * \"lineOfCredit\": Home equity, line of credit * \"investment\": Generic investment (no details) * \"investmentTaxDeferred\": Generic tax-advantaged investment (no details) * \"employeeStockPurchasePlan\": ESPP, Employee Stock Ownership Plans (ESOP), Stock Purchase Plans * \"ira\": Individual Retirement Account (not Rollover or Roth) * \"401k\": 401K Plan * \"roth\": Roth IRA, Roth 401K * \"403b\": 403B Plan * \"529plan\": 529 Plan (True value is 529) * \"rollover\": Rollover IRA * \"ugma\": Uniform Gifts to Minors Act * \"utma\": Uniform Transfers to Minors Act * \"keogh\": Keogh Plan * \"457plan\": 457 Plan (True value is 457) * \"401a\": 401A Plan * \"brokerageAccount\": Brokerage Account * \"educationSavings\": Education Savings Account that is not a 529 * \"healthSavingsAccount\": HSA (Health Savings Accounts) * \"pension\": Pension * \"profitSharingPlan\": Profit Sharing Plan * \"roth401k\": Roth 401K * \"sepIRA\": Simplified Employee Pension IRA * \"simpleIRA\": Simple IRA * \"thriftSavingsPlan\": Thrift Savings Plan * \"variableAnnuity\": Variable Annuity * \"cryptocurrency\": Cryptocurrency Wallet, Cryptocurrency Account * \"mortgage\": Standard Mortgages * \"loan\": Auto loans, equity loans, other loans * \"studentLoan\": Student Loan * \"studentLoanGroup\": Student Loan Group * \"studentLoanAccount\": Student Loan Account
    type: str

    # The status of the most recent aggregation attempt for this account. Note: non-zero means the account was not accessed successfully for this report, and additional fields for this account may not be reliable.
    aggregationStatusCode: int

    # The cleared balance of the account as-of `balanceDate`
    balance: typing.Union[int, float]

    # A timestamp showing when the balance was captured
    balanceDate: int

    # a list of transaction records
    transactions: typing.List[ReportTransaction]

class TransactionsReportAccount(RequiredTransactionsReportAccount, OptionalTransactionsReportAccount):
    pass
