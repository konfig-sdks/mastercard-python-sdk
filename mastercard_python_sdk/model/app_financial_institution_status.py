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


class AppFinancialInstitutionStatus(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The registration status fields for each specific OAuth financial institution
    """


    class MetaOapg:
        required = {
            "createdDate",
            "lastModifiedDate",
            "decryptionKeyActivated",
            "id",
            "status",
        }
        
        class properties:
            id = schemas.Int64Schema
            decryptionKeyActivated = schemas.BoolSchema
            createdDate = schemas.Int64Schema
            lastModifiedDate = schemas.Int64Schema
            status = schemas.BoolSchema
            abbrvName = schemas.StrSchema
            logoUrl = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "decryptionKeyActivated": decryptionKeyActivated,
                "createdDate": createdDate,
                "lastModifiedDate": lastModifiedDate,
                "status": status,
                "abbrvName": abbrvName,
                "logoUrl": logoUrl,
            }
    
    createdDate: MetaOapg.properties.createdDate
    lastModifiedDate: MetaOapg.properties.lastModifiedDate
    decryptionKeyActivated: MetaOapg.properties.decryptionKeyActivated
    id: MetaOapg.properties.id
    status: MetaOapg.properties.status
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["decryptionKeyActivated"]) -> MetaOapg.properties.decryptionKeyActivated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createdDate"]) -> MetaOapg.properties.createdDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastModifiedDate"]) -> MetaOapg.properties.lastModifiedDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["abbrvName"]) -> MetaOapg.properties.abbrvName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["logoUrl"]) -> MetaOapg.properties.logoUrl: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "decryptionKeyActivated", "createdDate", "lastModifiedDate", "status", "abbrvName", "logoUrl", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["decryptionKeyActivated"]) -> MetaOapg.properties.decryptionKeyActivated: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createdDate"]) -> MetaOapg.properties.createdDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastModifiedDate"]) -> MetaOapg.properties.lastModifiedDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["abbrvName"]) -> typing.Union[MetaOapg.properties.abbrvName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["logoUrl"]) -> typing.Union[MetaOapg.properties.logoUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "decryptionKeyActivated", "createdDate", "lastModifiedDate", "status", "abbrvName", "logoUrl", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        createdDate: typing.Union[MetaOapg.properties.createdDate, decimal.Decimal, int, ],
        lastModifiedDate: typing.Union[MetaOapg.properties.lastModifiedDate, decimal.Decimal, int, ],
        decryptionKeyActivated: typing.Union[MetaOapg.properties.decryptionKeyActivated, bool, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
        status: typing.Union[MetaOapg.properties.status, bool, ],
        abbrvName: typing.Union[MetaOapg.properties.abbrvName, str, schemas.Unset] = schemas.unset,
        logoUrl: typing.Union[MetaOapg.properties.logoUrl, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AppFinancialInstitutionStatus':
        return super().__new__(
            cls,
            *args,
            createdDate=createdDate,
            lastModifiedDate=lastModifiedDate,
            decryptionKeyActivated=decryptionKeyActivated,
            id=id,
            status=status,
            abbrvName=abbrvName,
            logoUrl=logoUrl,
            _configuration=_configuration,
            **kwargs,
        )
