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


class CertifiedInstitution(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "stateAgg",
            "transAgg",
            "voi",
            "availBalance",
            "studentLoanData",
            "ach",
            "name",
            "voa",
            "loanPaymentDetails",
            "accountOwner",
            "aha",
            "id",
        }
        
        class properties:
            id = schemas.Int64Schema
            name = schemas.StrSchema
            transAgg = schemas.BoolSchema
            ach = schemas.BoolSchema
            stateAgg = schemas.BoolSchema
            voi = schemas.BoolSchema
            voa = schemas.BoolSchema
            aha = schemas.BoolSchema
            availBalance = schemas.BoolSchema
            accountOwner = schemas.BoolSchema
            studentLoanData = schemas.BoolSchema
            loanPaymentDetails = schemas.BoolSchema
            rssd = schemas.Int64Schema
            
            
            class childInstitutions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    min_items = 0
                    
                    @staticmethod
                    def items() -> typing.Type['ChildInstitution']:
                        return ChildInstitution
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ChildInstitution'], typing.List['ChildInstitution']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'childInstitutions':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ChildInstitution':
                    return super().__getitem__(i)
            __annotations__ = {
                "id": id,
                "name": name,
                "transAgg": transAgg,
                "ach": ach,
                "stateAgg": stateAgg,
                "voi": voi,
                "voa": voa,
                "aha": aha,
                "availBalance": availBalance,
                "accountOwner": accountOwner,
                "studentLoanData": studentLoanData,
                "loanPaymentDetails": loanPaymentDetails,
                "rssd": rssd,
                "childInstitutions": childInstitutions,
            }
    
    stateAgg: MetaOapg.properties.stateAgg
    transAgg: MetaOapg.properties.transAgg
    voi: MetaOapg.properties.voi
    availBalance: MetaOapg.properties.availBalance
    studentLoanData: MetaOapg.properties.studentLoanData
    ach: MetaOapg.properties.ach
    name: MetaOapg.properties.name
    voa: MetaOapg.properties.voa
    loanPaymentDetails: MetaOapg.properties.loanPaymentDetails
    accountOwner: MetaOapg.properties.accountOwner
    aha: MetaOapg.properties.aha
    id: MetaOapg.properties.id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transAgg"]) -> MetaOapg.properties.transAgg: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ach"]) -> MetaOapg.properties.ach: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stateAgg"]) -> MetaOapg.properties.stateAgg: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["voi"]) -> MetaOapg.properties.voi: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["voa"]) -> MetaOapg.properties.voa: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["aha"]) -> MetaOapg.properties.aha: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["availBalance"]) -> MetaOapg.properties.availBalance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accountOwner"]) -> MetaOapg.properties.accountOwner: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["studentLoanData"]) -> MetaOapg.properties.studentLoanData: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["loanPaymentDetails"]) -> MetaOapg.properties.loanPaymentDetails: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rssd"]) -> MetaOapg.properties.rssd: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["childInstitutions"]) -> MetaOapg.properties.childInstitutions: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "transAgg", "ach", "stateAgg", "voi", "voa", "aha", "availBalance", "accountOwner", "studentLoanData", "loanPaymentDetails", "rssd", "childInstitutions", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transAgg"]) -> MetaOapg.properties.transAgg: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ach"]) -> MetaOapg.properties.ach: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stateAgg"]) -> MetaOapg.properties.stateAgg: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["voi"]) -> MetaOapg.properties.voi: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["voa"]) -> MetaOapg.properties.voa: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["aha"]) -> MetaOapg.properties.aha: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["availBalance"]) -> MetaOapg.properties.availBalance: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountOwner"]) -> MetaOapg.properties.accountOwner: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["studentLoanData"]) -> MetaOapg.properties.studentLoanData: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["loanPaymentDetails"]) -> MetaOapg.properties.loanPaymentDetails: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rssd"]) -> typing.Union[MetaOapg.properties.rssd, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["childInstitutions"]) -> typing.Union[MetaOapg.properties.childInstitutions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "transAgg", "ach", "stateAgg", "voi", "voa", "aha", "availBalance", "accountOwner", "studentLoanData", "loanPaymentDetails", "rssd", "childInstitutions", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        stateAgg: typing.Union[MetaOapg.properties.stateAgg, bool, ],
        transAgg: typing.Union[MetaOapg.properties.transAgg, bool, ],
        voi: typing.Union[MetaOapg.properties.voi, bool, ],
        availBalance: typing.Union[MetaOapg.properties.availBalance, bool, ],
        studentLoanData: typing.Union[MetaOapg.properties.studentLoanData, bool, ],
        ach: typing.Union[MetaOapg.properties.ach, bool, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        voa: typing.Union[MetaOapg.properties.voa, bool, ],
        loanPaymentDetails: typing.Union[MetaOapg.properties.loanPaymentDetails, bool, ],
        accountOwner: typing.Union[MetaOapg.properties.accountOwner, bool, ],
        aha: typing.Union[MetaOapg.properties.aha, bool, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
        rssd: typing.Union[MetaOapg.properties.rssd, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        childInstitutions: typing.Union[MetaOapg.properties.childInstitutions, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CertifiedInstitution':
        return super().__new__(
            cls,
            *args,
            stateAgg=stateAgg,
            transAgg=transAgg,
            voi=voi,
            availBalance=availBalance,
            studentLoanData=studentLoanData,
            ach=ach,
            name=name,
            voa=voa,
            loanPaymentDetails=loanPaymentDetails,
            accountOwner=accountOwner,
            aha=aha,
            id=id,
            rssd=rssd,
            childInstitutions=childInstitutions,
            _configuration=_configuration,
            **kwargs,
        )

from mastercard_python_sdk.model.child_institution import ChildInstitution