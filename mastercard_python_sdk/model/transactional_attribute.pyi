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


class TransactionalAttribute(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    An attribute which represents some categorization/classification of
transactions. Enumerates those identified transactions and reports
aggregations of them over the requested time interval(s).
    """


    class MetaOapg:
        required = {
            "transactionIds",
            "aggregatedByTimePeriods",
            "streamIds",
            "attributeName",
        }
        
        class properties:
            
            
            class aggregatedByTimePeriods(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['TransactionalTimeInterval']:
                        return TransactionalTimeInterval
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['TransactionalTimeInterval'], typing.List['TransactionalTimeInterval']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'aggregatedByTimePeriods':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'TransactionalTimeInterval':
                    return super().__getitem__(i)
            attributeName = schemas.StrSchema
        
            @staticmethod
            def streamIds() -> typing.Type['TransactionalAttributeStreamIds']:
                return TransactionalAttributeStreamIds
        
            @staticmethod
            def transactionIds() -> typing.Type['TransactionalAttributeTransactionIds']:
                return TransactionalAttributeTransactionIds
            __annotations__ = {
                "aggregatedByTimePeriods": aggregatedByTimePeriods,
                "attributeName": attributeName,
                "streamIds": streamIds,
                "transactionIds": transactionIds,
            }
    
    transactionIds: 'TransactionalAttributeTransactionIds'
    aggregatedByTimePeriods: MetaOapg.properties.aggregatedByTimePeriods
    streamIds: 'TransactionalAttributeStreamIds'
    attributeName: MetaOapg.properties.attributeName
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["aggregatedByTimePeriods"]) -> MetaOapg.properties.aggregatedByTimePeriods: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attributeName"]) -> MetaOapg.properties.attributeName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["streamIds"]) -> 'TransactionalAttributeStreamIds': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transactionIds"]) -> 'TransactionalAttributeTransactionIds': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["aggregatedByTimePeriods", "attributeName", "streamIds", "transactionIds", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["aggregatedByTimePeriods"]) -> MetaOapg.properties.aggregatedByTimePeriods: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attributeName"]) -> MetaOapg.properties.attributeName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["streamIds"]) -> 'TransactionalAttributeStreamIds': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transactionIds"]) -> 'TransactionalAttributeTransactionIds': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["aggregatedByTimePeriods", "attributeName", "streamIds", "transactionIds", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        transactionIds: 'TransactionalAttributeTransactionIds',
        aggregatedByTimePeriods: typing.Union[MetaOapg.properties.aggregatedByTimePeriods, list, tuple, ],
        streamIds: 'TransactionalAttributeStreamIds',
        attributeName: typing.Union[MetaOapg.properties.attributeName, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TransactionalAttribute':
        return super().__new__(
            cls,
            *args,
            transactionIds=transactionIds,
            aggregatedByTimePeriods=aggregatedByTimePeriods,
            streamIds=streamIds,
            attributeName=attributeName,
            _configuration=_configuration,
            **kwargs,
        )

from mastercard_python_sdk.model.transactional_attribute_stream_ids import TransactionalAttributeStreamIds
from mastercard_python_sdk.model.transactional_attribute_transaction_ids import TransactionalAttributeTransactionIds
from mastercard_python_sdk.model.transactional_time_interval import TransactionalTimeInterval