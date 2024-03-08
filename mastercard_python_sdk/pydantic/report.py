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

from mastercard_python_sdk.pydantic.af_balance_analytics_report import AFBalanceAnalyticsReport
from mastercard_python_sdk.pydantic.af_cash_flow_analytics_report import AFCashFlowAnalyticsReport
from mastercard_python_sdk.pydantic.cash_flow_report import CashFlowReport
from mastercard_python_sdk.pydantic.pay_statement_report import PayStatementReport
from mastercard_python_sdk.pydantic.prequalification_report import PrequalificationReport
from mastercard_python_sdk.pydantic.statement_report import StatementReport
from mastercard_python_sdk.pydantic.transactions_report import TransactionsReport
from mastercard_python_sdk.pydantic.voa_report import VOAReport
from mastercard_python_sdk.pydantic.voa_with_income_report import VOAWithIncomeReport
from mastercard_python_sdk.pydantic.voe_payroll_report import VOEPayrollReport
from mastercard_python_sdk.pydantic.voe_transactions_report import VOETransactionsReport
from mastercard_python_sdk.pydantic.voi_report import VOIReport
from mastercard_python_sdk.pydantic.voie_payroll_report import VOIEPayrollReport
from mastercard_python_sdk.pydantic.voie_paystub_report import VOIEPaystubReport
from mastercard_python_sdk.pydantic.voie_paystub_with_tx_verify_report import VOIEPaystubWithTXVerifyReport

Report = typing.Union[AFBalanceAnalyticsReport,AFCashFlowAnalyticsReport,CashFlowReport,PrequalificationReport,PayStatementReport,StatementReport,TransactionsReport,VOAReport,VOAWithIncomeReport,VOEPayrollReport,VOETransactionsReport,VOIReport,VOIEPayrollReport,VOIEPaystubReport,VOIEPaystubWithTXVerifyReport]
Report = object
