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


class ReportSummary(BaseModel):
    # A report ID
    id: str = Field(alias='id')

    # Finicity indicator to track all activity associated with this report
    request_id: str = Field(alias='requestId')

    # Name of a Finicity partner
    requester_name: str = Field(alias='requesterName')

    # A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    created_date: int = Field(alias='createdDate')

    # A report type. Possible values:  * `voi`  * `voa`  * `voaHistory`  * `history`  * `voieTxVerify`  * `voieWithReport`  * `voieWithInterview`  * `paystatement`  * `preQualVoa`  * `assetSummary`  * `voie`  * `transactions`  * `statement`  * `voiePayroll`  * `voeTransactions`  * `voePayroll`  * `cfrp`  * `cfrb`  * `barpcra`  * `barpnoncra`  * `barbcra`  * `barbftc`  * `barbnoncra` 
    type: str = Field(alias='type')

    # A report generation status. Possible values:  * `inProgress`  * `success`  * `failure` 
    status: str = Field(alias='status')

    # A consumer ID. See Create Consumer API for how to create a consumer ID.
    consumer_id: typing.Optional[str] = Field(None, alias='consumerId')

    # Last 4 digits of a SSN
    consumer_ssn: typing.Optional[str] = Field(None, alias='consumerSsn')
    class Config:
        arbitrary_types_allowed = True
