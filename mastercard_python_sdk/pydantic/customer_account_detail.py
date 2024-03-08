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


class CustomerAccountDetail(BaseModel):
    # (Mortgage/Loan) Description of loan
    description: typing.Optional[str] = Field(None, alias='description')

    # (All Account Types) Most recent date of the following information. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    date_as_of: typing.Optional[int] = Field(None, alias='dateAsOf')

    # (Checking/Savings/CD/MoneyMarket) and (Mortgage/Loan) The available balance (typically the current balance with adjustments for any pending transactions)
    available_balance_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='availableBalanceAmount')

    # (Checking/Savings/CD/MoneyMarket) Date when account was opened. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    open_date: typing.Optional[int] = Field(None, alias='openDate')

    # (Checking/Savings/CD/MoneyMarket) Start date of period. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    period_start_date: typing.Optional[int] = Field(None, alias='periodStartDate')

    # End date of period. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    period_end_date: typing.Optional[int] = Field(None, alias='periodEndDate')

    # (Checking/Savings/CD/MoneyMarket) The APY for the current period interest rate
    period_interest_rate: typing.Optional[typing.Union[int, float]] = Field(None, alias='periodInterestRate')

    # (Checking/Savings/CD/MoneyMarket) Amount deposited in period
    period_deposit_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='periodDepositAmount')

    # (Checking/Savings/CD/MoneyMarket) Interest accrued during the current period
    period_interest_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='periodInterestAmount')

    # (Checking/Savings/CD/MoneyMarket) Interest accrued year-to-date
    interest_ytd_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='interestYtdAmount')

    # (Checking/Savings/CD/MoneyMarket) Interest earned in prior year
    interest_prior_ytd_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='interestPriorYtdAmount')

    # (Checking/Savings/CD/MoneyMarket) Maturity date of account type. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    maturity_date: typing.Optional[int] = Field(None, alias='maturityDate')

    # (Credit Card/Line Of Credit) and (Mortgage/Loan) The account's current interest rate
    interest_rate: typing.Optional[str] = Field(None, alias='interestRate')

    # (Credit Card/Line Of Credit) The available credit (typically the credit limit minus the current balance)
    credit_available_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='creditAvailableAmount')

    # (Credit Card/Line Of Credit) The account's credit limit
    credit_max_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='creditMaxAmount')

    # (Credit Card/Line Of Credit) Currently available cash advance
    cash_advance_available_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='cashAdvanceAvailableAmount')

    # (Credit Card/Line Of Credit) Maximum cash advance amount
    cash_advance_max_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='cashAdvanceMaxAmount')

    # (Credit Card/Line Of Credit) Balance of current cash advance
    cash_advance_balance: typing.Optional[typing.Union[int, float]] = Field(None, alias='cashAdvanceBalance')

    # (Credit Card/Line Of Credit) Interest rate for cash advances
    cash_advance_interest_rate: typing.Optional[typing.Union[int, float]] = Field(None, alias='cashAdvanceInterestRate')

    # (Credit Card/Line Of Credit) and (Investment) Current balance
    current_balance: typing.Optional[typing.Union[int, float]] = Field(None, alias='currentBalance')

    # (Credit Card/Line Of Credit) and (Mortgage/Loan) Minimum payment due
    payment_min_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='paymentMinAmount')

    # (Credit Card/Line Of Credit) Due date for the next payment. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    payment_due_date: typing.Optional[int] = Field(None, alias='paymentDueDate')

    # (Credit Card/Line Of Credit) Prior balance in last statement
    previous_balance: typing.Optional[typing.Union[int, float]] = Field(None, alias='previousBalance')

    # (Credit Card/Line Of Credit) Start date of statement period. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    statement_start_date: typing.Optional[int] = Field(None, alias='statementStartDate')

    # (Credit Card/Line Of Credit) End date of statement period. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    statement_end_date: typing.Optional[int] = Field(None, alias='statementEndDate')

    # (Credit Card/Line Of Credit) Purchase amount of statement period
    statement_purchase_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='statementPurchaseAmount')

    # (Credit Card/Line Of Credit) Finance amount of statement period
    statement_finance_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='statementFinanceAmount')

    # (Credit Card/Line Of Credit) Credit amount applied in statement period
    statement_credit_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='statementCreditAmount')

    # (Credit Card/Line Of Credit) Earned reward balance
    reward_earned_balance: typing.Optional[int] = Field(None, alias='rewardEarnedBalance')

    # (Credit Card/Line Of Credit) Balance past due
    past_due_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='pastDueAmount')

    # (Credit Card/Line Of Credit) and (Mortgage/Loan) The amount received in the last payment
    last_payment_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='lastPaymentAmount')

    # (Credit Card/Line Of Credit) The date of the last payment. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    last_payment_date: typing.Optional[int] = Field(None, alias='lastPaymentDate')

    # (Credit Card/Line Of Credit) Balance of statement at close
    statement_close_balance: typing.Optional[typing.Union[int, float]] = Field(None, alias='statementCloseBalance')

    # (Mortgage/Loan) Length of loan in months
    term_of_ml: typing.Optional[str] = Field(None, alias='termOfMl')

    # (Mortgage/Loan) Holder of the mortgage or loan
    ml_holder_name: typing.Optional[str] = Field(None, alias='mlHolderName')

    # (Mortgage/Loan) Late fee charged
    late_fee_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='lateFeeAmount')

    # (Mortgage/Loan) The amount required to payoff the loan
    payoff_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='payoffAmount')

    # (Mortgage/Loan) Date of final payment. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    payoff_amount_date: typing.Optional[int] = Field(None, alias='payoffAmountDate')

    # (Mortgage/Loan) Original date of loan maturity. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    original_maturity_date: typing.Optional[int] = Field(None, alias='originalMaturityDate')

    # (Mortgage/Loan) The principal balance
    principal_balance: typing.Optional[typing.Union[int, float]] = Field(None, alias='principalBalance')

    # (Mortgage/Loan) The escrow balance
    escrow_balance: typing.Optional[typing.Union[int, float]] = Field(None, alias='escrowBalance')

    # (Mortgage/Loan) Period of interest
    interest_period: typing.Optional[str] = Field(None, alias='interestPeriod')

    # (Mortgage/Loan) Original loan amount
    initial_ml_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='initialMlAmount')

    # (Mortgage/Loan) Original date of loan. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    initial_ml_date: typing.Optional[int] = Field(None, alias='initialMlDate')

    # (Mortgage/Loan) Amount towards principal in next payment
    next_payment_principal_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='nextPaymentPrincipalAmount')

    # (Mortgage/Loan) Amount of interest in next payment
    next_payment_interest_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='nextPaymentInterestAmount')

    # (Mortgage/Loan) Minimum payment due
    next_payment: typing.Optional[typing.Union[int, float]] = Field(None, alias='nextPayment')

    # (Mortgage/Loan) Due date for the next payment. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    next_payment_date: typing.Optional[int] = Field(None, alias='nextPaymentDate')

    # (Mortgage/Loan) Due date of last payment. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    last_payment_due_date: typing.Optional[int] = Field(None, alias='lastPaymentDueDate')

    # (Mortgage/Loan) The date of the last payment. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    last_payment_receive_date: typing.Optional[int] = Field(None, alias='lastPaymentReceiveDate')

    # (Mortgage/Loan) Amount towards principal in last payment
    last_payment_principal_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='lastPaymentPrincipalAmount')

    # (Mortgage/Loan) Amount of interest in last payment
    last_payment_interest_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='lastPaymentInterestAmount')

    # (Mortgage/Loan) Amount towards escrow in last payment
    last_payment_escrow_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='lastPaymentEscrowAmount')

    # (Mortgage/Loan) Amount of last fee in last payment
    last_payment_last_fee_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='lastPaymentLastFeeAmount')

    # (Mortgage/Loan) Amount of late charge in last payment
    last_payment_late_charge: typing.Optional[typing.Union[int, float]] = Field(None, alias='lastPaymentLateCharge')

    # (Mortgage/Loan) Principal paid year-to-date
    ytd_principal_paid: typing.Optional[typing.Union[int, float]] = Field(None, alias='ytdPrincipalPaid')

    # (Mortgage/Loan) Interest paid year-to-date
    ytd_interest_paid: typing.Optional[typing.Union[int, float]] = Field(None, alias='ytdInterestPaid')

    # (Mortgage/Loan) Insurance paid year-to-date
    ytd_insurance_paid: typing.Optional[typing.Union[int, float]] = Field(None, alias='ytdInsurancePaid')

    # (Mortgage/Loan) Tax paid year-to-date
    ytd_tax_paid: typing.Optional[typing.Union[int, float]] = Field(None, alias='ytdTaxPaid')

    # (Mortgage/Loan) Enrolled in autopay (F/Y)
    auto_pay_enrolled: typing.Optional[bool] = Field(None, alias='autoPayEnrolled')

    # Margin trading indicator (true / false)
    margin_allowed: typing.Optional[bool] = Field(None, alias='marginAllowed')

    # Cash account allowed indicator (true / false)
    cash_account_allowed: typing.Optional[bool] = Field(None, alias='cashAccountAllowed')

    # (Mortgage/Loan) Collateral on loan
    collateral: typing.Optional[str] = Field(None, alias='collateral')

    # (Mortgage/Loan) Current school
    current_school: typing.Optional[str] = Field(None, alias='currentSchool')

    # (Mortgage/Loan) First payment due date. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    first_payment_date: typing.Optional[int] = Field(None, alias='firstPaymentDate')

    # (Mortgage/Loan) First mortgage (F/Y)
    first_mortgage: typing.Optional[bool] = Field(None, alias='firstMortgage')

    # (Mortgage/Loan) Frequency of payments (monthly, etc.)
    loan_payment_freq: typing.Optional[str] = Field(None, alias='loanPaymentFreq')

    # (Mortgage/Loan) Original school
    original_school: typing.Optional[str] = Field(None, alias='originalSchool')

    # (Mortgage/Loan) Recurring payment amount
    recurring_payment_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='recurringPaymentAmount')

    # (Mortgage/Loan) Owner of loan
    lender: typing.Optional[str] = Field(None, alias='lender')

    # (Mortgage/Loan) Ending balance
    ending_balance_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='endingBalanceAmount')

    # (Mortgage/Loan) Type of loan term
    loan_term_type: typing.Optional[str] = Field(None, alias='loanTermType')

    # (Mortgage/Loan) Number of payments made
    payments_made: typing.Optional[int] = Field(None, alias='paymentsMade')

    # (Mortgage/Loan) Balloon payment amount
    balloon_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='balloonAmount')

    # (Mortgage/Loan) Projected interest on the loan
    projected_interest: typing.Optional[typing.Union[int, float]] = Field(None, alias='projectedInterest')

    # (Mortgage/Loan) Interest paid since inception of loan (life to date)
    interest_paid_ltd: typing.Optional[typing.Union[int, float]] = Field(None, alias='interestPaidLtd')

    # (Mortgage/Loan) Type of interest rate
    interest_rate_type: typing.Optional[str] = Field(None, alias='interestRateType')

    # (Mortgage/Loan) Type of loan payment
    loan_payment_type: typing.Optional[str] = Field(None, alias='loanPaymentType')

    # (Mortgage/Loan) Type of repayment plan for the student loan
    repayment_plan: typing.Optional[str] = Field(None, alias='repaymentPlan')

    # (Mortgage/Loan) Number of payments remaining before loan is paid off
    payments_remaining: typing.Optional[int] = Field(None, alias='paymentsRemaining')

    # (Investment) Net interest earned after deducting interest paid out
    margin_balance: typing.Optional[typing.Union[int, float]] = Field(None, alias='marginBalance')

    # (Investment) Sum of short balance
    short_balance: typing.Optional[typing.Union[int, float]] = Field(None, alias='shortBalance')

    # (Investment) Amount available for cash withdrawal
    available_cash_balance: typing.Optional[typing.Union[int, float]] = Field(None, alias='availableCashBalance')

    # (Investment) amount payable to an investor at maturity
    maturity_value_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='maturityValueAmount')

    # (Investment) Vested amount in account
    vested_balance: typing.Optional[typing.Union[int, float]] = Field(None, alias='vestedBalance')

    # (Investment) Employer matched contributions
    emp_match_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='empMatchAmount')

    # (Investment) Employer pretax contribution amount
    emp_pretax_contrib_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='empPretaxContribAmount')

    # (Investment) Employer pretax contribution amount year to date
    emp_pretax_contrib_amount_ytd: typing.Optional[typing.Union[int, float]] = Field(None, alias='empPretaxContribAmountYtd')

    # (Investment) Total year to date contributions
    contrib_total_ytd: typing.Optional[typing.Union[int, float]] = Field(None, alias='contribTotalYtd')

    # (Investment) Cash balance of account
    cash_balance_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='cashBalanceAmount')

    # (Investment) Pre-tax amount of total balance
    pre_tax_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='preTaxAmount')

    # (Investment) After-tax amount of total balance
    after_tax_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='afterTaxAmount')

    # (Investment) Amount matched
    match_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='matchAmount')

    # (Investment) Amount of balance for profit sharing
    profit_sharing_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='profitSharingAmount')

    # (Investment) Amount of balance rolled over from original account (401k, etc.)
    rollover_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='rolloverAmount')

    # (Investment) Other vested amount
    other_vest_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='otherVestAmount')

    # (Investment) Other nonvested amount
    other_nonvest_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='otherNonvestAmount')

    # (Investment) Current loan balance
    current_loan_balance: typing.Optional[typing.Union[int, float]] = Field(None, alias='currentLoanBalance')

    # (Investment) Interest rate of loan
    loan_rate: typing.Optional[typing.Union[int, float]] = Field(None, alias='loanRate')

    # (Investment) Money available to buy securities
    buy_power: typing.Optional[typing.Union[int, float]] = Field(None, alias='buyPower')

    # (Investment) Life to date of money rolled over
    rollover_ltd: typing.Optional[typing.Union[int, float]] = Field(None, alias='rolloverLtd')

    # (Student Loan) The federal unique loan identifying number
    loan_award_id: typing.Optional[str] = Field(None, alias='loanAwardId')

    # (Student Loan) The original interest rate to which the loan was disbursed, in APY
    original_interest_rate: typing.Optional[typing.Union[int, float]] = Field(None, alias='originalInterestRate')

    # (Student Loan) The financial institution guarantor of the loan (who will pay the loan amount to the owner if the borrower defaults)
    guarantor: typing.Optional[str] = Field(None, alias='guarantor')

    # (Student Loan) Owner of the loan
    owner: typing.Optional[str] = Field(None, alias='owner')

    # (Student Loan) The indication of the presence of an interest subsidy (i.e. subsidized)
    interest_subsidy_type: typing.Optional[str] = Field(None, alias='interestSubsidyType')

    # (Student Loan) The total outstanding interest balance
    interest_balance: typing.Optional[typing.Union[int, float]] = Field(None, alias='interestBalance')

    # (Student Loan) The number of months still outstanding on a loan
    remaining_term_of_ml: typing.Optional[typing.Union[int, float]] = Field(None, alias='remainingTermOfMl')

    # (Student Loan) Initial interest rate of loan
    initial_interest_rate: typing.Optional[typing.Union[int, float]] = Field(None, alias='initialInterestRate')

    # (Student Loan) The total outstanding fees balance
    fees_balance: typing.Optional[typing.Union[int, float]] = Field(None, alias='feesBalance')

    # (Student Loan) Loan interest paid year-to-date
    loan_ytd_interest_paid: typing.Optional[typing.Union[int, float]] = Field(None, alias='loanYtdInterestPaid')

    # (Student Loan) Loan fees paid year-to-date
    loan_ytd_fees_paid: typing.Optional[typing.Union[int, float]] = Field(None, alias='loanYtdFeesPaid')

    # (Student Loan) Loan principal paid year-to-date
    loan_ytd_principal_paid: typing.Optional[typing.Union[int, float]] = Field(None, alias='loanYtdPrincipalPaid')

    # (Student Loan) The repayment status phase (i.e. In School, Grace, Repayment, Deferment, Forbearance)
    loan_status: typing.Optional[str] = Field(None, alias='loanStatus')

    # (Student Loan) The start date of the current status. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    loan_status_start_date: typing.Optional[int] = Field(None, alias='loanStatusStartDate')

    # (Student Loan) The end date of the current status. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    loan_status_end_date: typing.Optional[int] = Field(None, alias='loanStatusEndDate')

    # (Student Loan) The interest rate of multiple interest rates and balances at the group level, in APY
    weighted_interest_rate: typing.Optional[typing.Union[int, float]] = Field(None, alias='weightedInterestRate')

    # (Student Loan) The start date of the current repayment plan. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    repayment_plan_start_date: typing.Optional[int] = Field(None, alias='repaymentPlanStartDate')

    # (Student Loan) The end date of the current repayment plan. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    repayment_plan_end_date: typing.Optional[int] = Field(None, alias='repaymentPlanEndDate')

    # (Student Loan) The expected date of the payoff date. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    expected_payoff_date: typing.Optional[int] = Field(None, alias='expectedPayoffDate')

    # (Student Loan) The date the borrower graduated or dropped below half-time enrollment in school. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    out_of_school_date: typing.Optional[int] = Field(None, alias='outOfSchoolDate')

    # (Student Loan) The date the loan enters into repayment. A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    convert_to_repayment: typing.Optional[int] = Field(None, alias='convertToRepayment')

    # (Student Loan) The number of days past a due date that a payment should have been made
    days_delinquent: typing.Optional[int] = Field(None, alias='daysDelinquent')

    # (Student Loan) The total amount paid towards the principal balance
    total_principal_paid: typing.Optional[typing.Union[int, float]] = Field(None, alias='totalPrincipalPaid')

    # (Student Loan) The total amount paid towards interest
    total_interest_paid: typing.Optional[typing.Union[int, float]] = Field(None, alias='totalInterestPaid')

    # (Student Loan) The total amount paid
    total_amount_paid: typing.Optional[typing.Union[int, float]] = Field(None, alias='totalAmountPaid')
    class Config:
        arbitrary_types_allowed = True
