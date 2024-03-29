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


class PaymentHistoryAccountSummary(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Account-level summary of transactions
    """


    class MetaOapg:
        required = {
            "beginningBalance",
            "institutionIcon",
            "accountName",
            "endDate",
            "accountType",
            "currentBalance",
            "accountOwner",
            "totalNonSufficientFunds",
            "beginDate",
            "averageMonthlyBalance",
            "daysSinceNonsufficientFunds",
            "accountNumberDisplay",
            "currency",
            "financialInstitution",
            "status",
        }
        
        class properties:
            accountNumberDisplay = schemas.StrSchema
            financialInstitution = schemas.StrSchema
            institutionIcon = schemas.StrSchema
            currency = schemas.StrSchema
            status = schemas.StrSchema
            accountName = schemas.StrSchema
        
            @staticmethod
            def accountOwner() -> typing.Type['PaymentHistoryAccountSummaryAccountOwner']:
                return PaymentHistoryAccountSummaryAccountOwner
            accountType = schemas.StrSchema
            beginningBalance = schemas.NumberSchema
            averageMonthlyBalance = schemas.NumberSchema
            currentBalance = schemas.NumberSchema
            beginDate = schemas.StrSchema
            endDate = schemas.StrSchema
            daysSinceNonsufficientFunds = schemas.IntSchema
            totalNonsufficientFunds = schemas.NumberSchema
            __annotations__ = {
                "accountNumberDisplay": accountNumberDisplay,
                "financialInstitution": financialInstitution,
                "institutionIcon": institutionIcon,
                "currency": currency,
                "status": status,
                "accountName": accountName,
                "accountOwner": accountOwner,
                "accountType": accountType,
                "beginningBalance": beginningBalance,
                "averageMonthlyBalance": averageMonthlyBalance,
                "currentBalance": currentBalance,
                "beginDate": beginDate,
                "endDate": endDate,
                "daysSinceNonsufficientFunds": daysSinceNonsufficientFunds,
                "totalNonsufficientFunds": totalNonsufficientFunds,
            }
    
    beginningBalance: MetaOapg.properties.beginningBalance
    institutionIcon: MetaOapg.properties.institutionIcon
    accountName: MetaOapg.properties.accountName
    endDate: MetaOapg.properties.endDate
    accountType: MetaOapg.properties.accountType
    currentBalance: MetaOapg.properties.currentBalance
    accountOwner: 'PaymentHistoryAccountSummaryAccountOwner'
    totalNonSufficientFunds: schemas.AnyTypeSchema
    beginDate: MetaOapg.properties.beginDate
    averageMonthlyBalance: MetaOapg.properties.averageMonthlyBalance
    daysSinceNonsufficientFunds: MetaOapg.properties.daysSinceNonsufficientFunds
    accountNumberDisplay: MetaOapg.properties.accountNumberDisplay
    currency: MetaOapg.properties.currency
    financialInstitution: MetaOapg.properties.financialInstitution
    status: MetaOapg.properties.status
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accountNumberDisplay"]) -> MetaOapg.properties.accountNumberDisplay: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["financialInstitution"]) -> MetaOapg.properties.financialInstitution: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["institutionIcon"]) -> MetaOapg.properties.institutionIcon: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accountName"]) -> MetaOapg.properties.accountName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accountOwner"]) -> 'PaymentHistoryAccountSummaryAccountOwner': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accountType"]) -> MetaOapg.properties.accountType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["beginningBalance"]) -> MetaOapg.properties.beginningBalance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["averageMonthlyBalance"]) -> MetaOapg.properties.averageMonthlyBalance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currentBalance"]) -> MetaOapg.properties.currentBalance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["beginDate"]) -> MetaOapg.properties.beginDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endDate"]) -> MetaOapg.properties.endDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["daysSinceNonsufficientFunds"]) -> MetaOapg.properties.daysSinceNonsufficientFunds: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalNonsufficientFunds"]) -> MetaOapg.properties.totalNonsufficientFunds: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["accountNumberDisplay", "financialInstitution", "institutionIcon", "currency", "status", "accountName", "accountOwner", "accountType", "beginningBalance", "averageMonthlyBalance", "currentBalance", "beginDate", "endDate", "daysSinceNonsufficientFunds", "totalNonsufficientFunds", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountNumberDisplay"]) -> MetaOapg.properties.accountNumberDisplay: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["financialInstitution"]) -> MetaOapg.properties.financialInstitution: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["institutionIcon"]) -> MetaOapg.properties.institutionIcon: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountName"]) -> MetaOapg.properties.accountName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountOwner"]) -> 'PaymentHistoryAccountSummaryAccountOwner': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountType"]) -> MetaOapg.properties.accountType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["beginningBalance"]) -> MetaOapg.properties.beginningBalance: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["averageMonthlyBalance"]) -> MetaOapg.properties.averageMonthlyBalance: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currentBalance"]) -> MetaOapg.properties.currentBalance: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["beginDate"]) -> MetaOapg.properties.beginDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endDate"]) -> MetaOapg.properties.endDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["daysSinceNonsufficientFunds"]) -> MetaOapg.properties.daysSinceNonsufficientFunds: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalNonsufficientFunds"]) -> typing.Union[MetaOapg.properties.totalNonsufficientFunds, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["accountNumberDisplay", "financialInstitution", "institutionIcon", "currency", "status", "accountName", "accountOwner", "accountType", "beginningBalance", "averageMonthlyBalance", "currentBalance", "beginDate", "endDate", "daysSinceNonsufficientFunds", "totalNonsufficientFunds", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        beginningBalance: typing.Union[MetaOapg.properties.beginningBalance, decimal.Decimal, int, float, ],
        institutionIcon: typing.Union[MetaOapg.properties.institutionIcon, str, ],
        accountName: typing.Union[MetaOapg.properties.accountName, str, ],
        endDate: typing.Union[MetaOapg.properties.endDate, str, ],
        accountType: typing.Union[MetaOapg.properties.accountType, str, ],
        currentBalance: typing.Union[MetaOapg.properties.currentBalance, decimal.Decimal, int, float, ],
        accountOwner: 'PaymentHistoryAccountSummaryAccountOwner',
        totalNonSufficientFunds: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        beginDate: typing.Union[MetaOapg.properties.beginDate, str, ],
        averageMonthlyBalance: typing.Union[MetaOapg.properties.averageMonthlyBalance, decimal.Decimal, int, float, ],
        daysSinceNonsufficientFunds: typing.Union[MetaOapg.properties.daysSinceNonsufficientFunds, decimal.Decimal, int, ],
        accountNumberDisplay: typing.Union[MetaOapg.properties.accountNumberDisplay, str, ],
        currency: typing.Union[MetaOapg.properties.currency, str, ],
        financialInstitution: typing.Union[MetaOapg.properties.financialInstitution, str, ],
        status: typing.Union[MetaOapg.properties.status, str, ],
        totalNonsufficientFunds: typing.Union[MetaOapg.properties.totalNonsufficientFunds, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PaymentHistoryAccountSummary':
        return super().__new__(
            cls,
            *args,
            beginningBalance=beginningBalance,
            institutionIcon=institutionIcon,
            accountName=accountName,
            endDate=endDate,
            accountType=accountType,
            currentBalance=currentBalance,
            accountOwner=accountOwner,
            totalNonSufficientFunds=totalNonSufficientFunds,
            beginDate=beginDate,
            averageMonthlyBalance=averageMonthlyBalance,
            daysSinceNonsufficientFunds=daysSinceNonsufficientFunds,
            accountNumberDisplay=accountNumberDisplay,
            currency=currency,
            financialInstitution=financialInstitution,
            status=status,
            totalNonsufficientFunds=totalNonsufficientFunds,
            _configuration=_configuration,
            **kwargs,
        )

from mastercard_python_sdk.model.payment_history_account_summary_account_owner import PaymentHistoryAccountSummaryAccountOwner
