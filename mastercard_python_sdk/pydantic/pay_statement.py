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


class PayStatement(BaseModel):
    # The label to be associated with the pay statement. This label will allow the paystub to go through data extraction. * `lastPayPeriod`: default label that should be used for the VOIE - Paystub products * `lastPayPeriodMinusOne`: the second most recent pay statement * `lastPayPeriodMinusTwo`: the third most recent pay statement * `previousYearLastPayPeriod` Last pay statement of the previous calendar year * `previousYear2LastPayPeriod`: last pay statement of the calendar year 2 years prior * `earliestPayPeriod`: the earliest pay statement
    label: str = Field(alias='label')

    # A Base64 encoded pay statement file. Finicity supports PDF, JPG, or PNG files.
    statement: str = Field(alias='statement')
    class Config:
        arbitrary_types_allowed = True
