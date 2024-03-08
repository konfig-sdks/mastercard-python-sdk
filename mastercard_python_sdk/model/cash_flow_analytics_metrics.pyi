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


class CashFlowAnalyticsMetrics(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Cash flow analytics metrics and calculations
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def inflow() -> typing.Type['CashFlowInflowAttributes']:
                return CashFlowInflowAttributes
        
            @staticmethod
            def negativeTriggers() -> typing.Type['CashFlowNegativeTriggers']:
                return CashFlowNegativeTriggers
        
            @staticmethod
            def outflow() -> typing.Type['CashFlowOutflowAttributes']:
                return CashFlowOutflowAttributes
            
            
            class revenueByMonthForTheReportTimePeriod(
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
                ) -> 'revenueByMonthForTheReportTimePeriod':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ObbDateRangeAndAmount':
                    return super().__getitem__(i)
            revenueForTheReportTimePeriod = schemas.NumberSchema
        
            @staticmethod
            def transactionAnalytics() -> typing.Type['CashFlowTransactionAnalyticsAttributes']:
                return CashFlowTransactionAnalyticsAttributes
            __annotations__ = {
                "inflow": inflow,
                "negativeTriggers": negativeTriggers,
                "outflow": outflow,
                "revenueByMonthForTheReportTimePeriod": revenueByMonthForTheReportTimePeriod,
                "revenueForTheReportTimePeriod": revenueForTheReportTimePeriod,
                "transactionAnalytics": transactionAnalytics,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["inflow"]) -> 'CashFlowInflowAttributes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["negativeTriggers"]) -> 'CashFlowNegativeTriggers': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["outflow"]) -> 'CashFlowOutflowAttributes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["revenueByMonthForTheReportTimePeriod"]) -> MetaOapg.properties.revenueByMonthForTheReportTimePeriod: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["revenueForTheReportTimePeriod"]) -> MetaOapg.properties.revenueForTheReportTimePeriod: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transactionAnalytics"]) -> 'CashFlowTransactionAnalyticsAttributes': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["inflow", "negativeTriggers", "outflow", "revenueByMonthForTheReportTimePeriod", "revenueForTheReportTimePeriod", "transactionAnalytics", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["inflow"]) -> typing.Union['CashFlowInflowAttributes', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["negativeTriggers"]) -> typing.Union['CashFlowNegativeTriggers', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["outflow"]) -> typing.Union['CashFlowOutflowAttributes', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["revenueByMonthForTheReportTimePeriod"]) -> typing.Union[MetaOapg.properties.revenueByMonthForTheReportTimePeriod, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["revenueForTheReportTimePeriod"]) -> typing.Union[MetaOapg.properties.revenueForTheReportTimePeriod, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transactionAnalytics"]) -> typing.Union['CashFlowTransactionAnalyticsAttributes', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["inflow", "negativeTriggers", "outflow", "revenueByMonthForTheReportTimePeriod", "revenueForTheReportTimePeriod", "transactionAnalytics", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        inflow: typing.Union['CashFlowInflowAttributes', schemas.Unset] = schemas.unset,
        negativeTriggers: typing.Union['CashFlowNegativeTriggers', schemas.Unset] = schemas.unset,
        outflow: typing.Union['CashFlowOutflowAttributes', schemas.Unset] = schemas.unset,
        revenueByMonthForTheReportTimePeriod: typing.Union[MetaOapg.properties.revenueByMonthForTheReportTimePeriod, list, tuple, schemas.Unset] = schemas.unset,
        revenueForTheReportTimePeriod: typing.Union[MetaOapg.properties.revenueForTheReportTimePeriod, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        transactionAnalytics: typing.Union['CashFlowTransactionAnalyticsAttributes', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CashFlowAnalyticsMetrics':
        return super().__new__(
            cls,
            *args,
            inflow=inflow,
            negativeTriggers=negativeTriggers,
            outflow=outflow,
            revenueByMonthForTheReportTimePeriod=revenueByMonthForTheReportTimePeriod,
            revenueForTheReportTimePeriod=revenueForTheReportTimePeriod,
            transactionAnalytics=transactionAnalytics,
            _configuration=_configuration,
            **kwargs,
        )

from mastercard_python_sdk.model.cash_flow_inflow_attributes import CashFlowInflowAttributes
from mastercard_python_sdk.model.cash_flow_negative_triggers import CashFlowNegativeTriggers
from mastercard_python_sdk.model.cash_flow_outflow_attributes import CashFlowOutflowAttributes
from mastercard_python_sdk.model.cash_flow_transaction_analytics_attributes import CashFlowTransactionAnalyticsAttributes
from mastercard_python_sdk.model.obb_date_range_and_amount import ObbDateRangeAndAmount
