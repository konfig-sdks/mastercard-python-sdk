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


class CashFlowInflowAttributes(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Inflow Attributes
    """


    class MetaOapg:
        required = {
            "historicCountOfDepositTransactions",
            "minimumDepositByMonthForTheReportTimePeriod",
            "countDepositsByMonthForTheReportTimePeriod",
            "sumDepositsByMonthForTheReportTimePeriod",
            "maximumDepositByMonthForTheReportTimePeriod",
        }
        
        class properties:
            
            
            class countDepositsByMonthForTheReportTimePeriod(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ObbDateRangeAndCount']:
                        return ObbDateRangeAndCount
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ObbDateRangeAndCount'], typing.List['ObbDateRangeAndCount']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'countDepositsByMonthForTheReportTimePeriod':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ObbDateRangeAndCount':
                    return super().__getitem__(i)
            historicCountOfDepositTransactions = schemas.IntSchema
            
            
            class maximumDepositByMonthForTheReportTimePeriod(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ObbDateRangeAndAmount']:
                        return ObbDateRangeAndAmount
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ObbDateRangeAndAmount'], typing.List['ObbDateRangeAndAmount']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'maximumDepositByMonthForTheReportTimePeriod':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ObbDateRangeAndAmount':
                    return super().__getitem__(i)
            
            
            class minimumDepositByMonthForTheReportTimePeriod(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ObbDateRangeAndAmount']:
                        return ObbDateRangeAndAmount
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ObbDateRangeAndAmount'], typing.List['ObbDateRangeAndAmount']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'minimumDepositByMonthForTheReportTimePeriod':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ObbDateRangeAndAmount':
                    return super().__getitem__(i)
            
            
            class sumDepositsByMonthForTheReportTimePeriod(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ObbDateRangeAndAmount']:
                        return ObbDateRangeAndAmount
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ObbDateRangeAndAmount'], typing.List['ObbDateRangeAndAmount']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'sumDepositsByMonthForTheReportTimePeriod':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ObbDateRangeAndAmount':
                    return super().__getitem__(i)
            
            
            class averageDepositByMonthForTheReportTimePeriod(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ObbDateRangeAndAmount']:
                        return ObbDateRangeAndAmount
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ObbDateRangeAndAmount'], typing.List['ObbDateRangeAndAmount']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'averageDepositByMonthForTheReportTimePeriod':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ObbDateRangeAndAmount':
                    return super().__getitem__(i)
            historicSumOfDeposits = schemas.NumberSchema
            __annotations__ = {
                "countDepositsByMonthForTheReportTimePeriod": countDepositsByMonthForTheReportTimePeriod,
                "historicCountOfDepositTransactions": historicCountOfDepositTransactions,
                "maximumDepositByMonthForTheReportTimePeriod": maximumDepositByMonthForTheReportTimePeriod,
                "minimumDepositByMonthForTheReportTimePeriod": minimumDepositByMonthForTheReportTimePeriod,
                "sumDepositsByMonthForTheReportTimePeriod": sumDepositsByMonthForTheReportTimePeriod,
                "averageDepositByMonthForTheReportTimePeriod": averageDepositByMonthForTheReportTimePeriod,
                "historicSumOfDeposits": historicSumOfDeposits,
            }
    
    historicCountOfDepositTransactions: MetaOapg.properties.historicCountOfDepositTransactions
    minimumDepositByMonthForTheReportTimePeriod: MetaOapg.properties.minimumDepositByMonthForTheReportTimePeriod
    countDepositsByMonthForTheReportTimePeriod: MetaOapg.properties.countDepositsByMonthForTheReportTimePeriod
    sumDepositsByMonthForTheReportTimePeriod: MetaOapg.properties.sumDepositsByMonthForTheReportTimePeriod
    maximumDepositByMonthForTheReportTimePeriod: MetaOapg.properties.maximumDepositByMonthForTheReportTimePeriod
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["countDepositsByMonthForTheReportTimePeriod"]) -> MetaOapg.properties.countDepositsByMonthForTheReportTimePeriod: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["historicCountOfDepositTransactions"]) -> MetaOapg.properties.historicCountOfDepositTransactions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maximumDepositByMonthForTheReportTimePeriod"]) -> MetaOapg.properties.maximumDepositByMonthForTheReportTimePeriod: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["minimumDepositByMonthForTheReportTimePeriod"]) -> MetaOapg.properties.minimumDepositByMonthForTheReportTimePeriod: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sumDepositsByMonthForTheReportTimePeriod"]) -> MetaOapg.properties.sumDepositsByMonthForTheReportTimePeriod: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["averageDepositByMonthForTheReportTimePeriod"]) -> MetaOapg.properties.averageDepositByMonthForTheReportTimePeriod: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["historicSumOfDeposits"]) -> MetaOapg.properties.historicSumOfDeposits: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["countDepositsByMonthForTheReportTimePeriod", "historicCountOfDepositTransactions", "maximumDepositByMonthForTheReportTimePeriod", "minimumDepositByMonthForTheReportTimePeriod", "sumDepositsByMonthForTheReportTimePeriod", "averageDepositByMonthForTheReportTimePeriod", "historicSumOfDeposits", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["countDepositsByMonthForTheReportTimePeriod"]) -> MetaOapg.properties.countDepositsByMonthForTheReportTimePeriod: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["historicCountOfDepositTransactions"]) -> MetaOapg.properties.historicCountOfDepositTransactions: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maximumDepositByMonthForTheReportTimePeriod"]) -> MetaOapg.properties.maximumDepositByMonthForTheReportTimePeriod: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["minimumDepositByMonthForTheReportTimePeriod"]) -> MetaOapg.properties.minimumDepositByMonthForTheReportTimePeriod: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sumDepositsByMonthForTheReportTimePeriod"]) -> MetaOapg.properties.sumDepositsByMonthForTheReportTimePeriod: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["averageDepositByMonthForTheReportTimePeriod"]) -> typing.Union[MetaOapg.properties.averageDepositByMonthForTheReportTimePeriod, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["historicSumOfDeposits"]) -> typing.Union[MetaOapg.properties.historicSumOfDeposits, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["countDepositsByMonthForTheReportTimePeriod", "historicCountOfDepositTransactions", "maximumDepositByMonthForTheReportTimePeriod", "minimumDepositByMonthForTheReportTimePeriod", "sumDepositsByMonthForTheReportTimePeriod", "averageDepositByMonthForTheReportTimePeriod", "historicSumOfDeposits", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        historicCountOfDepositTransactions: typing.Union[MetaOapg.properties.historicCountOfDepositTransactions, decimal.Decimal, int, ],
        minimumDepositByMonthForTheReportTimePeriod: typing.Union[MetaOapg.properties.minimumDepositByMonthForTheReportTimePeriod, list, tuple, ],
        countDepositsByMonthForTheReportTimePeriod: typing.Union[MetaOapg.properties.countDepositsByMonthForTheReportTimePeriod, list, tuple, ],
        sumDepositsByMonthForTheReportTimePeriod: typing.Union[MetaOapg.properties.sumDepositsByMonthForTheReportTimePeriod, list, tuple, ],
        maximumDepositByMonthForTheReportTimePeriod: typing.Union[MetaOapg.properties.maximumDepositByMonthForTheReportTimePeriod, list, tuple, ],
        averageDepositByMonthForTheReportTimePeriod: typing.Union[MetaOapg.properties.averageDepositByMonthForTheReportTimePeriod, list, tuple, schemas.Unset] = schemas.unset,
        historicSumOfDeposits: typing.Union[MetaOapg.properties.historicSumOfDeposits, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CashFlowInflowAttributes':
        return super().__new__(
            cls,
            *args,
            historicCountOfDepositTransactions=historicCountOfDepositTransactions,
            minimumDepositByMonthForTheReportTimePeriod=minimumDepositByMonthForTheReportTimePeriod,
            countDepositsByMonthForTheReportTimePeriod=countDepositsByMonthForTheReportTimePeriod,
            sumDepositsByMonthForTheReportTimePeriod=sumDepositsByMonthForTheReportTimePeriod,
            maximumDepositByMonthForTheReportTimePeriod=maximumDepositByMonthForTheReportTimePeriod,
            averageDepositByMonthForTheReportTimePeriod=averageDepositByMonthForTheReportTimePeriod,
            historicSumOfDeposits=historicSumOfDeposits,
            _configuration=_configuration,
            **kwargs,
        )

from mastercard_python_sdk.model.obb_date_range_and_amount import ObbDateRangeAndAmount
from mastercard_python_sdk.model.obb_date_range_and_count import ObbDateRangeAndCount
