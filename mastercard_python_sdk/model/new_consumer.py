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


class NewConsumer(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A new consumer to be created
    """


    class MetaOapg:
        required = {
            "birthday",
            "zip",
            "firstName",
            "lastName",
            "address",
            "city",
            "phone",
            "state",
            "ssn",
        }
        
        class properties:
            firstName = schemas.StrSchema
            lastName = schemas.StrSchema
            address = schemas.StrSchema
            city = schemas.StrSchema
            state = schemas.StrSchema
            zip = schemas.StrSchema
            phone = schemas.StrSchema
            ssn = schemas.StrSchema
        
            @staticmethod
            def birthday() -> typing.Type['Birthday']:
                return Birthday
            email = schemas.StrSchema
            suffix = schemas.StrSchema
            __annotations__ = {
                "firstName": firstName,
                "lastName": lastName,
                "address": address,
                "city": city,
                "state": state,
                "zip": zip,
                "phone": phone,
                "ssn": ssn,
                "birthday": birthday,
                "email": email,
                "suffix": suffix,
            }
    
    birthday: 'Birthday'
    zip: MetaOapg.properties.zip
    firstName: MetaOapg.properties.firstName
    lastName: MetaOapg.properties.lastName
    address: MetaOapg.properties.address
    city: MetaOapg.properties.city
    phone: MetaOapg.properties.phone
    state: MetaOapg.properties.state
    ssn: MetaOapg.properties.ssn
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["firstName"]) -> MetaOapg.properties.firstName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastName"]) -> MetaOapg.properties.lastName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address"]) -> MetaOapg.properties.address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["city"]) -> MetaOapg.properties.city: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["zip"]) -> MetaOapg.properties.zip: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phone"]) -> MetaOapg.properties.phone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ssn"]) -> MetaOapg.properties.ssn: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["birthday"]) -> 'Birthday': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["suffix"]) -> MetaOapg.properties.suffix: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["firstName", "lastName", "address", "city", "state", "zip", "phone", "ssn", "birthday", "email", "suffix", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["firstName"]) -> MetaOapg.properties.firstName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastName"]) -> MetaOapg.properties.lastName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address"]) -> MetaOapg.properties.address: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["city"]) -> MetaOapg.properties.city: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["zip"]) -> MetaOapg.properties.zip: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phone"]) -> MetaOapg.properties.phone: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ssn"]) -> MetaOapg.properties.ssn: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["birthday"]) -> 'Birthday': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["suffix"]) -> typing.Union[MetaOapg.properties.suffix, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["firstName", "lastName", "address", "city", "state", "zip", "phone", "ssn", "birthday", "email", "suffix", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        birthday: 'Birthday',
        zip: typing.Union[MetaOapg.properties.zip, str, ],
        firstName: typing.Union[MetaOapg.properties.firstName, str, ],
        lastName: typing.Union[MetaOapg.properties.lastName, str, ],
        address: typing.Union[MetaOapg.properties.address, str, ],
        city: typing.Union[MetaOapg.properties.city, str, ],
        phone: typing.Union[MetaOapg.properties.phone, str, ],
        state: typing.Union[MetaOapg.properties.state, str, ],
        ssn: typing.Union[MetaOapg.properties.ssn, str, ],
        email: typing.Union[MetaOapg.properties.email, str, schemas.Unset] = schemas.unset,
        suffix: typing.Union[MetaOapg.properties.suffix, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'NewConsumer':
        return super().__new__(
            cls,
            *args,
            birthday=birthday,
            zip=zip,
            firstName=firstName,
            lastName=lastName,
            address=address,
            city=city,
            phone=phone,
            state=state,
            ssn=ssn,
            email=email,
            suffix=suffix,
            _configuration=_configuration,
            **kwargs,
        )

from mastercard_python_sdk.model.birthday import Birthday