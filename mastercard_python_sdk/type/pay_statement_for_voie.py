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

from mastercard_python_sdk.type.direct_deposit import DirectDeposit
from mastercard_python_sdk.type.employee import Employee
from mastercard_python_sdk.type.employer import Employer
from mastercard_python_sdk.type.pay_stat import PayStat
from mastercard_python_sdk.type.pay_statement_for_voie_institutions import PayStatementForVoieInstitutions

class RequiredPayStatementForVoie(TypedDict):
    # This will display true if the pay statement is billable. If a pay statement has been digitized previously, this will display as false as it will not be billable.
    billable: bool

    # The asset ID of the stored pay statement
    assetId: str

    employer: Employer

    employee: Employee

    # Information pertaining to the earnings on the pay statement
    payStat: typing.List[PayStat]

    institutions: PayStatementForVoieInstitutions

class OptionalPayStatementForVoie(TypedDict, total=False):
    # The pay period of the pay statement
    payPeriod: str

    # The listed pay date for the pay statement
    payDate: int

    # The beginning of the pay period
    startDate: int

    # The end of the pay period
    endDate: int

    # The total pay after deductions for the employee for the current pay period
    netPayCurrent: typing.Union[int, float]

    # The total accumulation of pay after deductions for the employee for the current pay year
    netPayYTD: typing.Union[int, float]

    # The total pay before deductions for the employee for the current pay period
    grossPayCurrent: typing.Union[int, float]

    # The total accumulation of pay before deductions for the employee for the current pay year
    grossPayYTD: typing.Union[int, float]

    # The payroll provider extracted from the pay statement
    payrollProvider: str

    # Information pertaining to the direct deposits on the pay statement
    directDeposits: typing.List[DirectDeposit]

    # Error code for the asset
    errorCode: int

    # Error message for the asset
    errorMessage: str

class PayStatementForVoie(RequiredPayStatementForVoie, OptionalPayStatementForVoie):
    pass
