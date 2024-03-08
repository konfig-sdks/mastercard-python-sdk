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
from mastercard_python_sdk.paths.aggregation_v1_customers_customer_id_accounts_account_id_statement import get
from mastercard_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestAggregationV1CustomersCustomerIdAccountsAccountIdStatement(ApiTestMixin, unittest.TestCase):
    """
    AggregationV1CustomersCustomerIdAccountsAccountIdStatement unit test stubs
        Get Customer Account Statement
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()