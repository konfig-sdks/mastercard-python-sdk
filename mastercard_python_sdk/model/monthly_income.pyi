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


class MonthlyIncome(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Current estimated monthly pay for the employment.

This is a mandatory field only for VOIE-payroll report type.
    """


    class MetaOapg:
        required = {
            "estimatedMonthlyTotalPay",
        }
        
        class properties:
            estimatedMonthlyTotalPay = schemas.NumberSchema
            estimatedMonthlyBasePay = schemas.NumberSchema
            estimatedMonthlyOvertimePay = schemas.NumberSchema
            estimatedMonthlyBonusPay = schemas.NumberSchema
            estimatedMonthlyOtherPay = schemas.NumberSchema
            estimatedMonthlyCommissionPay = schemas.NumberSchema
            __annotations__ = {
                "estimatedMonthlyTotalPay": estimatedMonthlyTotalPay,
                "estimatedMonthlyBasePay": estimatedMonthlyBasePay,
                "estimatedMonthlyOvertimePay": estimatedMonthlyOvertimePay,
                "estimatedMonthlyBonusPay": estimatedMonthlyBonusPay,
                "estimatedMonthlyOtherPay": estimatedMonthlyOtherPay,
                "estimatedMonthlyCommissionPay": estimatedMonthlyCommissionPay,
            }
    
    estimatedMonthlyTotalPay: MetaOapg.properties.estimatedMonthlyTotalPay
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["estimatedMonthlyTotalPay"]) -> MetaOapg.properties.estimatedMonthlyTotalPay: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["estimatedMonthlyBasePay"]) -> MetaOapg.properties.estimatedMonthlyBasePay: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["estimatedMonthlyOvertimePay"]) -> MetaOapg.properties.estimatedMonthlyOvertimePay: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["estimatedMonthlyBonusPay"]) -> MetaOapg.properties.estimatedMonthlyBonusPay: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["estimatedMonthlyOtherPay"]) -> MetaOapg.properties.estimatedMonthlyOtherPay: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["estimatedMonthlyCommissionPay"]) -> MetaOapg.properties.estimatedMonthlyCommissionPay: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["estimatedMonthlyTotalPay", "estimatedMonthlyBasePay", "estimatedMonthlyOvertimePay", "estimatedMonthlyBonusPay", "estimatedMonthlyOtherPay", "estimatedMonthlyCommissionPay", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["estimatedMonthlyTotalPay"]) -> MetaOapg.properties.estimatedMonthlyTotalPay: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["estimatedMonthlyBasePay"]) -> typing.Union[MetaOapg.properties.estimatedMonthlyBasePay, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["estimatedMonthlyOvertimePay"]) -> typing.Union[MetaOapg.properties.estimatedMonthlyOvertimePay, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["estimatedMonthlyBonusPay"]) -> typing.Union[MetaOapg.properties.estimatedMonthlyBonusPay, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["estimatedMonthlyOtherPay"]) -> typing.Union[MetaOapg.properties.estimatedMonthlyOtherPay, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["estimatedMonthlyCommissionPay"]) -> typing.Union[MetaOapg.properties.estimatedMonthlyCommissionPay, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["estimatedMonthlyTotalPay", "estimatedMonthlyBasePay", "estimatedMonthlyOvertimePay", "estimatedMonthlyBonusPay", "estimatedMonthlyOtherPay", "estimatedMonthlyCommissionPay", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        estimatedMonthlyTotalPay: typing.Union[MetaOapg.properties.estimatedMonthlyTotalPay, decimal.Decimal, int, float, ],
        estimatedMonthlyBasePay: typing.Union[MetaOapg.properties.estimatedMonthlyBasePay, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        estimatedMonthlyOvertimePay: typing.Union[MetaOapg.properties.estimatedMonthlyOvertimePay, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        estimatedMonthlyBonusPay: typing.Union[MetaOapg.properties.estimatedMonthlyBonusPay, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        estimatedMonthlyOtherPay: typing.Union[MetaOapg.properties.estimatedMonthlyOtherPay, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        estimatedMonthlyCommissionPay: typing.Union[MetaOapg.properties.estimatedMonthlyCommissionPay, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MonthlyIncome':
        return super().__new__(
            cls,
            *args,
            estimatedMonthlyTotalPay=estimatedMonthlyTotalPay,
            estimatedMonthlyBasePay=estimatedMonthlyBasePay,
            estimatedMonthlyOvertimePay=estimatedMonthlyOvertimePay,
            estimatedMonthlyBonusPay=estimatedMonthlyBonusPay,
            estimatedMonthlyOtherPay=estimatedMonthlyOtherPay,
            estimatedMonthlyCommissionPay=estimatedMonthlyCommissionPay,
            _configuration=_configuration,
            **kwargs,
        )
