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
from pydantic import BaseModel, Field, RootModel

from mastercard_python_sdk.pydantic.payment_history_account_summary_account_owner import PaymentHistoryAccountSummaryAccountOwner

class PaymentHistoryAccountSummary(BaseModel):
    # Last four digits of the account
    account_number_display: str = Field(alias='accountNumberDisplay')

    # Name of the account's institution
    financial_institution: str = Field(alias='financialInstitution')

    # URL of institution icon
    institution_icon: str = Field(alias='institutionIcon')

    # A currency code
    currency: str = Field(alias='currency')

    # An account status
    status: str = Field(alias='status')

    # The account name from the institution
    account_name: str = Field(alias='accountName')

    account_owner: PaymentHistoryAccountSummaryAccountOwner = Field(alias='accountOwner')

    # The list of supported account types. * \"checking\": Standard checking * \"savings\": Standard savings * \"cd\": Certificates of deposit * \"moneyMarket\": Money Market * \"creditCard\": Standard credit cards * \"lineOfCredit\": Home equity, line of credit * \"investment\": Generic investment (no details) * \"investmentTaxDeferred\": Generic tax-advantaged investment (no details) * \"employeeStockPurchasePlan\": ESPP, Employee Stock Ownership Plans (ESOP), Stock Purchase Plans * \"ira\": Individual Retirement Account (not Rollover or Roth) * \"401k\": 401K Plan * \"roth\": Roth IRA, Roth 401K * \"403b\": 403B Plan * \"529plan\": 529 Plan (True value is 529) * \"rollover\": Rollover IRA * \"ugma\": Uniform Gifts to Minors Act * \"utma\": Uniform Transfers to Minors Act * \"keogh\": Keogh Plan * \"457plan\": 457 Plan (True value is 457) * \"401a\": 401A Plan * \"brokerageAccount\": Brokerage Account * \"educationSavings\": Education Savings Account that is not a 529 * \"healthSavingsAccount\": HSA (Health Savings Accounts) * \"pension\": Pension * \"profitSharingPlan\": Profit Sharing Plan * \"roth401k\": Roth 401K * \"sepIRA\": Simplified Employee Pension IRA * \"simpleIRA\": Simple IRA * \"thriftSavingsPlan\": Thrift Savings Plan * \"variableAnnuity\": Variable Annuity * \"cryptocurrency\": Cryptocurrency Wallet, Cryptocurrency Account * \"mortgage\": Standard Mortgages * \"loan\": Auto loans, equity loans, other loans * \"studentLoan\": Student Loan * \"studentLoanGroup\": Student Loan Group * \"studentLoanAccount\": Student Loan Account
    account_type: str = Field(alias='accountType')

    # Beginning balance of account
    beginning_balance: typing.Union[int, float] = Field(alias='beginningBalance')

    # Monthly average balance of account
    average_monthly_balance: typing.Union[int, float] = Field(alias='averageMonthlyBalance')

    # Current balance of account
    current_balance: typing.Union[int, float] = Field(alias='currentBalance')

    # Begin date of account
    begin_date: str = Field(alias='beginDate')

    # End date of account
    end_date: str = Field(alias='endDate')

    # Days since the latest NSF transaction for this account
    days_since_nonsufficient_funds: int = Field(alias='daysSinceNonsufficientFunds')

    # Total of NSF transactions in this account
    total_nonsufficient_funds: typing.Optional[typing.Union[int, float]] = Field(None, alias='totalNonsufficientFunds')
    class Config:
        arbitrary_types_allowed = True
