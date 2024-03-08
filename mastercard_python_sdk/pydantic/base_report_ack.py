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

from mastercard_python_sdk.pydantic.error_message import ErrorMessage

class BaseReportAck(BaseModel):
    # Title of the report
    title: typing.Optional[str] = Field(None, alias='title')

    # A report ID
    id: typing.Optional[str] = Field(None, alias='id')

    # The type of customer (\"active\" or \"testing\" or \"\" for all types)
    customer_type: typing.Optional[str] = Field(None, alias='customerType')

    # A customer ID represented as a number. See Add Customer API for how to create a customer ID.
    customer_id: typing.Optional[int] = Field(None, alias='customerId')

    # Finicity indicator to track all activity associated with this report
    request_id: typing.Optional[str] = Field(None, alias='requestId')

    # Name of a Finicity partner
    requester_name: typing.Optional[str] = Field(None, alias='requesterName')

    # A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/). Note: If the report is retrieved on a day other than the day it was generated, on the header of the PDF version of the report there will be a \"Retrieved Date\" populated.
    created_date: typing.Optional[int] = Field(None, alias='createdDate')

    # A consumer ID. See Create Consumer API for how to create a consumer ID.
    consumer_id: typing.Optional[str] = Field(None, alias='consumerId')

    # Last 4 digits of a SSN
    consumer_ssn: typing.Optional[str] = Field(None, alias='consumerSsn')

    # A report type. Possible values:  * `voi`  * `voa`  * `voaHistory`  * `history`  * `voieTxVerify`  * `voieWithReport`  * `voieWithInterview`  * `paystatement`  * `preQualVoa`  * `assetSummary`  * `voie`  * `transactions`  * `statement`  * `voiePayroll`  * `voeTransactions`  * `voePayroll`  * `cfrp`  * `cfrb`  * `barpcra`  * `barpnoncra`  * `barbcra`  * `barbftc`  * `barbnoncra` 
    type: typing.Optional[str] = Field(None, alias='type')

    # A report generation status. Possible values:  * `inProgress`  * `success`  * `failure` 
    status: typing.Optional[str] = Field(None, alias='status')

    # In case errors occurred during the report generation
    errors: typing.Optional[typing.List[ErrorMessage]] = Field(None, alias='errors')
    class Config:
        arbitrary_types_allowed = True
