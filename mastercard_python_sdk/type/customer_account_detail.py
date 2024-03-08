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


class RequiredCustomerAccountDetail(TypedDict):
    pass

class OptionalCustomerAccountDetail(TypedDict, total=False):
    # (Mortgage/Loan) Description of loan
    description: str

    # (All Account Types) Most recent date of the following information. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    dateAsOf: int

    # (Checking/Savings/CD/MoneyMarket) and (Mortgage/Loan) The available balance (typically the current balance with adjustments for any pending transactions)
    availableBalanceAmount: typing.Union[int, float]

    # (Checking/Savings/CD/MoneyMarket) Date when account was opened. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    openDate: int

    # (Checking/Savings/CD/MoneyMarket) Start date of period. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    periodStartDate: int

    # End date of period. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    periodEndDate: int

    # (Checking/Savings/CD/MoneyMarket) The APY for the current period interest rate
    periodInterestRate: typing.Union[int, float]

    # (Checking/Savings/CD/MoneyMarket) Amount deposited in period
    periodDepositAmount: typing.Union[int, float]

    # (Checking/Savings/CD/MoneyMarket) Interest accrued during the current period
    periodInterestAmount: typing.Union[int, float]

    # (Checking/Savings/CD/MoneyMarket) Interest accrued year-to-date
    interestYtdAmount: typing.Union[int, float]

    # (Checking/Savings/CD/MoneyMarket) Interest earned in prior year
    interestPriorYtdAmount: typing.Union[int, float]

    # (Checking/Savings/CD/MoneyMarket) Maturity date of account type. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    maturityDate: int

    # (Credit Card/Line Of Credit) and (Mortgage/Loan) The account's current interest rate
    interestRate: str

    # (Credit Card/Line Of Credit) The available credit (typically the credit limit minus the current balance)
    creditAvailableAmount: typing.Union[int, float]

    # (Credit Card/Line Of Credit) The account's credit limit
    creditMaxAmount: typing.Union[int, float]

    # (Credit Card/Line Of Credit) Currently available cash advance
    cashAdvanceAvailableAmount: typing.Union[int, float]

    # (Credit Card/Line Of Credit) Maximum cash advance amount
    cashAdvanceMaxAmount: typing.Union[int, float]

    # (Credit Card/Line Of Credit) Balance of current cash advance
    cashAdvanceBalance: typing.Union[int, float]

    # (Credit Card/Line Of Credit) Interest rate for cash advances
    cashAdvanceInterestRate: typing.Union[int, float]

    # (Credit Card/Line Of Credit) and (Investment) Current balance
    currentBalance: typing.Union[int, float]

    # (Credit Card/Line Of Credit) and (Mortgage/Loan) Minimum payment due
    paymentMinAmount: typing.Union[int, float]

    # (Credit Card/Line Of Credit) Due date for the next payment. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    paymentDueDate: int

    # (Credit Card/Line Of Credit) Prior balance in last statement
    previousBalance: typing.Union[int, float]

    # (Credit Card/Line Of Credit) Start date of statement period. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    statementStartDate: int

    # (Credit Card/Line Of Credit) End date of statement period. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    statementEndDate: int

    # (Credit Card/Line Of Credit) Purchase amount of statement period
    statementPurchaseAmount: typing.Union[int, float]

    # (Credit Card/Line Of Credit) Finance amount of statement period
    statementFinanceAmount: typing.Union[int, float]

    # (Credit Card/Line Of Credit) Credit amount applied in statement period
    statementCreditAmount: typing.Union[int, float]

    # (Credit Card/Line Of Credit) Earned reward balance
    rewardEarnedBalance: int

    # (Credit Card/Line Of Credit) Balance past due
    pastDueAmount: typing.Union[int, float]

    # (Credit Card/Line Of Credit) and (Mortgage/Loan) The amount received in the last payment
    lastPaymentAmount: typing.Union[int, float]

    # (Credit Card/Line Of Credit) The date of the last payment. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    lastPaymentDate: int

    # (Credit Card/Line Of Credit) Balance of statement at close
    statementCloseBalance: typing.Union[int, float]

    # (Mortgage/Loan) Length of loan in months
    termOfMl: str

    # (Mortgage/Loan) Holder of the mortgage or loan
    mlHolderName: str

    # (Mortgage/Loan) Late fee charged
    lateFeeAmount: typing.Union[int, float]

    # (Mortgage/Loan) The amount required to payoff the loan
    payoffAmount: typing.Union[int, float]

    # (Mortgage/Loan) Date of final payment. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    payoffAmountDate: int

    # (Mortgage/Loan) Original date of loan maturity. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    originalMaturityDate: int

    # (Mortgage/Loan) The principal balance
    principalBalance: typing.Union[int, float]

    # (Mortgage/Loan) The escrow balance
    escrowBalance: typing.Union[int, float]

    # (Mortgage/Loan) Period of interest
    interestPeriod: str

    # (Mortgage/Loan) Original loan amount
    initialMlAmount: typing.Union[int, float]

    # (Mortgage/Loan) Original date of loan. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    initialMlDate: int

    # (Mortgage/Loan) Amount towards principal in next payment
    nextPaymentPrincipalAmount: typing.Union[int, float]

    # (Mortgage/Loan) Amount of interest in next payment
    nextPaymentInterestAmount: typing.Union[int, float]

    # (Mortgage/Loan) Minimum payment due
    nextPayment: typing.Union[int, float]

    # (Mortgage/Loan) Due date for the next payment. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    nextPaymentDate: int

    # (Mortgage/Loan) Due date of last payment. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    lastPaymentDueDate: int

    # (Mortgage/Loan) The date of the last payment. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    lastPaymentReceiveDate: int

    # (Mortgage/Loan) Amount towards principal in last payment
    lastPaymentPrincipalAmount: typing.Union[int, float]

    # (Mortgage/Loan) Amount of interest in last payment
    lastPaymentInterestAmount: typing.Union[int, float]

    # (Mortgage/Loan) Amount towards escrow in last payment
    lastPaymentEscrowAmount: typing.Union[int, float]

    # (Mortgage/Loan) Amount of last fee in last payment
    lastPaymentLastFeeAmount: typing.Union[int, float]

    # (Mortgage/Loan) Amount of late charge in last payment
    lastPaymentLateCharge: typing.Union[int, float]

    # (Mortgage/Loan) Principal paid year-to-date
    ytdPrincipalPaid: typing.Union[int, float]

    # (Mortgage/Loan) Interest paid year-to-date
    ytdInterestPaid: typing.Union[int, float]

    # (Mortgage/Loan) Insurance paid year-to-date
    ytdInsurancePaid: typing.Union[int, float]

    # (Mortgage/Loan) Tax paid year-to-date
    ytdTaxPaid: typing.Union[int, float]

    # (Mortgage/Loan) Enrolled in autopay (F/Y)
    autoPayEnrolled: bool

    # Margin trading indicator (true / false)
    marginAllowed: bool

    # Cash account allowed indicator (true / false)
    cashAccountAllowed: bool

    # (Mortgage/Loan) Collateral on loan
    collateral: str

    # (Mortgage/Loan) Current school
    currentSchool: str

    # (Mortgage/Loan) First payment due date. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    firstPaymentDate: int

    # (Mortgage/Loan) First mortgage (F/Y)
    firstMortgage: bool

    # (Mortgage/Loan) Frequency of payments (monthly, etc.)
    loanPaymentFreq: str

    # (Mortgage/Loan) Original school
    originalSchool: str

    # (Mortgage/Loan) Recurring payment amount
    recurringPaymentAmount: typing.Union[int, float]

    # (Mortgage/Loan) Owner of loan
    lender: str

    # (Mortgage/Loan) Ending balance
    endingBalanceAmount: typing.Union[int, float]

    # (Mortgage/Loan) Type of loan term
    loanTermType: str

    # (Mortgage/Loan) Number of payments made
    paymentsMade: int

    # (Mortgage/Loan) Balloon payment amount
    balloonAmount: typing.Union[int, float]

    # (Mortgage/Loan) Projected interest on the loan
    projectedInterest: typing.Union[int, float]

    # (Mortgage/Loan) Interest paid since inception of loan (life to date)
    interestPaidLtd: typing.Union[int, float]

    # (Mortgage/Loan) Type of interest rate
    interestRateType: str

    # (Mortgage/Loan) Type of loan payment
    loanPaymentType: str

    # (Mortgage/Loan) Type of repayment plan for the student loan
    repaymentPlan: str

    # (Mortgage/Loan) Number of payments remaining before loan is paid off
    paymentsRemaining: int

    # (Investment) Net interest earned after deducting interest paid out
    marginBalance: typing.Union[int, float]

    # (Investment) Sum of short balance
    shortBalance: typing.Union[int, float]

    # (Investment) Amount available for cash withdrawal
    availableCashBalance: typing.Union[int, float]

    # (Investment) amount payable to an investor at maturity
    maturityValueAmount: typing.Union[int, float]

    # (Investment) Vested amount in account
    vestedBalance: typing.Union[int, float]

    # (Investment) Employer matched contributions
    empMatchAmount: typing.Union[int, float]

    # (Investment) Employer pretax contribution amount
    empPretaxContribAmount: typing.Union[int, float]

    # (Investment) Employer pretax contribution amount year to date
    empPretaxContribAmountYtd: typing.Union[int, float]

    # (Investment) Total year to date contributions
    contribTotalYtd: typing.Union[int, float]

    # (Investment) Cash balance of account
    cashBalanceAmount: typing.Union[int, float]

    # (Investment) Pre-tax amount of total balance
    preTaxAmount: typing.Union[int, float]

    # (Investment) After-tax amount of total balance
    afterTaxAmount: typing.Union[int, float]

    # (Investment) Amount matched
    matchAmount: typing.Union[int, float]

    # (Investment) Amount of balance for profit sharing
    profitSharingAmount: typing.Union[int, float]

    # (Investment) Amount of balance rolled over from original account (401k, etc.)
    rolloverAmount: typing.Union[int, float]

    # (Investment) Other vested amount
    otherVestAmount: typing.Union[int, float]

    # (Investment) Other nonvested amount
    otherNonvestAmount: typing.Union[int, float]

    # (Investment) Current loan balance
    currentLoanBalance: typing.Union[int, float]

    # (Investment) Interest rate of loan
    loanRate: typing.Union[int, float]

    # (Investment) Money available to buy securities
    buyPower: typing.Union[int, float]

    # (Investment) Life to date of money rolled over
    rolloverLtd: typing.Union[int, float]

    # (Student Loan) The federal unique loan identifying number
    loanAwardId: str

    # (Student Loan) The original interest rate to which the loan was disbursed, in APY
    originalInterestRate: typing.Union[int, float]

    # (Student Loan) The financial institution guarantor of the loan (who will pay the loan amount to the owner if the borrower defaults)
    guarantor: str

    # (Student Loan) Owner of the loan
    owner: str

    # (Student Loan) The indication of the presence of an interest subsidy (i.e. subsidized)
    interestSubsidyType: str

    # (Student Loan) The total outstanding interest balance
    interestBalance: typing.Union[int, float]

    # (Student Loan) The number of months still outstanding on a loan
    remainingTermOfMl: typing.Union[int, float]

    # (Student Loan) Initial interest rate of loan
    initialInterestRate: typing.Union[int, float]

    # (Student Loan) The total outstanding fees balance
    feesBalance: typing.Union[int, float]

    # (Student Loan) Loan interest paid year-to-date
    loanYtdInterestPaid: typing.Union[int, float]

    # (Student Loan) Loan fees paid year-to-date
    loanYtdFeesPaid: typing.Union[int, float]

    # (Student Loan) Loan principal paid year-to-date
    loanYtdPrincipalPaid: typing.Union[int, float]

    # (Student Loan) The repayment status phase (i.e. In School, Grace, Repayment, Deferment, Forbearance)
    loanStatus: str

    # (Student Loan) The start date of the current status. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    loanStatusStartDate: int

    # (Student Loan) The end date of the current status. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    loanStatusEndDate: int

    # (Student Loan) The interest rate of multiple interest rates and balances at the group level, in APY
    weightedInterestRate: typing.Union[int, float]

    # (Student Loan) The start date of the current repayment plan. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    repaymentPlanStartDate: int

    # (Student Loan) The end date of the current repayment plan. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    repaymentPlanEndDate: int

    # (Student Loan) The expected date of the payoff date. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    expectedPayoffDate: int

    # (Student Loan) The date the borrower graduated or dropped below half-time enrollment in school. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    outOfSchoolDate: int

    # (Student Loan) The date the loan enters into repayment. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    convertToRepayment: int

    # (Student Loan) The number of days past a due date that a payment should have been made
    daysDelinquent: int

    # (Student Loan) The total amount paid towards the principal balance
    totalPrincipalPaid: typing.Union[int, float]

    # (Student Loan) The total amount paid towards interest
    totalInterestPaid: typing.Union[int, float]

    # (Student Loan) The total amount paid
    totalAmountPaid: typing.Union[int, float]

class CustomerAccountDetail(RequiredCustomerAccountDetail, OptionalCustomerAccountDetail):
    pass
