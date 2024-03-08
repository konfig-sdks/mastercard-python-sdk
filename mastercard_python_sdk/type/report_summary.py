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


class RequiredReportSummary(TypedDict):
    # A report ID
    id: str

    # Finicity indicator to track all activity associated with this report
    requestId: str

    # Name of a Finicity partner
    requesterName: str

    # A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    createdDate: int

    # A report type. Possible values:  * `voi`  * `voa`  * `voaHistory`  * `history`  * `voieTxVerify`  * `voieWithReport`  * `voieWithInterview`  * `paystatement`  * `preQualVoa`  * `assetSummary`  * `voie`  * `transactions`  * `statement`  * `voiePayroll`  * `voeTransactions`  * `voePayroll`  * `cfrp`  * `cfrb`  * `barpcra`  * `barpnoncra`  * `barbcra`  * `barbftc`  * `barbnoncra` 
    type: str

    # A report generation status. Possible values:  * `inProgress`  * `success`  * `failure` 
    status: str

class OptionalReportSummary(TypedDict, total=False):
    # A consumer ID. See Create Consumer API for how to create a consumer ID.
    consumerId: str

    # Last 4 digits of a SSN
    consumerSsn: str

class ReportSummary(RequiredReportSummary, OptionalReportSummary):
    pass
