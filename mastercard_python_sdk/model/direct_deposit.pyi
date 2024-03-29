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


class DirectDeposit(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            amountCurrent = schemas.NumberSchema
            accountLastFour = schemas.StrSchema
            __annotations__ = {
                "amountCurrent": amountCurrent,
                "accountLastFour": accountLastFour,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amountCurrent"]) -> MetaOapg.properties.amountCurrent: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accountLastFour"]) -> MetaOapg.properties.accountLastFour: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["amountCurrent", "accountLastFour", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amountCurrent"]) -> typing.Union[MetaOapg.properties.amountCurrent, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountLastFour"]) -> typing.Union[MetaOapg.properties.accountLastFour, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["amountCurrent", "accountLastFour", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        amountCurrent: typing.Union[MetaOapg.properties.amountCurrent, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        accountLastFour: typing.Union[MetaOapg.properties.accountLastFour, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DirectDeposit':
        return super().__new__(
            cls,
            *args,
            amountCurrent=amountCurrent,
            accountLastFour=accountLastFour,
            _configuration=_configuration,
            **kwargs,
        )
