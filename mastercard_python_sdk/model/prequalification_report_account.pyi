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


class PrequalificationReportAccount(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            id = schemas.Int64Schema
            number = schemas.StrSchema
            ownerName = schemas.StrSchema
            ownerAddress = schemas.StrSchema
            name = schemas.StrSchema
            type = schemas.StrSchema
            aggregationStatusCode = schemas.Int32Schema
            balance = schemas.NumberSchema
            balanceDate = schemas.Int64Schema
            availableBalance = schemas.NumberSchema
            averageMonthlyBalance = schemas.NumberSchema
            totNumberInsufficientFundsFeeDebitTxAccount = schemas.Int32Schema
            totNumberInsufficientFundsFeeDebitTxOver6MonthsAccount = schemas.Int32Schema
            totNumberDaysSinceMostRecentInsufficientFundsFeeDebitTxAccount = schemas.Int64Schema
            
            
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
            def asset() -> typing.Type['PrequalificationReportAssetSummary']:
                return PrequalificationReportAssetSummary
        
            @staticmethod
            def details() -> typing.Type['AccountDetails']:
                return AccountDetails
            __annotations__ = {
                "id": id,
                "number": number,
                "ownerName": ownerName,
                "ownerAddress": ownerAddress,
                "name": name,
                "type": type,
                "aggregationStatusCode": aggregationStatusCode,
                "balance": balance,
                "balanceDate": balanceDate,
                "availableBalance": availableBalance,
                "averageMonthlyBalance": averageMonthlyBalance,
                "totNumberInsufficientFundsFeeDebitTxAccount": totNumberInsufficientFundsFeeDebitTxAccount,
                "totNumberInsufficientFundsFeeDebitTxOver6MonthsAccount": totNumberInsufficientFundsFeeDebitTxOver6MonthsAccount,
                "totNumberDaysSinceMostRecentInsufficientFundsFeeDebitTxAccount": totNumberDaysSinceMostRecentInsufficientFundsFeeDebitTxAccount,
                "transactions": transactions,
                "asset": asset,
                "details": details,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["number"]) -> MetaOapg.properties.number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ownerName"]) -> MetaOapg.properties.ownerName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ownerAddress"]) -> MetaOapg.properties.ownerAddress: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["aggregationStatusCode"]) -> MetaOapg.properties.aggregationStatusCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["balance"]) -> MetaOapg.properties.balance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["balanceDate"]) -> MetaOapg.properties.balanceDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["availableBalance"]) -> MetaOapg.properties.availableBalance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["averageMonthlyBalance"]) -> MetaOapg.properties.averageMonthlyBalance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totNumberInsufficientFundsFeeDebitTxAccount"]) -> MetaOapg.properties.totNumberInsufficientFundsFeeDebitTxAccount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totNumberInsufficientFundsFeeDebitTxOver6MonthsAccount"]) -> MetaOapg.properties.totNumberInsufficientFundsFeeDebitTxOver6MonthsAccount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totNumberDaysSinceMostRecentInsufficientFundsFeeDebitTxAccount"]) -> MetaOapg.properties.totNumberDaysSinceMostRecentInsufficientFundsFeeDebitTxAccount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transactions"]) -> MetaOapg.properties.transactions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["asset"]) -> 'PrequalificationReportAssetSummary': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["details"]) -> 'AccountDetails': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "number", "ownerName", "ownerAddress", "name", "type", "aggregationStatusCode", "balance", "balanceDate", "availableBalance", "averageMonthlyBalance", "totNumberInsufficientFundsFeeDebitTxAccount", "totNumberInsufficientFundsFeeDebitTxOver6MonthsAccount", "totNumberDaysSinceMostRecentInsufficientFundsFeeDebitTxAccount", "transactions", "asset", "details", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["number"]) -> typing.Union[MetaOapg.properties.number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ownerName"]) -> typing.Union[MetaOapg.properties.ownerName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ownerAddress"]) -> typing.Union[MetaOapg.properties.ownerAddress, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["aggregationStatusCode"]) -> typing.Union[MetaOapg.properties.aggregationStatusCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["balance"]) -> typing.Union[MetaOapg.properties.balance, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["balanceDate"]) -> typing.Union[MetaOapg.properties.balanceDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["availableBalance"]) -> typing.Union[MetaOapg.properties.availableBalance, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["averageMonthlyBalance"]) -> typing.Union[MetaOapg.properties.averageMonthlyBalance, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totNumberInsufficientFundsFeeDebitTxAccount"]) -> typing.Union[MetaOapg.properties.totNumberInsufficientFundsFeeDebitTxAccount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totNumberInsufficientFundsFeeDebitTxOver6MonthsAccount"]) -> typing.Union[MetaOapg.properties.totNumberInsufficientFundsFeeDebitTxOver6MonthsAccount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totNumberDaysSinceMostRecentInsufficientFundsFeeDebitTxAccount"]) -> typing.Union[MetaOapg.properties.totNumberDaysSinceMostRecentInsufficientFundsFeeDebitTxAccount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transactions"]) -> typing.Union[MetaOapg.properties.transactions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["asset"]) -> typing.Union['PrequalificationReportAssetSummary', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["details"]) -> typing.Union['AccountDetails', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "number", "ownerName", "ownerAddress", "name", "type", "aggregationStatusCode", "balance", "balanceDate", "availableBalance", "averageMonthlyBalance", "totNumberInsufficientFundsFeeDebitTxAccount", "totNumberInsufficientFundsFeeDebitTxOver6MonthsAccount", "totNumberDaysSinceMostRecentInsufficientFundsFeeDebitTxAccount", "transactions", "asset", "details", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        number: typing.Union[MetaOapg.properties.number, str, schemas.Unset] = schemas.unset,
        ownerName: typing.Union[MetaOapg.properties.ownerName, str, schemas.Unset] = schemas.unset,
        ownerAddress: typing.Union[MetaOapg.properties.ownerAddress, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        aggregationStatusCode: typing.Union[MetaOapg.properties.aggregationStatusCode, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        balance: typing.Union[MetaOapg.properties.balance, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        balanceDate: typing.Union[MetaOapg.properties.balanceDate, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        availableBalance: typing.Union[MetaOapg.properties.availableBalance, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        averageMonthlyBalance: typing.Union[MetaOapg.properties.averageMonthlyBalance, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        totNumberInsufficientFundsFeeDebitTxAccount: typing.Union[MetaOapg.properties.totNumberInsufficientFundsFeeDebitTxAccount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        totNumberInsufficientFundsFeeDebitTxOver6MonthsAccount: typing.Union[MetaOapg.properties.totNumberInsufficientFundsFeeDebitTxOver6MonthsAccount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        totNumberDaysSinceMostRecentInsufficientFundsFeeDebitTxAccount: typing.Union[MetaOapg.properties.totNumberDaysSinceMostRecentInsufficientFundsFeeDebitTxAccount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        transactions: typing.Union[MetaOapg.properties.transactions, list, tuple, schemas.Unset] = schemas.unset,
        asset: typing.Union['PrequalificationReportAssetSummary', schemas.Unset] = schemas.unset,
        details: typing.Union['AccountDetails', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PrequalificationReportAccount':
        return super().__new__(
            cls,
            *args,
            id=id,
            number=number,
            ownerName=ownerName,
            ownerAddress=ownerAddress,
            name=name,
            type=type,
            aggregationStatusCode=aggregationStatusCode,
            balance=balance,
            balanceDate=balanceDate,
            availableBalance=availableBalance,
            averageMonthlyBalance=averageMonthlyBalance,
            totNumberInsufficientFundsFeeDebitTxAccount=totNumberInsufficientFundsFeeDebitTxAccount,
            totNumberInsufficientFundsFeeDebitTxOver6MonthsAccount=totNumberInsufficientFundsFeeDebitTxOver6MonthsAccount,
            totNumberDaysSinceMostRecentInsufficientFundsFeeDebitTxAccount=totNumberDaysSinceMostRecentInsufficientFundsFeeDebitTxAccount,
            transactions=transactions,
            asset=asset,
            details=details,
            _configuration=_configuration,
            **kwargs,
        )

from mastercard_python_sdk.model.account_details import AccountDetails
from mastercard_python_sdk.model.prequalification_report_asset_summary import PrequalificationReportAssetSummary
from mastercard_python_sdk.model.report_transaction import ReportTransaction