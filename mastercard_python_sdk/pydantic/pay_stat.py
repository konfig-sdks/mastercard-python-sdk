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


class PayStat(BaseModel):
    # The earnings line's pay type description
    description: typing.Optional[str] = Field(None, alias='description')

    # The normalized category of the earnings with a number appended. The number is the will be the iterating number of the type's occurrence starting at one.
    name: typing.Optional[str] = Field(None, alias='name')

    # The categorization based on the earning line's description. Possible values: * \"bereavement\"  * \"bonus\"  * \"commission\"  * \"holiday\"  * \"jury duty\"  * \"overtime\"  * \"pension\"  * \"pto\"  * \"regular\"  * \"sick\"  * \"tips\"  * \"unknown\"  * \"vacation\"  * \"reimbursement\"  * \"stock\"  * \"benefit\"
    type: typing.Optional[str] = Field(None, alias='type')

    # The amount for the earning line paid out to the employee for the specified pay period.
    amount_current: typing.Optional[typing.Union[int, float]] = Field(None, alias='amountCurrent')

    # The amount for the earning line being paid out to the employee for the current pay year.
    amount_y_t_d: typing.Optional[typing.Union[int, float]] = Field(None, alias='amountYTD')
    class Config:
        arbitrary_types_allowed = True
