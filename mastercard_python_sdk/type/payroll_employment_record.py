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

from mastercard_python_sdk.type.payroll_employer_address import PayrollEmployerAddress

class RequiredPayrollEmploymentRecord(TypedDict):
    # Name of the employer as stated by the employer in the payroll system
    employerName: str

    # 'Status codes: `A` - Active, `NLE` - No Longer Employed, `L` - Leave, `O` - Other', `I` - Inactive, `U` - Unknown'
    employmentStatusCode: str

    # 'Status name: `Active`, `No Longer Employed`, `Leave` or `Other`, `Inactive`, or `Unknown`'
    employmentStatusName: str

    # The categorized work level status. Enumerations are:  * `Temporary`  * `Seasonal`  * `Retired`  * `Student`  * `Full Time`  * `Part Time`  * `Unspecified`  This is a new field, currently enabled only for testing reports. It will be added for all reports in August 2021. 
    workLevelStatus: str

class OptionalPayrollEmploymentRecord(TypedDict, total=False):
    # Employer identification number (EIN)
    legalEntityId: str

    # The original hired date of an employee at the company
    originalHireDate: int

    # If an employee leaves the company and returns later, then the employer states the latest hire date at the company
    latestHireDate: int

    # The most recent pay period’s end date.
    latestPayPeriodEndDate: int

    # The most recent pay date from an employer
    latestPayDate: int

    # The number of days since an employee was last paid
    daysSinceLastPay: int

    # The number of pay cadences an employee has not been paid; determined by the pay frequency
    numberPayCadenceWithoutPay: int

    # The date an employee ended their employment at the company
    employmentEndDate: int

    # The length of time an employee has been employed with that employer in ISO 8601 format (e.g. P1Y6M0D)
    employmentDuration: str

    # Array of addresses
    employerAddress: typing.List[PayrollEmployerAddress]

    # Describes the employment status - it will be true if it is not directly stated by the employer, and false otherwise
    derivedEmploymentStatus: bool

    # The abbreviate code for the employment level names (workLevelName) that we receive from the employer
    workLevelCode: str

    # The employment level name is whatever we receive from the employer, such as full time, part time, temp, contractor, and more
    workLevelName: str

    # Employee job title
    positionTitle: str

    # The length of time an employee has been employed at their current or latest position for this employment in ISO 8601 format (eg P1Y6M0D)
    positionDuration: str

class PayrollEmploymentRecord(RequiredPayrollEmploymentRecord, OptionalPayrollEmploymentRecord):
    pass
