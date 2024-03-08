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

from mastercard_python_sdk.model.business import Business as BusinessSchema
from mastercard_python_sdk.model.phone_number_format import PhoneNumberFormat as PhoneNumberFormatSchema
from mastercard_python_sdk.model.new_business import NewBusiness as NewBusinessSchema
from mastercard_python_sdk.model.error_message import ErrorMessage as ErrorMessageSchema
from mastercard_python_sdk.model.new_address import NewAddress as NewAddressSchema

from mastercard_python_sdk.type.new_address import NewAddress
from mastercard_python_sdk.type.business import Business
from mastercard_python_sdk.type.new_business import NewBusiness
from mastercard_python_sdk.type.phone_number_format import PhoneNumberFormat
from mastercard_python_sdk.type.error_message import ErrorMessage

from ...api_client import Dictionary
from mastercard_python_sdk.pydantic.business import Business as BusinessPydantic
from mastercard_python_sdk.pydantic.new_address import NewAddress as NewAddressPydantic
from mastercard_python_sdk.pydantic.error_message import ErrorMessage as ErrorMessagePydantic
from mastercard_python_sdk.pydantic.phone_number_format import PhoneNumberFormat as PhoneNumberFormatPydantic
from mastercard_python_sdk.pydantic.new_business import NewBusiness as NewBusinessPydantic

from . import path

# Path params
CustomerIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'customer_id': typing.Union[CustomerIdSchema, str, ],
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
    name="customer_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=CustomerIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = NewBusinessSchema


request_body_new_business = api_client.RequestBody(
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
SchemaFor200ResponseBodyApplicationJson = BusinessSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: Business


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: Business


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor404ResponseBodyApplicationJson = ErrorMessageSchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: ErrorMessage


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: ErrorMessage


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
    },
)
SchemaFor409ResponseBodyApplicationJson = ErrorMessageSchema


@dataclass
class ApiResponseFor409(api_client.ApiResponse):
    body: ErrorMessage


@dataclass
class ApiResponseFor409Async(api_client.AsyncApiResponse):
    body: ErrorMessage


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
    '404': _response_for_404,
    '409': _response_for_409,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_new_business_mapped_args(
        self,
        name: str,
        personally_liable: bool,
        address: NewAddress,
        phone_number: PhoneNumberFormat,
        customer_id: str,
        url: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        tax_id: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if name is not None:
            _body["name"] = name
        if personally_liable is not None:
            _body["personallyLiable"] = personally_liable
        if address is not None:
            _body["address"] = address
        if phone_number is not None:
            _body["phoneNumber"] = phone_number
        if url is not None:
            _body["url"] = url
        if email is not None:
            _body["email"] = email
        if type is not None:
            _body["type"] = type
        if tax_id is not None:
            _body["taxId"] = tax_id
        args.body = _body
        if customer_id is not None:
            _path_params["customer_id"] = customer_id
        args.path = _path_params
        return args

    async def _acreate_new_business_oapg(
        self,
        body: typing.Any = None,
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
        Create a New Business for a Customer
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
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
            path_template='/business-services/customers/{customer_id}/businesses',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_new_business.serialize(body, content_type)
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


    def _create_new_business_oapg(
        self,
        body: typing.Any = None,
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
        Create a New Business for a Customer
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
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
            path_template='/business-services/customers/{customer_id}/businesses',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_new_business.serialize(body, content_type)
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


class CreateNewBusinessRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_new_business(
        self,
        name: str,
        personally_liable: bool,
        address: NewAddress,
        phone_number: PhoneNumberFormat,
        customer_id: str,
        url: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        tax_id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_business_mapped_args(
            name=name,
            personally_liable=personally_liable,
            address=address,
            phone_number=phone_number,
            customer_id=customer_id,
            url=url,
            email=email,
            type=type,
            tax_id=tax_id,
        )
        return await self._acreate_new_business_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def create_new_business(
        self,
        name: str,
        personally_liable: bool,
        address: NewAddress,
        phone_number: PhoneNumberFormat,
        customer_id: str,
        url: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        tax_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_business_mapped_args(
            name=name,
            personally_liable=personally_liable,
            address=address,
            phone_number=phone_number,
            customer_id=customer_id,
            url=url,
            email=email,
            type=type,
            tax_id=tax_id,
        )
        return self._create_new_business_oapg(
            body=args.body,
            path_params=args.path,
        )

class CreateNewBusiness(BaseApi):

    async def acreate_new_business(
        self,
        name: str,
        personally_liable: bool,
        address: NewAddress,
        phone_number: PhoneNumberFormat,
        customer_id: str,
        url: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        tax_id: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> BusinessPydantic:
        raw_response = await self.raw.acreate_new_business(
            name=name,
            personally_liable=personally_liable,
            address=address,
            phone_number=phone_number,
            customer_id=customer_id,
            url=url,
            email=email,
            type=type,
            tax_id=tax_id,
            **kwargs,
        )
        if validate:
            return RootModel[BusinessPydantic](raw_response.body).root
        return api_client.construct_model_instance(BusinessPydantic, raw_response.body)
    
    
    def create_new_business(
        self,
        name: str,
        personally_liable: bool,
        address: NewAddress,
        phone_number: PhoneNumberFormat,
        customer_id: str,
        url: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        tax_id: typing.Optional[str] = None,
        validate: bool = False,
    ) -> BusinessPydantic:
        raw_response = self.raw.create_new_business(
            name=name,
            personally_liable=personally_liable,
            address=address,
            phone_number=phone_number,
            customer_id=customer_id,
            url=url,
            email=email,
            type=type,
            tax_id=tax_id,
        )
        if validate:
            return RootModel[BusinessPydantic](raw_response.body).root
        return api_client.construct_model_instance(BusinessPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        name: str,
        personally_liable: bool,
        address: NewAddress,
        phone_number: PhoneNumberFormat,
        customer_id: str,
        url: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        tax_id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_business_mapped_args(
            name=name,
            personally_liable=personally_liable,
            address=address,
            phone_number=phone_number,
            customer_id=customer_id,
            url=url,
            email=email,
            type=type,
            tax_id=tax_id,
        )
        return await self._acreate_new_business_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        name: str,
        personally_liable: bool,
        address: NewAddress,
        phone_number: PhoneNumberFormat,
        customer_id: str,
        url: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        tax_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_business_mapped_args(
            name=name,
            personally_liable=personally_liable,
            address=address,
            phone_number=phone_number,
            customer_id=customer_id,
            url=url,
            email=email,
            type=type,
            tax_id=tax_id,
        )
        return self._create_new_business_oapg(
            body=args.body,
            path_params=args.path,
        )

