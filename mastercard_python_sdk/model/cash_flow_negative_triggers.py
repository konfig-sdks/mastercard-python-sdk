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


class CashFlowNegativeTriggers(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Transactions that may be warning signs of bad creditworthiness
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def insufficientFundFees() -> typing.Type['CashFlowInsufficientFundsFees']:
                return CashFlowInsufficientFundsFees
            __annotations__ = {
                "insufficientFundFees": insufficientFundFees,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["insufficientFundFees"]) -> 'CashFlowInsufficientFundsFees': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["insufficientFundFees", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["insufficientFundFees"]) -> typing.Union['CashFlowInsufficientFundsFees', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["insufficientFundFees", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        insufficientFundFees: typing.Union['CashFlowInsufficientFundsFees', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CashFlowNegativeTriggers':
        return super().__new__(
            cls,
            *args,
            insufficientFundFees=insufficientFundFees,
            _configuration=_configuration,
            **kwargs,
        )

from mastercard_python_sdk.model.cash_flow_insufficient_funds_fees import CashFlowInsufficientFundsFees
