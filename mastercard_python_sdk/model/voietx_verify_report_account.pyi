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


class VOIETXVerifyReportAccount(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "number",
            "aggregationStatusCode",
            "name",
            "id",
            "transactions",
            "type",
        }
        
        class properties:
            id = schemas.Int64Schema
            number = schemas.StrSchema
            name = schemas.StrSchema
            type = schemas.StrSchema
            aggregationStatusCode = schemas.Int32Schema
            
            
            class transactions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ReportTransactionNewTxBased']:
                        return ReportTransactionNewTxBased
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ReportTransactionNewTxBased'], typing.List['ReportTransactionNewTxBased']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'transactions':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ReportTransactionNewTxBased':
                    return super().__getitem__(i)
            ownerName = schemas.StrSchema
            ownerAddress = schemas.StrSchema
            
            
            class incomeStreams(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['VOIETXVerifyReportIncomeStream']:
                        return VOIETXVerifyReportIncomeStream
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['VOIETXVerifyReportIncomeStream'], typing.List['VOIETXVerifyReportIncomeStream']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'incomeStreams':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'VOIETXVerifyReportIncomeStream':
                    return super().__getitem__(i)
            balance = schemas.NumberSchema
            averageMonthlyBalance = schemas.NumberSchema
        
            @staticmethod
            def details() -> typing.Type['AccountDetailsTxBased']:
                return AccountDetailsTxBased
        
            @staticmethod
            def position() -> typing.Type['ReportAccountPosition']:
                return ReportAccountPosition
            availableBalance = schemas.NumberSchema
            __annotations__ = {
                "id": id,
                "number": number,
                "name": name,
                "type": type,
                "aggregationStatusCode": aggregationStatusCode,
                "transactions": transactions,
                "ownerName": ownerName,
                "ownerAddress": ownerAddress,
                "incomeStreams": incomeStreams,
                "balance": balance,
                "averageMonthlyBalance": averageMonthlyBalance,
                "details": details,
                "position": position,
                "availableBalance": availableBalance,
            }
    
    number: MetaOapg.properties.number
    aggregationStatusCode: MetaOapg.properties.aggregationStatusCode
    name: MetaOapg.properties.name
    id: MetaOapg.properties.id
    transactions: MetaOapg.properties.transactions
    type: MetaOapg.properties.type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["number"]) -> MetaOapg.properties.number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["aggregationStatusCode"]) -> MetaOapg.properties.aggregationStatusCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transactions"]) -> MetaOapg.properties.transactions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ownerName"]) -> MetaOapg.properties.ownerName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ownerAddress"]) -> MetaOapg.properties.ownerAddress: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["incomeStreams"]) -> MetaOapg.properties.incomeStreams: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["balance"]) -> MetaOapg.properties.balance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["averageMonthlyBalance"]) -> MetaOapg.properties.averageMonthlyBalance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["details"]) -> 'AccountDetailsTxBased': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["position"]) -> 'ReportAccountPosition': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["availableBalance"]) -> MetaOapg.properties.availableBalance: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "number", "name", "type", "aggregationStatusCode", "transactions", "ownerName", "ownerAddress", "incomeStreams", "balance", "averageMonthlyBalance", "details", "position", "availableBalance", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["number"]) -> MetaOapg.properties.number: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["aggregationStatusCode"]) -> MetaOapg.properties.aggregationStatusCode: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transactions"]) -> MetaOapg.properties.transactions: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ownerName"]) -> typing.Union[MetaOapg.properties.ownerName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ownerAddress"]) -> typing.Union[MetaOapg.properties.ownerAddress, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["incomeStreams"]) -> typing.Union[MetaOapg.properties.incomeStreams, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["balance"]) -> typing.Union[MetaOapg.properties.balance, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["averageMonthlyBalance"]) -> typing.Union[MetaOapg.properties.averageMonthlyBalance, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["details"]) -> typing.Union['AccountDetailsTxBased', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["position"]) -> typing.Union['ReportAccountPosition', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["availableBalance"]) -> typing.Union[MetaOapg.properties.availableBalance, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "number", "name", "type", "aggregationStatusCode", "transactions", "ownerName", "ownerAddress", "incomeStreams", "balance", "averageMonthlyBalance", "details", "position", "availableBalance", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        number: typing.Union[MetaOapg.properties.number, str, ],
        aggregationStatusCode: typing.Union[MetaOapg.properties.aggregationStatusCode, decimal.Decimal, int, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
        transactions: typing.Union[MetaOapg.properties.transactions, list, tuple, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        ownerName: typing.Union[MetaOapg.properties.ownerName, str, schemas.Unset] = schemas.unset,
        ownerAddress: typing.Union[MetaOapg.properties.ownerAddress, str, schemas.Unset] = schemas.unset,
        incomeStreams: typing.Union[MetaOapg.properties.incomeStreams, list, tuple, schemas.Unset] = schemas.unset,
        balance: typing.Union[MetaOapg.properties.balance, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        averageMonthlyBalance: typing.Union[MetaOapg.properties.averageMonthlyBalance, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        details: typing.Union['AccountDetailsTxBased', schemas.Unset] = schemas.unset,
        position: typing.Union['ReportAccountPosition', schemas.Unset] = schemas.unset,
        availableBalance: typing.Union[MetaOapg.properties.availableBalance, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'VOIETXVerifyReportAccount':
        return super().__new__(
            cls,
            *args,
            number=number,
            aggregationStatusCode=aggregationStatusCode,
            name=name,
            id=id,
            transactions=transactions,
            type=type,
            ownerName=ownerName,
            ownerAddress=ownerAddress,
            incomeStreams=incomeStreams,
            balance=balance,
            averageMonthlyBalance=averageMonthlyBalance,
            details=details,
            position=position,
            availableBalance=availableBalance,
            _configuration=_configuration,
            **kwargs,
        )

from mastercard_python_sdk.model.account_details_tx_based import AccountDetailsTxBased
from mastercard_python_sdk.model.report_account_position import ReportAccountPosition
from mastercard_python_sdk.model.report_transaction_new_tx_based import ReportTransactionNewTxBased
from mastercard_python_sdk.model.voietx_verify_report_income_stream import VOIETXVerifyReportIncomeStream