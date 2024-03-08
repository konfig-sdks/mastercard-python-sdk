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
from mastercard_python_sdk.model.borrowers import Borrowers as BorrowersSchema
from mastercard_python_sdk.model.connect_joint_borrower_parameters import ConnectJointBorrowerParameters as ConnectJointBorrowerParametersSchema
from mastercard_python_sdk.model.report_custom_fields import ReportCustomFields as ReportCustomFieldsSchema
from mastercard_python_sdk.model.connect_url import ConnectUrl as ConnectUrlSchema

from mastercard_python_sdk.type.connect_url import ConnectUrl
from mastercard_python_sdk.type.borrowers import Borrowers
from mastercard_python_sdk.type.connect_joint_borrower_parameters import ConnectJointBorrowerParameters
from mastercard_python_sdk.type.report_custom_fields import ReportCustomFields
from mastercard_python_sdk.type.error_message import ErrorMessage

from ...api_client import Dictionary
from mastercard_python_sdk.pydantic.report_custom_fields import ReportCustomFields as ReportCustomFieldsPydantic
from mastercard_python_sdk.pydantic.borrowers import Borrowers as BorrowersPydantic
from mastercard_python_sdk.pydantic.error_message import ErrorMessage as ErrorMessagePydantic
from mastercard_python_sdk.pydantic.connect_url import ConnectUrl as ConnectUrlPydantic
from mastercard_python_sdk.pydantic.connect_joint_borrower_parameters import ConnectJointBorrowerParameters as ConnectJointBorrowerParametersPydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = ConnectJointBorrowerParametersSchema


request_body_connect_joint_borrower_parameters = api_client.RequestBody(
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
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '401': _response_for_401,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _generate_joint_borrower_url_mapped_args(
        self,
        partner_id: str,
        borrowers: Borrowers,
        language: typing.Optional[str] = None,
        redirect_uri: typing.Optional[str] = None,
        webhook: typing.Optional[str] = None,
        webhook_content_type: typing.Optional[str] = None,
        webhook_data: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        webhook_headers: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        institution_settings: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        experience: typing.Optional[str] = None,
        from_date: typing.Optional[int] = None,
        report_custom_fields: typing.Optional[ReportCustomFields] = None,
        single_use_url: typing.Optional[bool] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if language is not None:
            _body["language"] = language
        if partner_id is not None:
            _body["partnerId"] = partner_id
        if borrowers is not None:
            _body["borrowers"] = borrowers
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
        if institution_settings is not None:
            _body["institutionSettings"] = institution_settings
        if experience is not None:
            _body["experience"] = experience
        if from_date is not None:
            _body["fromDate"] = from_date
        if report_custom_fields is not None:
            _body["reportCustomFields"] = report_custom_fields
        if single_use_url is not None:
            _body["singleUseUrl"] = single_use_url
        args.body = _body
        return args

    async def _agenerate_joint_borrower_url_oapg(
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
        Generate Connect URL - Joint Borrower
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
            path_template='/connect/v2/generate/jointBorrower',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_connect_joint_borrower_parameters.serialize(body, content_type)
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


    def _generate_joint_borrower_url_oapg(
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
        Generate Connect URL - Joint Borrower
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
            path_template='/connect/v2/generate/jointBorrower',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_connect_joint_borrower_parameters.serialize(body, content_type)
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


class GenerateJointBorrowerUrlRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def agenerate_joint_borrower_url(
        self,
        partner_id: str,
        borrowers: Borrowers,
        language: typing.Optional[str] = None,
        redirect_uri: typing.Optional[str] = None,
        webhook: typing.Optional[str] = None,
        webhook_content_type: typing.Optional[str] = None,
        webhook_data: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        webhook_headers: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        institution_settings: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        experience: typing.Optional[str] = None,
        from_date: typing.Optional[int] = None,
        report_custom_fields: typing.Optional[ReportCustomFields] = None,
        single_use_url: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._generate_joint_borrower_url_mapped_args(
            partner_id=partner_id,
            borrowers=borrowers,
            language=language,
            redirect_uri=redirect_uri,
            webhook=webhook,
            webhook_content_type=webhook_content_type,
            webhook_data=webhook_data,
            webhook_headers=webhook_headers,
            institution_settings=institution_settings,
            experience=experience,
            from_date=from_date,
            report_custom_fields=report_custom_fields,
            single_use_url=single_use_url,
        )
        return await self._agenerate_joint_borrower_url_oapg(
            body=args.body,
            **kwargs,
        )
    
    def generate_joint_borrower_url(
        self,
        partner_id: str,
        borrowers: Borrowers,
        language: typing.Optional[str] = None,
        redirect_uri: typing.Optional[str] = None,
        webhook: typing.Optional[str] = None,
        webhook_content_type: typing.Optional[str] = None,
        webhook_data: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        webhook_headers: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        institution_settings: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        experience: typing.Optional[str] = None,
        from_date: typing.Optional[int] = None,
        report_custom_fields: typing.Optional[ReportCustomFields] = None,
        single_use_url: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._generate_joint_borrower_url_mapped_args(
            partner_id=partner_id,
            borrowers=borrowers,
            language=language,
            redirect_uri=redirect_uri,
            webhook=webhook,
            webhook_content_type=webhook_content_type,
            webhook_data=webhook_data,
            webhook_headers=webhook_headers,
            institution_settings=institution_settings,
            experience=experience,
            from_date=from_date,
            report_custom_fields=report_custom_fields,
            single_use_url=single_use_url,
        )
        return self._generate_joint_borrower_url_oapg(
            body=args.body,
        )

class GenerateJointBorrowerUrl(BaseApi):

    async def agenerate_joint_borrower_url(
        self,
        partner_id: str,
        borrowers: Borrowers,
        language: typing.Optional[str] = None,
        redirect_uri: typing.Optional[str] = None,
        webhook: typing.Optional[str] = None,
        webhook_content_type: typing.Optional[str] = None,
        webhook_data: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        webhook_headers: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        institution_settings: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        experience: typing.Optional[str] = None,
        from_date: typing.Optional[int] = None,
        report_custom_fields: typing.Optional[ReportCustomFields] = None,
        single_use_url: typing.Optional[bool] = None,
        validate: bool = False,
        **kwargs,
    ) -> ConnectUrlPydantic:
        raw_response = await self.raw.agenerate_joint_borrower_url(
            partner_id=partner_id,
            borrowers=borrowers,
            language=language,
            redirect_uri=redirect_uri,
            webhook=webhook,
            webhook_content_type=webhook_content_type,
            webhook_data=webhook_data,
            webhook_headers=webhook_headers,
            institution_settings=institution_settings,
            experience=experience,
            from_date=from_date,
            report_custom_fields=report_custom_fields,
            single_use_url=single_use_url,
            **kwargs,
        )
        if validate:
            return ConnectUrlPydantic(**raw_response.body)
        return api_client.construct_model_instance(ConnectUrlPydantic, raw_response.body)
    
    
    def generate_joint_borrower_url(
        self,
        partner_id: str,
        borrowers: Borrowers,
        language: typing.Optional[str] = None,
        redirect_uri: typing.Optional[str] = None,
        webhook: typing.Optional[str] = None,
        webhook_content_type: typing.Optional[str] = None,
        webhook_data: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        webhook_headers: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        institution_settings: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        experience: typing.Optional[str] = None,
        from_date: typing.Optional[int] = None,
        report_custom_fields: typing.Optional[ReportCustomFields] = None,
        single_use_url: typing.Optional[bool] = None,
        validate: bool = False,
    ) -> ConnectUrlPydantic:
        raw_response = self.raw.generate_joint_borrower_url(
            partner_id=partner_id,
            borrowers=borrowers,
            language=language,
            redirect_uri=redirect_uri,
            webhook=webhook,
            webhook_content_type=webhook_content_type,
            webhook_data=webhook_data,
            webhook_headers=webhook_headers,
            institution_settings=institution_settings,
            experience=experience,
            from_date=from_date,
            report_custom_fields=report_custom_fields,
            single_use_url=single_use_url,
        )
        if validate:
            return ConnectUrlPydantic(**raw_response.body)
        return api_client.construct_model_instance(ConnectUrlPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        partner_id: str,
        borrowers: Borrowers,
        language: typing.Optional[str] = None,
        redirect_uri: typing.Optional[str] = None,
        webhook: typing.Optional[str] = None,
        webhook_content_type: typing.Optional[str] = None,
        webhook_data: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        webhook_headers: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        institution_settings: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        experience: typing.Optional[str] = None,
        from_date: typing.Optional[int] = None,
        report_custom_fields: typing.Optional[ReportCustomFields] = None,
        single_use_url: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._generate_joint_borrower_url_mapped_args(
            partner_id=partner_id,
            borrowers=borrowers,
            language=language,
            redirect_uri=redirect_uri,
            webhook=webhook,
            webhook_content_type=webhook_content_type,
            webhook_data=webhook_data,
            webhook_headers=webhook_headers,
            institution_settings=institution_settings,
            experience=experience,
            from_date=from_date,
            report_custom_fields=report_custom_fields,
            single_use_url=single_use_url,
        )
        return await self._agenerate_joint_borrower_url_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        partner_id: str,
        borrowers: Borrowers,
        language: typing.Optional[str] = None,
        redirect_uri: typing.Optional[str] = None,
        webhook: typing.Optional[str] = None,
        webhook_content_type: typing.Optional[str] = None,
        webhook_data: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        webhook_headers: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        institution_settings: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        experience: typing.Optional[str] = None,
        from_date: typing.Optional[int] = None,
        report_custom_fields: typing.Optional[ReportCustomFields] = None,
        single_use_url: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._generate_joint_borrower_url_mapped_args(
            partner_id=partner_id,
            borrowers=borrowers,
            language=language,
            redirect_uri=redirect_uri,
            webhook=webhook,
            webhook_content_type=webhook_content_type,
            webhook_data=webhook_data,
            webhook_headers=webhook_headers,
            institution_settings=institution_settings,
            experience=experience,
            from_date=from_date,
            report_custom_fields=report_custom_fields,
            single_use_url=single_use_url,
        )
        return self._generate_joint_borrower_url_oapg(
            body=args.body,
        )

