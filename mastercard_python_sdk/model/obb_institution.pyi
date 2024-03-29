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


class ObbInstitution(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Details of the financial institution this account is home to
    """


    class MetaOapg:
        required = {
            "institutionId",
        }
        
        class properties:
            institutionId = schemas.IntSchema
            
            
            class institutionIconUrl(
                schemas.StrSchema
            ):
                pass
            
            
            class institutionName(
                schemas.StrSchema
            ):
                pass
            
            
            class institutionPrimaryColor(
                schemas.StrSchema
            ):
                pass
            __annotations__ = {
                "institutionId": institutionId,
                "institutionIconUrl": institutionIconUrl,
                "institutionName": institutionName,
                "institutionPrimaryColor": institutionPrimaryColor,
            }
    
    institutionId: MetaOapg.properties.institutionId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["institutionId"]) -> MetaOapg.properties.institutionId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["institutionIconUrl"]) -> MetaOapg.properties.institutionIconUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["institutionName"]) -> MetaOapg.properties.institutionName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["institutionPrimaryColor"]) -> MetaOapg.properties.institutionPrimaryColor: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["institutionId", "institutionIconUrl", "institutionName", "institutionPrimaryColor", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["institutionId"]) -> MetaOapg.properties.institutionId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["institutionIconUrl"]) -> typing.Union[MetaOapg.properties.institutionIconUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["institutionName"]) -> typing.Union[MetaOapg.properties.institutionName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["institutionPrimaryColor"]) -> typing.Union[MetaOapg.properties.institutionPrimaryColor, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["institutionId", "institutionIconUrl", "institutionName", "institutionPrimaryColor", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        institutionId: typing.Union[MetaOapg.properties.institutionId, decimal.Decimal, int, ],
        institutionIconUrl: typing.Union[MetaOapg.properties.institutionIconUrl, str, schemas.Unset] = schemas.unset,
        institutionName: typing.Union[MetaOapg.properties.institutionName, str, schemas.Unset] = schemas.unset,
        institutionPrimaryColor: typing.Union[MetaOapg.properties.institutionPrimaryColor, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ObbInstitution':
        return super().__new__(
            cls,
            *args,
            institutionId=institutionId,
            institutionIconUrl=institutionIconUrl,
            institutionName=institutionName,
            institutionPrimaryColor=institutionPrimaryColor,
            _configuration=_configuration,
            **kwargs,
        )
