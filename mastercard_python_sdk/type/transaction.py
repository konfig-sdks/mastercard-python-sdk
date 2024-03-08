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

from mastercard_python_sdk.type.categorization import Categorization

class RequiredTransaction(TypedDict):
    # The description value is from the financial institution (FI), often known as the payee. The value \"No description provided by institution\" is returned when the FI doesn't provide one
    description: str

    # A transaction ID
    id: int

    # The total amount of the transaction. Transactions for deposits are positive values, withdrawals and debits are negative values.
    amount: typing.Union[int, float]

    # An account ID represented as a number
    accountId: int

    # A customer ID represented as a number. See Add Customer API for how to create a customer ID.
    customerId: int

    # One of \"active\", \"pending\", or \"shadow\" (see [Transaction Status](https://developer.mastercard.com/open-banking-us/documentation/products/manage/transaction-data/#transaction-status))
    status: str

    # A date in Unix epoch time (in seconds). Represents the timestamp of the transaction when it was added to our platform. See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    createdDate: int

class OptionalTransaction(TypedDict, total=False):
    # The institution must provide either a description, a memo, or both. We recommended concatenating the two fields into a single value.
    memo: str

    # If provided by the institution, the following values may be returned in the field of a record: * \"atm\"  * \"cash\"  * \"check\"  * \"credit\"  * \"debit\"  * \"deposit\"  * \"directDebit\"  * \"directDeposit\"  * \"dividend\"  * \"fee\"  * \"interest\"  * \"other\"  * \"payment\"  * \"pointOfSale\"  * \"repeatPayment\"  * \"serviceCharge\"  * \"transfer\"
    type: str

    # A date in Unix epoch time (in seconds). Represents the timestamp of the transaction when it occurred. See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    transactionDate: int

    # A date in Unix epoch time (in seconds). Represents the timestamp of the transaction when it was posted or cleared by the institution. This value isn't required for student loan transaction data. See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    postedDate: int

    # A date in Unix epoch time (in seconds). Represents the first timestamp of the transaction recorded in the `effectiveDate` field. See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    firstEffectiveDate: int

    # A date in Unix epoch time (in seconds). Represents the timestamp of the transaction when it became effective on an account by an institution. See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    effectiveDate: int

    # A date in Unix epoch time (in seconds). Represents the timestamp of the transaction expiration date when it became expires on an account by an institution. See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    optionExpireDate: int

    # The check number of the transaction
    checkNum: str

    # The portion of the transaction allocated to escrow
    escrowAmount: typing.Union[int, float]

    # The portion of the overall transaction amount applied to fees
    feeAmount: typing.Union[int, float]

    # Temporarily hold funds if you overpay or underpay your monthly payment
    suspenseAmount: typing.Union[int, float]

    # The portion of the transaction allocated to interest
    interestAmount: typing.Union[int, float]

    # The portion of the transaction allocated to principal
    principalAmount: typing.Union[int, float]

    # The strike price of the option contract
    optionStrikePrice: typing.Union[int, float]

    # The number of units (individual shares) in the transaction
    unitQuantity: int

    # Share price for the investment unit: stocks, mutual funds, ETFs
    unitPrice: typing.Union[int, float]

    categorization: Categorization

    # The ending balance after the transaction was posted
    runningBalanceAmount: typing.Union[int, float]

    # The type of sub account the funds came from
    subaccountSecurityType: str

    # Transaction commission
    commissionAmount: int

    # Ticker symbol for the investment related to the transaction
    ticker: str

    # Keywords in the `description` and `memo` fields were used to translate investment transactions into these types.  Possible values: * \"cancel\"  * \"purchaseToClose\"  * \"purchaseToCover\"  * \"contribution\"  * \"optionExercise\"  * \"optionExpiration\"  * \"fee\"  * \"soldToClose\"  * \"soldToOpen\"  * \"split\"  * \"transfer\"  * \"returnOfCapital\"  * \"income\"  * \"purchased\"  * \"sold\"  * \"dividendReinvest\"  * \"tax\"  * \"dividend\"  * \"reinvestOfIncome\"  * \"interest\"  * \"deposit\"  * \"otherInfo\"
    investmentTransactionType: str

    # Taxes applicable to the investment trade
    taxesAmount: int

    # If the foreign amount value is present then this is the currency code of that foreign amount
    currencySymbol: str

    # Capital gains applied in short, long, or miscellaneous terms for tax purposes
    incomeType: str

    # Denominator of the stock split for the transaction
    splitDenominator: typing.Union[int, float]

    # Numerator of the stock split for the transaction
    splitNumerator: typing.Union[int, float]

    # Shares per contract of the underlying stock option
    sharesPerContract: typing.Union[int, float]

    # The sub account where the funds came from
    subAccountFund: str

    # The security ID of the transaction
    securityId: str

    # The security type. This field is related to the `securityId` field. Possible values: * \"CUSIP\"  * \"ISIN\"  * \"SEDOL\"  * \"SICC\"  * \"VALOR\"  * \"WKN\"
    securityIdType: str

class Transaction(RequiredTransaction, OptionalTransaction):
    pass
