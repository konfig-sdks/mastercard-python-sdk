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


class RequiredCustomerAccountPosition(TypedDict):
    pass

class OptionalCustomerAccountPosition(TypedDict, total=False):
    # The description of the holding
    description: str

    # The ID of the investment position
    id: int

    # The investment position's market ticker symbol
    symbol: str

    # The number of units of the holding
    units: typing.Union[int, float]

    # The current price of the investment holding
    currentPrice: typing.Union[int, float]

    # The security name for the investment holding
    securityName: str

    # The transaction type of the holding, such as cash, margin, and more
    transactionType: str

    # Market value of an investment position at the time of retrieval
    marketValue: typing.Union[int, float]

    # The percent change in value since the previous day
    changePercent: typing.Union[int, float]

    # The value amount change since the previous day
    dailyChange: typing.Union[int, float]

    # The total cost of acquiring the security
    costBasis: typing.Union[int, float]

    # The type of the holding
    holdType: str

    # The security type for the investment holding
    invSecurityType: str

    # The status of the holding
    status: str

    # A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    currentPriceDate: int

    # Type of security for the investment position
    securityType: str

    # Type of mutual fund, such as open ended
    mfType: str

    # Fund type assigned by the FI (long or short)
    posType: str

    # Total gain and loss of the position at the time of aggregation in dollars
    totalGLDollar: typing.Union[int, float]

    # Total gain and loss of the position at the time of aggregation in percentage
    totalGLPercent: typing.Union[int, float]

    # The strike price of the option contract
    optionStrikePrice: typing.Union[int, float]

    # The type of option contract (PUT or CALL)
    optionType: str

    # The number of shares per option contract
    optionSharesPerContract: typing.Union[int, float]

    # Expiration date of option
    optionExpireDate: date

    # Financial Institution (FI) defined asset class (COMMON STOCK, COMNEQTY, EQUITY/STOCK, CMA-ISA, CONVERTIBLE PREFERREDS, CORPORATE BONDS, OTHER MONEY FUNDS, ALLOCATION FUNDS, CMA-TAXABLE, FOREIGNEQUITYADRS, COMMONSTOCK, PREFERRED STOCKS, STABLE VALUE, FOREIGN EQUITY ADRS)
    fiAssetClass: str

    # An asset class is a grouping of comparable financial securities. These include equities (stocks), fixed income (bonds), and cash equivalent or money market instruments. (DOMESTICBOND, LARGESTOCK, INTLSTOCK, MONEYMRKT, OTHER)
    assetClass: str

    # Currency rate, ratio of currency to original currency
    currencyRate: typing.Union[int, float]

    # The security ID of the transaction
    securityId: str

    # The security type. This field is related to the `securityId` field. Possible values: * \"CUSIP\"  * \"ISIN\"  * \"SEDOL\"  * \"SICC\"  * \"VALOR\"  * \"WKN\"
    securityIdType: str

    # The per share cost of acquiring the security
    costBasisPerShare: typing.Union[int, float]

    # The subaccount's type, such as cash
    subAccountType: str

    # Symbol for the currency that the account is being converted into
    securityCurrency: str

    # The current day's gain and loss of the position at the time of aggregation in dollars
    todayGLDollar: typing.Union[int, float]

    # The current day's gain and loss of the position at the time of aggregation in percentage
    todayGLPercent: typing.Union[int, float]

class CustomerAccountPosition(RequiredCustomerAccountPosition, OptionalCustomerAccountPosition):
    pass
