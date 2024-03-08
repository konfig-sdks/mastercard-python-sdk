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

from mastercard_python_sdk.pydantic.categorization import Categorization

class Transaction(BaseModel):
    # The description value is from the financial institution (FI), often known as the payee. The value \"No description provided by institution\" is returned when the FI doesn't provide one
    description: str = Field(alias='description')

    # A transaction ID
    id: int = Field(alias='id')

    # The total amount of the transaction. Transactions for deposits are positive values, withdrawals and debits are negative values.
    amount: typing.Union[int, float] = Field(alias='amount')

    # An account ID represented as a number
    account_id: int = Field(alias='accountId')

    # A customer ID represented as a number. See Add Customer API for how to create a customer ID.
    customer_id: int = Field(alias='customerId')

    # One of \"active\", \"pending\", or \"shadow\" (see [Transaction Status](https://developer.mastercard.com/open-banking-us/documentation/products/manage/transaction-data/#transaction-status))
    status: str = Field(alias='status')

    # A date in Unix epoch time (in seconds). Represents the timestamp of the transaction when it was added to our platform. See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    created_date: int = Field(alias='createdDate')

    # The institution must provide either a description, a memo, or both. We recommended concatenating the two fields into a single value.
    memo: typing.Optional[str] = Field(None, alias='memo')

    # If provided by the institution, the following values may be returned in the field of a record: * \"atm\"  * \"cash\"  * \"check\"  * \"credit\"  * \"debit\"  * \"deposit\"  * \"directDebit\"  * \"directDeposit\"  * \"dividend\"  * \"fee\"  * \"interest\"  * \"other\"  * \"payment\"  * \"pointOfSale\"  * \"repeatPayment\"  * \"serviceCharge\"  * \"transfer\"
    type: typing.Optional[str] = Field(None, alias='type')

    # A date in Unix epoch time (in seconds). Represents the timestamp of the transaction when it occurred. See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    transaction_date: typing.Optional[int] = Field(None, alias='transactionDate')

    # A date in Unix epoch time (in seconds). Represents the timestamp of the transaction when it was posted or cleared by the institution. This value isn't required for student loan transaction data. See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    posted_date: typing.Optional[int] = Field(None, alias='postedDate')

    # A date in Unix epoch time (in seconds). Represents the first timestamp of the transaction recorded in the `effectiveDate` field. See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    first_effective_date: typing.Optional[int] = Field(None, alias='firstEffectiveDate')

    # A date in Unix epoch time (in seconds). Represents the timestamp of the transaction when it became effective on an account by an institution. See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    effective_date: typing.Optional[int] = Field(None, alias='effectiveDate')

    # A date in Unix epoch time (in seconds). Represents the timestamp of the transaction expiration date when it became expires on an account by an institution. See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    option_expire_date: typing.Optional[int] = Field(None, alias='optionExpireDate')

    # The check number of the transaction
    check_num: typing.Optional[str] = Field(None, alias='checkNum')

    # The portion of the transaction allocated to escrow
    escrow_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='escrowAmount')

    # The portion of the overall transaction amount applied to fees
    fee_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='feeAmount')

    # Temporarily hold funds if you overpay or underpay your monthly payment
    suspense_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='suspenseAmount')

    # The portion of the transaction allocated to interest
    interest_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='interestAmount')

    # The portion of the transaction allocated to principal
    principal_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='principalAmount')

    # The strike price of the option contract
    option_strike_price: typing.Optional[typing.Union[int, float]] = Field(None, alias='optionStrikePrice')

    # The number of units (individual shares) in the transaction
    unit_quantity: typing.Optional[int] = Field(None, alias='unitQuantity')

    # Share price for the investment unit: stocks, mutual funds, ETFs
    unit_price: typing.Optional[typing.Union[int, float]] = Field(None, alias='unitPrice')

    categorization: typing.Optional[Categorization] = Field(None, alias='categorization')

    # The ending balance after the transaction was posted
    running_balance_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='runningBalanceAmount')

    # The type of sub account the funds came from
    subaccount_security_type: typing.Optional[str] = Field(None, alias='subaccountSecurityType')

    # Transaction commission
    commission_amount: typing.Optional[int] = Field(None, alias='commissionAmount')

    # Ticker symbol for the investment related to the transaction
    ticker: typing.Optional[str] = Field(None, alias='ticker')

    # Keywords in the `description` and `memo` fields were used to translate investment transactions into these types.  Possible values: * \"cancel\"  * \"purchaseToClose\"  * \"purchaseToCover\"  * \"contribution\"  * \"optionExercise\"  * \"optionExpiration\"  * \"fee\"  * \"soldToClose\"  * \"soldToOpen\"  * \"split\"  * \"transfer\"  * \"returnOfCapital\"  * \"income\"  * \"purchased\"  * \"sold\"  * \"dividendReinvest\"  * \"tax\"  * \"dividend\"  * \"reinvestOfIncome\"  * \"interest\"  * \"deposit\"  * \"otherInfo\"
    investment_transaction_type: typing.Optional[str] = Field(None, alias='investmentTransactionType')

    # Taxes applicable to the investment trade
    taxes_amount: typing.Optional[int] = Field(None, alias='taxesAmount')

    # If the foreign amount value is present then this is the currency code of that foreign amount
    currency_symbol: typing.Optional[str] = Field(None, alias='currencySymbol')

    # Capital gains applied in short, long, or miscellaneous terms for tax purposes
    income_type: typing.Optional[str] = Field(None, alias='incomeType')

    # Denominator of the stock split for the transaction
    split_denominator: typing.Optional[typing.Union[int, float]] = Field(None, alias='splitDenominator')

    # Numerator of the stock split for the transaction
    split_numerator: typing.Optional[typing.Union[int, float]] = Field(None, alias='splitNumerator')

    # Shares per contract of the underlying stock option
    shares_per_contract: typing.Optional[typing.Union[int, float]] = Field(None, alias='sharesPerContract')

    # The sub account where the funds came from
    sub_account_fund: typing.Optional[str] = Field(None, alias='subAccountFund')

    # The security ID of the transaction
    security_id: typing.Optional[str] = Field(None, alias='securityId')

    # The security type. This field is related to the `securityId` field. Possible values: * \"CUSIP\"  * \"ISIN\"  * \"SEDOL\"  * \"SICC\"  * \"VALOR\"  * \"WKN\"
    security_id_type: typing.Optional[str] = Field(None, alias='securityIdType')
    class Config:
        arbitrary_types_allowed = True
