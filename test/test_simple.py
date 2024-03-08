# coding: utf-8

"""
    Open Banking

    OpenAPI specification for Finicity APIs.  Open Banking solutions in the US are provided by Finicity, a Mastercard company.

    The version of the OpenAPI document: 1.16.0
    Contact: apisupport@mastercard.com
    Created by: https://developer.mastercard.com/open-banking-us/documentation/support/
"""

import unittest

import os
from pprint import pprint
from mastercard_python_sdk import Mastercard

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        mastercard = Mastercard(
        
                        finicity_app_key = 'YOUR_API_KEY',
        
                        finicity_app_token = 'YOUR_API_KEY',
        )
        self.assertIsNotNone(mastercard)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
