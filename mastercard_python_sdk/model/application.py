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


class Application(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "ownerState",
            "image",
            "ownerPostalCode",
            "ownerName",
            "appName",
            "appDescription",
            "ownerCountry",
            "appUrl",
            "ownerCity",
            "ownerAddressLine2",
            "ownerAddressLine1",
        }
        
        class properties:
            appDescription = schemas.StrSchema
            appName = schemas.StrSchema
            appUrl = schemas.StrSchema
            ownerAddressLine1 = schemas.StrSchema
            ownerAddressLine2 = schemas.StrSchema
            ownerCity = schemas.StrSchema
            ownerCountry = schemas.StrSchema
            ownerName = schemas.StrSchema
            ownerPostalCode = schemas.StrSchema
            ownerState = schemas.StrSchema
            image = schemas.StrSchema
            __annotations__ = {
                "appDescription": appDescription,
                "appName": appName,
                "appUrl": appUrl,
                "ownerAddressLine1": ownerAddressLine1,
                "ownerAddressLine2": ownerAddressLine2,
                "ownerCity": ownerCity,
                "ownerCountry": ownerCountry,
                "ownerName": ownerName,
                "ownerPostalCode": ownerPostalCode,
                "ownerState": ownerState,
                "image": image,
            }
    
    ownerState: MetaOapg.properties.ownerState
    image: MetaOapg.properties.image
    ownerPostalCode: MetaOapg.properties.ownerPostalCode
    ownerName: MetaOapg.properties.ownerName
    appName: MetaOapg.properties.appName
    appDescription: MetaOapg.properties.appDescription
    ownerCountry: MetaOapg.properties.ownerCountry
    appUrl: MetaOapg.properties.appUrl
    ownerCity: MetaOapg.properties.ownerCity
    ownerAddressLine2: MetaOapg.properties.ownerAddressLine2
    ownerAddressLine1: MetaOapg.properties.ownerAddressLine1
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["appDescription"]) -> MetaOapg.properties.appDescription: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["appName"]) -> MetaOapg.properties.appName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["appUrl"]) -> MetaOapg.properties.appUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ownerAddressLine1"]) -> MetaOapg.properties.ownerAddressLine1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ownerAddressLine2"]) -> MetaOapg.properties.ownerAddressLine2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ownerCity"]) -> MetaOapg.properties.ownerCity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ownerCountry"]) -> MetaOapg.properties.ownerCountry: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ownerName"]) -> MetaOapg.properties.ownerName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ownerPostalCode"]) -> MetaOapg.properties.ownerPostalCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ownerState"]) -> MetaOapg.properties.ownerState: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["image"]) -> MetaOapg.properties.image: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["appDescription", "appName", "appUrl", "ownerAddressLine1", "ownerAddressLine2", "ownerCity", "ownerCountry", "ownerName", "ownerPostalCode", "ownerState", "image", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["appDescription"]) -> MetaOapg.properties.appDescription: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["appName"]) -> MetaOapg.properties.appName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["appUrl"]) -> MetaOapg.properties.appUrl: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ownerAddressLine1"]) -> MetaOapg.properties.ownerAddressLine1: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ownerAddressLine2"]) -> MetaOapg.properties.ownerAddressLine2: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ownerCity"]) -> MetaOapg.properties.ownerCity: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ownerCountry"]) -> MetaOapg.properties.ownerCountry: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ownerName"]) -> MetaOapg.properties.ownerName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ownerPostalCode"]) -> MetaOapg.properties.ownerPostalCode: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ownerState"]) -> MetaOapg.properties.ownerState: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["image"]) -> MetaOapg.properties.image: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["appDescription", "appName", "appUrl", "ownerAddressLine1", "ownerAddressLine2", "ownerCity", "ownerCountry", "ownerName", "ownerPostalCode", "ownerState", "image", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        ownerState: typing.Union[MetaOapg.properties.ownerState, str, ],
        image: typing.Union[MetaOapg.properties.image, str, ],
        ownerPostalCode: typing.Union[MetaOapg.properties.ownerPostalCode, str, ],
        ownerName: typing.Union[MetaOapg.properties.ownerName, str, ],
        appName: typing.Union[MetaOapg.properties.appName, str, ],
        appDescription: typing.Union[MetaOapg.properties.appDescription, str, ],
        ownerCountry: typing.Union[MetaOapg.properties.ownerCountry, str, ],
        appUrl: typing.Union[MetaOapg.properties.appUrl, str, ],
        ownerCity: typing.Union[MetaOapg.properties.ownerCity, str, ],
        ownerAddressLine2: typing.Union[MetaOapg.properties.ownerAddressLine2, str, ],
        ownerAddressLine1: typing.Union[MetaOapg.properties.ownerAddressLine1, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Application':
        return super().__new__(
            cls,
            *args,
            ownerState=ownerState,
            image=image,
            ownerPostalCode=ownerPostalCode,
            ownerName=ownerName,
            appName=appName,
            appDescription=appDescription,
            ownerCountry=ownerCountry,
            appUrl=appUrl,
            ownerCity=ownerCity,
            ownerAddressLine2=ownerAddressLine2,
            ownerAddressLine1=ownerAddressLine1,
            _configuration=_configuration,
            **kwargs,
        )
