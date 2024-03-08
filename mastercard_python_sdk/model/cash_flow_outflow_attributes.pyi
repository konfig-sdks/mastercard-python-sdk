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


class CashFlowOutflowAttributes(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Outflow attributes
    """


    class MetaOapg:
        required = {
            "countWithdrawalsByMonthForTheReportTimePeriod",
            "minimumWithdrawalByMonthForTheReportTimePeriod",
            "maximumWithdrawalByMonthForTheReportTimePeriod",
            "historicCountOfWithdrawalTransactions",
            "sumWithdrawalsByMonthForTheReportTimePeriod",
        }
        
        class properties:
            
            
            class countWithdrawalsByMonthForTheReportTimePeriod(
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
                ) -> 'countWithdrawalsByMonthForTheReportTimePeriod':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ObbDateRangeAndCount':
                    return super().__getitem__(i)
            historicCountOfWithdrawalTransactions = schemas.IntSchema
            
            
            class maximumWithdrawalByMonthForTheReportTimePeriod(
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
                ) -> 'maximumWithdrawalByMonthForTheReportTimePeriod':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ObbDateRangeAndAmount':
                    return super().__getitem__(i)
            
            
            class minimumWithdrawalByMonthForTheReportTimePeriod(
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
                ) -> 'minimumWithdrawalByMonthForTheReportTimePeriod':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ObbDateRangeAndAmount':
                    return super().__getitem__(i)
            
            
            class sumWithdrawalsByMonthForTheReportTimePeriod(
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
                ) -> 'sumWithdrawalsByMonthForTheReportTimePeriod':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ObbDateRangeAndAmount':
                    return super().__getitem__(i)
            
            
            class averageWithdrawalByMonthForTheReportTimePeriod(
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
                ) -> 'averageWithdrawalByMonthForTheReportTimePeriod':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ObbDateRangeAndAmount':
                    return super().__getitem__(i)
            historicSumOfWithdrawals = schemas.NumberSchema
            __annotations__ = {
                "countWithdrawalsByMonthForTheReportTimePeriod": countWithdrawalsByMonthForTheReportTimePeriod,
                "historicCountOfWithdrawalTransactions": historicCountOfWithdrawalTransactions,
                "maximumWithdrawalByMonthForTheReportTimePeriod": maximumWithdrawalByMonthForTheReportTimePeriod,
                "minimumWithdrawalByMonthForTheReportTimePeriod": minimumWithdrawalByMonthForTheReportTimePeriod,
                "sumWithdrawalsByMonthForTheReportTimePeriod": sumWithdrawalsByMonthForTheReportTimePeriod,
                "averageWithdrawalByMonthForTheReportTimePeriod": averageWithdrawalByMonthForTheReportTimePeriod,
                "historicSumOfWithdrawals": historicSumOfWithdrawals,
            }
    
    countWithdrawalsByMonthForTheReportTimePeriod: MetaOapg.properties.countWithdrawalsByMonthForTheReportTimePeriod
    minimumWithdrawalByMonthForTheReportTimePeriod: MetaOapg.properties.minimumWithdrawalByMonthForTheReportTimePeriod
    maximumWithdrawalByMonthForTheReportTimePeriod: MetaOapg.properties.maximumWithdrawalByMonthForTheReportTimePeriod
    historicCountOfWithdrawalTransactions: MetaOapg.properties.historicCountOfWithdrawalTransactions
    sumWithdrawalsByMonthForTheReportTimePeriod: MetaOapg.properties.sumWithdrawalsByMonthForTheReportTimePeriod
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["countWithdrawalsByMonthForTheReportTimePeriod"]) -> MetaOapg.properties.countWithdrawalsByMonthForTheReportTimePeriod: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["historicCountOfWithdrawalTransactions"]) -> MetaOapg.properties.historicCountOfWithdrawalTransactions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maximumWithdrawalByMonthForTheReportTimePeriod"]) -> MetaOapg.properties.maximumWithdrawalByMonthForTheReportTimePeriod: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["minimumWithdrawalByMonthForTheReportTimePeriod"]) -> MetaOapg.properties.minimumWithdrawalByMonthForTheReportTimePeriod: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sumWithdrawalsByMonthForTheReportTimePeriod"]) -> MetaOapg.properties.sumWithdrawalsByMonthForTheReportTimePeriod: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["averageWithdrawalByMonthForTheReportTimePeriod"]) -> MetaOapg.properties.averageWithdrawalByMonthForTheReportTimePeriod: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["historicSumOfWithdrawals"]) -> MetaOapg.properties.historicSumOfWithdrawals: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["countWithdrawalsByMonthForTheReportTimePeriod", "historicCountOfWithdrawalTransactions", "maximumWithdrawalByMonthForTheReportTimePeriod", "minimumWithdrawalByMonthForTheReportTimePeriod", "sumWithdrawalsByMonthForTheReportTimePeriod", "averageWithdrawalByMonthForTheReportTimePeriod", "historicSumOfWithdrawals", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["countWithdrawalsByMonthForTheReportTimePeriod"]) -> MetaOapg.properties.countWithdrawalsByMonthForTheReportTimePeriod: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["historicCountOfWithdrawalTransactions"]) -> MetaOapg.properties.historicCountOfWithdrawalTransactions: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maximumWithdrawalByMonthForTheReportTimePeriod"]) -> MetaOapg.properties.maximumWithdrawalByMonthForTheReportTimePeriod: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["minimumWithdrawalByMonthForTheReportTimePeriod"]) -> MetaOapg.properties.minimumWithdrawalByMonthForTheReportTimePeriod: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sumWithdrawalsByMonthForTheReportTimePeriod"]) -> MetaOapg.properties.sumWithdrawalsByMonthForTheReportTimePeriod: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["averageWithdrawalByMonthForTheReportTimePeriod"]) -> typing.Union[MetaOapg.properties.averageWithdrawalByMonthForTheReportTimePeriod, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["historicSumOfWithdrawals"]) -> typing.Union[MetaOapg.properties.historicSumOfWithdrawals, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["countWithdrawalsByMonthForTheReportTimePeriod", "historicCountOfWithdrawalTransactions", "maximumWithdrawalByMonthForTheReportTimePeriod", "minimumWithdrawalByMonthForTheReportTimePeriod", "sumWithdrawalsByMonthForTheReportTimePeriod", "averageWithdrawalByMonthForTheReportTimePeriod", "historicSumOfWithdrawals", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        countWithdrawalsByMonthForTheReportTimePeriod: typing.Union[MetaOapg.properties.countWithdrawalsByMonthForTheReportTimePeriod, list, tuple, ],
        minimumWithdrawalByMonthForTheReportTimePeriod: typing.Union[MetaOapg.properties.minimumWithdrawalByMonthForTheReportTimePeriod, list, tuple, ],
        maximumWithdrawalByMonthForTheReportTimePeriod: typing.Union[MetaOapg.properties.maximumWithdrawalByMonthForTheReportTimePeriod, list, tuple, ],
        historicCountOfWithdrawalTransactions: typing.Union[MetaOapg.properties.historicCountOfWithdrawalTransactions, decimal.Decimal, int, ],
        sumWithdrawalsByMonthForTheReportTimePeriod: typing.Union[MetaOapg.properties.sumWithdrawalsByMonthForTheReportTimePeriod, list, tuple, ],
        averageWithdrawalByMonthForTheReportTimePeriod: typing.Union[MetaOapg.properties.averageWithdrawalByMonthForTheReportTimePeriod, list, tuple, schemas.Unset] = schemas.unset,
        historicSumOfWithdrawals: typing.Union[MetaOapg.properties.historicSumOfWithdrawals, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CashFlowOutflowAttributes':
        return super().__new__(
            cls,
            *args,
            countWithdrawalsByMonthForTheReportTimePeriod=countWithdrawalsByMonthForTheReportTimePeriod,
            minimumWithdrawalByMonthForTheReportTimePeriod=minimumWithdrawalByMonthForTheReportTimePeriod,
            maximumWithdrawalByMonthForTheReportTimePeriod=maximumWithdrawalByMonthForTheReportTimePeriod,
            historicCountOfWithdrawalTransactions=historicCountOfWithdrawalTransactions,
            sumWithdrawalsByMonthForTheReportTimePeriod=sumWithdrawalsByMonthForTheReportTimePeriod,
            averageWithdrawalByMonthForTheReportTimePeriod=averageWithdrawalByMonthForTheReportTimePeriod,
            historicSumOfWithdrawals=historicSumOfWithdrawals,
            _configuration=_configuration,
            **kwargs,
        )

from mastercard_python_sdk.model.obb_date_range_and_amount import ObbDateRangeAndAmount
from mastercard_python_sdk.model.obb_date_range_and_count import ObbDateRangeAndCount
