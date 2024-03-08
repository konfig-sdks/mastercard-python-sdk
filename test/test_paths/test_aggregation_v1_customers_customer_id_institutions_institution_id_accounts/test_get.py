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
from mastercard_python_sdk.paths.aggregation_v1_customers_customer_id_institutions_institution_id_accounts import get
from mastercard_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestAggregationV1CustomersCustomerIdInstitutionsInstitutionIdAccounts(ApiTestMixin, unittest.TestCase):
    """
    AggregationV1CustomersCustomerIdInstitutionsInstitutionIdAccounts unit test stubs
        Get Customer Accounts by Institution ID
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
