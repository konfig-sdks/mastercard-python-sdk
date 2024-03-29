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


class CashFlowTransactionAnalyticsAttributes(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Transaction Analytics Attributes
    """


    class MetaOapg:
        required = {
            "activityWithdrawalsDebitsForTheReportTimePeriod",
            "activityDepositsCreditsForTheReportTimePeriod",
            "averageTransactionValueByMonthForTheReportTimePeriod",
        }
        
        class properties:
            
            
            class activityDepositsCreditsForTheReportTimePeriod(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['CashFlowActivityDepositsCredits']:
                        return CashFlowActivityDepositsCredits
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['CashFlowActivityDepositsCredits'], typing.List['CashFlowActivityDepositsCredits']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'activityDepositsCreditsForTheReportTimePeriod':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'CashFlowActivityDepositsCredits':
                    return super().__getitem__(i)
            
            
            class activityWithdrawalsDebitsForTheReportTimePeriod(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['CashFlowActivityWithdrawalsDebits']:
                        return CashFlowActivityWithdrawalsDebits
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['CashFlowActivityWithdrawalsDebits'], typing.List['CashFlowActivityWithdrawalsDebits']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'activityWithdrawalsDebitsForTheReportTimePeriod':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'CashFlowActivityWithdrawalsDebits':
                    return super().__getitem__(i)
            
            
            class averageTransactionValueByMonthForTheReportTimePeriod(
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
                ) -> 'averageTransactionValueByMonthForTheReportTimePeriod':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ObbDateRangeAndAmount':
                    return super().__getitem__(i)
        
            @staticmethod
            def historicWeeksWithZeroTransactions() -> typing.Type['CashFlowNumWeeksZeros']:
                return CashFlowNumWeeksZeros
        
            @staticmethod
            def lastTransactionDate() -> typing.Type['CashFlowTransactionAnalyticsAttributesLastTransactionDate']:
                return CashFlowTransactionAnalyticsAttributesLastTransactionDate
            
            
            class netCashFlowByMonthForTheReportTimePeriod(
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
                ) -> 'netCashFlowByMonthForTheReportTimePeriod':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ObbDateRangeAndAmount':
                    return super().__getitem__(i)
            netCashFlowForTheReportTimePeriod = schemas.NumberSchema
            __annotations__ = {
                "activityDepositsCreditsForTheReportTimePeriod": activityDepositsCreditsForTheReportTimePeriod,
                "activityWithdrawalsDebitsForTheReportTimePeriod": activityWithdrawalsDebitsForTheReportTimePeriod,
                "averageTransactionValueByMonthForTheReportTimePeriod": averageTransactionValueByMonthForTheReportTimePeriod,
                "historicWeeksWithZeroTransactions": historicWeeksWithZeroTransactions,
                "lastTransactionDate": lastTransactionDate,
                "netCashFlowByMonthForTheReportTimePeriod": netCashFlowByMonthForTheReportTimePeriod,
                "netCashFlowForTheReportTimePeriod": netCashFlowForTheReportTimePeriod,
            }
    
    activityWithdrawalsDebitsForTheReportTimePeriod: MetaOapg.properties.activityWithdrawalsDebitsForTheReportTimePeriod
    activityDepositsCreditsForTheReportTimePeriod: MetaOapg.properties.activityDepositsCreditsForTheReportTimePeriod
    averageTransactionValueByMonthForTheReportTimePeriod: MetaOapg.properties.averageTransactionValueByMonthForTheReportTimePeriod
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["activityDepositsCreditsForTheReportTimePeriod"]) -> MetaOapg.properties.activityDepositsCreditsForTheReportTimePeriod: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["activityWithdrawalsDebitsForTheReportTimePeriod"]) -> MetaOapg.properties.activityWithdrawalsDebitsForTheReportTimePeriod: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["averageTransactionValueByMonthForTheReportTimePeriod"]) -> MetaOapg.properties.averageTransactionValueByMonthForTheReportTimePeriod: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["historicWeeksWithZeroTransactions"]) -> 'CashFlowNumWeeksZeros': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastTransactionDate"]) -> 'CashFlowTransactionAnalyticsAttributesLastTransactionDate': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["netCashFlowByMonthForTheReportTimePeriod"]) -> MetaOapg.properties.netCashFlowByMonthForTheReportTimePeriod: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["netCashFlowForTheReportTimePeriod"]) -> MetaOapg.properties.netCashFlowForTheReportTimePeriod: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["activityDepositsCreditsForTheReportTimePeriod", "activityWithdrawalsDebitsForTheReportTimePeriod", "averageTransactionValueByMonthForTheReportTimePeriod", "historicWeeksWithZeroTransactions", "lastTransactionDate", "netCashFlowByMonthForTheReportTimePeriod", "netCashFlowForTheReportTimePeriod", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["activityDepositsCreditsForTheReportTimePeriod"]) -> MetaOapg.properties.activityDepositsCreditsForTheReportTimePeriod: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["activityWithdrawalsDebitsForTheReportTimePeriod"]) -> MetaOapg.properties.activityWithdrawalsDebitsForTheReportTimePeriod: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["averageTransactionValueByMonthForTheReportTimePeriod"]) -> MetaOapg.properties.averageTransactionValueByMonthForTheReportTimePeriod: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["historicWeeksWithZeroTransactions"]) -> typing.Union['CashFlowNumWeeksZeros', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastTransactionDate"]) -> typing.Union['CashFlowTransactionAnalyticsAttributesLastTransactionDate', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["netCashFlowByMonthForTheReportTimePeriod"]) -> typing.Union[MetaOapg.properties.netCashFlowByMonthForTheReportTimePeriod, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["netCashFlowForTheReportTimePeriod"]) -> typing.Union[MetaOapg.properties.netCashFlowForTheReportTimePeriod, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["activityDepositsCreditsForTheReportTimePeriod", "activityWithdrawalsDebitsForTheReportTimePeriod", "averageTransactionValueByMonthForTheReportTimePeriod", "historicWeeksWithZeroTransactions", "lastTransactionDate", "netCashFlowByMonthForTheReportTimePeriod", "netCashFlowForTheReportTimePeriod", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        activityWithdrawalsDebitsForTheReportTimePeriod: typing.Union[MetaOapg.properties.activityWithdrawalsDebitsForTheReportTimePeriod, list, tuple, ],
        activityDepositsCreditsForTheReportTimePeriod: typing.Union[MetaOapg.properties.activityDepositsCreditsForTheReportTimePeriod, list, tuple, ],
        averageTransactionValueByMonthForTheReportTimePeriod: typing.Union[MetaOapg.properties.averageTransactionValueByMonthForTheReportTimePeriod, list, tuple, ],
        historicWeeksWithZeroTransactions: typing.Union['CashFlowNumWeeksZeros', schemas.Unset] = schemas.unset,
        lastTransactionDate: typing.Union['CashFlowTransactionAnalyticsAttributesLastTransactionDate', schemas.Unset] = schemas.unset,
        netCashFlowByMonthForTheReportTimePeriod: typing.Union[MetaOapg.properties.netCashFlowByMonthForTheReportTimePeriod, list, tuple, schemas.Unset] = schemas.unset,
        netCashFlowForTheReportTimePeriod: typing.Union[MetaOapg.properties.netCashFlowForTheReportTimePeriod, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CashFlowTransactionAnalyticsAttributes':
        return super().__new__(
            cls,
            *args,
            activityWithdrawalsDebitsForTheReportTimePeriod=activityWithdrawalsDebitsForTheReportTimePeriod,
            activityDepositsCreditsForTheReportTimePeriod=activityDepositsCreditsForTheReportTimePeriod,
            averageTransactionValueByMonthForTheReportTimePeriod=averageTransactionValueByMonthForTheReportTimePeriod,
            historicWeeksWithZeroTransactions=historicWeeksWithZeroTransactions,
            lastTransactionDate=lastTransactionDate,
            netCashFlowByMonthForTheReportTimePeriod=netCashFlowByMonthForTheReportTimePeriod,
            netCashFlowForTheReportTimePeriod=netCashFlowForTheReportTimePeriod,
            _configuration=_configuration,
            **kwargs,
        )

from mastercard_python_sdk.model.cash_flow_activity_deposits_credits import CashFlowActivityDepositsCredits
from mastercard_python_sdk.model.cash_flow_activity_withdrawals_debits import CashFlowActivityWithdrawalsDebits
from mastercard_python_sdk.model.cash_flow_num_weeks_zeros import CashFlowNumWeeksZeros
from mastercard_python_sdk.model.cash_flow_transaction_analytics_attributes_last_transaction_date import CashFlowTransactionAnalyticsAttributesLastTransactionDate
from mastercard_python_sdk.model.obb_date_range_and_amount import ObbDateRangeAndAmount
