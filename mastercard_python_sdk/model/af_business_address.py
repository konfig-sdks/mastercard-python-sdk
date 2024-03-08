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


class AFBusinessAddress(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            addressLine1 = schemas.StrSchema
            addressLine2 = schemas.StrSchema
            city = schemas.StrSchema
            state = schemas.StrSchema
            country = schemas.StrSchema
            postalCode = schemas.StrSchema
            __annotations__ = {
                "addressLine1": addressLine1,
                "addressLine2": addressLine2,
                "city": city,
                "state": state,
                "country": country,
                "postalCode": postalCode,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["addressLine1"]) -> MetaOapg.properties.addressLine1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["addressLine2"]) -> MetaOapg.properties.addressLine2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["city"]) -> MetaOapg.properties.city: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["country"]) -> MetaOapg.properties.country: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["postalCode"]) -> MetaOapg.properties.postalCode: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["addressLine1", "addressLine2", "city", "state", "country", "postalCode", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["addressLine1"]) -> typing.Union[MetaOapg.properties.addressLine1, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["addressLine2"]) -> typing.Union[MetaOapg.properties.addressLine2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["city"]) -> typing.Union[MetaOapg.properties.city, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> typing.Union[MetaOapg.properties.state, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["country"]) -> typing.Union[MetaOapg.properties.country, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["postalCode"]) -> typing.Union[MetaOapg.properties.postalCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["addressLine1", "addressLine2", "city", "state", "country", "postalCode", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        addressLine1: typing.Union[MetaOapg.properties.addressLine1, str, schemas.Unset] = schemas.unset,
        addressLine2: typing.Union[MetaOapg.properties.addressLine2, str, schemas.Unset] = schemas.unset,
        city: typing.Union[MetaOapg.properties.city, str, schemas.Unset] = schemas.unset,
        state: typing.Union[MetaOapg.properties.state, str, schemas.Unset] = schemas.unset,
        country: typing.Union[MetaOapg.properties.country, str, schemas.Unset] = schemas.unset,
        postalCode: typing.Union[MetaOapg.properties.postalCode, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AFBusinessAddress':
        return super().__new__(
            cls,
            *args,
            addressLine1=addressLine1,
            addressLine2=addressLine2,
            city=city,
            state=state,
            country=country,
            postalCode=postalCode,
            _configuration=_configuration,
            **kwargs,
        )
