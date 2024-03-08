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


class ConnectEmailParameters(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "consumerId",
            "customerId",
            "partnerId",
            "email",
        }
        
        class properties:
            partnerId = schemas.StrSchema
            customerId = schemas.StrSchema
            consumerId = schemas.StrSchema
        
            @staticmethod
            def email() -> typing.Type['EmailOptions']:
                return EmailOptions
            language = schemas.StrSchema
            redirectUri = schemas.StrSchema
            webhook = schemas.StrSchema
            webhookContentType = schemas.StrSchema
            webhookData = schemas.DictSchema
            webhookHeaders = schemas.DictSchema
            institutionSettings = schemas.DictSchema
            experience = schemas.StrSchema
            singleUseUrl = schemas.BoolSchema
            fromDate = schemas.Int64Schema
        
            @staticmethod
            def reportCustomFields() -> typing.Type['ReportCustomFields']:
                return ReportCustomFields
        
            @staticmethod
            def optionalConsumerInfo() -> typing.Type['ConsumerInfo']:
                return ConsumerInfo
            __annotations__ = {
                "partnerId": partnerId,
                "customerId": customerId,
                "consumerId": consumerId,
                "email": email,
                "language": language,
                "redirectUri": redirectUri,
                "webhook": webhook,
                "webhookContentType": webhookContentType,
                "webhookData": webhookData,
                "webhookHeaders": webhookHeaders,
                "institutionSettings": institutionSettings,
                "experience": experience,
                "singleUseUrl": singleUseUrl,
                "fromDate": fromDate,
                "reportCustomFields": reportCustomFields,
                "optionalConsumerInfo": optionalConsumerInfo,
            }
    
    consumerId: MetaOapg.properties.consumerId
    customerId: MetaOapg.properties.customerId
    partnerId: MetaOapg.properties.partnerId
    email: 'EmailOptions'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["partnerId"]) -> MetaOapg.properties.partnerId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customerId"]) -> MetaOapg.properties.customerId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["consumerId"]) -> MetaOapg.properties.consumerId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> 'EmailOptions': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["language"]) -> MetaOapg.properties.language: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["redirectUri"]) -> MetaOapg.properties.redirectUri: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["webhook"]) -> MetaOapg.properties.webhook: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["webhookContentType"]) -> MetaOapg.properties.webhookContentType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["webhookData"]) -> MetaOapg.properties.webhookData: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["webhookHeaders"]) -> MetaOapg.properties.webhookHeaders: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["institutionSettings"]) -> MetaOapg.properties.institutionSettings: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["experience"]) -> MetaOapg.properties.experience: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["singleUseUrl"]) -> MetaOapg.properties.singleUseUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fromDate"]) -> MetaOapg.properties.fromDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reportCustomFields"]) -> 'ReportCustomFields': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["optionalConsumerInfo"]) -> 'ConsumerInfo': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["partnerId", "customerId", "consumerId", "email", "language", "redirectUri", "webhook", "webhookContentType", "webhookData", "webhookHeaders", "institutionSettings", "experience", "singleUseUrl", "fromDate", "reportCustomFields", "optionalConsumerInfo", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["partnerId"]) -> MetaOapg.properties.partnerId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customerId"]) -> MetaOapg.properties.customerId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["consumerId"]) -> MetaOapg.properties.consumerId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> 'EmailOptions': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["language"]) -> typing.Union[MetaOapg.properties.language, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["redirectUri"]) -> typing.Union[MetaOapg.properties.redirectUri, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["webhook"]) -> typing.Union[MetaOapg.properties.webhook, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["webhookContentType"]) -> typing.Union[MetaOapg.properties.webhookContentType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["webhookData"]) -> typing.Union[MetaOapg.properties.webhookData, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["webhookHeaders"]) -> typing.Union[MetaOapg.properties.webhookHeaders, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["institutionSettings"]) -> typing.Union[MetaOapg.properties.institutionSettings, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["experience"]) -> typing.Union[MetaOapg.properties.experience, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["singleUseUrl"]) -> typing.Union[MetaOapg.properties.singleUseUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fromDate"]) -> typing.Union[MetaOapg.properties.fromDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reportCustomFields"]) -> typing.Union['ReportCustomFields', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["optionalConsumerInfo"]) -> typing.Union['ConsumerInfo', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["partnerId", "customerId", "consumerId", "email", "language", "redirectUri", "webhook", "webhookContentType", "webhookData", "webhookHeaders", "institutionSettings", "experience", "singleUseUrl", "fromDate", "reportCustomFields", "optionalConsumerInfo", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        consumerId: typing.Union[MetaOapg.properties.consumerId, str, ],
        customerId: typing.Union[MetaOapg.properties.customerId, str, ],
        partnerId: typing.Union[MetaOapg.properties.partnerId, str, ],
        email: 'EmailOptions',
        language: typing.Union[MetaOapg.properties.language, str, schemas.Unset] = schemas.unset,
        redirectUri: typing.Union[MetaOapg.properties.redirectUri, str, schemas.Unset] = schemas.unset,
        webhook: typing.Union[MetaOapg.properties.webhook, str, schemas.Unset] = schemas.unset,
        webhookContentType: typing.Union[MetaOapg.properties.webhookContentType, str, schemas.Unset] = schemas.unset,
        webhookData: typing.Union[MetaOapg.properties.webhookData, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        webhookHeaders: typing.Union[MetaOapg.properties.webhookHeaders, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        institutionSettings: typing.Union[MetaOapg.properties.institutionSettings, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        experience: typing.Union[MetaOapg.properties.experience, str, schemas.Unset] = schemas.unset,
        singleUseUrl: typing.Union[MetaOapg.properties.singleUseUrl, bool, schemas.Unset] = schemas.unset,
        fromDate: typing.Union[MetaOapg.properties.fromDate, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        reportCustomFields: typing.Union['ReportCustomFields', schemas.Unset] = schemas.unset,
        optionalConsumerInfo: typing.Union['ConsumerInfo', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ConnectEmailParameters':
        return super().__new__(
            cls,
            *args,
            consumerId=consumerId,
            customerId=customerId,
            partnerId=partnerId,
            email=email,
            language=language,
            redirectUri=redirectUri,
            webhook=webhook,
            webhookContentType=webhookContentType,
            webhookData=webhookData,
            webhookHeaders=webhookHeaders,
            institutionSettings=institutionSettings,
            experience=experience,
            singleUseUrl=singleUseUrl,
            fromDate=fromDate,
            reportCustomFields=reportCustomFields,
            optionalConsumerInfo=optionalConsumerInfo,
            _configuration=_configuration,
            **kwargs,
        )

from mastercard_python_sdk.model.consumer_info import ConsumerInfo
from mastercard_python_sdk.model.email_options import EmailOptions
from mastercard_python_sdk.model.report_custom_fields import ReportCustomFields
