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
from mastercard_python_sdk.paths.aggregation_v2_customers_customer_id_institution_logins_institution_login_id_accounts import post
from mastercard_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestAggregationV2CustomersCustomerIdInstitutionLoginsInstitutionLoginIdAccounts(ApiTestMixin, unittest.TestCase):
    """
    AggregationV2CustomersCustomerIdInstitutionLoginsInstitutionLoginIdAccounts unit test stubs
        Refresh Customer Account by Institution Login ID for Data Access Tiers
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 204
    response_body = ''


if __name__ == '__main__':
    unittest.main()
