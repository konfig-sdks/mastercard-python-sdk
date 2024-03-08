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


class FixConnectParameters(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "institutionLoginId",
            "customerId",
            "partnerId",
        }
        
        class properties:
            partnerId = schemas.StrSchema
            customerId = schemas.StrSchema
            institutionLoginId = schemas.StrSchema
            language = schemas.StrSchema
            redirectUri = schemas.StrSchema
            webhook = schemas.StrSchema
            webhookContentType = schemas.StrSchema
            webhookData = schemas.DictSchema
            webhookHeaders = schemas.DictSchema
            experience = schemas.StrSchema
            singleUseUrl = schemas.BoolSchema
            isWebView = schemas.BoolSchema
            __annotations__ = {
                "partnerId": partnerId,
                "customerId": customerId,
                "institutionLoginId": institutionLoginId,
                "language": language,
                "redirectUri": redirectUri,
                "webhook": webhook,
                "webhookContentType": webhookContentType,
                "webhookData": webhookData,
                "webhookHeaders": webhookHeaders,
                "experience": experience,
                "singleUseUrl": singleUseUrl,
                "isWebView": isWebView,
            }
    
    institutionLoginId: MetaOapg.properties.institutionLoginId
    customerId: MetaOapg.properties.customerId
    partnerId: MetaOapg.properties.partnerId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["partnerId"]) -> MetaOapg.properties.partnerId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customerId"]) -> MetaOapg.properties.customerId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["institutionLoginId"]) -> MetaOapg.properties.institutionLoginId: ...
    
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
    def __getitem__(self, name: typing_extensions.Literal["experience"]) -> MetaOapg.properties.experience: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["singleUseUrl"]) -> MetaOapg.properties.singleUseUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isWebView"]) -> MetaOapg.properties.isWebView: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["partnerId", "customerId", "institutionLoginId", "language", "redirectUri", "webhook", "webhookContentType", "webhookData", "webhookHeaders", "experience", "singleUseUrl", "isWebView", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["partnerId"]) -> MetaOapg.properties.partnerId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customerId"]) -> MetaOapg.properties.customerId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["institutionLoginId"]) -> MetaOapg.properties.institutionLoginId: ...
    
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
    def get_item_oapg(self, name: typing_extensions.Literal["experience"]) -> typing.Union[MetaOapg.properties.experience, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["singleUseUrl"]) -> typing.Union[MetaOapg.properties.singleUseUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isWebView"]) -> typing.Union[MetaOapg.properties.isWebView, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["partnerId", "customerId", "institutionLoginId", "language", "redirectUri", "webhook", "webhookContentType", "webhookData", "webhookHeaders", "experience", "singleUseUrl", "isWebView", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        institutionLoginId: typing.Union[MetaOapg.properties.institutionLoginId, str, ],
        customerId: typing.Union[MetaOapg.properties.customerId, str, ],
        partnerId: typing.Union[MetaOapg.properties.partnerId, str, ],
        language: typing.Union[MetaOapg.properties.language, str, schemas.Unset] = schemas.unset,
        redirectUri: typing.Union[MetaOapg.properties.redirectUri, str, schemas.Unset] = schemas.unset,
        webhook: typing.Union[MetaOapg.properties.webhook, str, schemas.Unset] = schemas.unset,
        webhookContentType: typing.Union[MetaOapg.properties.webhookContentType, str, schemas.Unset] = schemas.unset,
        webhookData: typing.Union[MetaOapg.properties.webhookData, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        webhookHeaders: typing.Union[MetaOapg.properties.webhookHeaders, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        experience: typing.Union[MetaOapg.properties.experience, str, schemas.Unset] = schemas.unset,
        singleUseUrl: typing.Union[MetaOapg.properties.singleUseUrl, bool, schemas.Unset] = schemas.unset,
        isWebView: typing.Union[MetaOapg.properties.isWebView, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FixConnectParameters':
        return super().__new__(
            cls,
            *args,
            institutionLoginId=institutionLoginId,
            customerId=customerId,
            partnerId=partnerId,
            language=language,
            redirectUri=redirectUri,
            webhook=webhook,
            webhookContentType=webhookContentType,
            webhookData=webhookData,
            webhookHeaders=webhookHeaders,
            experience=experience,
            singleUseUrl=singleUseUrl,
            isWebView=isWebView,
            _configuration=_configuration,
            **kwargs,
        )
