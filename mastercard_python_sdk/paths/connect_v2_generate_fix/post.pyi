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
from mastercard_python_sdk.model.fix_connect_parameters import FixConnectParameters as FixConnectParametersSchema
from mastercard_python_sdk.model.connect_url import ConnectUrl as ConnectUrlSchema

from mastercard_python_sdk.type.connect_url import ConnectUrl
from mastercard_python_sdk.type.fix_connect_parameters import FixConnectParameters
from mastercard_python_sdk.type.error_message import ErrorMessage

from ...api_client import Dictionary
from mastercard_python_sdk.pydantic.fix_connect_parameters import FixConnectParameters as FixConnectParametersPydantic
from mastercard_python_sdk.pydantic.error_message import ErrorMessage as ErrorMessagePydantic
from mastercard_python_sdk.pydantic.connect_url import ConnectUrl as ConnectUrlPydantic

# body param
SchemaForRequestBodyApplicationJson = FixConnectParametersSchema


request_body_fix_connect_parameters = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = ConnectUrlSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ConnectUrl


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ConnectUrl


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
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _fix_url_generation_mapped_args(
        self,
        partner_id: str,
        customer_id: str,
        institution_login_id: str,
        language: typing.Optional[str] = None,
        redirect_uri: typing.Optional[str] = None,
        webhook: typing.Optional[str] = None,
        webhook_content_type: typing.Optional[str] = None,
        webhook_data: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        webhook_headers: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        experience: typing.Optional[str] = None,
        single_use_url: typing.Optional[bool] = None,
        is_web_view: typing.Optional[bool] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if language is not None:
            _body["language"] = language
        if partner_id is not None:
            _body["partnerId"] = partner_id
        if customer_id is not None:
            _body["customerId"] = customer_id
        if institution_login_id is not None:
            _body["institutionLoginId"] = institution_login_id
        if redirect_uri is not None:
            _body["redirectUri"] = redirect_uri
        if webhook is not None:
            _body["webhook"] = webhook
        if webhook_content_type is not None:
            _body["webhookContentType"] = webhook_content_type
        if webhook_data is not None:
            _body["webhookData"] = webhook_data
        if webhook_headers is not None:
            _body["webhookHeaders"] = webhook_headers
        if experience is not None:
            _body["experience"] = experience
        if single_use_url is not None:
            _body["singleUseUrl"] = single_use_url
        if is_web_view is not None:
            _body["isWebView"] = is_web_view
        args.body = _body
        return args

    async def _afix_url_generation_oapg(
        self,
        body: typing.Any = None,
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
        Generate Fix Connect URL
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
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
            path_template='/connect/v2/generate/fix',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_fix_connect_parameters.serialize(body, content_type)
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


    def _fix_url_generation_oapg(
        self,
        body: typing.Any = None,
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
        Generate Fix Connect URL
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
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
            path_template='/connect/v2/generate/fix',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_fix_connect_parameters.serialize(body, content_type)
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


class FixUrlGenerationRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def afix_url_generation(
        self,
        partner_id: str,
        customer_id: str,
        institution_login_id: str,
        language: typing.Optional[str] = None,
        redirect_uri: typing.Optional[str] = None,
        webhook: typing.Optional[str] = None,
        webhook_content_type: typing.Optional[str] = None,
        webhook_data: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        webhook_headers: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        experience: typing.Optional[str] = None,
        single_use_url: typing.Optional[bool] = None,
        is_web_view: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._fix_url_generation_mapped_args(
            partner_id=partner_id,
            customer_id=customer_id,
            institution_login_id=institution_login_id,
            language=language,
            redirect_uri=redirect_uri,
            webhook=webhook,
            webhook_content_type=webhook_content_type,
            webhook_data=webhook_data,
            webhook_headers=webhook_headers,
            experience=experience,
            single_use_url=single_use_url,
            is_web_view=is_web_view,
        )
        return await self._afix_url_generation_oapg(
            body=args.body,
            **kwargs,
        )
    
    def fix_url_generation(
        self,
        partner_id: str,
        customer_id: str,
        institution_login_id: str,
        language: typing.Optional[str] = None,
        redirect_uri: typing.Optional[str] = None,
        webhook: typing.Optional[str] = None,
        webhook_content_type: typing.Optional[str] = None,
        webhook_data: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        webhook_headers: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        experience: typing.Optional[str] = None,
        single_use_url: typing.Optional[bool] = None,
        is_web_view: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._fix_url_generation_mapped_args(
            partner_id=partner_id,
            customer_id=customer_id,
            institution_login_id=institution_login_id,
            language=language,
            redirect_uri=redirect_uri,
            webhook=webhook,
            webhook_content_type=webhook_content_type,
            webhook_data=webhook_data,
            webhook_headers=webhook_headers,
            experience=experience,
            single_use_url=single_use_url,
            is_web_view=is_web_view,
        )
        return self._fix_url_generation_oapg(
            body=args.body,
        )

class FixUrlGeneration(BaseApi):

    async def afix_url_generation(
        self,
        partner_id: str,
        customer_id: str,
        institution_login_id: str,
        language: typing.Optional[str] = None,
        redirect_uri: typing.Optional[str] = None,
        webhook: typing.Optional[str] = None,
        webhook_content_type: typing.Optional[str] = None,
        webhook_data: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        webhook_headers: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        experience: typing.Optional[str] = None,
        single_use_url: typing.Optional[bool] = None,
        is_web_view: typing.Optional[bool] = None,
        validate: bool = False,
        **kwargs,
    ) -> ConnectUrlPydantic:
        raw_response = await self.raw.afix_url_generation(
            partner_id=partner_id,
            customer_id=customer_id,
            institution_login_id=institution_login_id,
            language=language,
            redirect_uri=redirect_uri,
            webhook=webhook,
            webhook_content_type=webhook_content_type,
            webhook_data=webhook_data,
            webhook_headers=webhook_headers,
            experience=experience,
            single_use_url=single_use_url,
            is_web_view=is_web_view,
            **kwargs,
        )
        if validate:
            return ConnectUrlPydantic(**raw_response.body)
        return api_client.construct_model_instance(ConnectUrlPydantic, raw_response.body)
    
    
    def fix_url_generation(
        self,
        partner_id: str,
        customer_id: str,
        institution_login_id: str,
        language: typing.Optional[str] = None,
        redirect_uri: typing.Optional[str] = None,
        webhook: typing.Optional[str] = None,
        webhook_content_type: typing.Optional[str] = None,
        webhook_data: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        webhook_headers: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        experience: typing.Optional[str] = None,
        single_use_url: typing.Optional[bool] = None,
        is_web_view: typing.Optional[bool] = None,
        validate: bool = False,
    ) -> ConnectUrlPydantic:
        raw_response = self.raw.fix_url_generation(
            partner_id=partner_id,
            customer_id=customer_id,
            institution_login_id=institution_login_id,
            language=language,
            redirect_uri=redirect_uri,
            webhook=webhook,
            webhook_content_type=webhook_content_type,
            webhook_data=webhook_data,
            webhook_headers=webhook_headers,
            experience=experience,
            single_use_url=single_use_url,
            is_web_view=is_web_view,
        )
        if validate:
            return ConnectUrlPydantic(**raw_response.body)
        return api_client.construct_model_instance(ConnectUrlPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        partner_id: str,
        customer_id: str,
        institution_login_id: str,
        language: typing.Optional[str] = None,
        redirect_uri: typing.Optional[str] = None,
        webhook: typing.Optional[str] = None,
        webhook_content_type: typing.Optional[str] = None,
        webhook_data: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        webhook_headers: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        experience: typing.Optional[str] = None,
        single_use_url: typing.Optional[bool] = None,
        is_web_view: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._fix_url_generation_mapped_args(
            partner_id=partner_id,
            customer_id=customer_id,
            institution_login_id=institution_login_id,
            language=language,
            redirect_uri=redirect_uri,
            webhook=webhook,
            webhook_content_type=webhook_content_type,
            webhook_data=webhook_data,
            webhook_headers=webhook_headers,
            experience=experience,
            single_use_url=single_use_url,
            is_web_view=is_web_view,
        )
        return await self._afix_url_generation_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        partner_id: str,
        customer_id: str,
        institution_login_id: str,
        language: typing.Optional[str] = None,
        redirect_uri: typing.Optional[str] = None,
        webhook: typing.Optional[str] = None,
        webhook_content_type: typing.Optional[str] = None,
        webhook_data: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        webhook_headers: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        experience: typing.Optional[str] = None,
        single_use_url: typing.Optional[bool] = None,
        is_web_view: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._fix_url_generation_mapped_args(
            partner_id=partner_id,
            customer_id=customer_id,
            institution_login_id=institution_login_id,
            language=language,
            redirect_uri=redirect_uri,
            webhook=webhook,
            webhook_content_type=webhook_content_type,
            webhook_data=webhook_data,
            webhook_headers=webhook_headers,
            experience=experience,
            single_use_url=single_use_url,
            is_web_view=is_web_view,
        )
        return self._fix_url_generation_oapg(
            body=args.body,
        )
