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

from mastercard_python_sdk.model.birthday import Birthday as BirthdaySchema
from mastercard_python_sdk.model.error_message import ErrorMessage as ErrorMessageSchema
from mastercard_python_sdk.model.consumer_update import ConsumerUpdate as ConsumerUpdateSchema

from mastercard_python_sdk.type.consumer_update import ConsumerUpdate
from mastercard_python_sdk.type.birthday import Birthday
from mastercard_python_sdk.type.error_message import ErrorMessage

from ...api_client import Dictionary
from mastercard_python_sdk.pydantic.consumer_update import ConsumerUpdate as ConsumerUpdatePydantic
from mastercard_python_sdk.pydantic.error_message import ErrorMessage as ErrorMessagePydantic
from mastercard_python_sdk.pydantic.birthday import Birthday as BirthdayPydantic

from . import path

# Path params
ConsumerIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'consumerId': typing.Union[ConsumerIdSchema, str, ],
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


request_path_consumer_id = api_client.PathParameter(
    name="consumerId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ConsumerIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = ConsumerUpdateSchema


request_body_consumer_update = api_client.RequestBody(
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


@dataclass
class ApiResponseFor204(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor204Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_204 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor204,
    response_cls_async=ApiResponseFor204Async,
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
_status_code_to_response = {
    '204': _response_for_204,
    '400': _response_for_400,
    '401': _response_for_401,
    '404': _response_for_404,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _modify_by_id_mapped_args(
        self,
        consumer_id: str,
        first_name: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        address: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        zip: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        ssn: typing.Optional[str] = None,
        birthday: typing.Optional[Birthday] = None,
        email: typing.Optional[str] = None,
        suffix: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if first_name is not None:
            _body["firstName"] = first_name
        if last_name is not None:
            _body["lastName"] = last_name
        if address is not None:
            _body["address"] = address
        if city is not None:
            _body["city"] = city
        if state is not None:
            _body["state"] = state
        if zip is not None:
            _body["zip"] = zip
        if phone is not None:
            _body["phone"] = phone
        if ssn is not None:
            _body["ssn"] = ssn
        if birthday is not None:
            _body["birthday"] = birthday
        if email is not None:
            _body["email"] = email
        if suffix is not None:
            _body["suffix"] = suffix
        args.body = _body
        if consumer_id is not None:
            _path_params["consumerId"] = consumer_id
        args.path = _path_params
        return args

    async def _amodify_by_id_oapg(
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
        ApiResponseFor204Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Modify Consumer by ID
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_consumer_id,
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
        method = 'put'.upper()
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
            path_template='/decisioning/v1/consumers/{consumerId}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_consumer_update.serialize(body, content_type)
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


    def _modify_by_id_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor204,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Modify Consumer by ID
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_consumer_id,
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
        method = 'put'.upper()
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
            path_template='/decisioning/v1/consumers/{consumerId}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_consumer_update.serialize(body, content_type)
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


class ModifyByIdRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def amodify_by_id(
        self,
        consumer_id: str,
        first_name: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        address: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        zip: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        ssn: typing.Optional[str] = None,
        birthday: typing.Optional[Birthday] = None,
        email: typing.Optional[str] = None,
        suffix: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor204Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._modify_by_id_mapped_args(
            consumer_id=consumer_id,
            first_name=first_name,
            last_name=last_name,
            address=address,
            city=city,
            state=state,
            zip=zip,
            phone=phone,
            ssn=ssn,
            birthday=birthday,
            email=email,
            suffix=suffix,
        )
        return await self._amodify_by_id_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def modify_by_id(
        self,
        consumer_id: str,
        first_name: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        address: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        zip: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        ssn: typing.Optional[str] = None,
        birthday: typing.Optional[Birthday] = None,
        email: typing.Optional[str] = None,
        suffix: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor204,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._modify_by_id_mapped_args(
            consumer_id=consumer_id,
            first_name=first_name,
            last_name=last_name,
            address=address,
            city=city,
            state=state,
            zip=zip,
            phone=phone,
            ssn=ssn,
            birthday=birthday,
            email=email,
            suffix=suffix,
        )
        return self._modify_by_id_oapg(
            body=args.body,
            path_params=args.path,
        )

class ModifyById(BaseApi):

    async def amodify_by_id(
        self,
        consumer_id: str,
        first_name: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        address: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        zip: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        ssn: typing.Optional[str] = None,
        birthday: typing.Optional[Birthday] = None,
        email: typing.Optional[str] = None,
        suffix: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.amodify_by_id(
            consumer_id=consumer_id,
            first_name=first_name,
            last_name=last_name,
            address=address,
            city=city,
            state=state,
            zip=zip,
            phone=phone,
            ssn=ssn,
            birthday=birthday,
            email=email,
            suffix=suffix,
            **kwargs,
        )
    
    
    def modify_by_id(
        self,
        consumer_id: str,
        first_name: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        address: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        zip: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        ssn: typing.Optional[str] = None,
        birthday: typing.Optional[Birthday] = None,
        email: typing.Optional[str] = None,
        suffix: typing.Optional[str] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.modify_by_id(
            consumer_id=consumer_id,
            first_name=first_name,
            last_name=last_name,
            address=address,
            city=city,
            state=state,
            zip=zip,
            phone=phone,
            ssn=ssn,
            birthday=birthday,
            email=email,
            suffix=suffix,
        )


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aput(
        self,
        consumer_id: str,
        first_name: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        address: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        zip: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        ssn: typing.Optional[str] = None,
        birthday: typing.Optional[Birthday] = None,
        email: typing.Optional[str] = None,
        suffix: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor204Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._modify_by_id_mapped_args(
            consumer_id=consumer_id,
            first_name=first_name,
            last_name=last_name,
            address=address,
            city=city,
            state=state,
            zip=zip,
            phone=phone,
            ssn=ssn,
            birthday=birthday,
            email=email,
            suffix=suffix,
        )
        return await self._amodify_by_id_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def put(
        self,
        consumer_id: str,
        first_name: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        address: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        zip: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        ssn: typing.Optional[str] = None,
        birthday: typing.Optional[Birthday] = None,
        email: typing.Optional[str] = None,
        suffix: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor204,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._modify_by_id_mapped_args(
            consumer_id=consumer_id,
            first_name=first_name,
            last_name=last_name,
            address=address,
            city=city,
            state=state,
            zip=zip,
            phone=phone,
            ssn=ssn,
            birthday=birthday,
            email=email,
            suffix=suffix,
        )
        return self._modify_by_id_oapg(
            body=args.body,
            path_params=args.path,
        )

