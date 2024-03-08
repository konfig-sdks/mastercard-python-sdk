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


class AccountOwnerIdentityInsights(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    List of account owner Identity Insights
    """


    class MetaOapg:
        
        class properties:
            isEmailValid = schemas.BoolSchema
            emailFirstSeenDays = schemas.NumberSchema
            emailDomainCreationDate = schemas.StrSchema
            emailToName = schemas.StrSchema
            ipRisk = schemas.NumberSchema
            ipRiskScore = schemas.NumberSchema
            ipLastSeenDays = schemas.NumberSchema
            ipGeolocationCountryCode = schemas.StrSchema
            ipGeolocationSubdivision = schemas.StrSchema
            ipPhoneDistance = schemas.NumberSchema
            ipAddressDistance = schemas.NumberSchema
            isPhoneValid = schemas.BoolSchema
            phoneLineType = schemas.StrSchema
            phoneCarrier = schemas.StrSchema
            phoneCountryCode = schemas.StrSchema
            phoneLastSeenDays = schemas.NumberSchema
            phoneEmailFirstSeenDays = schemas.NumberSchema
            phoneToName = schemas.StrSchema
            phoneToAddress = schemas.StrSchema
            addressValidityLevel = schemas.NumberSchema
            addressToName = schemas.StrSchema
            identityNetworkScore = schemas.NumberSchema
            identityRiskScore = schemas.NumberSchema
            
            
            class warnings(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'warnings':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "isEmailValid": isEmailValid,
                "emailFirstSeenDays": emailFirstSeenDays,
                "emailDomainCreationDate": emailDomainCreationDate,
                "emailToName": emailToName,
                "ipRisk": ipRisk,
                "ipRiskScore": ipRiskScore,
                "ipLastSeenDays": ipLastSeenDays,
                "ipGeolocationCountryCode": ipGeolocationCountryCode,
                "ipGeolocationSubdivision": ipGeolocationSubdivision,
                "ipPhoneDistance": ipPhoneDistance,
                "ipAddressDistance": ipAddressDistance,
                "isPhoneValid": isPhoneValid,
                "phoneLineType": phoneLineType,
                "phoneCarrier": phoneCarrier,
                "phoneCountryCode": phoneCountryCode,
                "phoneLastSeenDays": phoneLastSeenDays,
                "phoneEmailFirstSeenDays": phoneEmailFirstSeenDays,
                "phoneToName": phoneToName,
                "phoneToAddress": phoneToAddress,
                "addressValidityLevel": addressValidityLevel,
                "addressToName": addressToName,
                "identityNetworkScore": identityNetworkScore,
                "identityRiskScore": identityRiskScore,
                "warnings": warnings,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isEmailValid"]) -> MetaOapg.properties.isEmailValid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["emailFirstSeenDays"]) -> MetaOapg.properties.emailFirstSeenDays: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["emailDomainCreationDate"]) -> MetaOapg.properties.emailDomainCreationDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["emailToName"]) -> MetaOapg.properties.emailToName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ipRisk"]) -> MetaOapg.properties.ipRisk: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ipRiskScore"]) -> MetaOapg.properties.ipRiskScore: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ipLastSeenDays"]) -> MetaOapg.properties.ipLastSeenDays: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ipGeolocationCountryCode"]) -> MetaOapg.properties.ipGeolocationCountryCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ipGeolocationSubdivision"]) -> MetaOapg.properties.ipGeolocationSubdivision: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ipPhoneDistance"]) -> MetaOapg.properties.ipPhoneDistance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ipAddressDistance"]) -> MetaOapg.properties.ipAddressDistance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isPhoneValid"]) -> MetaOapg.properties.isPhoneValid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phoneLineType"]) -> MetaOapg.properties.phoneLineType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phoneCarrier"]) -> MetaOapg.properties.phoneCarrier: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phoneCountryCode"]) -> MetaOapg.properties.phoneCountryCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phoneLastSeenDays"]) -> MetaOapg.properties.phoneLastSeenDays: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phoneEmailFirstSeenDays"]) -> MetaOapg.properties.phoneEmailFirstSeenDays: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phoneToName"]) -> MetaOapg.properties.phoneToName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phoneToAddress"]) -> MetaOapg.properties.phoneToAddress: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["addressValidityLevel"]) -> MetaOapg.properties.addressValidityLevel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["addressToName"]) -> MetaOapg.properties.addressToName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["identityNetworkScore"]) -> MetaOapg.properties.identityNetworkScore: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["identityRiskScore"]) -> MetaOapg.properties.identityRiskScore: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["warnings"]) -> MetaOapg.properties.warnings: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["isEmailValid", "emailFirstSeenDays", "emailDomainCreationDate", "emailToName", "ipRisk", "ipRiskScore", "ipLastSeenDays", "ipGeolocationCountryCode", "ipGeolocationSubdivision", "ipPhoneDistance", "ipAddressDistance", "isPhoneValid", "phoneLineType", "phoneCarrier", "phoneCountryCode", "phoneLastSeenDays", "phoneEmailFirstSeenDays", "phoneToName", "phoneToAddress", "addressValidityLevel", "addressToName", "identityNetworkScore", "identityRiskScore", "warnings", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isEmailValid"]) -> typing.Union[MetaOapg.properties.isEmailValid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["emailFirstSeenDays"]) -> typing.Union[MetaOapg.properties.emailFirstSeenDays, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["emailDomainCreationDate"]) -> typing.Union[MetaOapg.properties.emailDomainCreationDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["emailToName"]) -> typing.Union[MetaOapg.properties.emailToName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ipRisk"]) -> typing.Union[MetaOapg.properties.ipRisk, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ipRiskScore"]) -> typing.Union[MetaOapg.properties.ipRiskScore, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ipLastSeenDays"]) -> typing.Union[MetaOapg.properties.ipLastSeenDays, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ipGeolocationCountryCode"]) -> typing.Union[MetaOapg.properties.ipGeolocationCountryCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ipGeolocationSubdivision"]) -> typing.Union[MetaOapg.properties.ipGeolocationSubdivision, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ipPhoneDistance"]) -> typing.Union[MetaOapg.properties.ipPhoneDistance, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ipAddressDistance"]) -> typing.Union[MetaOapg.properties.ipAddressDistance, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isPhoneValid"]) -> typing.Union[MetaOapg.properties.isPhoneValid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phoneLineType"]) -> typing.Union[MetaOapg.properties.phoneLineType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phoneCarrier"]) -> typing.Union[MetaOapg.properties.phoneCarrier, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phoneCountryCode"]) -> typing.Union[MetaOapg.properties.phoneCountryCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phoneLastSeenDays"]) -> typing.Union[MetaOapg.properties.phoneLastSeenDays, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phoneEmailFirstSeenDays"]) -> typing.Union[MetaOapg.properties.phoneEmailFirstSeenDays, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phoneToName"]) -> typing.Union[MetaOapg.properties.phoneToName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phoneToAddress"]) -> typing.Union[MetaOapg.properties.phoneToAddress, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["addressValidityLevel"]) -> typing.Union[MetaOapg.properties.addressValidityLevel, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["addressToName"]) -> typing.Union[MetaOapg.properties.addressToName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["identityNetworkScore"]) -> typing.Union[MetaOapg.properties.identityNetworkScore, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["identityRiskScore"]) -> typing.Union[MetaOapg.properties.identityRiskScore, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["warnings"]) -> typing.Union[MetaOapg.properties.warnings, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["isEmailValid", "emailFirstSeenDays", "emailDomainCreationDate", "emailToName", "ipRisk", "ipRiskScore", "ipLastSeenDays", "ipGeolocationCountryCode", "ipGeolocationSubdivision", "ipPhoneDistance", "ipAddressDistance", "isPhoneValid", "phoneLineType", "phoneCarrier", "phoneCountryCode", "phoneLastSeenDays", "phoneEmailFirstSeenDays", "phoneToName", "phoneToAddress", "addressValidityLevel", "addressToName", "identityNetworkScore", "identityRiskScore", "warnings", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        isEmailValid: typing.Union[MetaOapg.properties.isEmailValid, bool, schemas.Unset] = schemas.unset,
        emailFirstSeenDays: typing.Union[MetaOapg.properties.emailFirstSeenDays, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        emailDomainCreationDate: typing.Union[MetaOapg.properties.emailDomainCreationDate, str, schemas.Unset] = schemas.unset,
        emailToName: typing.Union[MetaOapg.properties.emailToName, str, schemas.Unset] = schemas.unset,
        ipRisk: typing.Union[MetaOapg.properties.ipRisk, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        ipRiskScore: typing.Union[MetaOapg.properties.ipRiskScore, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        ipLastSeenDays: typing.Union[MetaOapg.properties.ipLastSeenDays, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        ipGeolocationCountryCode: typing.Union[MetaOapg.properties.ipGeolocationCountryCode, str, schemas.Unset] = schemas.unset,
        ipGeolocationSubdivision: typing.Union[MetaOapg.properties.ipGeolocationSubdivision, str, schemas.Unset] = schemas.unset,
        ipPhoneDistance: typing.Union[MetaOapg.properties.ipPhoneDistance, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        ipAddressDistance: typing.Union[MetaOapg.properties.ipAddressDistance, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        isPhoneValid: typing.Union[MetaOapg.properties.isPhoneValid, bool, schemas.Unset] = schemas.unset,
        phoneLineType: typing.Union[MetaOapg.properties.phoneLineType, str, schemas.Unset] = schemas.unset,
        phoneCarrier: typing.Union[MetaOapg.properties.phoneCarrier, str, schemas.Unset] = schemas.unset,
        phoneCountryCode: typing.Union[MetaOapg.properties.phoneCountryCode, str, schemas.Unset] = schemas.unset,
        phoneLastSeenDays: typing.Union[MetaOapg.properties.phoneLastSeenDays, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        phoneEmailFirstSeenDays: typing.Union[MetaOapg.properties.phoneEmailFirstSeenDays, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        phoneToName: typing.Union[MetaOapg.properties.phoneToName, str, schemas.Unset] = schemas.unset,
        phoneToAddress: typing.Union[MetaOapg.properties.phoneToAddress, str, schemas.Unset] = schemas.unset,
        addressValidityLevel: typing.Union[MetaOapg.properties.addressValidityLevel, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        addressToName: typing.Union[MetaOapg.properties.addressToName, str, schemas.Unset] = schemas.unset,
        identityNetworkScore: typing.Union[MetaOapg.properties.identityNetworkScore, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        identityRiskScore: typing.Union[MetaOapg.properties.identityRiskScore, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        warnings: typing.Union[MetaOapg.properties.warnings, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AccountOwnerIdentityInsights':
        return super().__new__(
            cls,
            *args,
            isEmailValid=isEmailValid,
            emailFirstSeenDays=emailFirstSeenDays,
            emailDomainCreationDate=emailDomainCreationDate,
            emailToName=emailToName,
            ipRisk=ipRisk,
            ipRiskScore=ipRiskScore,
            ipLastSeenDays=ipLastSeenDays,
            ipGeolocationCountryCode=ipGeolocationCountryCode,
            ipGeolocationSubdivision=ipGeolocationSubdivision,
            ipPhoneDistance=ipPhoneDistance,
            ipAddressDistance=ipAddressDistance,
            isPhoneValid=isPhoneValid,
            phoneLineType=phoneLineType,
            phoneCarrier=phoneCarrier,
            phoneCountryCode=phoneCountryCode,
            phoneLastSeenDays=phoneLastSeenDays,
            phoneEmailFirstSeenDays=phoneEmailFirstSeenDays,
            phoneToName=phoneToName,
            phoneToAddress=phoneToAddress,
            addressValidityLevel=addressValidityLevel,
            addressToName=addressToName,
            identityNetworkScore=identityNetworkScore,
            identityRiskScore=identityRiskScore,
            warnings=warnings,
            _configuration=_configuration,
            **kwargs,
        )