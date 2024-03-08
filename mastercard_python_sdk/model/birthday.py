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


class Birthday(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A birth date
    """


    class MetaOapg:
        
        class properties:
            year = schemas.Int32Schema
            month = schemas.Int32Schema
            dayOfMonth = schemas.Int32Schema
            __annotations__ = {
                "year": year,
                "month": month,
                "dayOfMonth": dayOfMonth,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["year"]) -> MetaOapg.properties.year: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["month"]) -> MetaOapg.properties.month: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dayOfMonth"]) -> MetaOapg.properties.dayOfMonth: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["year", "month", "dayOfMonth", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["year"]) -> typing.Union[MetaOapg.properties.year, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["month"]) -> typing.Union[MetaOapg.properties.month, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dayOfMonth"]) -> typing.Union[MetaOapg.properties.dayOfMonth, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["year", "month", "dayOfMonth", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        year: typing.Union[MetaOapg.properties.year, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        month: typing.Union[MetaOapg.properties.month, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        dayOfMonth: typing.Union[MetaOapg.properties.dayOfMonth, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Birthday':
        return super().__new__(
            cls,
            *args,
            year=year,
            month=month,
            dayOfMonth=dayOfMonth,
            _configuration=_configuration,
            **kwargs,
        )