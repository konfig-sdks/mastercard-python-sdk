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


class AccountOwner(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Owner of a customer account
    """


    class MetaOapg:
        required = {
            "ownerName",
            "ownerAddress",
        }
        
        class properties:
            ownerName = schemas.StrSchema
            ownerAddress = schemas.StrSchema
            asOfDate = schemas.Int64Schema
            __annotations__ = {
                "ownerName": ownerName,
                "ownerAddress": ownerAddress,
                "asOfDate": asOfDate,
            }
    
    ownerName: MetaOapg.properties.ownerName
    ownerAddress: MetaOapg.properties.ownerAddress
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ownerName"]) -> MetaOapg.properties.ownerName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ownerAddress"]) -> MetaOapg.properties.ownerAddress: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["asOfDate"]) -> MetaOapg.properties.asOfDate: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["ownerName", "ownerAddress", "asOfDate", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ownerName"]) -> MetaOapg.properties.ownerName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ownerAddress"]) -> MetaOapg.properties.ownerAddress: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["asOfDate"]) -> typing.Union[MetaOapg.properties.asOfDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["ownerName", "ownerAddress", "asOfDate", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        ownerName: typing.Union[MetaOapg.properties.ownerName, str, ],
        ownerAddress: typing.Union[MetaOapg.properties.ownerAddress, str, ],
        asOfDate: typing.Union[MetaOapg.properties.asOfDate, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AccountOwner':
        return super().__new__(
            cls,
            *args,
            ownerName=ownerName,
            ownerAddress=ownerAddress,
            asOfDate=asOfDate,
            _configuration=_configuration,
            **kwargs,
        )
