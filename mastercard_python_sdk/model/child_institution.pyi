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


class ChildInstitution(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "institutionId",
            "parentRSSD",
            "rssd",
            "name",
        }
        
        class properties:
            rssd = schemas.Int64Schema
            parentRSSD = schemas.Int64Schema
            name = schemas.StrSchema
            institutionId = schemas.Int64Schema
            __annotations__ = {
                "rssd": rssd,
                "parentRSSD": parentRSSD,
                "name": name,
                "institutionId": institutionId,
            }
    
    institutionId: MetaOapg.properties.institutionId
    parentRSSD: MetaOapg.properties.parentRSSD
    rssd: MetaOapg.properties.rssd
    name: MetaOapg.properties.name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rssd"]) -> MetaOapg.properties.rssd: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parentRSSD"]) -> MetaOapg.properties.parentRSSD: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["institutionId"]) -> MetaOapg.properties.institutionId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["rssd", "parentRSSD", "name", "institutionId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rssd"]) -> MetaOapg.properties.rssd: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parentRSSD"]) -> MetaOapg.properties.parentRSSD: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["institutionId"]) -> MetaOapg.properties.institutionId: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["rssd", "parentRSSD", "name", "institutionId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        institutionId: typing.Union[MetaOapg.properties.institutionId, decimal.Decimal, int, ],
        parentRSSD: typing.Union[MetaOapg.properties.parentRSSD, decimal.Decimal, int, ],
        rssd: typing.Union[MetaOapg.properties.rssd, decimal.Decimal, int, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ChildInstitution':
        return super().__new__(
            cls,
            *args,
            institutionId=institutionId,
            parentRSSD=parentRSSD,
            rssd=rssd,
            name=name,
            _configuration=_configuration,
            **kwargs,
        )