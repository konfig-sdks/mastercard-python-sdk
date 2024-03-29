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


class CashFlowReportAccount(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            id = schemas.IntSchema
            ownerName = schemas.StrSchema
            ownerAddress = schemas.StrSchema
            name = schemas.StrSchema
            number = schemas.StrSchema
            type = schemas.StrSchema
            aggregationStatusCode = schemas.IntSchema
            currentBalance = schemas.NumberSchema
            availableBalance = schemas.NumberSchema
            balanceDate = schemas.Int64Schema
            
            
            class transactions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ReportTransaction']:
                        return ReportTransaction
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ReportTransaction'], typing.List['ReportTransaction']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'transactions':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ReportTransaction':
                    return super().__getitem__(i)
        
            @staticmethod
            def cashFlowBalance() -> typing.Type['CashFlowCashFlowBalance']:
                return CashFlowCashFlowBalance
        
            @staticmethod
            def cashFlowCredit() -> typing.Type['CashFlowCashFlowCredit']:
                return CashFlowCashFlowCredit
        
            @staticmethod
            def cashFlowDebit() -> typing.Type['CashFlowCashFlowDebit']:
                return CashFlowCashFlowDebit
        
            @staticmethod
            def cashFlowCharacteristic() -> typing.Type['CashFlowCashFlowCharacteristic']:
                return CashFlowCashFlowCharacteristic
            __annotations__ = {
                "id": id,
                "ownerName": ownerName,
                "ownerAddress": ownerAddress,
                "name": name,
                "number": number,
                "type": type,
                "aggregationStatusCode": aggregationStatusCode,
                "currentBalance": currentBalance,
                "availableBalance": availableBalance,
                "balanceDate": balanceDate,
                "transactions": transactions,
                "cashFlowBalance": cashFlowBalance,
                "cashFlowCredit": cashFlowCredit,
                "cashFlowDebit": cashFlowDebit,
                "cashFlowCharacteristic": cashFlowCharacteristic,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ownerName"]) -> MetaOapg.properties.ownerName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ownerAddress"]) -> MetaOapg.properties.ownerAddress: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["number"]) -> MetaOapg.properties.number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["aggregationStatusCode"]) -> MetaOapg.properties.aggregationStatusCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currentBalance"]) -> MetaOapg.properties.currentBalance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["availableBalance"]) -> MetaOapg.properties.availableBalance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["balanceDate"]) -> MetaOapg.properties.balanceDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transactions"]) -> MetaOapg.properties.transactions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cashFlowBalance"]) -> 'CashFlowCashFlowBalance': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cashFlowCredit"]) -> 'CashFlowCashFlowCredit': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cashFlowDebit"]) -> 'CashFlowCashFlowDebit': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cashFlowCharacteristic"]) -> 'CashFlowCashFlowCharacteristic': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "ownerName", "ownerAddress", "name", "number", "type", "aggregationStatusCode", "currentBalance", "availableBalance", "balanceDate", "transactions", "cashFlowBalance", "cashFlowCredit", "cashFlowDebit", "cashFlowCharacteristic", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ownerName"]) -> typing.Union[MetaOapg.properties.ownerName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ownerAddress"]) -> typing.Union[MetaOapg.properties.ownerAddress, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["number"]) -> typing.Union[MetaOapg.properties.number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["aggregationStatusCode"]) -> typing.Union[MetaOapg.properties.aggregationStatusCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currentBalance"]) -> typing.Union[MetaOapg.properties.currentBalance, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["availableBalance"]) -> typing.Union[MetaOapg.properties.availableBalance, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["balanceDate"]) -> typing.Union[MetaOapg.properties.balanceDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transactions"]) -> typing.Union[MetaOapg.properties.transactions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cashFlowBalance"]) -> typing.Union['CashFlowCashFlowBalance', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cashFlowCredit"]) -> typing.Union['CashFlowCashFlowCredit', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cashFlowDebit"]) -> typing.Union['CashFlowCashFlowDebit', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cashFlowCharacteristic"]) -> typing.Union['CashFlowCashFlowCharacteristic', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "ownerName", "ownerAddress", "name", "number", "type", "aggregationStatusCode", "currentBalance", "availableBalance", "balanceDate", "transactions", "cashFlowBalance", "cashFlowCredit", "cashFlowDebit", "cashFlowCharacteristic", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        ownerName: typing.Union[MetaOapg.properties.ownerName, str, schemas.Unset] = schemas.unset,
        ownerAddress: typing.Union[MetaOapg.properties.ownerAddress, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        number: typing.Union[MetaOapg.properties.number, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        aggregationStatusCode: typing.Union[MetaOapg.properties.aggregationStatusCode, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        currentBalance: typing.Union[MetaOapg.properties.currentBalance, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        availableBalance: typing.Union[MetaOapg.properties.availableBalance, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        balanceDate: typing.Union[MetaOapg.properties.balanceDate, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        transactions: typing.Union[MetaOapg.properties.transactions, list, tuple, schemas.Unset] = schemas.unset,
        cashFlowBalance: typing.Union['CashFlowCashFlowBalance', schemas.Unset] = schemas.unset,
        cashFlowCredit: typing.Union['CashFlowCashFlowCredit', schemas.Unset] = schemas.unset,
        cashFlowDebit: typing.Union['CashFlowCashFlowDebit', schemas.Unset] = schemas.unset,
        cashFlowCharacteristic: typing.Union['CashFlowCashFlowCharacteristic', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CashFlowReportAccount':
        return super().__new__(
            cls,
            *args,
            id=id,
            ownerName=ownerName,
            ownerAddress=ownerAddress,
            name=name,
            number=number,
            type=type,
            aggregationStatusCode=aggregationStatusCode,
            currentBalance=currentBalance,
            availableBalance=availableBalance,
            balanceDate=balanceDate,
            transactions=transactions,
            cashFlowBalance=cashFlowBalance,
            cashFlowCredit=cashFlowCredit,
            cashFlowDebit=cashFlowDebit,
            cashFlowCharacteristic=cashFlowCharacteristic,
            _configuration=_configuration,
            **kwargs,
        )

from mastercard_python_sdk.model.cash_flow_cash_flow_balance import CashFlowCashFlowBalance
from mastercard_python_sdk.model.cash_flow_cash_flow_characteristic import CashFlowCashFlowCharacteristic
from mastercard_python_sdk.model.cash_flow_cash_flow_credit import CashFlowCashFlowCredit
from mastercard_python_sdk.model.cash_flow_cash_flow_debit import CashFlowCashFlowDebit
from mastercard_python_sdk.model.report_transaction import ReportTransaction
