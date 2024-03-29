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


class PayrollVOIEIncomeRecord(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            payFrequency = schemas.StrSchema
            payType = schemas.StrSchema
            basePayRate = schemas.NumberSchema
            basePayRateUnit = schemas.StrSchema
            oldestPayStatementAvailable = schemas.StrSchema
            
            
            class annualIncome(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['AnnualIncome']:
                        return AnnualIncome
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['AnnualIncome'], typing.List['AnnualIncome']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'annualIncome':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'AnnualIncome':
                    return super().__getitem__(i)
        
            @staticmethod
            def monthlyIncome() -> typing.Type['MonthlyIncome']:
                return MonthlyIncome
            
            
            class directPayStatements(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['DirectPayStatements']:
                        return DirectPayStatements
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['DirectPayStatements'], typing.List['DirectPayStatements']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'directPayStatements':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'DirectPayStatements':
                    return super().__getitem__(i)
            __annotations__ = {
                "payFrequency": payFrequency,
                "payType": payType,
                "basePayRate": basePayRate,
                "basePayRateUnit": basePayRateUnit,
                "oldestPayStatementAvailable": oldestPayStatementAvailable,
                "annualIncome": annualIncome,
                "monthlyIncome": monthlyIncome,
                "directPayStatements": directPayStatements,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payFrequency"]) -> MetaOapg.properties.payFrequency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payType"]) -> MetaOapg.properties.payType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["basePayRate"]) -> MetaOapg.properties.basePayRate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["basePayRateUnit"]) -> MetaOapg.properties.basePayRateUnit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["oldestPayStatementAvailable"]) -> MetaOapg.properties.oldestPayStatementAvailable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["annualIncome"]) -> MetaOapg.properties.annualIncome: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["monthlyIncome"]) -> 'MonthlyIncome': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["directPayStatements"]) -> MetaOapg.properties.directPayStatements: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["payFrequency", "payType", "basePayRate", "basePayRateUnit", "oldestPayStatementAvailable", "annualIncome", "monthlyIncome", "directPayStatements", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payFrequency"]) -> typing.Union[MetaOapg.properties.payFrequency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payType"]) -> typing.Union[MetaOapg.properties.payType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["basePayRate"]) -> typing.Union[MetaOapg.properties.basePayRate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["basePayRateUnit"]) -> typing.Union[MetaOapg.properties.basePayRateUnit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["oldestPayStatementAvailable"]) -> typing.Union[MetaOapg.properties.oldestPayStatementAvailable, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["annualIncome"]) -> typing.Union[MetaOapg.properties.annualIncome, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["monthlyIncome"]) -> typing.Union['MonthlyIncome', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["directPayStatements"]) -> typing.Union[MetaOapg.properties.directPayStatements, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["payFrequency", "payType", "basePayRate", "basePayRateUnit", "oldestPayStatementAvailable", "annualIncome", "monthlyIncome", "directPayStatements", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        payFrequency: typing.Union[MetaOapg.properties.payFrequency, str, schemas.Unset] = schemas.unset,
        payType: typing.Union[MetaOapg.properties.payType, str, schemas.Unset] = schemas.unset,
        basePayRate: typing.Union[MetaOapg.properties.basePayRate, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        basePayRateUnit: typing.Union[MetaOapg.properties.basePayRateUnit, str, schemas.Unset] = schemas.unset,
        oldestPayStatementAvailable: typing.Union[MetaOapg.properties.oldestPayStatementAvailable, str, schemas.Unset] = schemas.unset,
        annualIncome: typing.Union[MetaOapg.properties.annualIncome, list, tuple, schemas.Unset] = schemas.unset,
        monthlyIncome: typing.Union['MonthlyIncome', schemas.Unset] = schemas.unset,
        directPayStatements: typing.Union[MetaOapg.properties.directPayStatements, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PayrollVOIEIncomeRecord':
        return super().__new__(
            cls,
            *args,
            payFrequency=payFrequency,
            payType=payType,
            basePayRate=basePayRate,
            basePayRateUnit=basePayRateUnit,
            oldestPayStatementAvailable=oldestPayStatementAvailable,
            annualIncome=annualIncome,
            monthlyIncome=monthlyIncome,
            directPayStatements=directPayStatements,
            _configuration=_configuration,
            **kwargs,
        )

from mastercard_python_sdk.model.annual_income import AnnualIncome
from mastercard_python_sdk.model.direct_pay_statements import DirectPayStatements
from mastercard_python_sdk.model.monthly_income import MonthlyIncome
