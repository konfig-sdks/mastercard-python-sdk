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


class CashFlowAnalyticsAccountResult(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "accountId",
            "currentReportRequest",
            "historicDataAvailability",
            "accountDetails",
        }
        
        class properties:
        
            @staticmethod
            def accountDetails() -> typing.Type['ObbAccountDetails']:
                return ObbAccountDetails
            accountId = schemas.Int64Schema
        
            @staticmethod
            def currentReportRequest() -> typing.Type['ObbCurrentReportRequestDetails']:
                return ObbCurrentReportRequestDetails
        
            @staticmethod
            def historicDataAvailability() -> typing.Type['ObbDataAvailability']:
                return ObbDataAvailability
        
            @staticmethod
            def cashflowAnalyticsMetrics() -> typing.Type['CashFlowAnalyticsMetrics']:
                return CashFlowAnalyticsMetrics
            __annotations__ = {
                "accountDetails": accountDetails,
                "accountId": accountId,
                "currentReportRequest": currentReportRequest,
                "historicDataAvailability": historicDataAvailability,
                "cashflowAnalyticsMetrics": cashflowAnalyticsMetrics,
            }
    
    accountId: MetaOapg.properties.accountId
    currentReportRequest: 'ObbCurrentReportRequestDetails'
    historicDataAvailability: 'ObbDataAvailability'
    accountDetails: 'ObbAccountDetails'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accountDetails"]) -> 'ObbAccountDetails': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accountId"]) -> MetaOapg.properties.accountId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currentReportRequest"]) -> 'ObbCurrentReportRequestDetails': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["historicDataAvailability"]) -> 'ObbDataAvailability': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cashflowAnalyticsMetrics"]) -> 'CashFlowAnalyticsMetrics': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["accountDetails", "accountId", "currentReportRequest", "historicDataAvailability", "cashflowAnalyticsMetrics", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountDetails"]) -> 'ObbAccountDetails': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountId"]) -> MetaOapg.properties.accountId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currentReportRequest"]) -> 'ObbCurrentReportRequestDetails': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["historicDataAvailability"]) -> 'ObbDataAvailability': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cashflowAnalyticsMetrics"]) -> typing.Union['CashFlowAnalyticsMetrics', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["accountDetails", "accountId", "currentReportRequest", "historicDataAvailability", "cashflowAnalyticsMetrics", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        accountId: typing.Union[MetaOapg.properties.accountId, decimal.Decimal, int, ],
        currentReportRequest: 'ObbCurrentReportRequestDetails',
        historicDataAvailability: 'ObbDataAvailability',
        accountDetails: 'ObbAccountDetails',
        cashflowAnalyticsMetrics: typing.Union['CashFlowAnalyticsMetrics', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CashFlowAnalyticsAccountResult':
        return super().__new__(
            cls,
            *args,
            accountId=accountId,
            currentReportRequest=currentReportRequest,
            historicDataAvailability=historicDataAvailability,
            accountDetails=accountDetails,
            cashflowAnalyticsMetrics=cashflowAnalyticsMetrics,
            _configuration=_configuration,
            **kwargs,
        )

from mastercard_python_sdk.model.cash_flow_analytics_metrics import CashFlowAnalyticsMetrics
from mastercard_python_sdk.model.obb_account_details import ObbAccountDetails
from mastercard_python_sdk.model.obb_current_report_request_details import ObbCurrentReportRequestDetails
from mastercard_python_sdk.model.obb_data_availability import ObbDataAvailability
