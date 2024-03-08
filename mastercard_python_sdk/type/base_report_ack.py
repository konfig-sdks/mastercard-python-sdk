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

from mastercard_python_sdk.type.error_message import ErrorMessage

class RequiredBaseReportAck(TypedDict):
    pass

class OptionalBaseReportAck(TypedDict, total=False):
    # Title of the report
    title: str

    # A report ID
    id: str

    # The type of customer (\"active\" or \"testing\" or \"\" for all types)
    customerType: str

    # A customer ID represented as a number. See Add Customer API for how to create a customer ID.
    customerId: int

    # Finicity indicator to track all activity associated with this report
    requestId: str

    # Name of a Finicity partner
    requesterName: str

    # A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/). Note: If the report is retrieved on a day other than the day it was generated, on the header of the PDF version of the report there will be a \"Retrieved Date\" populated.
    createdDate: int

    # A consumer ID. See Create Consumer API for how to create a consumer ID.
    consumerId: str

    # Last 4 digits of a SSN
    consumerSsn: str

    # A report type. Possible values:  * `voi`  * `voa`  * `voaHistory`  * `history`  * `voieTxVerify`  * `voieWithReport`  * `voieWithInterview`  * `paystatement`  * `preQualVoa`  * `assetSummary`  * `voie`  * `transactions`  * `statement`  * `voiePayroll`  * `voeTransactions`  * `voePayroll`  * `cfrp`  * `cfrb`  * `barpcra`  * `barpnoncra`  * `barbcra`  * `barbftc`  * `barbnoncra` 
    type: str

    # A report generation status. Possible values:  * `inProgress`  * `success`  * `failure` 
    status: str

    # In case errors occurred during the report generation
    errors: typing.List[ErrorMessage]

class BaseReportAck(RequiredBaseReportAck, OptionalBaseReportAck):
    pass
