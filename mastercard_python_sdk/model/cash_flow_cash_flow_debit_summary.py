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


class CashFlowCashFlowDebitSummary(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "monthlyCashFlowDebitSummaries",
            "twelveMonthDebitTotal",
            "sixMonthDebitTotalLessTransfers",
            "twoMonthDebitTotalLessTransfers",
            "twoMonthDebitTotal",
            "sixMonthDebitTotal",
            "twelveMonthDebitTotalLessTransfers",
        }
        
        class properties:
            
            
            class monthlyCashFlowDebitSummaries(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['CashFlowMonthlyCashFlowDebitSummaries']:
                        return CashFlowMonthlyCashFlowDebitSummaries
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['CashFlowMonthlyCashFlowDebitSummaries'], typing.List['CashFlowMonthlyCashFlowDebitSummaries']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'monthlyCashFlowDebitSummaries':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'CashFlowMonthlyCashFlowDebitSummaries':
                    return super().__getitem__(i)
            twelveMonthDebitTotal = schemas.NumberSchema
            twelveMonthDebitTotalLessTransfers = schemas.NumberSchema
            sixMonthDebitTotal = schemas.NumberSchema
            sixMonthDebitTotalLessTransfers = schemas.NumberSchema
            twoMonthDebitTotal = schemas.NumberSchema
            twoMonthDebitTotalLessTransfers = schemas.NumberSchema
            __annotations__ = {
                "monthlyCashFlowDebitSummaries": monthlyCashFlowDebitSummaries,
                "twelveMonthDebitTotal": twelveMonthDebitTotal,
                "twelveMonthDebitTotalLessTransfers": twelveMonthDebitTotalLessTransfers,
                "sixMonthDebitTotal": sixMonthDebitTotal,
                "sixMonthDebitTotalLessTransfers": sixMonthDebitTotalLessTransfers,
                "twoMonthDebitTotal": twoMonthDebitTotal,
                "twoMonthDebitTotalLessTransfers": twoMonthDebitTotalLessTransfers,
            }
    
    monthlyCashFlowDebitSummaries: MetaOapg.properties.monthlyCashFlowDebitSummaries
    twelveMonthDebitTotal: MetaOapg.properties.twelveMonthDebitTotal
    sixMonthDebitTotalLessTransfers: MetaOapg.properties.sixMonthDebitTotalLessTransfers
    twoMonthDebitTotalLessTransfers: MetaOapg.properties.twoMonthDebitTotalLessTransfers
    twoMonthDebitTotal: MetaOapg.properties.twoMonthDebitTotal
    sixMonthDebitTotal: MetaOapg.properties.sixMonthDebitTotal
    twelveMonthDebitTotalLessTransfers: MetaOapg.properties.twelveMonthDebitTotalLessTransfers
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["monthlyCashFlowDebitSummaries"]) -> MetaOapg.properties.monthlyCashFlowDebitSummaries: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["twelveMonthDebitTotal"]) -> MetaOapg.properties.twelveMonthDebitTotal: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["twelveMonthDebitTotalLessTransfers"]) -> MetaOapg.properties.twelveMonthDebitTotalLessTransfers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sixMonthDebitTotal"]) -> MetaOapg.properties.sixMonthDebitTotal: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sixMonthDebitTotalLessTransfers"]) -> MetaOapg.properties.sixMonthDebitTotalLessTransfers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["twoMonthDebitTotal"]) -> MetaOapg.properties.twoMonthDebitTotal: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["twoMonthDebitTotalLessTransfers"]) -> MetaOapg.properties.twoMonthDebitTotalLessTransfers: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["monthlyCashFlowDebitSummaries", "twelveMonthDebitTotal", "twelveMonthDebitTotalLessTransfers", "sixMonthDebitTotal", "sixMonthDebitTotalLessTransfers", "twoMonthDebitTotal", "twoMonthDebitTotalLessTransfers", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["monthlyCashFlowDebitSummaries"]) -> MetaOapg.properties.monthlyCashFlowDebitSummaries: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["twelveMonthDebitTotal"]) -> MetaOapg.properties.twelveMonthDebitTotal: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["twelveMonthDebitTotalLessTransfers"]) -> MetaOapg.properties.twelveMonthDebitTotalLessTransfers: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sixMonthDebitTotal"]) -> MetaOapg.properties.sixMonthDebitTotal: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sixMonthDebitTotalLessTransfers"]) -> MetaOapg.properties.sixMonthDebitTotalLessTransfers: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["twoMonthDebitTotal"]) -> MetaOapg.properties.twoMonthDebitTotal: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["twoMonthDebitTotalLessTransfers"]) -> MetaOapg.properties.twoMonthDebitTotalLessTransfers: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["monthlyCashFlowDebitSummaries", "twelveMonthDebitTotal", "twelveMonthDebitTotalLessTransfers", "sixMonthDebitTotal", "sixMonthDebitTotalLessTransfers", "twoMonthDebitTotal", "twoMonthDebitTotalLessTransfers", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        monthlyCashFlowDebitSummaries: typing.Union[MetaOapg.properties.monthlyCashFlowDebitSummaries, list, tuple, ],
        twelveMonthDebitTotal: typing.Union[MetaOapg.properties.twelveMonthDebitTotal, decimal.Decimal, int, float, ],
        sixMonthDebitTotalLessTransfers: typing.Union[MetaOapg.properties.sixMonthDebitTotalLessTransfers, decimal.Decimal, int, float, ],
        twoMonthDebitTotalLessTransfers: typing.Union[MetaOapg.properties.twoMonthDebitTotalLessTransfers, decimal.Decimal, int, float, ],
        twoMonthDebitTotal: typing.Union[MetaOapg.properties.twoMonthDebitTotal, decimal.Decimal, int, float, ],
        sixMonthDebitTotal: typing.Union[MetaOapg.properties.sixMonthDebitTotal, decimal.Decimal, int, float, ],
        twelveMonthDebitTotalLessTransfers: typing.Union[MetaOapg.properties.twelveMonthDebitTotalLessTransfers, decimal.Decimal, int, float, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CashFlowCashFlowDebitSummary':
        return super().__new__(
            cls,
            *args,
            monthlyCashFlowDebitSummaries=monthlyCashFlowDebitSummaries,
            twelveMonthDebitTotal=twelveMonthDebitTotal,
            sixMonthDebitTotalLessTransfers=sixMonthDebitTotalLessTransfers,
            twoMonthDebitTotalLessTransfers=twoMonthDebitTotalLessTransfers,
            twoMonthDebitTotal=twoMonthDebitTotal,
            sixMonthDebitTotal=sixMonthDebitTotal,
            twelveMonthDebitTotalLessTransfers=twelveMonthDebitTotalLessTransfers,
            _configuration=_configuration,
            **kwargs,
        )

from mastercard_python_sdk.model.cash_flow_monthly_cash_flow_debit_summaries import CashFlowMonthlyCashFlowDebitSummaries