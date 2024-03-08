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
from mastercard_python_sdk.paths.decisioning_v2_customers_customer_id_asset_summary import post
from mastercard_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestDecisioningV2CustomersCustomerIdAssetSummary(ApiTestMixin, unittest.TestCase):
    """
    DecisioningV2CustomersCustomerIdAssetSummary unit test stubs
        Generate Prequalification (Non-CRA) Report
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 202






if __name__ == '__main__':
    unittest.main()
