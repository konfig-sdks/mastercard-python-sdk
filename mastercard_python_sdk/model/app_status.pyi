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


class AppStatus(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Registration status details for the application
    """


    class MetaOapg:
        required = {
            "preAppId",
            "appName",
            "modifiedDate",
            "partnerId",
            "submittedDate",
            "status",
        }
        
        class properties:
            partnerId = schemas.StrSchema
            preAppId = schemas.StrSchema
            appName = schemas.StrSchema
            submittedDate = schemas.Int64Schema
            modifiedDate = schemas.Int64Schema
            status = schemas.StrSchema
            note = schemas.StrSchema
            applicationId = schemas.StrSchema
            scopes = schemas.StrSchema
            
            
            class institutionDetails(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['AppFinancialInstitutionStatus']:
                        return AppFinancialInstitutionStatus
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['AppFinancialInstitutionStatus'], typing.List['AppFinancialInstitutionStatus']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'institutionDetails':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'AppFinancialInstitutionStatus':
                    return super().__getitem__(i)
            __annotations__ = {
                "partnerId": partnerId,
                "preAppId": preAppId,
                "appName": appName,
                "submittedDate": submittedDate,
                "modifiedDate": modifiedDate,
                "status": status,
                "note": note,
                "applicationId": applicationId,
                "scopes": scopes,
                "institutionDetails": institutionDetails,
            }
    
    preAppId: MetaOapg.properties.preAppId
    appName: MetaOapg.properties.appName
    modifiedDate: MetaOapg.properties.modifiedDate
    partnerId: MetaOapg.properties.partnerId
    submittedDate: MetaOapg.properties.submittedDate
    status: MetaOapg.properties.status
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["partnerId"]) -> MetaOapg.properties.partnerId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["preAppId"]) -> MetaOapg.properties.preAppId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["appName"]) -> MetaOapg.properties.appName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["submittedDate"]) -> MetaOapg.properties.submittedDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["modifiedDate"]) -> MetaOapg.properties.modifiedDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["note"]) -> MetaOapg.properties.note: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["applicationId"]) -> MetaOapg.properties.applicationId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scopes"]) -> MetaOapg.properties.scopes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["institutionDetails"]) -> MetaOapg.properties.institutionDetails: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["partnerId", "preAppId", "appName", "submittedDate", "modifiedDate", "status", "note", "applicationId", "scopes", "institutionDetails", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["partnerId"]) -> MetaOapg.properties.partnerId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["preAppId"]) -> MetaOapg.properties.preAppId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["appName"]) -> MetaOapg.properties.appName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["submittedDate"]) -> MetaOapg.properties.submittedDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["modifiedDate"]) -> MetaOapg.properties.modifiedDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["note"]) -> typing.Union[MetaOapg.properties.note, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["applicationId"]) -> typing.Union[MetaOapg.properties.applicationId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scopes"]) -> typing.Union[MetaOapg.properties.scopes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["institutionDetails"]) -> typing.Union[MetaOapg.properties.institutionDetails, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["partnerId", "preAppId", "appName", "submittedDate", "modifiedDate", "status", "note", "applicationId", "scopes", "institutionDetails", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        preAppId: typing.Union[MetaOapg.properties.preAppId, str, ],
        appName: typing.Union[MetaOapg.properties.appName, str, ],
        modifiedDate: typing.Union[MetaOapg.properties.modifiedDate, decimal.Decimal, int, ],
        partnerId: typing.Union[MetaOapg.properties.partnerId, str, ],
        submittedDate: typing.Union[MetaOapg.properties.submittedDate, decimal.Decimal, int, ],
        status: typing.Union[MetaOapg.properties.status, str, ],
        note: typing.Union[MetaOapg.properties.note, str, schemas.Unset] = schemas.unset,
        applicationId: typing.Union[MetaOapg.properties.applicationId, str, schemas.Unset] = schemas.unset,
        scopes: typing.Union[MetaOapg.properties.scopes, str, schemas.Unset] = schemas.unset,
        institutionDetails: typing.Union[MetaOapg.properties.institutionDetails, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AppStatus':
        return super().__new__(
            cls,
            *args,
            preAppId=preAppId,
            appName=appName,
            modifiedDate=modifiedDate,
            partnerId=partnerId,
            submittedDate=submittedDate,
            status=status,
            note=note,
            applicationId=applicationId,
            scopes=scopes,
            institutionDetails=institutionDetails,
            _configuration=_configuration,
            **kwargs,
        )

from mastercard_python_sdk.model.app_financial_institution_status import AppFinancialInstitutionStatus
