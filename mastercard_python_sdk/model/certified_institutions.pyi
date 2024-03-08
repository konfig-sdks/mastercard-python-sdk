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


class CertifiedInstitutions(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A list of financial institutions from the Get Certified Institutions API
    """


    class MetaOapg:
        required = {
            "institutions",
            "moreAvailable",
            "found",
            "requestedDate",
            "displaying",
        }
        
        class properties:
            found = schemas.IntSchema
            displaying = schemas.IntSchema
            moreAvailable = schemas.BoolSchema
            requestedDate = schemas.Int64Schema
            
            
            class institutions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['CertifiedInstitution']:
                        return CertifiedInstitution
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['CertifiedInstitution'], typing.List['CertifiedInstitution']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'institutions':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'CertifiedInstitution':
                    return super().__getitem__(i)
            __annotations__ = {
                "found": found,
                "displaying": displaying,
                "moreAvailable": moreAvailable,
                "requestedDate": requestedDate,
                "institutions": institutions,
            }
    
    institutions: MetaOapg.properties.institutions
    moreAvailable: MetaOapg.properties.moreAvailable
    found: MetaOapg.properties.found
    requestedDate: MetaOapg.properties.requestedDate
    displaying: MetaOapg.properties.displaying
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["found"]) -> MetaOapg.properties.found: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["displaying"]) -> MetaOapg.properties.displaying: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["moreAvailable"]) -> MetaOapg.properties.moreAvailable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["requestedDate"]) -> MetaOapg.properties.requestedDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["institutions"]) -> MetaOapg.properties.institutions: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["found", "displaying", "moreAvailable", "requestedDate", "institutions", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["found"]) -> MetaOapg.properties.found: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["displaying"]) -> MetaOapg.properties.displaying: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["moreAvailable"]) -> MetaOapg.properties.moreAvailable: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["requestedDate"]) -> MetaOapg.properties.requestedDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["institutions"]) -> MetaOapg.properties.institutions: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["found", "displaying", "moreAvailable", "requestedDate", "institutions", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        institutions: typing.Union[MetaOapg.properties.institutions, list, tuple, ],
        moreAvailable: typing.Union[MetaOapg.properties.moreAvailable, bool, ],
        found: typing.Union[MetaOapg.properties.found, decimal.Decimal, int, ],
        requestedDate: typing.Union[MetaOapg.properties.requestedDate, decimal.Decimal, int, ],
        displaying: typing.Union[MetaOapg.properties.displaying, decimal.Decimal, int, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CertifiedInstitutions':
        return super().__new__(
            cls,
            *args,
            institutions=institutions,
            moreAvailable=moreAvailable,
            found=found,
            requestedDate=requestedDate,
            displaying=displaying,
            _configuration=_configuration,
            **kwargs,
        )

from mastercard_python_sdk.model.certified_institution import CertifiedInstitution