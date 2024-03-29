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


class ThirdPartyAccessProvenance(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Provenance regarding the calling client like `clientFingerprint`, `ipAddress` and `token`.
    """


    class MetaOapg:
        
        class properties:
            clientFingerprint = schemas.StrSchema
            ipAddress = schemas.StrSchema
            token = schemas.StrSchema
            __annotations__ = {
                "clientFingerprint": clientFingerprint,
                "ipAddress": ipAddress,
                "token": token,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["clientFingerprint"]) -> MetaOapg.properties.clientFingerprint: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ipAddress"]) -> MetaOapg.properties.ipAddress: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["token"]) -> MetaOapg.properties.token: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["clientFingerprint", "ipAddress", "token", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["clientFingerprint"]) -> typing.Union[MetaOapg.properties.clientFingerprint, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ipAddress"]) -> typing.Union[MetaOapg.properties.ipAddress, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["token"]) -> typing.Union[MetaOapg.properties.token, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["clientFingerprint", "ipAddress", "token", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        clientFingerprint: typing.Union[MetaOapg.properties.clientFingerprint, str, schemas.Unset] = schemas.unset,
        ipAddress: typing.Union[MetaOapg.properties.ipAddress, str, schemas.Unset] = schemas.unset,
        token: typing.Union[MetaOapg.properties.token, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ThirdPartyAccessProvenance':
        return super().__new__(
            cls,
            *args,
            clientFingerprint=clientFingerprint,
            ipAddress=ipAddress,
            token=token,
            _configuration=_configuration,
            **kwargs,
        )
