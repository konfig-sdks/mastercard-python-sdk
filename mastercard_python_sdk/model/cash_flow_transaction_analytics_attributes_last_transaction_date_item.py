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


class CashFlowTransactionAnalyticsAttributesLastTransactionDateItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "date",
        }
        
        class properties:
            date = schemas.StrSchema
            depositsCredits = schemas.NumberSchema
            withdrawalsDebits = schemas.NumberSchema
            zeroAmountTransaction = schemas.NumberSchema
            transactionDescription = schemas.StrSchema
            __annotations__ = {
                "date": date,
                "depositsCredits": depositsCredits,
                "withdrawalsDebits": withdrawalsDebits,
                "zeroAmountTransaction": zeroAmountTransaction,
                "transactionDescription": transactionDescription,
            }
    
    date: MetaOapg.properties.date
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date"]) -> MetaOapg.properties.date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["depositsCredits"]) -> MetaOapg.properties.depositsCredits: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["withdrawalsDebits"]) -> MetaOapg.properties.withdrawalsDebits: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["zeroAmountTransaction"]) -> MetaOapg.properties.zeroAmountTransaction: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transactionDescription"]) -> MetaOapg.properties.transactionDescription: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["date", "depositsCredits", "withdrawalsDebits", "zeroAmountTransaction", "transactionDescription", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date"]) -> MetaOapg.properties.date: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["depositsCredits"]) -> typing.Union[MetaOapg.properties.depositsCredits, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["withdrawalsDebits"]) -> typing.Union[MetaOapg.properties.withdrawalsDebits, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["zeroAmountTransaction"]) -> typing.Union[MetaOapg.properties.zeroAmountTransaction, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transactionDescription"]) -> typing.Union[MetaOapg.properties.transactionDescription, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["date", "depositsCredits", "withdrawalsDebits", "zeroAmountTransaction", "transactionDescription", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        date: typing.Union[MetaOapg.properties.date, str, ],
        depositsCredits: typing.Union[MetaOapg.properties.depositsCredits, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        withdrawalsDebits: typing.Union[MetaOapg.properties.withdrawalsDebits, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        zeroAmountTransaction: typing.Union[MetaOapg.properties.zeroAmountTransaction, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        transactionDescription: typing.Union[MetaOapg.properties.transactionDescription, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CashFlowTransactionAnalyticsAttributesLastTransactionDateItem':
        return super().__new__(
            cls,
            *args,
            date=date,
            depositsCredits=depositsCredits,
            withdrawalsDebits=withdrawalsDebits,
            zeroAmountTransaction=zeroAmountTransaction,
            transactionDescription=transactionDescription,
            _configuration=_configuration,
            **kwargs,
        )