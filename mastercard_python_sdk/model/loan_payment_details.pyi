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


class LoanPaymentDetails(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Loan payment details for a customer account
    """


    class MetaOapg:
        required = {
            "loanPaymentNumber",
            "loanPaymentAddress",
            "loanNumber",
        }
        
        class properties:
            loanNumber = schemas.StrSchema
            loanPaymentNumber = schemas.StrSchema
            loanPaymentAddress = schemas.StrSchema
        
            @staticmethod
            def accountDetail() -> typing.Type['LoanPaymentDetailsAccount']:
                return LoanPaymentDetailsAccount
            __annotations__ = {
                "loanNumber": loanNumber,
                "loanPaymentNumber": loanPaymentNumber,
                "loanPaymentAddress": loanPaymentAddress,
                "accountDetail": accountDetail,
            }
    
    loanPaymentNumber: MetaOapg.properties.loanPaymentNumber
    loanPaymentAddress: MetaOapg.properties.loanPaymentAddress
    loanNumber: MetaOapg.properties.loanNumber
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["loanNumber"]) -> MetaOapg.properties.loanNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["loanPaymentNumber"]) -> MetaOapg.properties.loanPaymentNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["loanPaymentAddress"]) -> MetaOapg.properties.loanPaymentAddress: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accountDetail"]) -> 'LoanPaymentDetailsAccount': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["loanNumber", "loanPaymentNumber", "loanPaymentAddress", "accountDetail", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["loanNumber"]) -> MetaOapg.properties.loanNumber: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["loanPaymentNumber"]) -> MetaOapg.properties.loanPaymentNumber: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["loanPaymentAddress"]) -> MetaOapg.properties.loanPaymentAddress: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountDetail"]) -> typing.Union['LoanPaymentDetailsAccount', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["loanNumber", "loanPaymentNumber", "loanPaymentAddress", "accountDetail", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        loanPaymentNumber: typing.Union[MetaOapg.properties.loanPaymentNumber, str, ],
        loanPaymentAddress: typing.Union[MetaOapg.properties.loanPaymentAddress, str, ],
        loanNumber: typing.Union[MetaOapg.properties.loanNumber, str, ],
        accountDetail: typing.Union['LoanPaymentDetailsAccount', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LoanPaymentDetails':
        return super().__new__(
            cls,
            *args,
            loanPaymentNumber=loanPaymentNumber,
            loanPaymentAddress=loanPaymentAddress,
            loanNumber=loanNumber,
            accountDetail=accountDetail,
            _configuration=_configuration,
            **kwargs,
        )

from mastercard_python_sdk.model.loan_payment_details_account import LoanPaymentDetailsAccount
