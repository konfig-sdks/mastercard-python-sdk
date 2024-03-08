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


class Borrower(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "consumerId",
            "customerId",
            "type",
        }
        
        class properties:
            customerId = schemas.StrSchema
            consumerId = schemas.StrSchema
            type = schemas.StrSchema
        
            @staticmethod
            def optionalConsumerInfo() -> typing.Type['ConsumerInfo']:
                return ConsumerInfo
            __annotations__ = {
                "customerId": customerId,
                "consumerId": consumerId,
                "type": type,
                "optionalConsumerInfo": optionalConsumerInfo,
            }
    
    consumerId: MetaOapg.properties.consumerId
    customerId: MetaOapg.properties.customerId
    type: MetaOapg.properties.type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customerId"]) -> MetaOapg.properties.customerId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["consumerId"]) -> MetaOapg.properties.consumerId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["optionalConsumerInfo"]) -> 'ConsumerInfo': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["customerId", "consumerId", "type", "optionalConsumerInfo", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customerId"]) -> MetaOapg.properties.customerId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["consumerId"]) -> MetaOapg.properties.consumerId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["optionalConsumerInfo"]) -> typing.Union['ConsumerInfo', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["customerId", "consumerId", "type", "optionalConsumerInfo", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        consumerId: typing.Union[MetaOapg.properties.consumerId, str, ],
        customerId: typing.Union[MetaOapg.properties.customerId, str, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        optionalConsumerInfo: typing.Union['ConsumerInfo', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Borrower':
        return super().__new__(
            cls,
            *args,
            consumerId=consumerId,
            customerId=customerId,
            type=type,
            optionalConsumerInfo=optionalConsumerInfo,
            _configuration=_configuration,
            **kwargs,
        )

from mastercard_python_sdk.model.consumer_info import ConsumerInfo
