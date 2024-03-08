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


class CustomerAccountPosition(BaseModel):
    # The description of the holding
    description: typing.Optional[str] = Field(None, alias='description')

    # The ID of the investment position
    id: typing.Optional[int] = Field(None, alias='id')

    # The investment position's market ticker symbol
    symbol: typing.Optional[str] = Field(None, alias='symbol')

    # The number of units of the holding
    units: typing.Optional[typing.Union[int, float]] = Field(None, alias='units')

    # The current price of the investment holding
    current_price: typing.Optional[typing.Union[int, float]] = Field(None, alias='currentPrice')

    # The security name for the investment holding
    security_name: typing.Optional[str] = Field(None, alias='securityName')

    # The transaction type of the holding, such as cash, margin, and more
    transaction_type: typing.Optional[str] = Field(None, alias='transactionType')

    # Market value of an investment position at the time of retrieval
    market_value: typing.Optional[typing.Union[int, float]] = Field(None, alias='marketValue')

    # The percent change in value since the previous day
    change_percent: typing.Optional[typing.Union[int, float]] = Field(None, alias='changePercent')

    # The value amount change since the previous day
    daily_change: typing.Optional[typing.Union[int, float]] = Field(None, alias='dailyChange')

    # The total cost of acquiring the security
    cost_basis: typing.Optional[typing.Union[int, float]] = Field(None, alias='costBasis')

    # The type of the holding
    hold_type: typing.Optional[str] = Field(None, alias='holdType')

    # The security type for the investment holding
    inv_security_type: typing.Optional[str] = Field(None, alias='invSecurityType')

    # The status of the holding
    status: typing.Optional[str] = Field(None, alias='status')

    # A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    current_price_date: typing.Optional[int] = Field(None, alias='currentPriceDate')

    # Type of security for the investment position
    security_type: typing.Optional[str] = Field(None, alias='securityType')

    # Type of mutual fund, such as open ended
    mf_type: typing.Optional[str] = Field(None, alias='mfType')

    # Fund type assigned by the FI (long or short)
    pos_type: typing.Optional[str] = Field(None, alias='posType')

    # Total gain and loss of the position at the time of aggregation in dollars
    total_g_l_dollar: typing.Optional[typing.Union[int, float]] = Field(None, alias='totalGLDollar')

    # Total gain and loss of the position at the time of aggregation in percentage
    total_g_l_percent: typing.Optional[typing.Union[int, float]] = Field(None, alias='totalGLPercent')

    # The strike price of the option contract
    option_strike_price: typing.Optional[typing.Union[int, float]] = Field(None, alias='optionStrikePrice')

    # The type of option contract (PUT or CALL)
    option_type: typing.Optional[str] = Field(None, alias='optionType')

    # The number of shares per option contract
    option_shares_per_contract: typing.Optional[typing.Union[int, float]] = Field(None, alias='optionSharesPerContract')

    # Expiration date of option
    option_expire_date: typing.Optional[date] = Field(None, alias='optionExpireDate')

    # Financial Institution (FI) defined asset class (COMMON STOCK, COMNEQTY, EQUITY/STOCK, CMA-ISA, CONVERTIBLE PREFERREDS, CORPORATE BONDS, OTHER MONEY FUNDS, ALLOCATION FUNDS, CMA-TAXABLE, FOREIGNEQUITYADRS, COMMONSTOCK, PREFERRED STOCKS, STABLE VALUE, FOREIGN EQUITY ADRS)
    fi_asset_class: typing.Optional[str] = Field(None, alias='fiAssetClass')

    # An asset class is a grouping of comparable financial securities. These include equities (stocks), fixed income (bonds), and cash equivalent or money market instruments. (DOMESTICBOND, LARGESTOCK, INTLSTOCK, MONEYMRKT, OTHER)
    asset_class: typing.Optional[str] = Field(None, alias='assetClass')

    # Currency rate, ratio of currency to original currency
    currency_rate: typing.Optional[typing.Union[int, float]] = Field(None, alias='currencyRate')

    # The security ID of the transaction
    security_id: typing.Optional[str] = Field(None, alias='securityId')

    # The security type. This field is related to the `securityId` field. Possible values: * \"CUSIP\"  * \"ISIN\"  * \"SEDOL\"  * \"SICC\"  * \"VALOR\"  * \"WKN\"
    security_id_type: typing.Optional[str] = Field(None, alias='securityIdType')

    # The per share cost of acquiring the security
    cost_basis_per_share: typing.Optional[typing.Union[int, float]] = Field(None, alias='costBasisPerShare')

    # The subaccount's type, such as cash
    sub_account_type: typing.Optional[str] = Field(None, alias='subAccountType')

    # Symbol for the currency that the account is being converted into
    security_currency: typing.Optional[str] = Field(None, alias='securityCurrency')

    # The current day's gain and loss of the position at the time of aggregation in dollars
    today_g_l_dollar: typing.Optional[typing.Union[int, float]] = Field(None, alias='todayGLDollar')

    # The current day's gain and loss of the position at the time of aggregation in percentage
    today_g_l_percent: typing.Optional[typing.Union[int, float]] = Field(None, alias='todayGLPercent')
    class Config:
        arbitrary_types_allowed = True
