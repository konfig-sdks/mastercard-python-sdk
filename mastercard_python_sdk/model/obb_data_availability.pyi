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


class ObbDataAvailability(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Availability of historical data at the time the report was requested
    """


    class MetaOapg:
        required = {
            "historicAvailableDays",
            "historicDataAvailability",
        }
        
        class properties:
            historicAvailableDays = schemas.IntSchema
            
            
            class historicDataAvailability(
                schemas.StrSchema
            ):
                pass
            
            
            class historicAvailabilityBeginDate(
                schemas.StrSchema
            ):
                pass
            
            
            class historicAvailabilityEndDate(
                schemas.StrSchema
            ):
                pass
            __annotations__ = {
                "historicAvailableDays": historicAvailableDays,
                "historicDataAvailability": historicDataAvailability,
                "historicAvailabilityBeginDate": historicAvailabilityBeginDate,
                "historicAvailabilityEndDate": historicAvailabilityEndDate,
            }
    
    historicAvailableDays: MetaOapg.properties.historicAvailableDays
    historicDataAvailability: MetaOapg.properties.historicDataAvailability
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["historicAvailableDays"]) -> MetaOapg.properties.historicAvailableDays: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["historicDataAvailability"]) -> MetaOapg.properties.historicDataAvailability: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["historicAvailabilityBeginDate"]) -> MetaOapg.properties.historicAvailabilityBeginDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["historicAvailabilityEndDate"]) -> MetaOapg.properties.historicAvailabilityEndDate: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["historicAvailableDays", "historicDataAvailability", "historicAvailabilityBeginDate", "historicAvailabilityEndDate", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["historicAvailableDays"]) -> MetaOapg.properties.historicAvailableDays: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["historicDataAvailability"]) -> MetaOapg.properties.historicDataAvailability: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["historicAvailabilityBeginDate"]) -> typing.Union[MetaOapg.properties.historicAvailabilityBeginDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["historicAvailabilityEndDate"]) -> typing.Union[MetaOapg.properties.historicAvailabilityEndDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["historicAvailableDays", "historicDataAvailability", "historicAvailabilityBeginDate", "historicAvailabilityEndDate", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        historicAvailableDays: typing.Union[MetaOapg.properties.historicAvailableDays, decimal.Decimal, int, ],
        historicDataAvailability: typing.Union[MetaOapg.properties.historicDataAvailability, str, ],
        historicAvailabilityBeginDate: typing.Union[MetaOapg.properties.historicAvailabilityBeginDate, str, schemas.Unset] = schemas.unset,
        historicAvailabilityEndDate: typing.Union[MetaOapg.properties.historicAvailabilityEndDate, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ObbDataAvailability':
        return super().__new__(
            cls,
            *args,
            historicAvailableDays=historicAvailableDays,
            historicDataAvailability=historicDataAvailability,
            historicAvailabilityBeginDate=historicAvailabilityBeginDate,
            historicAvailabilityEndDate=historicAvailabilityEndDate,
            _configuration=_configuration,
            **kwargs,
        )