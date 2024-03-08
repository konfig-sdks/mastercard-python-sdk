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


class CashFlowMonthlycashflowDebits(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "averageDebitAmount",
            "totalDebitsAmount",
            "month",
            "totalDebitsAmountLessTransfers",
            "numberOfDebitsLessTransfers",
            "numberOfDebits",
            "largestDebit",
        }
        
        class properties:
            month = schemas.Int64Schema
            numberOfDebits = schemas.StrSchema
            totalDebitsAmount = schemas.NumberSchema
            largestDebit = schemas.NumberSchema
            numberOfDebitsLessTransfers = schemas.StrSchema
            totalDebitsAmountLessTransfers = schemas.NumberSchema
            averageDebitAmount = schemas.NumberSchema
            __annotations__ = {
                "month": month,
                "numberOfDebits": numberOfDebits,
                "totalDebitsAmount": totalDebitsAmount,
                "largestDebit": largestDebit,
                "numberOfDebitsLessTransfers": numberOfDebitsLessTransfers,
                "totalDebitsAmountLessTransfers": totalDebitsAmountLessTransfers,
                "averageDebitAmount": averageDebitAmount,
            }
    
    averageDebitAmount: MetaOapg.properties.averageDebitAmount
    totalDebitsAmount: MetaOapg.properties.totalDebitsAmount
    month: MetaOapg.properties.month
    totalDebitsAmountLessTransfers: MetaOapg.properties.totalDebitsAmountLessTransfers
    numberOfDebitsLessTransfers: MetaOapg.properties.numberOfDebitsLessTransfers
    numberOfDebits: MetaOapg.properties.numberOfDebits
    largestDebit: MetaOapg.properties.largestDebit
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["month"]) -> MetaOapg.properties.month: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["numberOfDebits"]) -> MetaOapg.properties.numberOfDebits: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalDebitsAmount"]) -> MetaOapg.properties.totalDebitsAmount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["largestDebit"]) -> MetaOapg.properties.largestDebit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["numberOfDebitsLessTransfers"]) -> MetaOapg.properties.numberOfDebitsLessTransfers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalDebitsAmountLessTransfers"]) -> MetaOapg.properties.totalDebitsAmountLessTransfers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["averageDebitAmount"]) -> MetaOapg.properties.averageDebitAmount: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["month", "numberOfDebits", "totalDebitsAmount", "largestDebit", "numberOfDebitsLessTransfers", "totalDebitsAmountLessTransfers", "averageDebitAmount", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["month"]) -> MetaOapg.properties.month: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["numberOfDebits"]) -> MetaOapg.properties.numberOfDebits: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalDebitsAmount"]) -> MetaOapg.properties.totalDebitsAmount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["largestDebit"]) -> MetaOapg.properties.largestDebit: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["numberOfDebitsLessTransfers"]) -> MetaOapg.properties.numberOfDebitsLessTransfers: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalDebitsAmountLessTransfers"]) -> MetaOapg.properties.totalDebitsAmountLessTransfers: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["averageDebitAmount"]) -> MetaOapg.properties.averageDebitAmount: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["month", "numberOfDebits", "totalDebitsAmount", "largestDebit", "numberOfDebitsLessTransfers", "totalDebitsAmountLessTransfers", "averageDebitAmount", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        averageDebitAmount: typing.Union[MetaOapg.properties.averageDebitAmount, decimal.Decimal, int, float, ],
        totalDebitsAmount: typing.Union[MetaOapg.properties.totalDebitsAmount, decimal.Decimal, int, float, ],
        month: typing.Union[MetaOapg.properties.month, decimal.Decimal, int, ],
        totalDebitsAmountLessTransfers: typing.Union[MetaOapg.properties.totalDebitsAmountLessTransfers, decimal.Decimal, int, float, ],
        numberOfDebitsLessTransfers: typing.Union[MetaOapg.properties.numberOfDebitsLessTransfers, str, ],
        numberOfDebits: typing.Union[MetaOapg.properties.numberOfDebits, str, ],
        largestDebit: typing.Union[MetaOapg.properties.largestDebit, decimal.Decimal, int, float, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CashFlowMonthlycashflowDebits':
        return super().__new__(
            cls,
            *args,
            averageDebitAmount=averageDebitAmount,
            totalDebitsAmount=totalDebitsAmount,
            month=month,
            totalDebitsAmountLessTransfers=totalDebitsAmountLessTransfers,
            numberOfDebitsLessTransfers=numberOfDebitsLessTransfers,
            numberOfDebits=numberOfDebits,
            largestDebit=largestDebit,
            _configuration=_configuration,
            **kwargs,
        )
