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


class VOIEWithStatementData(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "assetIds",
        }
        
        class properties:
            
            
            class assetIds(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'assetIds':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            extractEarnings = schemas.BoolSchema
            extractDeductions = schemas.BoolSchema
            extractDirectDeposit = schemas.BoolSchema
            __annotations__ = {
                "assetIds": assetIds,
                "extractEarnings": extractEarnings,
                "extractDeductions": extractDeductions,
                "extractDirectDeposit": extractDirectDeposit,
            }
    
    assetIds: MetaOapg.properties.assetIds
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assetIds"]) -> MetaOapg.properties.assetIds: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["extractEarnings"]) -> MetaOapg.properties.extractEarnings: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["extractDeductions"]) -> MetaOapg.properties.extractDeductions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["extractDirectDeposit"]) -> MetaOapg.properties.extractDirectDeposit: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["assetIds", "extractEarnings", "extractDeductions", "extractDirectDeposit", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assetIds"]) -> MetaOapg.properties.assetIds: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["extractEarnings"]) -> typing.Union[MetaOapg.properties.extractEarnings, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["extractDeductions"]) -> typing.Union[MetaOapg.properties.extractDeductions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["extractDirectDeposit"]) -> typing.Union[MetaOapg.properties.extractDirectDeposit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["assetIds", "extractEarnings", "extractDeductions", "extractDirectDeposit", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        assetIds: typing.Union[MetaOapg.properties.assetIds, list, tuple, ],
        extractEarnings: typing.Union[MetaOapg.properties.extractEarnings, bool, schemas.Unset] = schemas.unset,
        extractDeductions: typing.Union[MetaOapg.properties.extractDeductions, bool, schemas.Unset] = schemas.unset,
        extractDirectDeposit: typing.Union[MetaOapg.properties.extractDirectDeposit, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'VOIEWithStatementData':
        return super().__new__(
            cls,
            *args,
            assetIds=assetIds,
            extractEarnings=extractEarnings,
            extractDeductions=extractDeductions,
            extractDirectDeposit=extractDirectDeposit,
            _configuration=_configuration,
            **kwargs,
        )
