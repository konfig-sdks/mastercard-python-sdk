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

from mastercard_python_sdk.pydantic.third_party_access_period import ThirdPartyAccessPeriod

class ThirdPartyAccessProduct(BaseModel):
    # Third party access token can be generated for the following product types:   * \"moneyTransferDetails\": Retrieve account details for money transfer * \"availableBalance\": Retrieves the latest cached available and cleared     account balances for an account. * \"availableBalanceLive\": Retrieves the available and cleared account balances live from the financial institution * \"accountOwner\": Retrieves names and addresses of the account owner from a financial institution. * \"paymentIndicator\": Get the Payment Success Indicator response, scoring the likelihood of payment settlement * \"paymentFeedback\": Create feedback loop for Payment Success Indicator (PSI) and/or Payment Routing Optimizer (PRO) * \"paymentRouting\": Product recommends the best rail to use as well as the best time to initiate the payment
    product: str = Field(alias='product')

    # An account ID
    account_id: str = Field(alias='accountId')

    access_period: ThirdPartyAccessPeriod = Field(alias='accessPeriod')

    # The Finicity Partner ID who should be billed when the Requester requests data from Finicity. If no value specified, then the Recipient will be billed.
    payor_id: typing.Optional[str] = Field(None, alias='payorId')

    # Max number of calls to the consented product (consented API)
    max_calls: typing.Optional[int] = Field(None, alias='maxCalls')
    class Config:
        arbitrary_types_allowed = True
