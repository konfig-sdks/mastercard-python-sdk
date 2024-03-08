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


class RequiredDeductions(TypedDict):
    # Deduction types:  * `Federal tax`: Federal tax withholdings  * `State tax`: State tax withholdings  * `Local tax`: Local tax withholdings  * `Social security tax`: Social security tax withholdings  * `Medicare tax`: Medicare withholdings  * `SUI SDI VPDI tax`: SUI SDI VPDI tax  * Retirement deductions: Retirement withholdings  * `Benefit deductions`: Medical/Health benefits withholdings (i.e. medical, dental, vision, insurance)  * `Garnishment deductions`: Garnishment withholdings, (i.e. bankruptcy, student loan, state garnishments, tax levy garnishments, child support)  * `Other deductions`: Other withholdings, includes any other uncommon withholdings, pension plan, stock plans, etc. 
    type: str

    # Amount associated with deduction
    amount: typing.Union[int, float]

class OptionalDeductions(TypedDict, total=False):
    pass

class Deductions(RequiredDeductions, OptionalDeductions):
    pass
