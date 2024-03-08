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


class StatementReportAck(
    schemas.ComposedSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A Statement report being generated
    """


    class MetaOapg:
        required = {
            "consumerId",
            "title",
            "type",
            "constraints",
            "consumerSsn",
            "customerType",
            "createdDate",
            "portfolioId",
            "requestId",
            "requesterName",
            "customerId",
            "id",
            "status",
        }
        
        
        class all_of_1(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                
                class properties:
                
                    @staticmethod
                    def constraints() -> typing.Type['StatementReportConstraints']:
                        return StatementReportConstraints
                    __annotations__ = {
                        "constraints": constraints,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["constraints"]) -> 'StatementReportConstraints': ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["constraints", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["constraints"]) -> typing.Union['StatementReportConstraints', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["constraints", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                constraints: typing.Union['StatementReportConstraints', schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *args,
                    constraints=constraints,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        @classmethod
        @functools.lru_cache()
        def all_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                BaseReportAckWithPortfolioId,
                cls.all_of_1,
            ]

    
    consumerId: schemas.AnyTypeSchema
    title: schemas.AnyTypeSchema
    type: schemas.AnyTypeSchema
    constraints: schemas.AnyTypeSchema
    consumerSsn: schemas.AnyTypeSchema
    customerType: schemas.AnyTypeSchema
    createdDate: schemas.AnyTypeSchema
    portfolioId: schemas.AnyTypeSchema
    requestId: schemas.AnyTypeSchema
    requesterName: schemas.AnyTypeSchema
    customerId: schemas.AnyTypeSchema
    id: schemas.AnyTypeSchema
    status: schemas.AnyTypeSchema

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'StatementReportAck':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from mastercard_python_sdk.model.base_report_ack_with_portfolio_id import BaseReportAckWithPortfolioId
from mastercard_python_sdk.model.statement_report_constraints import StatementReportConstraints
