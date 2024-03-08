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


class Categorization(BaseModel):
    # A normalized payee, derived from the transaction's description and memo fields
    normalized_payee_name: str = Field(alias='normalizedPayeeName')

    # The different categories for transactions. * \"ATM Fee\"  * \"Advertising\"  * \"Air Travel\"  * \"Alcohol & Bars\"  * \"Allowance\"  * \"Amusement\"  * \"Arts\"  * \"Auto & Transport\"  * \"Auto Insurance\"  * \"Auto Payment\"  * \"Baby Supplies\"  * \"Babysitter & Daycare\"  * \"Bank Fee\"  * \"Bills & Utilities\"  * \"Bonus\"  * \"Books\"  * \"Books & Supplies\"  * \"Business Services\"  * \"Buy\"  * \"Cash & ATM\"  * \"Charity\"  * \"Check\"  * \"Child Support\"  * \"Clothing\"  * \"Coffee Shops\"  * \"Credit Card Payment\"  * \"Dentist\"  * \"Deposit\"  * \"Dividend & Cap Gains\"  * \"Doctor\"  * \"Education\"  * \"Electronics & Software\"  * \"Entertainment\"  * \"Eyecare\"  * \"Fast Food\"  * \"Federal Tax\"  * \"Fees & Charges\"  * \"Finance Charge\"  * \"Financial\"  * \"Financial Advisor\"  * \"Food & Dining\"  * \"Furnishings\"  * \"Gas & Fuel\"  * \"Gift\"  * \"Gifts & Donations\"  * \"Groceries\"  * \"Gym\"  * \"Hair\"  * \"Health & Fitness\"  * \"Health Insurance\"  * \"Hobbies\"  * \"Home\"  * \"Home Improvement\"  * \"Home Insurance\"  * \"Home Phone\"  * \"Home Services\"  * \"Home Supplies\"  * \"Hotel\"  * \"Income\"  * \"Interest Income\"  * \"Internet\"  * \"Investments\"  * \"Kids\"  * \"Kids Activities\"  * \"Late Fee\"  * \"Laundry\"  * \"Lawn & Garden\"  * \"Legal\"  * \"Life Insurance\"  * \"Loan Fees and Charges\"  * \"Loan Insurance\"  * \"Loan Interest\"  * \"Loan Payment\"  * \"Loan Principal\"  * \"Loans\"  * \"Local Tax\"  * \"Low Balance\"  * \"Mobile Phone\"  * \"Mortgage & Rent\"  * \"Movies & DVDs\"  * \"Music\"  * \"Newspapers & Magazines\"  * \"Office Supplies\"  * \"Parking\"  * \"Paycheck\"  * \"Personal Care\"  * \"Pet Food & Supplies\"  * \"Pet Grooming\"  * \"Pets\"  * \"Pharmacy\"  * \"Printing\"  * \"Property Tax\"  * \"Public Transportation\"  * \"Reimbursement\"  * \"Rental Car & Taxi\"  * \"Restaurants\"  * \"Sales Tax\"  * \"Sell\"  * \"Service & Parts\"  * \"Service Fee\"  * \"Shipping\"  * \"Shopping\"  * \"Spa & Massage\"  * \"Sporting Goods\"  * \"Sports\"  * \"State Tax\"  * \"Streaming Services\"  * \"Student Loan\"  * \"Taxes\"  * \"Television\"  * \"Toys\"  * \"Trade Commissions\"  * \"Transfer\"  * \"Transfer for Cash Spending\"  * \"Travel\"  * \"Tuition\"  * \"Uncategorized\"  * \"Utilities\"  * \"Vacation\"  * \"Veterinary\"  * \"Internet / Broadband Charges\"
    category: str = Field(alias='category')

    # Country code is Iso3166-1 Alpha-2 code and Alpha 3 standard (max length 3).
    country: str = Field(alias='country')

    # City
    city: typing.Optional[str] = Field(None, alias='city')

    # State
    state: typing.Optional[str] = Field(None, alias='state')

    # A ZIP code
    postal_code: typing.Optional[str] = Field(None, alias='postalCode')

    # Combines the `description` and `memo` data together, removing duplicated information and numbers and special characters
    best_representation: typing.Optional[str] = Field(None, alias='bestRepresentation')
    class Config:
        arbitrary_types_allowed = True
