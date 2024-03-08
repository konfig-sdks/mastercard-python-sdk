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


class StreamModel(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Describes a history of repeated transactions between the same parties.
    """


    class MetaOapg:
        required = {
            "payee",
            "transactionIds",
            "payor",
            "id",
            "recency",
            "cadence",
        }
        
        class properties:
            cadence = schemas.IntSchema
            id = schemas.StrSchema
            payee = schemas.StrSchema
            payor = schemas.StrSchema
            recency = schemas.IntSchema
        
            @staticmethod
            def transactionIds() -> typing.Type['StreamModelTransactionIds']:
                return StreamModelTransactionIds
            __annotations__ = {
                "cadence": cadence,
                "id": id,
                "payee": payee,
                "payor": payor,
                "recency": recency,
                "transactionIds": transactionIds,
            }
    
    payee: MetaOapg.properties.payee
    transactionIds: 'StreamModelTransactionIds'
    payor: MetaOapg.properties.payor
    id: MetaOapg.properties.id
    recency: MetaOapg.properties.recency
    cadence: MetaOapg.properties.cadence
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cadence"]) -> MetaOapg.properties.cadence: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payee"]) -> MetaOapg.properties.payee: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payor"]) -> MetaOapg.properties.payor: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recency"]) -> MetaOapg.properties.recency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transactionIds"]) -> 'StreamModelTransactionIds': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["cadence", "id", "payee", "payor", "recency", "transactionIds", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cadence"]) -> MetaOapg.properties.cadence: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payee"]) -> MetaOapg.properties.payee: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payor"]) -> MetaOapg.properties.payor: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recency"]) -> MetaOapg.properties.recency: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transactionIds"]) -> 'StreamModelTransactionIds': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["cadence", "id", "payee", "payor", "recency", "transactionIds", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        payee: typing.Union[MetaOapg.properties.payee, str, ],
        transactionIds: 'StreamModelTransactionIds',
        payor: typing.Union[MetaOapg.properties.payor, str, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        recency: typing.Union[MetaOapg.properties.recency, decimal.Decimal, int, ],
        cadence: typing.Union[MetaOapg.properties.cadence, decimal.Decimal, int, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'StreamModel':
        return super().__new__(
            cls,
            *args,
            payee=payee,
            transactionIds=transactionIds,
            payor=payor,
            id=id,
            recency=recency,
            cadence=cadence,
            _configuration=_configuration,
            **kwargs,
        )

from mastercard_python_sdk.model.stream_model_transaction_ids import StreamModelTransactionIds
