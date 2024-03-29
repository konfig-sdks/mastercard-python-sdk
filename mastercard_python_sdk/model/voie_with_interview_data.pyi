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


class VOIEWithInterviewData(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "txVerifyInterview",
        }
        
        class properties:
            
            
            class txVerifyInterview(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['TxVerifyInterview']:
                        return TxVerifyInterview
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['TxVerifyInterview'], typing.List['TxVerifyInterview']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'txVerifyInterview':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'TxVerifyInterview':
                    return super().__getitem__(i)
            extractEarnings = schemas.BoolSchema
            extractDeductions = schemas.BoolSchema
            extractDirectDeposit = schemas.BoolSchema
            __annotations__ = {
                "txVerifyInterview": txVerifyInterview,
                "extractEarnings": extractEarnings,
                "extractDeductions": extractDeductions,
                "extractDirectDeposit": extractDirectDeposit,
            }
    
    txVerifyInterview: MetaOapg.properties.txVerifyInterview
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["txVerifyInterview"]) -> MetaOapg.properties.txVerifyInterview: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["extractEarnings"]) -> MetaOapg.properties.extractEarnings: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["extractDeductions"]) -> MetaOapg.properties.extractDeductions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["extractDirectDeposit"]) -> MetaOapg.properties.extractDirectDeposit: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["txVerifyInterview", "extractEarnings", "extractDeductions", "extractDirectDeposit", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["txVerifyInterview"]) -> MetaOapg.properties.txVerifyInterview: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["extractEarnings"]) -> typing.Union[MetaOapg.properties.extractEarnings, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["extractDeductions"]) -> typing.Union[MetaOapg.properties.extractDeductions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["extractDirectDeposit"]) -> typing.Union[MetaOapg.properties.extractDirectDeposit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["txVerifyInterview", "extractEarnings", "extractDeductions", "extractDirectDeposit", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        txVerifyInterview: typing.Union[MetaOapg.properties.txVerifyInterview, list, tuple, ],
        extractEarnings: typing.Union[MetaOapg.properties.extractEarnings, bool, schemas.Unset] = schemas.unset,
        extractDeductions: typing.Union[MetaOapg.properties.extractDeductions, bool, schemas.Unset] = schemas.unset,
        extractDirectDeposit: typing.Union[MetaOapg.properties.extractDirectDeposit, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'VOIEWithInterviewData':
        return super().__new__(
            cls,
            *args,
            txVerifyInterview=txVerifyInterview,
            extractEarnings=extractEarnings,
            extractDeductions=extractDeductions,
            extractDirectDeposit=extractDirectDeposit,
            _configuration=_configuration,
            **kwargs,
        )

from mastercard_python_sdk.model.tx_verify_interview import TxVerifyInterview
