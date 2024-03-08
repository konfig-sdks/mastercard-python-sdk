# coding: utf-8

"""
    Open Banking

    OpenAPI specification for Finicity APIs.  Open Banking solutions in the US are provided by Finicity, a Mastercard company.

    The version of the OpenAPI document: 1.16.0
    Contact: apisupport@mastercard.com
    Created by: https://developer.mastercard.com/open-banking-us/documentation/support/
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from mastercard_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from mastercard_python_sdk.api_response import AsyncGeneratorResponse
from mastercard_python_sdk import api_client, exceptions
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

from mastercard_python_sdk.model.error_message import ErrorMessage as ErrorMessageSchema
from mastercard_python_sdk.model.certified_institutions import CertifiedInstitutions as CertifiedInstitutionsSchema

from mastercard_python_sdk.type.certified_institutions import CertifiedInstitutions
from mastercard_python_sdk.type.error_message import ErrorMessage

from ...api_client import Dictionary
from mastercard_python_sdk.pydantic.error_message import ErrorMessage as ErrorMessagePydantic
from mastercard_python_sdk.pydantic.certified_institutions import CertifiedInstitutions as CertifiedInstitutionsPydantic

# Query params
SearchSchema = schemas.StrSchema
StartSchema = schemas.Int32Schema


class LimitSchema(
    schemas.Int32Schema
):
    pass
TypeSchema = schemas.StrSchema


class SupportedCountriesSchema(
    schemas.ListSchema
):


    class MetaOapg:
        
        
        class items(
            schemas.StrSchema
        ):
            pass

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'SupportedCountriesSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'search': typing.Union[SearchSchema, str, ],
        'start': typing.Union[StartSchema, decimal.Decimal, int, ],
        'limit': typing.Union[LimitSchema, decimal.Decimal, int, ],
        'type': typing.Union[TypeSchema, str, ],
        'supportedCountries': typing.Union[SupportedCountriesSchema, list, tuple, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_search = api_client.QueryParameter(
    name="search",
    style=api_client.ParameterStyle.FORM,
    schema=SearchSchema,
    explode=True,
)
request_query_start = api_client.QueryParameter(
    name="start",
    style=api_client.ParameterStyle.FORM,
    schema=StartSchema,
    explode=True,
)
request_query_limit = api_client.QueryParameter(
    name="limit",
    style=api_client.ParameterStyle.FORM,
    schema=LimitSchema,
    explode=True,
)
request_query_type = api_client.QueryParameter(
    name="type",
    style=api_client.ParameterStyle.FORM,
    schema=TypeSchema,
    explode=True,
)
request_query_supported_countries = api_client.QueryParameter(
    name="supportedCountries",
    style=api_client.ParameterStyle.FORM,
    schema=SupportedCountriesSchema,
)
SchemaFor200ResponseBodyApplicationJson = CertifiedInstitutionsSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: CertifiedInstitutions


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: CertifiedInstitutions


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = ErrorMessageSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: ErrorMessage


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: ErrorMessage


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor401ResponseBodyApplicationJson = ErrorMessageSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: ErrorMessage


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: ErrorMessage


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _list_certified_institutions_mapped_args(
        self,
        search: typing.Optional[str] = None,
        start: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        type: typing.Optional[str] = None,
        supported_countries: typing.Optional[typing.List[str]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if search is not None:
            _query_params["search"] = search
        if start is not None:
            _query_params["start"] = start
        if limit is not None:
            _query_params["limit"] = limit
        if type is not None:
            _query_params["type"] = type
        if supported_countries is not None:
            _query_params["supportedCountries"] = supported_countries
        args.query = _query_params
        return args

    async def _alist_certified_institutions_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Get Certified Institutions
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_search,
            request_query_start,
            request_query_limit,
            request_query_type,
            request_query_supported_countries,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/institution/v2/certifiedInstitutions',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _list_certified_institutions_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Get Certified Institutions
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_search,
            request_query_start,
            request_query_limit,
            request_query_type,
            request_query_supported_countries,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/institution/v2/certifiedInstitutions',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class ListCertifiedInstitutionsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def alist_certified_institutions(
        self,
        search: typing.Optional[str] = None,
        start: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        type: typing.Optional[str] = None,
        supported_countries: typing.Optional[typing.List[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_certified_institutions_mapped_args(
            search=search,
            start=start,
            limit=limit,
            type=type,
            supported_countries=supported_countries,
        )
        return await self._alist_certified_institutions_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def list_certified_institutions(
        self,
        search: typing.Optional[str] = None,
        start: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        type: typing.Optional[str] = None,
        supported_countries: typing.Optional[typing.List[str]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_certified_institutions_mapped_args(
            search=search,
            start=start,
            limit=limit,
            type=type,
            supported_countries=supported_countries,
        )
        return self._list_certified_institutions_oapg(
            query_params=args.query,
        )

class ListCertifiedInstitutions(BaseApi):

    async def alist_certified_institutions(
        self,
        search: typing.Optional[str] = None,
        start: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        type: typing.Optional[str] = None,
        supported_countries: typing.Optional[typing.List[str]] = None,
        validate: bool = False,
        **kwargs,
    ) -> CertifiedInstitutionsPydantic:
        raw_response = await self.raw.alist_certified_institutions(
            search=search,
            start=start,
            limit=limit,
            type=type,
            supported_countries=supported_countries,
            **kwargs,
        )
        if validate:
            return CertifiedInstitutionsPydantic(**raw_response.body)
        return api_client.construct_model_instance(CertifiedInstitutionsPydantic, raw_response.body)
    
    
    def list_certified_institutions(
        self,
        search: typing.Optional[str] = None,
        start: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        type: typing.Optional[str] = None,
        supported_countries: typing.Optional[typing.List[str]] = None,
        validate: bool = False,
    ) -> CertifiedInstitutionsPydantic:
        raw_response = self.raw.list_certified_institutions(
            search=search,
            start=start,
            limit=limit,
            type=type,
            supported_countries=supported_countries,
        )
        if validate:
            return CertifiedInstitutionsPydantic(**raw_response.body)
        return api_client.construct_model_instance(CertifiedInstitutionsPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        search: typing.Optional[str] = None,
        start: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        type: typing.Optional[str] = None,
        supported_countries: typing.Optional[typing.List[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_certified_institutions_mapped_args(
            search=search,
            start=start,
            limit=limit,
            type=type,
            supported_countries=supported_countries,
        )
        return await self._alist_certified_institutions_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        search: typing.Optional[str] = None,
        start: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        type: typing.Optional[str] = None,
        supported_countries: typing.Optional[typing.List[str]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_certified_institutions_mapped_args(
            search=search,
            start=start,
            limit=limit,
            type=type,
            supported_countries=supported_countries,
        )
        return self._list_certified_institutions_oapg(
            query_params=args.query,
        )

