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


class PortfolioConsumer(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "birthday",
            "firstName",
            "lastName",
            "customerId",
            "id",
            "ssn",
        }
        
        class properties:
            id = schemas.StrSchema
            firstName = schemas.StrSchema
            lastName = schemas.StrSchema
            customerId = schemas.Int64Schema
            ssn = schemas.StrSchema
        
            @staticmethod
            def birthday() -> typing.Type['Birthday']:
                return Birthday
            suffix = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "firstName": firstName,
                "lastName": lastName,
                "customerId": customerId,
                "ssn": ssn,
                "birthday": birthday,
                "suffix": suffix,
            }
    
    birthday: 'Birthday'
    firstName: MetaOapg.properties.firstName
    lastName: MetaOapg.properties.lastName
    customerId: MetaOapg.properties.customerId
    id: MetaOapg.properties.id
    ssn: MetaOapg.properties.ssn
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["firstName"]) -> MetaOapg.properties.firstName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastName"]) -> MetaOapg.properties.lastName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customerId"]) -> MetaOapg.properties.customerId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ssn"]) -> MetaOapg.properties.ssn: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["birthday"]) -> 'Birthday': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["suffix"]) -> MetaOapg.properties.suffix: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "firstName", "lastName", "customerId", "ssn", "birthday", "suffix", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["firstName"]) -> MetaOapg.properties.firstName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastName"]) -> MetaOapg.properties.lastName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customerId"]) -> MetaOapg.properties.customerId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ssn"]) -> MetaOapg.properties.ssn: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["birthday"]) -> 'Birthday': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["suffix"]) -> typing.Union[MetaOapg.properties.suffix, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "firstName", "lastName", "customerId", "ssn", "birthday", "suffix", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        birthday: 'Birthday',
        firstName: typing.Union[MetaOapg.properties.firstName, str, ],
        lastName: typing.Union[MetaOapg.properties.lastName, str, ],
        customerId: typing.Union[MetaOapg.properties.customerId, decimal.Decimal, int, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        ssn: typing.Union[MetaOapg.properties.ssn, str, ],
        suffix: typing.Union[MetaOapg.properties.suffix, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PortfolioConsumer':
        return super().__new__(
            cls,
            *args,
            birthday=birthday,
            firstName=firstName,
            lastName=lastName,
            customerId=customerId,
            id=id,
            ssn=ssn,
            suffix=suffix,
            _configuration=_configuration,
            **kwargs,
        )

from mastercard_python_sdk.model.birthday import Birthday