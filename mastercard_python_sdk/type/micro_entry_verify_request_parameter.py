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


class RequiredMicroEntryVerifyRequestParameter(TypedDict):
    pass

class OptionalMicroEntryVerifyRequestParameter(TypedDict, total=False):
    # Your Partner ID displayed in the [Developer Dashboard](https://developer.mastercard.com/account/log-in)
    partnerId: str

    # A customer ID. See Add Customer API for how to create a customer ID.
    customerId: str

    # The URL that customers will be redirected to after completing Finicity Connect. Required unless Connect is embedded inside our application (iframe).
    redirectUri: str

    # The publicly available URL you want to be notified with events as the user progresses through the application. See [Connect Webhook Event](https://developer.mastercard.com/open-banking-us/documentation/webhooks/webhooks-connect/) for event details.
    webhook: str

    # The content type the webhook events will be sent in. Supported types: \"application/json\" and \"application/xml\".
    webhookContentType: str

    # Allows additional identifiable information to be inserted into the payload of connect webhook events. See: [Custom Webhooks](https://developer.mastercard.com/open-banking-us/documentation/webhooks/webhooks-custom/).
    webhookData: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Allows additional identifiable information to be included as headers of connect webhook event. See: [Custom Webhooks](https://developer.mastercard.com/open-banking-us/documentation/webhooks/webhooks-custom/).
    webhookHeaders: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # The `experience` field allows you to customize: * Brand: color and logo * Icon: displayed on the \"Share your data\" page * Popular institutions: displayed on the Bank Search page * Report: the credit decisioning report to send when Connect completes. * MVS modules: financial, payroll, paystub  Note: the Finicity sales engineers (SE) help you set up a default experience for your company when you migrate to Connect 2.0. For each additional experience you create thereafter, they'll give you a unique ID. See [Generate Connect URL](https://developer.mastercard.com/open-banking-us/documentation/connect/generate-2-connect-url-apis/).  Experience values options: * \"default\": your default experience (must be defined) * GUID: the code for a different experience * Not defined: If you don't pass the experience parameter, then Connect's out of the box default experience (add accounts but no branding) is used, and the MVS modules will not run.
    experience: str

    # An account ID
    accountId: str

class MicroEntryVerifyRequestParameter(RequiredMicroEntryVerifyRequestParameter, OptionalMicroEntryVerifyRequestParameter):
    pass
