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

from mastercard_python_sdk.type.base_report_ack_with_portfolio_id import BaseReportAckWithPortfolioId
from mastercard_python_sdk.type.cash_flow_cash_flow_balance_summary import CashFlowCashFlowBalanceSummary
from mastercard_python_sdk.type.cash_flow_cash_flow_characteristics_summary import CashFlowCashFlowCharacteristicsSummary
from mastercard_python_sdk.type.cash_flow_cash_flow_credit_summary import CashFlowCashFlowCreditSummary
from mastercard_python_sdk.type.cash_flow_cash_flow_debit_summary import CashFlowCashFlowDebitSummary
from mastercard_python_sdk.type.cash_flow_possible_loan_deposits import CashFlowPossibleLoanDeposits
from mastercard_python_sdk.type.report_institution import ReportInstitution

CashFlowReport = typing.Union[BaseReportAckWithPortfolioId,typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]
CashFlowReport = object
