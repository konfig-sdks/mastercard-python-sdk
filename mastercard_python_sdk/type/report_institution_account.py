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

from mastercard_python_sdk.type.analytics_reports_account import AnalyticsReportsAccount
from mastercard_python_sdk.type.cash_flow_report_account import CashFlowReportAccount
from mastercard_python_sdk.type.prequalification_report_account import PrequalificationReportAccount
from mastercard_python_sdk.type.transactions_report_account import TransactionsReportAccount
from mastercard_python_sdk.type.voa_report_account import VOAReportAccount
from mastercard_python_sdk.type.voa_with_income_report_account import VOAWithIncomeReportAccount
from mastercard_python_sdk.type.voe_transactions_report_account import VOETransactionsReportAccount
from mastercard_python_sdk.type.voi_report_account import VOIReportAccount
from mastercard_python_sdk.type.voietx_verify_report_account import VOIETXVerifyReportAccount

ReportInstitutionAccount = typing.Union[AnalyticsReportsAccount,CashFlowReportAccount,PrequalificationReportAccount,TransactionsReportAccount,VOAReportAccount,VOAWithIncomeReportAccount,VOETransactionsReportAccount,VOIReportAccount,VOIETXVerifyReportAccount]
ReportInstitutionAccount = object
