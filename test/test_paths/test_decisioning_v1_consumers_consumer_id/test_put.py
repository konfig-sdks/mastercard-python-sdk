# coding: utf-8

"""
    Open Banking

    OpenAPI specification for Finicity APIs.  Open Banking solutions in the US are provided by Finicity, a Mastercard company.

    The version of the OpenAPI document: 1.16.0
    Contact: apisupport@mastercard.com
    Created by: https://developer.mastercard.com/open-banking-us/documentation/support/
"""

import unittest
from unittest.mock import patch

import urllib3

import mastercard_python_sdk
from mastercard_python_sdk.paths.decisioning_v1_consumers_consumer_id import put
from mastercard_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestDecisioningV1ConsumersConsumerId(ApiTestMixin, unittest.TestCase):
    """
    DecisioningV1ConsumersConsumerId unit test stubs
        Modify Consumer by ID
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 204
    response_body = ''




if __name__ == '__main__':
    unittest.main()
