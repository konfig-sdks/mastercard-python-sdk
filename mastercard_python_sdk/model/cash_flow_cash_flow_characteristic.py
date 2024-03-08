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


class CashFlowCashFlowCharacteristic(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "averageMonthlyNetLessTransfers",
            "monthlyCashFlowCharacteristics",
            "averageMonthlyNet",
        }
        
        class properties:
            
            
            class monthlyCashFlowCharacteristics(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['CashFlowMonthlyCashFlowCharacteristics']:
                        return CashFlowMonthlyCashFlowCharacteristics
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['CashFlowMonthlyCashFlowCharacteristics'], typing.List['CashFlowMonthlyCashFlowCharacteristics']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'monthlyCashFlowCharacteristics':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'CashFlowMonthlyCashFlowCharacteristics':
                    return super().__getitem__(i)
            averageMonthlyNet = schemas.NumberSchema
            averageMonthlyNetLessTransfers = schemas.NumberSchema
            twelveMonthTotalNet = schemas.NumberSchema
            twelveMonthTotalNetLessTransfers = schemas.NumberSchema
            sixMonthAverageTotalCreditsLessTotalDebits = schemas.NumberSchema
            sixMonthAverageTotalCreditsLessTotalDebitsLessTransfers = schemas.NumberSchema
            twoMonthAverageTotalCreditsLessTotalDebits = schemas.NumberSchema
            twoMonthAverageTotalCreditsLessTotalDebitsLessTransfers = schemas.NumberSchema
            __annotations__ = {
                "monthlyCashFlowCharacteristics": monthlyCashFlowCharacteristics,
                "averageMonthlyNet": averageMonthlyNet,
                "averageMonthlyNetLessTransfers": averageMonthlyNetLessTransfers,
                "twelveMonthTotalNet": twelveMonthTotalNet,
                "twelveMonthTotalNetLessTransfers": twelveMonthTotalNetLessTransfers,
                "sixMonthAverageTotalCreditsLessTotalDebits": sixMonthAverageTotalCreditsLessTotalDebits,
                "sixMonthAverageTotalCreditsLessTotalDebitsLessTransfers": sixMonthAverageTotalCreditsLessTotalDebitsLessTransfers,
                "twoMonthAverageTotalCreditsLessTotalDebits": twoMonthAverageTotalCreditsLessTotalDebits,
                "twoMonthAverageTotalCreditsLessTotalDebitsLessTransfers": twoMonthAverageTotalCreditsLessTotalDebitsLessTransfers,
            }
    
    averageMonthlyNetLessTransfers: MetaOapg.properties.averageMonthlyNetLessTransfers
    monthlyCashFlowCharacteristics: MetaOapg.properties.monthlyCashFlowCharacteristics
    averageMonthlyNet: MetaOapg.properties.averageMonthlyNet
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["monthlyCashFlowCharacteristics"]) -> MetaOapg.properties.monthlyCashFlowCharacteristics: ...
    
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
    def __getitem__(self, name: typing_extensions.Literal["twoMonthAverageTotalCreditsLessTotalDebitsLessTransfers"]) -> MetaOapg.properties.twoMonthAverageTotalCreditsLessTotalDebitsLessTransfers: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["monthlyCashFlowCharacteristics", "averageMonthlyNet", "averageMonthlyNetLessTransfers", "twelveMonthTotalNet", "twelveMonthTotalNetLessTransfers", "sixMonthAverageTotalCreditsLessTotalDebits", "sixMonthAverageTotalCreditsLessTotalDebitsLessTransfers", "twoMonthAverageTotalCreditsLessTotalDebits", "twoMonthAverageTotalCreditsLessTotalDebitsLessTransfers", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["monthlyCashFlowCharacteristics"]) -> MetaOapg.properties.monthlyCashFlowCharacteristics: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["averageMonthlyNet"]) -> MetaOapg.properties.averageMonthlyNet: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["averageMonthlyNetLessTransfers"]) -> MetaOapg.properties.averageMonthlyNetLessTransfers: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["twelveMonthTotalNet"]) -> typing.Union[MetaOapg.properties.twelveMonthTotalNet, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["twelveMonthTotalNetLessTransfers"]) -> typing.Union[MetaOapg.properties.twelveMonthTotalNetLessTransfers, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sixMonthAverageTotalCreditsLessTotalDebits"]) -> typing.Union[MetaOapg.properties.sixMonthAverageTotalCreditsLessTotalDebits, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sixMonthAverageTotalCreditsLessTotalDebitsLessTransfers"]) -> typing.Union[MetaOapg.properties.sixMonthAverageTotalCreditsLessTotalDebitsLessTransfers, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["twoMonthAverageTotalCreditsLessTotalDebits"]) -> typing.Union[MetaOapg.properties.twoMonthAverageTotalCreditsLessTotalDebits, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["twoMonthAverageTotalCreditsLessTotalDebitsLessTransfers"]) -> typing.Union[MetaOapg.properties.twoMonthAverageTotalCreditsLessTotalDebitsLessTransfers, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["monthlyCashFlowCharacteristics", "averageMonthlyNet", "averageMonthlyNetLessTransfers", "twelveMonthTotalNet", "twelveMonthTotalNetLessTransfers", "sixMonthAverageTotalCreditsLessTotalDebits", "sixMonthAverageTotalCreditsLessTotalDebitsLessTransfers", "twoMonthAverageTotalCreditsLessTotalDebits", "twoMonthAverageTotalCreditsLessTotalDebitsLessTransfers", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        averageMonthlyNetLessTransfers: typing.Union[MetaOapg.properties.averageMonthlyNetLessTransfers, decimal.Decimal, int, float, ],
        monthlyCashFlowCharacteristics: typing.Union[MetaOapg.properties.monthlyCashFlowCharacteristics, list, tuple, ],
        averageMonthlyNet: typing.Union[MetaOapg.properties.averageMonthlyNet, decimal.Decimal, int, float, ],
        twelveMonthTotalNet: typing.Union[MetaOapg.properties.twelveMonthTotalNet, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        twelveMonthTotalNetLessTransfers: typing.Union[MetaOapg.properties.twelveMonthTotalNetLessTransfers, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        sixMonthAverageTotalCreditsLessTotalDebits: typing.Union[MetaOapg.properties.sixMonthAverageTotalCreditsLessTotalDebits, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        sixMonthAverageTotalCreditsLessTotalDebitsLessTransfers: typing.Union[MetaOapg.properties.sixMonthAverageTotalCreditsLessTotalDebitsLessTransfers, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        twoMonthAverageTotalCreditsLessTotalDebits: typing.Union[MetaOapg.properties.twoMonthAverageTotalCreditsLessTotalDebits, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        twoMonthAverageTotalCreditsLessTotalDebitsLessTransfers: typing.Union[MetaOapg.properties.twoMonthAverageTotalCreditsLessTotalDebitsLessTransfers, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CashFlowCashFlowCharacteristic':
        return super().__new__(
            cls,
            *args,
            averageMonthlyNetLessTransfers=averageMonthlyNetLessTransfers,
            monthlyCashFlowCharacteristics=monthlyCashFlowCharacteristics,
            averageMonthlyNet=averageMonthlyNet,
            twelveMonthTotalNet=twelveMonthTotalNet,
            twelveMonthTotalNetLessTransfers=twelveMonthTotalNetLessTransfers,
            sixMonthAverageTotalCreditsLessTotalDebits=sixMonthAverageTotalCreditsLessTotalDebits,
            sixMonthAverageTotalCreditsLessTotalDebitsLessTransfers=sixMonthAverageTotalCreditsLessTotalDebitsLessTransfers,
            twoMonthAverageTotalCreditsLessTotalDebits=twoMonthAverageTotalCreditsLessTotalDebits,
            twoMonthAverageTotalCreditsLessTotalDebitsLessTransfers=twoMonthAverageTotalCreditsLessTotalDebitsLessTransfers,
            _configuration=_configuration,
            **kwargs,
        )

from mastercard_python_sdk.model.cash_flow_monthly_cash_flow_characteristics import CashFlowMonthlyCashFlowCharacteristics
