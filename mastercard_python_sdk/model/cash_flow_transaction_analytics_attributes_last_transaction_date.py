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


class CashFlowTransactionAnalyticsAttributesLastTransactionDate(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    Latest posted transaction(s) to the account. May be more than one if they share the same timestamp
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['CashFlowTransactionAnalyticsAttributesLastTransactionDateItem']:
            return CashFlowTransactionAnalyticsAttributesLastTransactionDateItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['CashFlowTransactionAnalyticsAttributesLastTransactionDateItem'], typing.List['CashFlowTransactionAnalyticsAttributesLastTransactionDateItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'CashFlowTransactionAnalyticsAttributesLastTransactionDate':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'CashFlowTransactionAnalyticsAttributesLastTransactionDateItem':
        return super().__getitem__(i)

from mastercard_python_sdk.model.cash_flow_transaction_analytics_attributes_last_transaction_date_item import CashFlowTransactionAnalyticsAttributesLastTransactionDateItem
