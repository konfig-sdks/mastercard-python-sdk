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


class ObbAverageWeeklyBalance(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "fromDate",
            "amount",
            "week",
            "toDate",
        }
        
        class properties:
            amount = schemas.NumberSchema
            
            
            class fromDate(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 10
                    min_length = 10
            
            
            class toDate(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 10
                    min_length = 10
            week = schemas.IntSchema
            __annotations__ = {
                "amount": amount,
                "fromDate": fromDate,
                "toDate": toDate,
                "week": week,
            }
    
    fromDate: MetaOapg.properties.fromDate
    amount: MetaOapg.properties.amount
    week: MetaOapg.properties.week
    toDate: MetaOapg.properties.toDate
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fromDate"]) -> MetaOapg.properties.fromDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["toDate"]) -> MetaOapg.properties.toDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["week"]) -> MetaOapg.properties.week: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["amount", "fromDate", "toDate", "week", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fromDate"]) -> MetaOapg.properties.fromDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["toDate"]) -> MetaOapg.properties.toDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["week"]) -> MetaOapg.properties.week: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["amount", "fromDate", "toDate", "week", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        fromDate: typing.Union[MetaOapg.properties.fromDate, str, ],
        amount: typing.Union[MetaOapg.properties.amount, decimal.Decimal, int, float, ],
        week: typing.Union[MetaOapg.properties.week, decimal.Decimal, int, ],
        toDate: typing.Union[MetaOapg.properties.toDate, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ObbAverageWeeklyBalance':
        return super().__new__(
            cls,
            *args,
            fromDate=fromDate,
            amount=amount,
            week=week,
            toDate=toDate,
            _configuration=_configuration,
            **kwargs,
        )
