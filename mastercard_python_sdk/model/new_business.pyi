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


class NewBusiness(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "personallyLiable",
            "address",
            "phoneNumber",
            "name",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
                pass
            personallyLiable = schemas.BoolSchema
        
            @staticmethod
            def address() -> typing.Type['NewAddress']:
                return NewAddress
        
            @staticmethod
            def phoneNumber() -> typing.Type['PhoneNumberFormat']:
                return PhoneNumberFormat
            
            
            class url(
                schemas.StrSchema
            ):
                pass
            email = schemas.StrSchema
            
            
            class type(
                schemas.StrSchema
            ):
                pass
            
            
            class taxId(
                schemas.StrSchema
            ):
                pass
            __annotations__ = {
                "name": name,
                "personallyLiable": personallyLiable,
                "address": address,
                "phoneNumber": phoneNumber,
                "url": url,
                "email": email,
                "type": type,
                "taxId": taxId,
            }
    
    personallyLiable: MetaOapg.properties.personallyLiable
    address: 'NewAddress'
    phoneNumber: 'PhoneNumberFormat'
    name: MetaOapg.properties.name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["personallyLiable"]) -> MetaOapg.properties.personallyLiable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address"]) -> 'NewAddress': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phoneNumber"]) -> 'PhoneNumberFormat': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["taxId"]) -> MetaOapg.properties.taxId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "personallyLiable", "address", "phoneNumber", "url", "email", "type", "taxId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["personallyLiable"]) -> MetaOapg.properties.personallyLiable: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address"]) -> 'NewAddress': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phoneNumber"]) -> 'PhoneNumberFormat': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> typing.Union[MetaOapg.properties.url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["taxId"]) -> typing.Union[MetaOapg.properties.taxId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "personallyLiable", "address", "phoneNumber", "url", "email", "type", "taxId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        personallyLiable: typing.Union[MetaOapg.properties.personallyLiable, bool, ],
        address: 'NewAddress',
        phoneNumber: 'PhoneNumberFormat',
        name: typing.Union[MetaOapg.properties.name, str, ],
        url: typing.Union[MetaOapg.properties.url, str, schemas.Unset] = schemas.unset,
        email: typing.Union[MetaOapg.properties.email, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        taxId: typing.Union[MetaOapg.properties.taxId, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'NewBusiness':
        return super().__new__(
            cls,
            *args,
            personallyLiable=personallyLiable,
            address=address,
            phoneNumber=phoneNumber,
            name=name,
            url=url,
            email=email,
            type=type,
            taxId=taxId,
            _configuration=_configuration,
            **kwargs,
        )

from mastercard_python_sdk.model.new_address import NewAddress
from mastercard_python_sdk.model.phone_number_format import PhoneNumberFormat
