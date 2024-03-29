# coding: utf-8

"""
    Open Banking

    OpenAPI specification for Finicity APIs.  Open Banking solutions in the US are provided by Finicity, a Mastercard company.

    The version of the OpenAPI document: 1.16.0
    Contact: apisupport@mastercard.com
    Created by: https://developer.mastercard.com/open-banking-us/documentation/support/
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from mastercard_python_sdk import schemas  # noqa: F401


class ReportCustomFields(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    The `reportCustomFields` parameter is used when experiences are associated with a credit decisioning report.

Designate up to 5 custom fields that you'd like associated with the report when it's generated. Every custom field consists of three variables: `label`, `value`, and `shown`. The `shown` variable is "true" or "false".
* "true": (default) display the custom field in the PDF report
* "false": don't display the custom field in the PDF report

For an experience that generates multiple reports, the `reportCustomFields` parameter gets passed to all reports.

All custom fields display in the Reseller Billing API.
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['ReportCustomField']:
            return ReportCustomField

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['ReportCustomField'], typing.List['ReportCustomField']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ReportCustomFields':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'ReportCustomField':
        return super().__getitem__(i)

from mastercard_python_sdk.model.report_custom_field import ReportCustomField
