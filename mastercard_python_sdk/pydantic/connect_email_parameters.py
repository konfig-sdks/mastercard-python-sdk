# coding: utf-8

"""
    Open Banking

    OpenAPI specification for Finicity APIs.  Open Banking solutions in the US are provided by Finicity, a Mastercard company.

    The version of the OpenAPI document: 1.16.0
    Contact: apisupport@mastercard.com
    Created by: https://developer.mastercard.com/open-banking-us/documentation/support/
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel

from mastercard_python_sdk.pydantic.consumer_info import ConsumerInfo
from mastercard_python_sdk.pydantic.email_options import EmailOptions
from mastercard_python_sdk.pydantic.report_custom_fields import ReportCustomFields

class ConnectEmailParameters(BaseModel):
    # Your Partner ID displayed in the [Developer Dashboard](https://developer.mastercard.com/account/log-in)
    partner_id: str = Field(alias='partnerId')

    # A customer ID. See Add Customer API for how to create a customer ID.
    customer_id: str = Field(alias='customerId')

    # A consumer ID. See Create Consumer API for how to create a consumer ID.
    consumer_id: str = Field(alias='consumerId')

    email: EmailOptions = Field(alias='email')

    # By default, the Connect application is in English. You don't need to pass this parameter unless you want to translate Connect into one of our supported languages.  * Spanish (United States): `es` * French (Canada): `fr` 
    language: typing.Optional[str] = Field(None, alias='language')

    # The URL that customers will be redirected to after completing Finicity Connect. Required unless Connect is embedded inside our application (iframe).
    redirect_uri: typing.Optional[str] = Field(None, alias='redirectUri')

    # The publicly available URL you want to be notified with events as the user progresses through the application. See [Connect Webhook Event](https://developer.mastercard.com/open-banking-us/documentation/webhooks/webhooks-connect/) for event details.
    webhook: typing.Optional[str] = Field(None, alias='webhook')

    # The content type the webhook events will be sent in. Supported types: \"application/json\" and \"application/xml\".
    webhook_content_type: typing.Optional[str] = Field(None, alias='webhookContentType')

    # Allows additional identifiable information to be inserted into the payload of connect webhook events. See: [Custom Webhooks](https://developer.mastercard.com/open-banking-us/documentation/webhooks/webhooks-custom/).
    webhook_data: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='webhookData')

    # Allows additional identifiable information to be included as headers of connect webhook event. See: [Custom Webhooks](https://developer.mastercard.com/open-banking-us/documentation/webhooks/webhooks-custom/).
    webhook_headers: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='webhookHeaders')

    # Advanced options for configuration of which institutions to display in. See [Institution Settings](https://developer.mastercard.com/open-banking-us/documentation/connect/connect-institutions-settings/).
    institution_settings: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='institutionSettings')

    # The `experience` field allows you to customize: * Brand: color and logo * Icon: displayed on the \"Share your data\" page * Popular institutions: displayed on the Bank Search page * Report: the credit decisioning report to send when Connect completes. * MVS modules: financial, payroll, paystub  Note: the Finicity sales engineers (SE) help you set up a default experience for your company when you migrate to Connect 2.0. For each additional experience you create thereafter, they'll give you a unique ID. See [Generate Connect URL](https://developer.mastercard.com/open-banking-us/documentation/connect/generate-2-connect-url-apis/).  Experience values options: * \"default\": your default experience (must be defined) * GUID: the code for a different experience * Not defined: If you don't pass the experience parameter, then Connect's out of the box default experience (add accounts but no branding) is used, and the MVS modules will not run.
    experience: typing.Optional[str] = Field(None, alias='experience')

    # \"true\": The URL link expires after a Connect session successfully completes.  Note: when the `singleUseUrl` and the `experience` parameters are passed in the same call, the `singleUseUrl` value overrides the `singleUseUrl` value configured in the `experience` parameter.
    single_use_url: typing.Optional[bool] = Field(None, alias='singleUseUrl')

    # The `fromDate` parameter is used when experiences are associated with a credit decisioning report and any other reports with transaction data. The value is in epoch time and must be 10 digits. Example: 1494449017. If it's greater than 10 digits, then the `fromDate` is set to the credit decisioning report's default `fromDate`.  For an experience that generates multiple reports, the `fromDate` gets passed to the reports that support it.  However, Connect doesn't pass this parameter to the following reports: * Pay Statement Extraction Report * VOIE - Paystub (with TXVerify) Report * Statement Report * Verification of Income Report * VOIE - Payroll Report  Note: this field isn't used if you're only collecting transaction data without a report.
    from_date: typing.Optional[int] = Field(None, alias='fromDate')

    report_custom_fields: typing.Optional[ReportCustomFields] = Field(None, alias='reportCustomFields')

    optional_consumer_info: typing.Optional[ConsumerInfo] = Field(None, alias='optionalConsumerInfo')
    class Config:
        arbitrary_types_allowed = True
