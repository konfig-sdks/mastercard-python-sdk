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


class CashFlowMonthlyCashFlowBalances(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "minDailyBalance",
            "maxDailyBalance",
            "month",
            "averageDailyBalance",
            "numberOfDaysPositiveBalance",
            "numberOfDaysNegativeBalance",
        }
        
        class properties:
            month = schemas.Int64Schema
            minDailyBalance = schemas.NumberSchema
            maxDailyBalance = schemas.NumberSchema
            averageDailyBalance = schemas.NumberSchema
            numberOfDaysNegativeBalance = schemas.StrSchema
            numberOfDaysPositiveBalance = schemas.StrSchema
            standardDeviationOfDailyBalance = schemas.StrSchema
            __annotations__ = {
                "month": month,
                "minDailyBalance": minDailyBalance,
                "maxDailyBalance": maxDailyBalance,
                "averageDailyBalance": averageDailyBalance,
                "numberOfDaysNegativeBalance": numberOfDaysNegativeBalance,
                "numberOfDaysPositiveBalance": numberOfDaysPositiveBalance,
                "standardDeviationOfDailyBalance": standardDeviationOfDailyBalance,
            }
    
    minDailyBalance: MetaOapg.properties.minDailyBalance
    maxDailyBalance: MetaOapg.properties.maxDailyBalance
    month: MetaOapg.properties.month
    averageDailyBalance: MetaOapg.properties.averageDailyBalance
    numberOfDaysPositiveBalance: MetaOapg.properties.numberOfDaysPositiveBalance
    numberOfDaysNegativeBalance: MetaOapg.properties.numberOfDaysNegativeBalance
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["month"]) -> MetaOapg.properties.month: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["minDailyBalance"]) -> MetaOapg.properties.minDailyBalance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxDailyBalance"]) -> MetaOapg.properties.maxDailyBalance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["averageDailyBalance"]) -> MetaOapg.properties.averageDailyBalance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["numberOfDaysNegativeBalance"]) -> MetaOapg.properties.numberOfDaysNegativeBalance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["numberOfDaysPositiveBalance"]) -> MetaOapg.properties.numberOfDaysPositiveBalance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["standardDeviationOfDailyBalance"]) -> MetaOapg.properties.standardDeviationOfDailyBalance: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["month", "minDailyBalance", "maxDailyBalance", "averageDailyBalance", "numberOfDaysNegativeBalance", "numberOfDaysPositiveBalance", "standardDeviationOfDailyBalance", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["month"]) -> MetaOapg.properties.month: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["minDailyBalance"]) -> MetaOapg.properties.minDailyBalance: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxDailyBalance"]) -> MetaOapg.properties.maxDailyBalance: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["averageDailyBalance"]) -> MetaOapg.properties.averageDailyBalance: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["numberOfDaysNegativeBalance"]) -> MetaOapg.properties.numberOfDaysNegativeBalance: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["numberOfDaysPositiveBalance"]) -> MetaOapg.properties.numberOfDaysPositiveBalance: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["standardDeviationOfDailyBalance"]) -> typing.Union[MetaOapg.properties.standardDeviationOfDailyBalance, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["month", "minDailyBalance", "maxDailyBalance", "averageDailyBalance", "numberOfDaysNegativeBalance", "numberOfDaysPositiveBalance", "standardDeviationOfDailyBalance", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        minDailyBalance: typing.Union[MetaOapg.properties.minDailyBalance, decimal.Decimal, int, float, ],
        maxDailyBalance: typing.Union[MetaOapg.properties.maxDailyBalance, decimal.Decimal, int, float, ],
        month: typing.Union[MetaOapg.properties.month, decimal.Decimal, int, ],
        averageDailyBalance: typing.Union[MetaOapg.properties.averageDailyBalance, decimal.Decimal, int, float, ],
        numberOfDaysPositiveBalance: typing.Union[MetaOapg.properties.numberOfDaysPositiveBalance, str, ],
        numberOfDaysNegativeBalance: typing.Union[MetaOapg.properties.numberOfDaysNegativeBalance, str, ],
        standardDeviationOfDailyBalance: typing.Union[MetaOapg.properties.standardDeviationOfDailyBalance, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CashFlowMonthlyCashFlowBalances':
        return super().__new__(
            cls,
            *args,
            minDailyBalance=minDailyBalance,
            maxDailyBalance=maxDailyBalance,
            month=month,
            averageDailyBalance=averageDailyBalance,
            numberOfDaysPositiveBalance=numberOfDaysPositiveBalance,
            numberOfDaysNegativeBalance=numberOfDaysNegativeBalance,
            standardDeviationOfDailyBalance=standardDeviationOfDailyBalance,
            _configuration=_configuration,
            **kwargs,
        )
