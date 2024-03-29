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


class CashFlowCashFlowCharacteristicsSummary(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "sixMonthAverageTotalCreditsLessTotalDebits",
            "sixMonthAverageTotalCreditsLessTotalDebitsLessTransfers",
            "twelveMonthTotalNet",
            "averageMonthlyNetLessTransfers",
            "twelveMonthTotalNetLessTransfers",
            "twoMonthAverageTotalCreditsLessTotalDebits",
            "averageMonthlyNet",
        }
        
        class properties:
            averageMonthlyNet = schemas.NumberSchema
            averageMonthlyNetLessTransfers = schemas.NumberSchema
            twelveMonthTotalNet = schemas.NumberSchema
            twelveMonthTotalNetLessTransfers = schemas.NumberSchema
            sixMonthAverageTotalCreditsLessTotalDebits = schemas.NumberSchema
            sixMonthAverageTotalCreditsLessTotalDebitsLessTransfers = schemas.NumberSchema
            twoMonthAverageTotalCreditsLessTotalDebits = schemas.NumberSchema
            
            
            class monthlyCashFlowCharacteristicsSummaries(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['CashFlowMonthlyCashFlowCharacteristicsSummaries']:
                        return CashFlowMonthlyCashFlowCharacteristicsSummaries
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['CashFlowMonthlyCashFlowCharacteristicsSummaries'], typing.List['CashFlowMonthlyCashFlowCharacteristicsSummaries']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'monthlyCashFlowCharacteristicsSummaries':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'CashFlowMonthlyCashFlowCharacteristicsSummaries':
                    return super().__getitem__(i)
            twoMonthAverageTotalCreditsLessTotalDebitsLessTransfers = schemas.NumberSchema
            __annotations__ = {
                "averageMonthlyNet": averageMonthlyNet,
                "averageMonthlyNetLessTransfers": averageMonthlyNetLessTransfers,
                "twelveMonthTotalNet": twelveMonthTotalNet,
                "twelveMonthTotalNetLessTransfers": twelveMonthTotalNetLessTransfers,
                "sixMonthAverageTotalCreditsLessTotalDebits": sixMonthAverageTotalCreditsLessTotalDebits,
                "sixMonthAverageTotalCreditsLessTotalDebitsLessTransfers": sixMonthAverageTotalCreditsLessTotalDebitsLessTransfers,
                "twoMonthAverageTotalCreditsLessTotalDebits": twoMonthAverageTotalCreditsLessTotalDebits,
                "monthlyCashFlowCharacteristicsSummaries": monthlyCashFlowCharacteristicsSummaries,
                "twoMonthAverageTotalCreditsLessTotalDebitsLessTransfers": twoMonthAverageTotalCreditsLessTotalDebitsLessTransfers,
            }
    
    sixMonthAverageTotalCreditsLessTotalDebits: MetaOapg.properties.sixMonthAverageTotalCreditsLessTotalDebits
    sixMonthAverageTotalCreditsLessTotalDebitsLessTransfers: MetaOapg.properties.sixMonthAverageTotalCreditsLessTotalDebitsLessTransfers
    twelveMonthTotalNet: MetaOapg.properties.twelveMonthTotalNet
    averageMonthlyNetLessTransfers: MetaOapg.properties.averageMonthlyNetLessTransfers
    twelveMonthTotalNetLessTransfers: MetaOapg.properties.twelveMonthTotalNetLessTransfers
    twoMonthAverageTotalCreditsLessTotalDebits: MetaOapg.properties.twoMonthAverageTotalCreditsLessTotalDebits
    averageMonthlyNet: MetaOapg.properties.averageMonthlyNet
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["averageMonthlyNet"]) -> MetaOapg.properties.averageMonthlyNet: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["averageMonthlyNetLessTransfers"]) -> MetaOapg.properties.averageMonthlyNetLessTransfers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["twelveMonthTotalNet"]) -> MetaOapg.properties.twelveMonthTotalNet: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["twelveMonthTotalNetLessTransfers"]) -> MetaOapg.properties.twelveMonthTotalNetLessTransfers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sixMonthAverageTotalCreditsLessTotalDebits"]) -> MetaOapg.properties.sixMonthAverageTotalCreditsLessTotalDebits: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sixMonthAverageTotalCreditsLessTotalDebitsLessTransfers"]) -> MetaOapg.properties.sixMonthAverageTotalCreditsLessTotalDebitsLessTransfers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["twoMonthAverageTotalCreditsLessTotalDebits"]) -> MetaOapg.properties.twoMonthAverageTotalCreditsLessTotalDebits: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["monthlyCashFlowCharacteristicsSummaries"]) -> MetaOapg.properties.monthlyCashFlowCharacteristicsSummaries: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["twoMonthAverageTotalCreditsLessTotalDebitsLessTransfers"]) -> MetaOapg.properties.twoMonthAverageTotalCreditsLessTotalDebitsLessTransfers: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["averageMonthlyNet", "averageMonthlyNetLessTransfers", "twelveMonthTotalNet", "twelveMonthTotalNetLessTransfers", "sixMonthAverageTotalCreditsLessTotalDebits", "sixMonthAverageTotalCreditsLessTotalDebitsLessTransfers", "twoMonthAverageTotalCreditsLessTotalDebits", "monthlyCashFlowCharacteristicsSummaries", "twoMonthAverageTotalCreditsLessTotalDebitsLessTransfers", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["averageMonthlyNet"]) -> MetaOapg.properties.averageMonthlyNet: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["averageMonthlyNetLessTransfers"]) -> MetaOapg.properties.averageMonthlyNetLessTransfers: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["twelveMonthTotalNet"]) -> MetaOapg.properties.twelveMonthTotalNet: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["twelveMonthTotalNetLessTransfers"]) -> MetaOapg.properties.twelveMonthTotalNetLessTransfers: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sixMonthAverageTotalCreditsLessTotalDebits"]) -> MetaOapg.properties.sixMonthAverageTotalCreditsLessTotalDebits: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sixMonthAverageTotalCreditsLessTotalDebitsLessTransfers"]) -> MetaOapg.properties.sixMonthAverageTotalCreditsLessTotalDebitsLessTransfers: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["twoMonthAverageTotalCreditsLessTotalDebits"]) -> MetaOapg.properties.twoMonthAverageTotalCreditsLessTotalDebits: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["monthlyCashFlowCharacteristicsSummaries"]) -> typing.Union[MetaOapg.properties.monthlyCashFlowCharacteristicsSummaries, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["twoMonthAverageTotalCreditsLessTotalDebitsLessTransfers"]) -> typing.Union[MetaOapg.properties.twoMonthAverageTotalCreditsLessTotalDebitsLessTransfers, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["averageMonthlyNet", "averageMonthlyNetLessTransfers", "twelveMonthTotalNet", "twelveMonthTotalNetLessTransfers", "sixMonthAverageTotalCreditsLessTotalDebits", "sixMonthAverageTotalCreditsLessTotalDebitsLessTransfers", "twoMonthAverageTotalCreditsLessTotalDebits", "monthlyCashFlowCharacteristicsSummaries", "twoMonthAverageTotalCreditsLessTotalDebitsLessTransfers", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        sixMonthAverageTotalCreditsLessTotalDebits: typing.Union[MetaOapg.properties.sixMonthAverageTotalCreditsLessTotalDebits, decimal.Decimal, int, float, ],
        sixMonthAverageTotalCreditsLessTotalDebitsLessTransfers: typing.Union[MetaOapg.properties.sixMonthAverageTotalCreditsLessTotalDebitsLessTransfers, decimal.Decimal, int, float, ],
        twelveMonthTotalNet: typing.Union[MetaOapg.properties.twelveMonthTotalNet, decimal.Decimal, int, float, ],
        averageMonthlyNetLessTransfers: typing.Union[MetaOapg.properties.averageMonthlyNetLessTransfers, decimal.Decimal, int, float, ],
        twelveMonthTotalNetLessTransfers: typing.Union[MetaOapg.properties.twelveMonthTotalNetLessTransfers, decimal.Decimal, int, float, ],
        twoMonthAverageTotalCreditsLessTotalDebits: typing.Union[MetaOapg.properties.twoMonthAverageTotalCreditsLessTotalDebits, decimal.Decimal, int, float, ],
        averageMonthlyNet: typing.Union[MetaOapg.properties.averageMonthlyNet, decimal.Decimal, int, float, ],
        monthlyCashFlowCharacteristicsSummaries: typing.Union[MetaOapg.properties.monthlyCashFlowCharacteristicsSummaries, list, tuple, schemas.Unset] = schemas.unset,
        twoMonthAverageTotalCreditsLessTotalDebitsLessTransfers: typing.Union[MetaOapg.properties.twoMonthAverageTotalCreditsLessTotalDebitsLessTransfers, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CashFlowCashFlowCharacteristicsSummary':
        return super().__new__(
            cls,
            *args,
            sixMonthAverageTotalCreditsLessTotalDebits=sixMonthAverageTotalCreditsLessTotalDebits,
            sixMonthAverageTotalCreditsLessTotalDebitsLessTransfers=sixMonthAverageTotalCreditsLessTotalDebitsLessTransfers,
            twelveMonthTotalNet=twelveMonthTotalNet,
            averageMonthlyNetLessTransfers=averageMonthlyNetLessTransfers,
            twelveMonthTotalNetLessTransfers=twelveMonthTotalNetLessTransfers,
            twoMonthAverageTotalCreditsLessTotalDebits=twoMonthAverageTotalCreditsLessTotalDebits,
            averageMonthlyNet=averageMonthlyNet,
            monthlyCashFlowCharacteristicsSummaries=monthlyCashFlowCharacteristicsSummaries,
            twoMonthAverageTotalCreditsLessTotalDebitsLessTransfers=twoMonthAverageTotalCreditsLessTotalDebitsLessTransfers,
            _configuration=_configuration,
            **kwargs,
        )

from mastercard_python_sdk.model.cash_flow_monthly_cash_flow_characteristics_summaries import CashFlowMonthlyCashFlowCharacteristicsSummaries
