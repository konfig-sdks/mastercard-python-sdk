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


class AccountOwnerDocumentation(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Account owner documentation
    """


    class MetaOapg:
        
        class properties:
            taxId = schemas.StrSchema
            taxIdCountry = schemas.StrSchema
            governmentId = schemas.StrSchema
            __annotations__ = {
                "taxId": taxId,
                "taxIdCountry": taxIdCountry,
                "governmentId": governmentId,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["taxId"]) -> MetaOapg.properties.taxId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["taxIdCountry"]) -> MetaOapg.properties.taxIdCountry: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["governmentId"]) -> MetaOapg.properties.governmentId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["taxId", "taxIdCountry", "governmentId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["taxId"]) -> typing.Union[MetaOapg.properties.taxId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["taxIdCountry"]) -> typing.Union[MetaOapg.properties.taxIdCountry, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["governmentId"]) -> typing.Union[MetaOapg.properties.governmentId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["taxId", "taxIdCountry", "governmentId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        taxId: typing.Union[MetaOapg.properties.taxId, str, schemas.Unset] = schemas.unset,
        taxIdCountry: typing.Union[MetaOapg.properties.taxIdCountry, str, schemas.Unset] = schemas.unset,
        governmentId: typing.Union[MetaOapg.properties.governmentId, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AccountOwnerDocumentation':
        return super().__new__(
            cls,
            *args,
            taxId=taxId,
            taxIdCountry=taxIdCountry,
            governmentId=governmentId,
            _configuration=_configuration,
            **kwargs,
        )