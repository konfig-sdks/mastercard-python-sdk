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

from mastercard_python_sdk.pydantic.payroll_employer_address import PayrollEmployerAddress

class PayrollEmploymentRecord(BaseModel):
    # Name of the employer as stated by the employer in the payroll system
    employer_name: str = Field(alias='employerName')

    # 'Status codes: `A` - Active, `NLE` - No Longer Employed, `L` - Leave, `O` - Other', `I` - Inactive, `U` - Unknown'
    employment_status_code: str = Field(alias='employmentStatusCode')

    # 'Status name: `Active`, `No Longer Employed`, `Leave` or `Other`, `Inactive`, or `Unknown`'
    employment_status_name: str = Field(alias='employmentStatusName')

    # The categorized work level status. Enumerations are:  * `Temporary`  * `Seasonal`  * `Retired`  * `Student`  * `Full Time`  * `Part Time`  * `Unspecified`  This is a new field, currently enabled only for testing reports. It will be added for all reports in August 2021. 
    work_level_status: str = Field(alias='workLevelStatus')

    # Employer identification number (EIN)
    legal_entity_id: typing.Optional[str] = Field(None, alias='legalEntityId')

    # The original hired date of an employee at the company
    original_hire_date: typing.Optional[int] = Field(None, alias='originalHireDate')

    # If an employee leaves the company and returns later, then the employer states the latest hire date at the company
    latest_hire_date: typing.Optional[int] = Field(None, alias='latestHireDate')

    # The most recent pay period’s end date.
    latest_pay_period_end_date: typing.Optional[int] = Field(None, alias='latestPayPeriodEndDate')

    # The most recent pay date from an employer
    latest_pay_date: typing.Optional[int] = Field(None, alias='latestPayDate')

    # The number of days since an employee was last paid
    days_since_last_pay: typing.Optional[int] = Field(None, alias='daysSinceLastPay')

    # The number of pay cadences an employee has not been paid; determined by the pay frequency
    number_pay_cadence_without_pay: typing.Optional[int] = Field(None, alias='numberPayCadenceWithoutPay')

    # The date an employee ended their employment at the company
    employment_end_date: typing.Optional[int] = Field(None, alias='employmentEndDate')

    # The length of time an employee has been employed with that employer in ISO 8601 format (e.g. P1Y6M0D)
    employment_duration: typing.Optional[str] = Field(None, alias='employmentDuration')

    # Array of addresses
    employer_address: typing.Optional[typing.List[PayrollEmployerAddress]] = Field(None, alias='employerAddress')

    # Describes the employment status - it will be true if it is not directly stated by the employer, and false otherwise
    derived_employment_status: typing.Optional[bool] = Field(None, alias='derivedEmploymentStatus')

    # The abbreviate code for the employment level names (workLevelName) that we receive from the employer
    work_level_code: typing.Optional[str] = Field(None, alias='workLevelCode')

    # The employment level name is whatever we receive from the employer, such as full time, part time, temp, contractor, and more
    work_level_name: typing.Optional[str] = Field(None, alias='workLevelName')

    # Employee job title
    position_title: typing.Optional[str] = Field(None, alias='positionTitle')

    # The length of time an employee has been employed at their current or latest position for this employment in ISO 8601 format (eg P1Y6M0D)
    position_duration: typing.Optional[str] = Field(None, alias='positionDuration')
    class Config:
        arbitrary_types_allowed = True
