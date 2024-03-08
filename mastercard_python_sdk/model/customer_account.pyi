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


class CustomerAccount(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    An account represents a bank account such as a checking or savings that the customer has added via the Connect interface.
    """


    class MetaOapg:
        required = {
            "number",
            "createdDate",
            "institutionId",
            "institutionLoginId",
            "customerId",
            "name",
            "accountNickname",
            "accountNumberDisplay",
            "currency",
            "id",
            "type",
            "status",
        }
        
        class properties:
            id = schemas.StrSchema
            number = schemas.StrSchema
            accountNumberDisplay = schemas.StrSchema
            name = schemas.StrSchema
            type = schemas.StrSchema
            status = schemas.StrSchema
            customerId = schemas.StrSchema
            institutionId = schemas.StrSchema
            createdDate = schemas.Int64Schema
            currency = schemas.StrSchema
            institutionLoginId = schemas.Int64Schema
            realAccountNumberLast4 = schemas.StrSchema
            balance = schemas.NumberSchema
            aggregationStatusCode = schemas.IntSchema
            balanceDate = schemas.Int64Schema
            aggregationSuccessDate = schemas.Int64Schema
            aggregationAttemptDate = schemas.Int64Schema
            lastUpdatedDate = schemas.Int64Schema
            marketSegment = schemas.StrSchema
            lastTransactionDate = schemas.Int64Schema
            oldestTransactionDate = schemas.Int64Schema
        
            @staticmethod
            def detail() -> typing.Type['CustomerAccountDetail']:
                return CustomerAccountDetail
            
            
            class position(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['CustomerAccountPosition']:
                        return CustomerAccountPosition
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['CustomerAccountPosition'], typing.List['CustomerAccountPosition']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'position':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'CustomerAccountPosition':
                    return super().__getitem__(i)
            displayPosition = schemas.Int32Schema
            parentAccount = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "number": number,
                "accountNumberDisplay": accountNumberDisplay,
                "name": name,
                "type": type,
                "status": status,
                "customerId": customerId,
                "institutionId": institutionId,
                "createdDate": createdDate,
                "currency": currency,
                "institutionLoginId": institutionLoginId,
                "realAccountNumberLast4": realAccountNumberLast4,
                "balance": balance,
                "aggregationStatusCode": aggregationStatusCode,
                "balanceDate": balanceDate,
                "aggregationSuccessDate": aggregationSuccessDate,
                "aggregationAttemptDate": aggregationAttemptDate,
                "lastUpdatedDate": lastUpdatedDate,
                "marketSegment": marketSegment,
                "lastTransactionDate": lastTransactionDate,
                "oldestTransactionDate": oldestTransactionDate,
                "detail": detail,
                "position": position,
                "displayPosition": displayPosition,
                "parentAccount": parentAccount,
            }
    
    number: MetaOapg.properties.number
    createdDate: MetaOapg.properties.createdDate
    institutionId: MetaOapg.properties.institutionId
    institutionLoginId: MetaOapg.properties.institutionLoginId
    customerId: MetaOapg.properties.customerId
    name: MetaOapg.properties.name
    accountNickname: schemas.AnyTypeSchema
    accountNumberDisplay: MetaOapg.properties.accountNumberDisplay
    currency: MetaOapg.properties.currency
    id: MetaOapg.properties.id
    type: MetaOapg.properties.type
    status: MetaOapg.properties.status
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["number"]) -> MetaOapg.properties.number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accountNumberDisplay"]) -> MetaOapg.properties.accountNumberDisplay: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customerId"]) -> MetaOapg.properties.customerId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["institutionId"]) -> MetaOapg.properties.institutionId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createdDate"]) -> MetaOapg.properties.createdDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["institutionLoginId"]) -> MetaOapg.properties.institutionLoginId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["realAccountNumberLast4"]) -> MetaOapg.properties.realAccountNumberLast4: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["balance"]) -> MetaOapg.properties.balance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["aggregationStatusCode"]) -> MetaOapg.properties.aggregationStatusCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["balanceDate"]) -> MetaOapg.properties.balanceDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["aggregationSuccessDate"]) -> MetaOapg.properties.aggregationSuccessDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["aggregationAttemptDate"]) -> MetaOapg.properties.aggregationAttemptDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastUpdatedDate"]) -> MetaOapg.properties.lastUpdatedDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["marketSegment"]) -> MetaOapg.properties.marketSegment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastTransactionDate"]) -> MetaOapg.properties.lastTransactionDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["oldestTransactionDate"]) -> MetaOapg.properties.oldestTransactionDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["detail"]) -> 'CustomerAccountDetail': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["position"]) -> MetaOapg.properties.position: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["displayPosition"]) -> MetaOapg.properties.displayPosition: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parentAccount"]) -> MetaOapg.properties.parentAccount: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "number", "accountNumberDisplay", "name", "type", "status", "customerId", "institutionId", "createdDate", "currency", "institutionLoginId", "realAccountNumberLast4", "balance", "aggregationStatusCode", "balanceDate", "aggregationSuccessDate", "aggregationAttemptDate", "lastUpdatedDate", "marketSegment", "lastTransactionDate", "oldestTransactionDate", "detail", "position", "displayPosition", "parentAccount", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["number"]) -> MetaOapg.properties.number: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountNumberDisplay"]) -> MetaOapg.properties.accountNumberDisplay: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customerId"]) -> MetaOapg.properties.customerId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["institutionId"]) -> MetaOapg.properties.institutionId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createdDate"]) -> MetaOapg.properties.createdDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["institutionLoginId"]) -> MetaOapg.properties.institutionLoginId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["realAccountNumberLast4"]) -> typing.Union[MetaOapg.properties.realAccountNumberLast4, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["balance"]) -> typing.Union[MetaOapg.properties.balance, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["aggregationStatusCode"]) -> typing.Union[MetaOapg.properties.aggregationStatusCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["balanceDate"]) -> typing.Union[MetaOapg.properties.balanceDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["aggregationSuccessDate"]) -> typing.Union[MetaOapg.properties.aggregationSuccessDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["aggregationAttemptDate"]) -> typing.Union[MetaOapg.properties.aggregationAttemptDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastUpdatedDate"]) -> typing.Union[MetaOapg.properties.lastUpdatedDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["marketSegment"]) -> typing.Union[MetaOapg.properties.marketSegment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastTransactionDate"]) -> typing.Union[MetaOapg.properties.lastTransactionDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["oldestTransactionDate"]) -> typing.Union[MetaOapg.properties.oldestTransactionDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["detail"]) -> typing.Union['CustomerAccountDetail', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["position"]) -> typing.Union[MetaOapg.properties.position, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["displayPosition"]) -> typing.Union[MetaOapg.properties.displayPosition, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parentAccount"]) -> typing.Union[MetaOapg.properties.parentAccount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "number", "accountNumberDisplay", "name", "type", "status", "customerId", "institutionId", "createdDate", "currency", "institutionLoginId", "realAccountNumberLast4", "balance", "aggregationStatusCode", "balanceDate", "aggregationSuccessDate", "aggregationAttemptDate", "lastUpdatedDate", "marketSegment", "lastTransactionDate", "oldestTransactionDate", "detail", "position", "displayPosition", "parentAccount", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        number: typing.Union[MetaOapg.properties.number, str, ],
        createdDate: typing.Union[MetaOapg.properties.createdDate, decimal.Decimal, int, ],
        institutionId: typing.Union[MetaOapg.properties.institutionId, str, ],
        institutionLoginId: typing.Union[MetaOapg.properties.institutionLoginId, decimal.Decimal, int, ],
        customerId: typing.Union[MetaOapg.properties.customerId, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        accountNickname: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        accountNumberDisplay: typing.Union[MetaOapg.properties.accountNumberDisplay, str, ],
        currency: typing.Union[MetaOapg.properties.currency, str, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        status: typing.Union[MetaOapg.properties.status, str, ],
        realAccountNumberLast4: typing.Union[MetaOapg.properties.realAccountNumberLast4, str, schemas.Unset] = schemas.unset,
        balance: typing.Union[MetaOapg.properties.balance, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        aggregationStatusCode: typing.Union[MetaOapg.properties.aggregationStatusCode, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        balanceDate: typing.Union[MetaOapg.properties.balanceDate, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        aggregationSuccessDate: typing.Union[MetaOapg.properties.aggregationSuccessDate, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        aggregationAttemptDate: typing.Union[MetaOapg.properties.aggregationAttemptDate, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        lastUpdatedDate: typing.Union[MetaOapg.properties.lastUpdatedDate, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        marketSegment: typing.Union[MetaOapg.properties.marketSegment, str, schemas.Unset] = schemas.unset,
        lastTransactionDate: typing.Union[MetaOapg.properties.lastTransactionDate, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        oldestTransactionDate: typing.Union[MetaOapg.properties.oldestTransactionDate, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        detail: typing.Union['CustomerAccountDetail', schemas.Unset] = schemas.unset,
        position: typing.Union[MetaOapg.properties.position, list, tuple, schemas.Unset] = schemas.unset,
        displayPosition: typing.Union[MetaOapg.properties.displayPosition, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        parentAccount: typing.Union[MetaOapg.properties.parentAccount, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CustomerAccount':
        return super().__new__(
            cls,
            *args,
            number=number,
            createdDate=createdDate,
            institutionId=institutionId,
            institutionLoginId=institutionLoginId,
            customerId=customerId,
            name=name,
            accountNickname=accountNickname,
            accountNumberDisplay=accountNumberDisplay,
            currency=currency,
            id=id,
            type=type,
            status=status,
            realAccountNumberLast4=realAccountNumberLast4,
            balance=balance,
            aggregationStatusCode=aggregationStatusCode,
            balanceDate=balanceDate,
            aggregationSuccessDate=aggregationSuccessDate,
            aggregationAttemptDate=aggregationAttemptDate,
            lastUpdatedDate=lastUpdatedDate,
            marketSegment=marketSegment,
            lastTransactionDate=lastTransactionDate,
            oldestTransactionDate=oldestTransactionDate,
            detail=detail,
            position=position,
            displayPosition=displayPosition,
            parentAccount=parentAccount,
            _configuration=_configuration,
            **kwargs,
        )

from mastercard_python_sdk.model.customer_account_detail import CustomerAccountDetail
from mastercard_python_sdk.model.customer_account_position import CustomerAccountPosition