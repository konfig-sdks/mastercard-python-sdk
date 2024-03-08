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

from mastercard_python_sdk.pydantic.customer_account_detail import CustomerAccountDetail
from mastercard_python_sdk.pydantic.customer_account_position import CustomerAccountPosition

class CustomerAccount(BaseModel):
    # An account ID
    id: str = Field(alias='id')

    # The account number from the institution
    number: str = Field(alias='number')

    # The account number from a financial institution in truncated format:    * Last four digits: \"1234\"    * Last four digits with suffix: \"1234-9\"    * Full value for string accounts: \"john@gmail.com\" example: '1234-9'
    account_number_display: str = Field(alias='accountNumberDisplay')

    # The account name from the institution
    name: str = Field(alias='name')

    # The list of supported account types. * \"checking\": Standard checking * \"savings\": Standard savings * \"cd\": Certificates of deposit * \"moneyMarket\": Money Market * \"creditCard\": Standard credit cards * \"lineOfCredit\": Home equity, line of credit * \"investment\": Generic investment (no details) * \"investmentTaxDeferred\": Generic tax-advantaged investment (no details) * \"employeeStockPurchasePlan\": ESPP, Employee Stock Ownership Plans (ESOP), Stock Purchase Plans * \"ira\": Individual Retirement Account (not Rollover or Roth) * \"401k\": 401K Plan * \"roth\": Roth IRA, Roth 401K * \"403b\": 403B Plan * \"529plan\": 529 Plan (True value is 529) * \"rollover\": Rollover IRA * \"ugma\": Uniform Gifts to Minors Act * \"utma\": Uniform Transfers to Minors Act * \"keogh\": Keogh Plan * \"457plan\": 457 Plan (True value is 457) * \"401a\": 401A Plan * \"brokerageAccount\": Brokerage Account * \"educationSavings\": Education Savings Account that is not a 529 * \"healthSavingsAccount\": HSA (Health Savings Accounts) * \"pension\": Pension * \"profitSharingPlan\": Profit Sharing Plan * \"roth401k\": Roth 401K * \"sepIRA\": Simplified Employee Pension IRA * \"simpleIRA\": Simple IRA * \"thriftSavingsPlan\": Thrift Savings Plan * \"variableAnnuity\": Variable Annuity * \"cryptocurrency\": Cryptocurrency Wallet, Cryptocurrency Account * \"mortgage\": Standard Mortgages * \"loan\": Auto loans, equity loans, other loans * \"studentLoan\": Student Loan * \"studentLoanGroup\": Student Loan Group * \"studentLoanAccount\": Student Loan Account
    type: str = Field(alias='type')

    # \"pending\" during account discovery, always \"active\" following   successful account activation
    status: str = Field(alias='status')

    # A customer ID. See Add Customer API for how to create a customer ID.
    customer_id: str = Field(alias='customerId')

    # The ID of a financial institution
    institution_id: str = Field(alias='institutionId')

    # A timestamp showing when the account was added to the system. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    created_date: int = Field(alias='createdDate')

    # A currency code
    currency: str = Field(alias='currency')

    # An institution login ID (from the account record), represented as a number
    institution_login_id: int = Field(alias='institutionLoginId')

    # The last 4 digits of the ACH account number
    real_account_number_last4: typing.Optional[str] = Field(None, alias='realAccountNumberLast4')

    # The cleared balance of the account as of `balanceDate`
    balance: typing.Optional[typing.Union[int, float]] = Field(None, alias='balance')

    # The status of the most recent aggregation attempt (see [Aggregation Status Codes](https://developer.mastercard.com/open-banking-us/documentation/products/manage/account-aggregation/#aggregation-status-codes)). Won't be present until you have run your first aggregation for the account.
    aggregation_status_code: typing.Optional[int] = Field(None, alias='aggregationStatusCode')

    # A timestamp showing when the balance was captured. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    balance_date: typing.Optional[int] = Field(None, alias='balanceDate')

    # A timestamp showing the last successful aggregation of the account. This will not be present until you have run your first aggregation for the account. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    aggregation_success_date: typing.Optional[int] = Field(None, alias='aggregationSuccessDate')

    # A timestamp showing the last aggregation attempt, whether successful or not. This will not be present until you have run your first aggregation for the account. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    aggregation_attempt_date: typing.Optional[int] = Field(None, alias='aggregationAttemptDate')

    # A timestamp showing when the account was last modified to the system. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    last_updated_date: typing.Optional[int] = Field(None, alias='lastUpdatedDate')

    # The market segment of the account. Possible values: personal, business
    market_segment: typing.Optional[str] = Field(None, alias='marketSegment')

    # The date of the latest transaction on the account. This will not be present until you have run your first aggregation for the account. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    last_transaction_date: typing.Optional[int] = Field(None, alias='lastTransactionDate')

    # The date of the oldest transaction in the transactions for the account. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    oldest_transaction_date: typing.Optional[int] = Field(None, alias='oldestTransactionDate')

    detail: typing.Optional[CustomerAccountDetail] = Field(None, alias='detail')

    # Investment holdings
    position: typing.Optional[typing.List[CustomerAccountPosition]] = Field(None, alias='position')

    # Display position of the account at the financial institution, \"1\"     being the top listed account
    display_position: typing.Optional[int] = Field(None, alias='displayPosition')

    # The assigned account ID for the account one level higher in the student loan account hierarchy
    parent_account: typing.Optional[str] = Field(None, alias='parentAccount')
    class Config:
        arbitrary_types_allowed = True
