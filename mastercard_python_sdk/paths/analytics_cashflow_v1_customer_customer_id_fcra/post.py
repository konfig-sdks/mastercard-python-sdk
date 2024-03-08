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

from mastercard_python_sdk.model.balance_and_cash_flow_analytics_report_constraints import BalanceAndCashFlowAnalyticsReportConstraints as BalanceAndCashFlowAnalyticsReportConstraintsSchema
from mastercard_python_sdk.model.obb_error_message import ObbErrorMessage as ObbErrorMessageSchema
from mastercard_python_sdk.model.obb_analytics_report_ack import ObbAnalyticsReportAck as ObbAnalyticsReportAckSchema

from mastercard_python_sdk.type.balance_and_cash_flow_analytics_report_constraints import BalanceAndCashFlowAnalyticsReportConstraints
from mastercard_python_sdk.type.obb_error_message import ObbErrorMessage
from mastercard_python_sdk.type.obb_analytics_report_ack import ObbAnalyticsReportAck

from ...api_client import Dictionary
from mastercard_python_sdk.pydantic.obb_error_message import ObbErrorMessage as ObbErrorMessagePydantic
from mastercard_python_sdk.pydantic.obb_analytics_report_ack import ObbAnalyticsReportAck as ObbAnalyticsReportAckPydantic
from mastercard_python_sdk.pydantic.balance_and_cash_flow_analytics_report_constraints import BalanceAndCashFlowAnalyticsReportConstraints as BalanceAndCashFlowAnalyticsReportConstraintsPydantic

from . import path

# Query params
ReferenceNumberSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'reference-number': typing.Union[ReferenceNumberSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_reference_number = api_client.QueryParameter(
    name="reference-number",
    style=api_client.ParameterStyle.FORM,
    schema=ReferenceNumberSchema,
    explode=True,
)
# Path params
CustomerIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'customerId': typing.Union[CustomerIdSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_customer_id = api_client.PathParameter(
    name="customerId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=CustomerIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = BalanceAndCashFlowAnalyticsReportConstraintsSchema


request_body_balance_and_cash_flow_analytics_report_constraints = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
_auth = [
    'FinicityAppKey',
    'FinicityAppToken',
]
SchemaFor200ResponseBodyApplicationJson = ObbAnalyticsReportAckSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ObbAnalyticsReportAck


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ObbAnalyticsReportAck


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = ObbErrorMessageSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: ObbErrorMessage


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: ObbErrorMessage


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor401ResponseBodyApplicationJson = ObbErrorMessageSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: ObbErrorMessage


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: ObbErrorMessage


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
)
SchemaFor403ResponseBodyApplicationJson = ObbErrorMessageSchema


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: ObbErrorMessage


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: ObbErrorMessage


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationJson),
    },
)
SchemaFor404ResponseBodyApplicationJson = ObbErrorMessageSchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: ObbErrorMessage


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: ObbErrorMessage


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
    },
)
SchemaFor409ResponseBodyApplicationJson = ObbErrorMessageSchema


@dataclass
class ApiResponseFor409(api_client.ApiResponse):
    body: ObbErrorMessage


@dataclass
class ApiResponseFor409Async(api_client.AsyncApiResponse):
    body: ObbErrorMessage


_response_for_409 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor409,
    response_cls_async=ApiResponseFor409Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor409ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '401': _response_for_401,
    '403': _response_for_403,
    '404': _response_for_404,
    '409': _response_for_409,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _generate_fcra_analytics_report_mapped_args(
        self,
        customer_id: str,
        account_ids: typing.Optional[typing.List[int]] = None,
        length_of_report: typing.Optional[int] = None,
        reference_number: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        _body = {}
        if account_ids is not None:
            _body["accountIds"] = account_ids
        if length_of_report is not None:
            _body["lengthOfReport"] = length_of_report
        args.body = _body
        if reference_number is not None:
            _query_params["reference-number"] = reference_number
        if customer_id is not None:
            _path_params["customerId"] = customer_id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _agenerate_fcra_analytics_report_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Generate Cash Flow Analytics - FCRA
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_customer_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_reference_number,
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
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/analytics/cashflow/v1/customer/{customerId}/fcra',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_balance_and_cash_flow_analytics_report_constraints.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
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


    def _generate_fcra_analytics_report_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Generate Cash Flow Analytics - FCRA
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_customer_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_reference_number,
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
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/analytics/cashflow/v1/customer/{customerId}/fcra',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_balance_and_cash_flow_analytics_report_constraints.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
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


class GenerateFcraAnalyticsReportRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def agenerate_fcra_analytics_report(
        self,
        customer_id: str,
        account_ids: typing.Optional[typing.List[int]] = None,
        length_of_report: typing.Optional[int] = None,
        reference_number: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._generate_fcra_analytics_report_mapped_args(
            customer_id=customer_id,
            account_ids=account_ids,
            length_of_report=length_of_report,
            reference_number=reference_number,
        )
        return await self._agenerate_fcra_analytics_report_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def generate_fcra_analytics_report(
        self,
        customer_id: str,
        account_ids: typing.Optional[typing.List[int]] = None,
        length_of_report: typing.Optional[int] = None,
        reference_number: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._generate_fcra_analytics_report_mapped_args(
            customer_id=customer_id,
            account_ids=account_ids,
            length_of_report=length_of_report,
            reference_number=reference_number,
        )
        return self._generate_fcra_analytics_report_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
        )

class GenerateFcraAnalyticsReport(BaseApi):

    async def agenerate_fcra_analytics_report(
        self,
        customer_id: str,
        account_ids: typing.Optional[typing.List[int]] = None,
        length_of_report: typing.Optional[int] = None,
        reference_number: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> ObbAnalyticsReportAckPydantic:
        raw_response = await self.raw.agenerate_fcra_analytics_report(
            customer_id=customer_id,
            account_ids=account_ids,
            length_of_report=length_of_report,
            reference_number=reference_number,
            **kwargs,
        )
        if validate:
            return ObbAnalyticsReportAckPydantic(**raw_response.body)
        return api_client.construct_model_instance(ObbAnalyticsReportAckPydantic, raw_response.body)
    
    
    def generate_fcra_analytics_report(
        self,
        customer_id: str,
        account_ids: typing.Optional[typing.List[int]] = None,
        length_of_report: typing.Optional[int] = None,
        reference_number: typing.Optional[str] = None,
        validate: bool = False,
    ) -> ObbAnalyticsReportAckPydantic:
        raw_response = self.raw.generate_fcra_analytics_report(
            customer_id=customer_id,
            account_ids=account_ids,
            length_of_report=length_of_report,
            reference_number=reference_number,
        )
        if validate:
            return ObbAnalyticsReportAckPydantic(**raw_response.body)
        return api_client.construct_model_instance(ObbAnalyticsReportAckPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        customer_id: str,
        account_ids: typing.Optional[typing.List[int]] = None,
        length_of_report: typing.Optional[int] = None,
        reference_number: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._generate_fcra_analytics_report_mapped_args(
            customer_id=customer_id,
            account_ids=account_ids,
            length_of_report=length_of_report,
            reference_number=reference_number,
        )
        return await self._agenerate_fcra_analytics_report_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        customer_id: str,
        account_ids: typing.Optional[typing.List[int]] = None,
        length_of_report: typing.Optional[int] = None,
        reference_number: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._generate_fcra_analytics_report_mapped_args(
            customer_id=customer_id,
            account_ids=account_ids,
            length_of_report=length_of_report,
            reference_number=reference_number,
        )
        return self._generate_fcra_analytics_report_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
        )

