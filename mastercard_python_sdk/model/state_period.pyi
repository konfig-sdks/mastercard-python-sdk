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


class StatePeriod(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Statistics for one period in the report of a StateAttribute.
    """


    class MetaOapg:
        required = {
            "endingValue",
            "endDate",
            "count",
            "startDate",
            "beginningValue",
        }
        
        class properties:
            beginningValue = schemas.NumberSchema
            count = schemas.IntSchema
            endDate = schemas.DateSchema
            endingValue = schemas.NumberSchema
            startDate = schemas.DateSchema
            max = schemas.NumberSchema
            mean = schemas.NumberSchema
            median = schemas.NumberSchema
            min = schemas.NumberSchema
            standardDeviation = schemas.NumberSchema
            sum = schemas.NumberSchema
            __annotations__ = {
                "beginningValue": beginningValue,
                "count": count,
                "endDate": endDate,
                "endingValue": endingValue,
                "startDate": startDate,
                "max": max,
                "mean": mean,
                "median": median,
                "min": min,
                "standardDeviation": standardDeviation,
                "sum": sum,
            }
    
    endingValue: MetaOapg.properties.endingValue
    endDate: MetaOapg.properties.endDate
    count: MetaOapg.properties.count
    startDate: MetaOapg.properties.startDate
    beginningValue: MetaOapg.properties.beginningValue
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["beginningValue"]) -> MetaOapg.properties.beginningValue: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["count"]) -> MetaOapg.properties.count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endDate"]) -> MetaOapg.properties.endDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endingValue"]) -> MetaOapg.properties.endingValue: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startDate"]) -> MetaOapg.properties.startDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["max"]) -> MetaOapg.properties.max: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mean"]) -> MetaOapg.properties.mean: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["median"]) -> MetaOapg.properties.median: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["min"]) -> MetaOapg.properties.min: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["standardDeviation"]) -> MetaOapg.properties.standardDeviation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sum"]) -> MetaOapg.properties.sum: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["beginningValue", "count", "endDate", "endingValue", "startDate", "max", "mean", "median", "min", "standardDeviation", "sum", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["beginningValue"]) -> MetaOapg.properties.beginningValue: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["count"]) -> MetaOapg.properties.count: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endDate"]) -> MetaOapg.properties.endDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endingValue"]) -> MetaOapg.properties.endingValue: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startDate"]) -> MetaOapg.properties.startDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["max"]) -> typing.Union[MetaOapg.properties.max, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mean"]) -> typing.Union[MetaOapg.properties.mean, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["median"]) -> typing.Union[MetaOapg.properties.median, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["min"]) -> typing.Union[MetaOapg.properties.min, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["standardDeviation"]) -> typing.Union[MetaOapg.properties.standardDeviation, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sum"]) -> typing.Union[MetaOapg.properties.sum, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["beginningValue", "count", "endDate", "endingValue", "startDate", "max", "mean", "median", "min", "standardDeviation", "sum", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        endingValue: typing.Union[MetaOapg.properties.endingValue, decimal.Decimal, int, float, ],
        endDate: typing.Union[MetaOapg.properties.endDate, str, date, ],
        count: typing.Union[MetaOapg.properties.count, decimal.Decimal, int, ],
        startDate: typing.Union[MetaOapg.properties.startDate, str, date, ],
        beginningValue: typing.Union[MetaOapg.properties.beginningValue, decimal.Decimal, int, float, ],
        max: typing.Union[MetaOapg.properties.max, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        mean: typing.Union[MetaOapg.properties.mean, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        median: typing.Union[MetaOapg.properties.median, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        min: typing.Union[MetaOapg.properties.min, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        standardDeviation: typing.Union[MetaOapg.properties.standardDeviation, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        sum: typing.Union[MetaOapg.properties.sum, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'StatePeriod':
        return super().__new__(
            cls,
            *args,
            endingValue=endingValue,
            endDate=endDate,
            count=count,
            startDate=startDate,
            beginningValue=beginningValue,
            max=max,
            mean=mean,
            median=median,
            min=min,
            standardDeviation=standardDeviation,
            sum=sum,
            _configuration=_configuration,
            **kwargs,
        )
