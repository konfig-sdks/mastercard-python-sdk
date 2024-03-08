<div align="left">

[![Visit Mastercard](./header.png)](https://finicity.com)

# Mastercard<a id="mastercard"></a>

OpenAPI specification for Finicity APIs.

Open Banking solutions in the US are provided by Finicity, a Mastercard
company.


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`mastercard.account_validation_assistance.get_micro_entries_details`](#mastercardaccount_validation_assistanceget_micro_entries_details)
  * [`mastercard.account_validation_assistance.initiate_micro_entries`](#mastercardaccount_validation_assistanceinitiate_micro_entries)
  * [`mastercard.account_validation_assistance.verify_micro_entries`](#mastercardaccount_validation_assistanceverify_micro_entries)
  * [`mastercard.accounts.get_by_id`](#mastercardaccountsget_by_id)
  * [`mastercard.accounts.get_by_institution_login`](#mastercardaccountsget_by_institution_login)
  * [`mastercard.accounts.get_customer_accounts`](#mastercardaccountsget_customer_accounts)
  * [`mastercard.accounts.get_customer_institution_accounts`](#mastercardaccountsget_customer_institution_accounts)
  * [`mastercard.accounts.refresh_customer_account_by_institution_login`](#mastercardaccountsrefresh_customer_account_by_institution_login)
  * [`mastercard.accounts.refresh_customer_aggregation`](#mastercardaccountsrefresh_customer_aggregation)
  * [`mastercard.accounts.refresh_customer_by_institution_login`](#mastercardaccountsrefresh_customer_by_institution_login)
  * [`mastercard.accounts.refresh_customer_data`](#mastercardaccountsrefresh_customer_data)
  * [`mastercard.accounts.remove_by_customer_id_and_account_id`](#mastercardaccountsremove_by_customer_id_and_account_id)
  * [`mastercard.accounts.remove_by_institution_login`](#mastercardaccountsremove_by_institution_login)
  * [`mastercard.accounts_(simple).get_basic_info`](#mastercardaccounts_simpleget_basic_info)
  * [`mastercard.accounts_(simple).get_basic_info_0`](#mastercardaccounts_simpleget_basic_info_0)
  * [`mastercard.accounts_(simple).get_basic_info_1`](#mastercardaccounts_simpleget_basic_info_1)
  * [`mastercard.accounts_(simple).get_basic_info_2`](#mastercardaccounts_simpleget_basic_info_2)
  * [`mastercard.app_registration.assign_applications`](#mastercardapp_registrationassign_applications)
  * [`mastercard.app_registration.create_new_application`](#mastercardapp_registrationcreate_new_application)
  * [`mastercard.app_registration.get_application_status`](#mastercardapp_registrationget_application_status)
  * [`mastercard.app_registration.migrate_institution_login_accounts`](#mastercardapp_registrationmigrate_institution_login_accounts)
  * [`mastercard.app_registration.update_registration`](#mastercardapp_registrationupdate_registration)
  * [`mastercard.assets.get_binary_file`](#mastercardassetsget_binary_file)
  * [`mastercard.authentication.create_access_token`](#mastercardauthenticationcreate_access_token)
  * [`mastercard.authentication.modify_partner_secret`](#mastercardauthenticationmodify_partner_secret)
  * [`mastercard.balance_analytics.generate_analytics_report`](#mastercardbalance_analyticsgenerate_analytics_report)
  * [`mastercard.balance_analytics.generate_fcra_analytics_report`](#mastercardbalance_analyticsgenerate_fcra_analytics_report)
  * [`mastercard.balance_analytics.generate_report`](#mastercardbalance_analyticsgenerate_report)
  * [`mastercard.balance_analytics.get_report_data`](#mastercardbalance_analyticsget_report_data)
  * [`mastercard.balance_analytics.get_report_data_fcra`](#mastercardbalance_analyticsget_report_data_fcra)
  * [`mastercard.bank_statements.generate_report`](#mastercardbank_statementsgenerate_report)
  * [`mastercard.bank_statements.get_customer_statement_in_pdf`](#mastercardbank_statementsget_customer_statement_in_pdf)
  * [`mastercard.bank_statements.get_multiple_statements`](#mastercardbank_statementsget_multiple_statements)
  * [`mastercard.businesses_api.create_new_business`](#mastercardbusinesses_apicreate_new_business)
  * [`mastercard.businesses_api.get_details_by_customer_id`](#mastercardbusinesses_apiget_details_by_customer_id)
  * [`mastercard.businesses_api.get_details_by_id`](#mastercardbusinesses_apiget_details_by_id)
  * [`mastercard.businesses_api.update_by_id`](#mastercardbusinesses_apiupdate_by_id)
  * [`mastercard.cash_flow.generate_personal_report`](#mastercardcash_flowgenerate_personal_report)
  * [`mastercard.cash_flow.generate_report_business`](#mastercardcash_flowgenerate_report_business)
  * [`mastercard.cash_flow_analytics.generate_analytics`](#mastercardcash_flow_analyticsgenerate_analytics)
  * [`mastercard.cash_flow_analytics.generate_fcra_analytics_report`](#mastercardcash_flow_analyticsgenerate_fcra_analytics_report)
  * [`mastercard.cash_flow_analytics.generate_report`](#mastercardcash_flow_analyticsgenerate_report)
  * [`mastercard.cash_flow_analytics.get_report_data`](#mastercardcash_flow_analyticsget_report_data)
  * [`mastercard.cash_flow_analytics.get_report_data_fcra`](#mastercardcash_flow_analyticsget_report_data_fcra)
  * [`mastercard.connect_🔗.fix_url_generation`](#mastercardconnect_%F0%9F%94%97fix_url_generation)
  * [`mastercard.connect_🔗.generate_joint_borrower_url`](#mastercardconnect_%F0%9F%94%97generate_joint_borrower_url)
  * [`mastercard.connect_🔗.generate_lite_url`](#mastercardconnect_%F0%9F%94%97generate_lite_url)
  * [`mastercard.connect_🔗.generate_url`](#mastercardconnect_%F0%9F%94%97generate_url)
  * [`mastercard.connect_🔗.send_connect_email`](#mastercardconnect_%F0%9F%94%97send_connect_email)
  * [`mastercard.connect_🔗.send_email_joint_borrower`](#mastercardconnect_%F0%9F%94%97send_email_joint_borrower)
  * [`mastercard.connect_🔗.verify_micro_entry_microdeposits`](#mastercardconnect_%F0%9F%94%97verify_micro_entry_microdeposits)
  * [`mastercard.consumers.create_consumer_record`](#mastercardconsumerscreate_consumer_record)
  * [`mastercard.consumers.get_by_customer_id`](#mastercardconsumersget_by_customer_id)
  * [`mastercard.consumers.get_by_id`](#mastercardconsumersget_by_id)
  * [`mastercard.consumers.modify_by_id`](#mastercardconsumersmodify_by_id)
  * [`mastercard.customer_authorization_details.get_authorization_details`](#mastercardcustomer_authorization_detailsget_authorization_details)
  * [`mastercard.customers.enroll_active_customer`](#mastercardcustomersenroll_active_customer)
  * [`mastercard.customers.enroll_testing_customer`](#mastercardcustomersenroll_testing_customer)
  * [`mastercard.customers.find_enrolled_users`](#mastercardcustomersfind_enrolled_users)
  * [`mastercard.customers.get_by_id`](#mastercardcustomersget_by_id)
  * [`mastercard.customers.get_with_app_data_by_id`](#mastercardcustomersget_with_app_data_by_id)
  * [`mastercard.customers.modify_by_id`](#mastercardcustomersmodify_by_id)
  * [`mastercard.customers.remove_by_id`](#mastercardcustomersremove_by_id)
  * [`mastercard.institutions.get_branding_by_id`](#mastercardinstitutionsget_branding_by_id)
  * [`mastercard.institutions.get_by_id_details`](#mastercardinstitutionsget_by_id_details)
  * [`mastercard.institutions.get_certified_institutions_with_rssd`](#mastercardinstitutionsget_certified_institutions_with_rssd)
  * [`mastercard.institutions.list_certified_institutions`](#mastercardinstitutionslist_certified_institutions)
  * [`mastercard.institutions.search_financial_institutions`](#mastercardinstitutionssearch_financial_institutions)
  * [`mastercard.pay_statements.upload_for_customer`](#mastercardpay_statementsupload_for_customer)
  * [`mastercard.payment_history.generate_customer_payment_report`](#mastercardpayment_historygenerate_customer_payment_report)
  * [`mastercard.payment_history.generate_fcra_payment_report`](#mastercardpayment_historygenerate_fcra_payment_report)
  * [`mastercard.payment_history.get_report_data`](#mastercardpayment_historyget_report_data)
  * [`mastercard.payment_history.get_report_data_fcra`](#mastercardpayment_historyget_report_data_fcra)
  * [`mastercard.payments.get_account_owner_details`](#mastercardpaymentsget_account_owner_details)
  * [`mastercard.payments.get_account_owner_details_0`](#mastercardpaymentsget_account_owner_details_0)
  * [`mastercard.payments.get_ach_details`](#mastercardpaymentsget_ach_details)
  * [`mastercard.payments.get_available_balance_live`](#mastercardpaymentsget_available_balance_live)
  * [`mastercard.payments.get_latest_cached_balance`](#mastercardpaymentsget_latest_cached_balance)
  * [`mastercard.payments.get_loan_payment_details`](#mastercardpaymentsget_loan_payment_details)
  * [`mastercard.portfolios.get_most_recent_reports`](#mastercardportfoliosget_most_recent_reports)
  * [`mastercard.portfolios.get_portfolio_by_consumer`](#mastercardportfoliosget_portfolio_by_consumer)
  * [`mastercard.reports.by_consumer_id`](#mastercardreportsby_consumer_id)
  * [`mastercard.reports.by_customer_id`](#mastercardreportsby_customer_id)
  * [`mastercard.reports.get_by_consumer_and_id`](#mastercardreportsget_by_consumer_and_id)
  * [`mastercard.reports.get_status`](#mastercardreportsget_status)
  * [`mastercard.third_party_access.generate_key`](#mastercardthird_party_accessgenerate_key)
  * [`mastercard.third_party_access.revoke_partners_access`](#mastercardthird_party_accessrevoke_partners_access)
  * [`mastercard.third_party_access.update_access`](#mastercardthird_party_accessupdate_access)
  * [`mastercard.transactions.get24_months_history_and_generate_report`](#mastercardtransactionsget24_months_history_and_generate_report)
  * [`mastercard.transactions.get_all_customer_transactions`](#mastercardtransactionsget_all_customer_transactions)
  * [`mastercard.transactions.get_by_id`](#mastercardtransactionsget_by_id)
  * [`mastercard.transactions.get_customer_account_transactions`](#mastercardtransactionsget_customer_account_transactions)
  * [`mastercard.transactions.load_historic_transactions_for_customer_account`](#mastercardtransactionsload_historic_transactions_for_customer_account)
  * [`mastercard.tx_push.delete_subscription`](#mastercardtx_pushdelete_subscription)
  * [`mastercard.tx_push.disable_notifications`](#mastercardtx_pushdisable_notifications)
  * [`mastercard.tx_push.inject_test_transaction`](#mastercardtx_pushinject_test_transaction)
  * [`mastercard.tx_push.subscribe_notifications`](#mastercardtx_pushsubscribe_notifications)
  * [`mastercard.verify_assets.customer_voa_report`](#mastercardverify_assetscustomer_voa_report)
  * [`mastercard.verify_assets.generate_voa_with_income_report`](#mastercardverify_assetsgenerate_voa_with_income_report)
  * [`mastercard.verify_assets.get_asset_summary`](#mastercardverify_assetsget_asset_summary)
  * [`mastercard.verify_assets.get_checking_savings_investment_accounts`](#mastercardverify_assetsget_checking_savings_investment_accounts)
  * [`mastercard.verify_income_and_employment.create_voi_report`](#mastercardverify_income_and_employmentcreate_voi_report)
  * [`mastercard.verify_income_and_employment.generate_pay_statement_report`](#mastercardverify_income_and_employmentgenerate_pay_statement_report)
  * [`mastercard.verify_income_and_employment.generate_voe_payroll_report`](#mastercardverify_income_and_employmentgenerate_voe_payroll_report)
  * [`mastercard.verify_income_and_employment.generate_voe_transactions_report`](#mastercardverify_income_and_employmentgenerate_voe_transactions_report)
  * [`mastercard.verify_income_and_employment.generate_voie_paystub_report`](#mastercardverify_income_and_employmentgenerate_voie_paystub_report)
  * [`mastercard.verify_income_and_employment.generate_voie_paystub_with_tx_verify_report`](#mastercardverify_income_and_employmentgenerate_voie_paystub_with_tx_verify_report)
  * [`mastercard.verify_income_and_employment.refresh_voie_payroll_report`](#mastercardverify_income_and_employmentrefresh_voie_payroll_report)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Mastercard&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from mastercard_python_sdk import Mastercard, ApiException

mastercard = Mastercard(

        finicity_app_key = 'YOUR_API_KEY',

        finicity_app_token = 'YOUR_API_KEY',
)

try:
    # Get Micro Entries Details
    get_micro_entries_details_response = mastercard.account_validation_assistance.get_micro_entries_details(
        customer_id="1005061234",
        account_id="5011648377",
    )
    print(get_micro_entries_details_response)
except ApiException as e:
    print("Exception when calling AccountValidationAssistanceApi.get_micro_entries_details: %s\n" % e)
    pprint(e.body)
    if e.status == 400:
        pprint(e.body["code"])
        pprint(e.body["title"])
        pprint(e.body["status"])
        pprint(e.body["level"])
        pprint(e.body["message"])
        pprint(e.body["user_message"])
        pprint(e.body["asset_id"])
        pprint(e.body["account_id"])
    if e.status == 401:
        pprint(e.body["code"])
        pprint(e.body["title"])
        pprint(e.body["status"])
        pprint(e.body["level"])
        pprint(e.body["message"])
        pprint(e.body["user_message"])
        pprint(e.body["asset_id"])
        pprint(e.body["account_id"])
    if e.status == 404:
        pprint(e.body["code"])
        pprint(e.body["title"])
        pprint(e.body["status"])
        pprint(e.body["level"])
        pprint(e.body["message"])
        pprint(e.body["user_message"])
        pprint(e.body["asset_id"])
        pprint(e.body["account_id"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python

import asyncio
from pprint import pprint
from mastercard_python_sdk import Mastercard, ApiException

mastercard = Mastercard(

        finicity_app_key = 'YOUR_API_KEY',

        finicity_app_token = 'YOUR_API_KEY',
)

async def main():
    try:
        # Get Micro Entries Details
        get_micro_entries_details_response = await mastercard.account_validation_assistance.aget_micro_entries_details(
            customer_id="1005061234",
            account_id="5011648377",
        )
        print(get_micro_entries_details_response)
    except ApiException as e:
        print("Exception when calling AccountValidationAssistanceApi.get_micro_entries_details: %s\n" % e)
        pprint(e.body)
        if e.status == 400:
            pprint(e.body["code"])
            pprint(e.body["title"])
            pprint(e.body["status"])
            pprint(e.body["level"])
            pprint(e.body["message"])
            pprint(e.body["user_message"])
            pprint(e.body["asset_id"])
            pprint(e.body["account_id"])
        if e.status == 401:
            pprint(e.body["code"])
            pprint(e.body["title"])
            pprint(e.body["status"])
            pprint(e.body["level"])
            pprint(e.body["message"])
            pprint(e.body["user_message"])
            pprint(e.body["asset_id"])
            pprint(e.body["account_id"])
        if e.status == 404:
            pprint(e.body["code"])
            pprint(e.body["title"])
            pprint(e.body["status"])
            pprint(e.body["level"])
            pprint(e.body["message"])
            pprint(e.body["user_message"])
            pprint(e.body["asset_id"])
            pprint(e.body["account_id"])
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)

asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from mastercard_python_sdk import Mastercard, ApiException

mastercard = Mastercard(

        finicity_app_key = 'YOUR_API_KEY',

        finicity_app_token = 'YOUR_API_KEY',
)

try:
    # Get Micro Entries Details
    get_micro_entries_details_response = mastercard.account_validation_assistance.raw.get_micro_entries_details(
        customer_id="1005061234",
        account_id="5011648377",
    )
    pprint(get_micro_entries_details_response.body)
    pprint(get_micro_entries_details_response.body["status"])
    pprint(get_micro_entries_details_response.body["status_description"])
    pprint(get_micro_entries_details_response.body["creation_date"])
    pprint(get_micro_entries_details_response.body["routing_number"])
    pprint(get_micro_entries_details_response.body["account_number_last4"])
    pprint(get_micro_entries_details_response.headers)
    pprint(get_micro_entries_details_response.status)
    pprint(get_micro_entries_details_response.round_trip_time)
except ApiException as e:
    print("Exception when calling AccountValidationAssistanceApi.get_micro_entries_details: %s\n" % e)
    pprint(e.body)
    if e.status == 400:
        pprint(e.body["code"])
        pprint(e.body["title"])
        pprint(e.body["status"])
        pprint(e.body["level"])
        pprint(e.body["message"])
        pprint(e.body["user_message"])
        pprint(e.body["asset_id"])
        pprint(e.body["account_id"])
    if e.status == 401:
        pprint(e.body["code"])
        pprint(e.body["title"])
        pprint(e.body["status"])
        pprint(e.body["level"])
        pprint(e.body["message"])
        pprint(e.body["user_message"])
        pprint(e.body["asset_id"])
        pprint(e.body["account_id"])
    if e.status == 404:
        pprint(e.body["code"])
        pprint(e.body["title"])
        pprint(e.body["status"])
        pprint(e.body["level"])
        pprint(e.body["message"])
        pprint(e.body["user_message"])
        pprint(e.body["asset_id"])
        pprint(e.body["account_id"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `mastercard.account_validation_assistance.get_micro_entries_details`<a id="mastercardaccount_validation_assistanceget_micro_entries_details"></a>

Fetch the micro entries details.
`customerId` and `accountId` are the identifiers of the customer and account receiving the micro entries.

  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_micro_entries_details_response = mastercard.account_validation_assistance.get_micro_entries_details(
    customer_id="1005061234",
    account_id="5011648377",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### account_id: `str`<a id="account_id-str"></a>

The account ID

#### 🔄 Return<a id="🔄-return"></a>

[`MicroDepositDetails`](./mastercard_python_sdk/pydantic/micro_deposit_details.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/microentry/v1/customers/{customerId}/accounts/{accountId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.account_validation_assistance.initiate_micro_entries`<a id="mastercardaccount_validation_assistanceinitiate_micro_entries"></a>

Initiate the micro entries to customer's account.

Two random micro amounts less than a dollar each will be deposited to provided customer's account.

  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
initiate_micro_entries_response = mastercard.account_validation_assistance.initiate_micro_entries(
    receiver={
        "routing_number": "123456789",
        "account_number": "123456",
        "account_type": "checking",
        "name": "Bob Smith",
        "memo": "micro deposit transfer",
    },
    customer_id="1005061234",
    institution_login_id="1007302745",
    callback_url="https://www.mydomain.com/listener",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### receiver: [`Receiver`](./mastercard_python_sdk/type/receiver.py)<a id="receiver-receivermastercard_python_sdktypereceiverpy"></a>


##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### institution_login_id: `str`<a id="institution_login_id-str"></a>

An institution login ID (from the account record)

##### callback_url: `str`<a id="callback_url-str"></a>

A callback URL where to receive micro deposit notifications

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MicroDepositInitiation`](./mastercard_python_sdk/type/micro_deposit_initiation.py)
#### 🔄 Return<a id="🔄-return"></a>

[`InitiatedMicroDeposit`](./mastercard_python_sdk/pydantic/initiated_micro_deposit.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/microentry/v1/customers/{customerId}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.account_validation_assistance.verify_micro_entries`<a id="mastercardaccount_validation_assistanceverify_micro_entries"></a>

Verify the micro entries as received by customer in customer's account.
Customer needs to verify the micro amounts received in customer's account. `customerId` and `accountId` are the identifiers of the customer and account  receiving the micro entries.

  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
verify_micro_entries_response = mastercard.account_validation_assistance.verify_micro_entries(
    amounts=[0.12, 0.15],
    customer_id="1005061234",
    account_id="5011648377",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### amounts: List[`Union[int, float]`]<a id="amounts-listunionint-float"></a>

The list of amounts to be verified

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### account_id: `str`<a id="account_id-str"></a>

The account ID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MicroDepositVerification`](./mastercard_python_sdk/type/micro_deposit_verification.py)
#### 🔄 Return<a id="🔄-return"></a>

[`VerifiedMicroDeposit`](./mastercard_python_sdk/pydantic/verified_micro_deposit.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/microentry/v1/customers/{customerId}/accounts/{accountId}/amounts` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.accounts.get_by_id`<a id="mastercardaccountsget_by_id"></a>

Get a customer account by ID.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = mastercard.accounts.get_by_id(
    customer_id="1005061234",
    account_id="5011648377",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### account_id: `str`<a id="account_id-str"></a>

The account ID

#### 🔄 Return<a id="🔄-return"></a>

[`CustomerAccount`](./mastercard_python_sdk/pydantic/customer_account.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/aggregation/v2/customers/{customerId}/accounts/{accountId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.accounts.get_by_institution_login`<a id="mastercardaccountsget_by_institution_login"></a>

Get all accounts associated with the given institution login. All accounts returned are accessible by a single set of credentials on a single institution.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_institution_login_response = mastercard.accounts.get_by_institution_login(
    customer_id="1005061234",
    institution_login_id="1007302745",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### institution_login_id: `str`<a id="institution_login_id-str"></a>

The institution login ID

#### 🔄 Return<a id="🔄-return"></a>

[`CustomerAccounts`](./mastercard_python_sdk/pydantic/customer_accounts.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/aggregation/v1/customers/{customerId}/institutionLogins/{institutionLoginId}/accounts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.accounts.get_customer_accounts`<a id="mastercardaccountsget_customer_accounts"></a>

Get all accounts owned by the given customer.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_customer_accounts_response = mastercard.accounts.get_customer_accounts(
    customer_id="1005061234",
    status="pending",
    account_type="ava",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### status: `str`<a id="status-str"></a>

A filter to fetch account in the given status

##### account_type: `str`<a id="account_type-str"></a>

A filter to fetch accounts for the given type. Currently supported types: \"ava\"

#### 🔄 Return<a id="🔄-return"></a>

[`CustomerAccounts`](./mastercard_python_sdk/pydantic/customer_accounts.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/aggregation/v1/customers/{customerId}/accounts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.accounts.get_customer_institution_accounts`<a id="mastercardaccountsget_customer_institution_accounts"></a>

Get all active accounts owned by the given customer at the given institution.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_customer_institution_accounts_response = mastercard.accounts.get_customer_institution_accounts(
    customer_id="1005061234",
    institution_id=4222,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### institution_id: `int`<a id="institution_id-int"></a>

The institution ID

#### 🔄 Return<a id="🔄-return"></a>

[`CustomerAccounts`](./mastercard_python_sdk/pydantic/customer_accounts.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/aggregation/v1/customers/{customerId}/institutions/{institutionId}/accounts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.accounts.refresh_customer_account_by_institution_login`<a id="mastercardaccountsrefresh_customer_account_by_institution_login"></a>

Refresh account and transaction data for all accounts associated with a given 'institutionLoginId` with a connection to the institution. Client apps are not permitted to automate calls to the Refresh services. Active accounts are automatically refreshed by Finicity once per day.

Apps may call Refresh services for a specific customer when there is a specific business case for the need of data that is up to date as of the moment. Please discuss with your account manager and systems engineer for further clarification.

Note: This service will be used for dynamic billing tiers ASD, AFD and ATD.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
mastercard.accounts.refresh_customer_account_by_institution_login(
    customer_id="1005061234",
    institution_login_id="1007302745",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### institution_login_id: `str`<a id="institution_login_id-str"></a>

The institution login ID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/aggregation/v2/customers/{customerId}/institutionLogins/{institutionLoginId}/accounts` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.accounts.refresh_customer_aggregation`<a id="mastercardaccountsrefresh_customer_aggregation"></a>

Refresh account and transaction data for all accounts associated with the  given `customerId` with a connection to the institution.

Client apps are not permitted to automate calls to the Refresh services. Active accounts are automatically refreshed by Finicity once per day. Because many financial institutions only post transactions once per day, calling Refresh services repeatedly is usually a waste of resources and is not recommended.

Apps may call Refresh services for a specific customer when there is a specific business case for the need of data that is up to date as of the moment. Please discuss with your account manager and systems engineer for further clarification.

The recommended timeout setting for this request is 120 seconds in order to receive a response. However, you can terminate the connection after making the call the operation will still complete. You will have to pull the account records to check for an updated aggregation attempt date to know when the refresh is complete.

Note: This service is not available for all tiers of dynamic billing.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
refresh_customer_aggregation_response = mastercard.accounts.refresh_customer_aggregation(
    customer_id="1005061234",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

#### 🔄 Return<a id="🔄-return"></a>

[`CustomerAccounts`](./mastercard_python_sdk/pydantic/customer_accounts.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/aggregation/v1/customers/{customerId}/accounts` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.accounts.refresh_customer_by_institution_login`<a id="mastercardaccountsrefresh_customer_by_institution_login"></a>

Refresh account and transaction data for all accounts associated with a given `institutionLoginId` with a connection to the institution.

Client apps are not permitted to automate calls to the Refresh services. Active accounts are automatically refreshed by Finicity once per day. Because many financial institutions only post transactions once per day, calling Refresh repeatedly is usually a waste of resources and is not recommended.

Apps may call Refresh services for a specific customer when there is a specific business case for the need of data that is up to date as of the moment. Please discuss with your account manager and systems engineer for further clarification.

The recommended timeout setting for this request is 120 seconds in order to receive a response. However, you can terminate the connection after making the call the operation will still complete. You will have to pull the account records to check for an updated aggregation attempt date to know when the refresh is complete.

Note: This service is not available for all tiers of dynamic billing.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
refresh_customer_by_institution_login_response = mastercard.accounts.refresh_customer_by_institution_login(
    customer_id="1005061234",
    institution_login_id="1007302745",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### institution_login_id: `str`<a id="institution_login_id-str"></a>

The institution login ID

#### 🔄 Return<a id="🔄-return"></a>

[`CustomerAccounts`](./mastercard_python_sdk/pydantic/customer_accounts.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/aggregation/v1/customers/{customerId}/institutionLogins/{institutionLoginId}/accounts` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.accounts.refresh_customer_data`<a id="mastercardaccountsrefresh_customer_data"></a>

Refresh account and transaction data for all accounts associated with the  given `customerId` with a connection to the institution.

Client apps are not permitted to automate calls to the Refresh services. Active accounts are automatically refreshed by Finicity once per day.
Apps may call Refresh services for a specific customer when there is a specific business case for the need of data that is up to date as of the moment. Please discuss with your account manager and systems engineer for further clarification.

Note: This service will be used for dynamic billing tiers ASD, AFD and ATD.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
mastercard.accounts.refresh_customer_data(
    customer_id="1005061234",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/aggregation/v2/customers/{customerId}/accounts` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.accounts.remove_by_customer_id_and_account_id`<a id="mastercardaccountsremove_by_customer_id_and_account_id"></a>

Remove the given account from Finicity aggregation.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
mastercard.accounts.remove_by_customer_id_and_account_id(
    customer_id="1005061234",
    account_id="5011648377",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### account_id: `str`<a id="account_id-str"></a>

The account ID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/aggregation/v1/customers/{customerId}/accounts/{accountId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.accounts.remove_by_institution_login`<a id="mastercardaccountsremove_by_institution_login"></a>

Remove from Finicity aggregation the set of accounts matching the institution login ID.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
mastercard.accounts.remove_by_institution_login(
    customer_id="1005061234",
    institution_login_id="1007302745",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### institution_login_id: `str`<a id="institution_login_id-str"></a>

The institution login ID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/aggregation/v1/customers/{customerId}/institutionLogins/{institutionLoginId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.accounts_(simple).get_basic_info`<a id="mastercardaccounts_simpleget_basic_info"></a>

This API is a lighter version of Get Customer Accounts by Institution ID, returning only basic information of active accounts owned by the given customer at the given institution.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_basic_info_response = mastercard.accounts_(simple).get_basic_info(
    customer_id="1005061234",
    institution_id=4222,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### institution_id: `int`<a id="institution_id-int"></a>

The institution ID

#### 🔄 Return<a id="🔄-return"></a>

[`CustomerAccountsSimple`](./mastercard_python_sdk/pydantic/customer_accounts_simple.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/aggregation/v1/customers/{customerId}/institutions/{institutionId}/accounts/simple` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.accounts_(simple).get_basic_info_0`<a id="mastercardaccounts_simpleget_basic_info_0"></a>

This API is a lighter version of Get Customer Accounts by Institution Login ID, returning only basic information of all active accounts owned by the given customer at the given institution login ID.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_basic_info_0_response = mastercard.accounts_(simple).get_basic_info_0(
    customer_id="1005061234",
    institution_login_id="1007302745",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### institution_login_id: `str`<a id="institution_login_id-str"></a>

The institution login ID

#### 🔄 Return<a id="🔄-return"></a>

[`CustomerAccountsSimple`](./mastercard_python_sdk/pydantic/customer_accounts_simple.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/aggregation/v1/customers/{customerId}/institutionLogins/{institutionLoginId}/accounts/simple` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.accounts_(simple).get_basic_info_1`<a id="mastercardaccounts_simpleget_basic_info_1"></a>

This API is a lighter version of Get Customer Accounts by ID, returning only basic information of a customer account.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_basic_info_1_response = mastercard.accounts_(simple).get_basic_info_1(
    customer_id="1005061234",
    account_id="5011648377",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### account_id: `str`<a id="account_id-str"></a>

The account ID

#### 🔄 Return<a id="🔄-return"></a>

[`CustomerAccountSimple`](./mastercard_python_sdk/pydantic/customer_account_simple.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/aggregation/v1/customers/{customerId}/accounts/{accountId}/simple` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.accounts_(simple).get_basic_info_2`<a id="mastercardaccounts_simpleget_basic_info_2"></a>

This API is a lighter version of Get Customer Accounts, returning only basic information of all active customer accounts.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_basic_info_2_response = mastercard.accounts_(simple).get_basic_info_2(
    customer_id="1005061234",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

#### 🔄 Return<a id="🔄-return"></a>

[`CustomerAccountsSimple`](./mastercard_python_sdk/pydantic/customer_accounts_simple.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/aggregation/v1/customers/{customerId}/accounts/simple` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.app_registration.assign_applications`<a id="mastercardapp_registrationassign_applications"></a>

If you have multiple applications for a single client, and you want to register their applications to access financial institutions using OAuth connections, then use this API to assign applications to an existing customer.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
mastercard.app_registration.assign_applications(
    customer_id="1005061234",
    application_id="123456789",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### application_id: `str`<a id="application_id-str"></a>

The application ID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/aggregation/v1/customers/{customerId}/applications/{applicationId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.app_registration.create_new_application`<a id="mastercardapp_registrationcreate_new_application"></a>

Register a new application to access financial institutions using OAuth connections.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_application_response = mastercard.app_registration.create_new_application(
    app_description="The app that makes your budgeting experience awesome",
    app_name="Awesome Budget App",
    app_url="https://www.finicity.com/",
    owner_address_line1="434 W Ascension Way",
    owner_address_line2="Suite #200",
    owner_city="Murray",
    owner_country="USA",
    owner_name="Finicity",
    owner_postal_code="84123",
    owner_state="UT",
    image="PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjxzdmcgICAKICAgeG1sbnM6c3ZnPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIKICAgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIgogICB2ZXJzaW9uPSIxLjEiCiAgIHZpZXdCb3g9IjAgMCAwIDAiCiAgIGhlaWdodD0iMCIKICAgd2lkdGg9IjAiPgogICAgPGcvPgo8L3N2Zz4K",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_description: `str`<a id="app_description-str"></a>

A short description of the app. This will be visible to end users in the FI interface.

##### app_name: `str`<a id="app_name-str"></a>

The name of the application assigned to the customer

##### app_url: `str`<a id="app_url-str"></a>

An URL for the app. This will be visible to end users in the FI interface.

##### owner_address_line1: `str`<a id="owner_address_line1-str"></a>

Address line 1

##### owner_address_line2: `str`<a id="owner_address_line2-str"></a>

Address line 2

##### owner_city: `str`<a id="owner_city-str"></a>

City for the business entity that owns the app. Information for registration purposes only and not given to the end user.

##### owner_country: `str`<a id="owner_country-str"></a>

Country for the  business entity that owns the app. Information for registration purposes only and not given to the end user.

##### owner_name: `str`<a id="owner_name-str"></a>

Business name for the business entity that owns the app. Information for registration purposes only and not given to the end user.

##### owner_postal_code: `str`<a id="owner_postal_code-str"></a>

Zip code for the business entity that owns the app. Information for registration purposes only and not given to the end user.

##### owner_state: `str`<a id="owner_state-str"></a>

State for the business entity that owns the app. Information for registration purposes only and not given to the end user.

##### image: `str`<a id="image-str"></a>

An app logo passed as a Base64 encoded image (1:1 SVG file, must be less than 50KB)

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Application`](./mastercard_python_sdk/type/application.py)
#### 🔄 Return<a id="🔄-return"></a>

[`RegisteredApplication`](./mastercard_python_sdk/pydantic/registered_application.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/aggregation/v1/partners/applications` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.app_registration.get_application_status`<a id="mastercardapp_registrationget_application_status"></a>

Get the status of your application registration(s).

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_application_status_response = mastercard.app_registration.get_application_status(
    pre_app_id="2581",
    application_id="123456789",
    status="P",
    app_name="Awesome Budget App",
    submitted_date=1607450357,
    modified_date=1607450357,
    page=1,
    page_size=20,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### pre_app_id: `str`<a id="pre_app_id-str"></a>

The application registration tracking ID

##### application_id: `str`<a id="application_id-str"></a>

The application ID

##### status: `str`<a id="status-str"></a>

Look up app registration requests by status

##### app_name: `str`<a id="app_name-str"></a>

Look up app registration requests by app name

##### submitted_date: `int`<a id="submitted_date-int"></a>

Look up app registration requests by the date they were submitted

##### modified_date: `int`<a id="modified_date-int"></a>

Look up app registration requests by the date the request was updated. This can be used to determine when a request was updated to \"A\" or \"R\".

##### page: `int`<a id="page-int"></a>

Index of the page of results to return

##### page_size: `int`<a id="page_size-int"></a>

Maximum number of results per page

#### 🔄 Return<a id="🔄-return"></a>

[`AppStatuses`](./mastercard_python_sdk/pydantic/app_statuses.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/aggregation/v2/partners/applications` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.app_registration.migrate_institution_login_accounts`<a id="mastercardapp_registrationmigrate_institution_login_accounts"></a>

The `institutionLoginId` parameter uses Finicity's internal FI mapping to move accounts from the current FI legacy connection to the new OAuth FI connection.

This API returns a list of accounts for the given institution login ID.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
migrate_institution_login_accounts_response = mastercard.app_registration.migrate_institution_login_accounts(
    customer_id="1005061234",
    institution_login_id="1007302745",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### institution_login_id: `str`<a id="institution_login_id-str"></a>

The institution login ID

#### 🔄 Return<a id="🔄-return"></a>

[`CustomerAccounts`](./mastercard_python_sdk/pydantic/customer_accounts.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/aggregation/v2/customers/{customerId}/institutionLogins/{institutionLoginId}/migration` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.app_registration.update_registration`<a id="mastercardapp_registrationupdate_registration"></a>

Update a registered application.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_registration_response = mastercard.app_registration.update_registration(
    app_description="The app that makes your budgeting experience awesome",
    app_name="Awesome Budget App",
    app_url="https://www.finicity.com/",
    owner_address_line1="434 W Ascension Way",
    owner_address_line2="Suite #200",
    owner_city="Murray",
    owner_country="USA",
    owner_name="Finicity",
    owner_postal_code="84123",
    owner_state="UT",
    image="PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjxzdmcgICAKICAgeG1sbnM6c3ZnPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIKICAgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIgogICB2ZXJzaW9uPSIxLjEiCiAgIHZpZXdCb3g9IjAgMCAwIDAiCiAgIGhlaWdodD0iMCIKICAgd2lkdGg9IjAiPgogICAgPGcvPgo8L3N2Zz4K",
    pre_app_id="2581",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_description: `str`<a id="app_description-str"></a>

A short description of the app. This will be visible to end users in the FI interface.

##### app_name: `str`<a id="app_name-str"></a>

The name of the application assigned to the customer

##### app_url: `str`<a id="app_url-str"></a>

An URL for the app. This will be visible to end users in the FI interface.

##### owner_address_line1: `str`<a id="owner_address_line1-str"></a>

Address line 1

##### owner_address_line2: `str`<a id="owner_address_line2-str"></a>

Address line 2

##### owner_city: `str`<a id="owner_city-str"></a>

City for the business entity that owns the app. Information for registration purposes only and not given to the end user.

##### owner_country: `str`<a id="owner_country-str"></a>

Country for the  business entity that owns the app. Information for registration purposes only and not given to the end user.

##### owner_name: `str`<a id="owner_name-str"></a>

Business name for the business entity that owns the app. Information for registration purposes only and not given to the end user.

##### owner_postal_code: `str`<a id="owner_postal_code-str"></a>

Zip code for the business entity that owns the app. Information for registration purposes only and not given to the end user.

##### owner_state: `str`<a id="owner_state-str"></a>

State for the business entity that owns the app. Information for registration purposes only and not given to the end user.

##### image: `str`<a id="image-str"></a>

An app logo passed as a Base64 encoded image (1:1 SVG file, must be less than 50KB)

##### pre_app_id: `str`<a id="pre_app_id-str"></a>

The application registration tracking ID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Application`](./mastercard_python_sdk/type/application.py)
#### 🔄 Return<a id="🔄-return"></a>

[`RegisteredApplication`](./mastercard_python_sdk/pydantic/registered_application.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/aggregation/v1/partners/applications/{preAppId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.assets.get_binary_file`<a id="mastercardassetsget_binary_file"></a>

Retrieve a binary file for the given asset ID.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_binary_file_response = mastercard.assets.get_binary_file(
    customer_id="1005061234",
    asset_id="097545c5-1c2a-4f20-a5ef-77f0820344c9-2018601178",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### asset_id: `str`<a id="asset_id-str"></a>

The asset ID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/aggregation/v1/customers/{customerId}/assets/{assetId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.authentication.create_access_token`<a id="mastercardauthenticationcreate_access_token"></a>

Send Partner ID and Partner Secret to the Partner Authentication service to obtain a token for accessing Finicity APIs.
* The token is valid for two hours and is required on all calls to the Finicity APIs
* As a best practice, use a single token for all calls. Assign a timestamp for each token, and then check the current timestamp before making any calls. If the token is greater than 90 minutes, generate a new one.
* ⚠️ After five failed attempts to authenticate, your account will be locked. Contact [support@finicity.com](mailto:support@finicity.com) to get help resetting your account.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_access_token_response = mastercard.authentication.create_access_token(
    partner_id="1234583871234",
    partner_secret="aqJ5Ic4SEVx2IgDQ6oR4",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### partner_id: `str`<a id="partner_id-str"></a>

Your Partner ID displayed in the [Developer Dashboard](https://developer.mastercard.com/account/log-in)

##### partner_secret: `str`<a id="partner_secret-str"></a>

Your Partner Secret displayed in the [Developer Dashboard](https://developer.mastercard.com/account/log-in)

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PartnerCredentials`](./mastercard_python_sdk/type/partner_credentials.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AccessToken`](./mastercard_python_sdk/pydantic/access_token.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/aggregation/v2/partners/authentication` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.authentication.modify_partner_secret`<a id="mastercardauthenticationmodify_partner_secret"></a>

Change the Partner Secret used to authenticate this partner.

The secret does not expire, but can be changed by calling this API. A valid Partner Secret may contain upper and lowercase characters, numbers, and the characters !, @, #, $, %, &, *, _, -, +. It must include at least one number and at least one letter, and its length should be between 12 and 255 characters.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
mastercard.authentication.modify_partner_secret(
    partner_id="1234583871234",
    partner_secret="aqJ5Ic4SEVx2IgDQ6oR4",
    new_partner_secret="OrU7tjiA3tIspCgb85xV",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### partner_id: `str`<a id="partner_id-str"></a>

Your Partner ID displayed in the [Developer Dashboard](https://developer.mastercard.com/account/log-in)

##### partner_secret: `str`<a id="partner_secret-str"></a>

Your Partner Secret displayed in the [Developer Dashboard](https://developer.mastercard.com/account/log-in)

##### new_partner_secret: `str`<a id="new_partner_secret-str"></a>

A new value for the Partner Secret

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PartnerCredentialsWithNewSecret`](./mastercard_python_sdk/type/partner_credentials_with_new_secret.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/aggregation/v2/partners/authentication` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.balance_analytics.generate_analytics_report`<a id="mastercardbalance_analyticsgenerate_analytics_report"></a>

Balance Analytics for Business analyzes bank balances over time to report metrics and identify behavior that may indicate risk.

Calculated metrics include:
* Current/available account balances
* Minimum/maximum/average account balances over the requested time
  period and broken down by month

* Daily ending balance of accounts for each day in the requested time
  period

* Propensity of the customer's account balances to increase week over
  week

* Number of days in the requested time period ending with a negative
  balance


This version of the API is intended for piloting and integration testing your application with the Balance Analytics product. It does not adhere to FCRA requirements, and should not be used for production/lending purposes. See _Generate Balance Analytics - FCRA_ for the FCRA compliant version of this API.

A successful call to this API will generate analytics and store a report within Finicity. The report can be retrieved via _Get Balance Analytics Report_ (operation: _GetObbAnalyticsReport_).

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_analytics_report_response = mastercard.balance_analytics.generate_analytics_report(
    customer_id="1005061234",
    account_ids=[
        1
    ],
    length_of_report=730,
    reference_number="abc123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### account_ids: List[`int`]<a id="account_ids-listint"></a>

The list of account IDs to include in the report. If omitted, all accounts on record for the customer will be used.

##### length_of_report: `int`<a id="length_of_report-int"></a>

Number of days to search for transactions. Must be one of 30, 90, 180, 270, 365, or 730. If omitted, defaults to 2 years from current time at which the request was received (730 days).

##### reference_number: `str`<a id="reference_number-str"></a>

Partner-provided reference number to correlate reports.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BalanceAndCashFlowAnalyticsReportConstraints`](./mastercard_python_sdk/type/balance_and_cash_flow_analytics_report_constraints.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ObbAnalyticsReportAck`](./mastercard_python_sdk/pydantic/obb_analytics_report_ack.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/analytics/balance/v1/customer/{customerId}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.balance_analytics.generate_fcra_analytics_report`<a id="mastercardbalance_analyticsgenerate_fcra_analytics_report"></a>

Balance Analytics for Business analyzes bank balances over time to report metrics and identify behavior that may indicate risk.

Calculated metrics include:
* Current/available account balances
* Minimum/maximum/average account balances over the requested time
  period and broken down by month

* Daily ending balance of accounts for each day in the requested time
  period

* Propensity of the customer's account balances to increase week over
  week

* Number of days in the requested time period ending with a negative
  balance


This version of the API is intended for production use. It maintains and enforces all compliance with FCRA rules and requirements.

*Note:* this is a premium service, billable per every successful API call for non-testing customers.

A successful call to this API will generate analytics and store a report within Finicity. The report can be retrieved via _Get Balance Analytics Report - FCRA_ (operation: _GetObbAnalyticsReportFCRA_).

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_fcra_analytics_report_response = mastercard.balance_analytics.generate_fcra_analytics_report(
    customer_id="1005061234",
    account_ids=[
        1
    ],
    length_of_report=730,
    reference_number="abc123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### account_ids: List[`int`]<a id="account_ids-listint"></a>

The list of account IDs to include in the report. If omitted, all accounts on record for the customer will be used.

##### length_of_report: `int`<a id="length_of_report-int"></a>

Number of days to search for transactions. Must be one of 30, 90, 180, 270, 365, or 730. If omitted, defaults to 2 years from current time at which the request was received (730 days).

##### reference_number: `str`<a id="reference_number-str"></a>

Partner-provided reference number to correlate reports.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BalanceAndCashFlowAnalyticsReportConstraints`](./mastercard_python_sdk/type/balance_and_cash_flow_analytics_report_constraints.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ObbAnalyticsReportAck`](./mastercard_python_sdk/pydantic/obb_analytics_report_ack.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/analytics/balance/v1/customer/{customerId}/fcra` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.balance_analytics.generate_report`<a id="mastercardbalance_analyticsgenerate_report"></a>

Generate a Balance Analytics Report for a given customer. This service retrieves up to two years of transaction history from connected accounts.

Balance  Analytics analyzes bank balances over time to report metrics and identify behavior that may indicate risk.

Before calling this API, A consumer or business may need to be created for the given customer ID based on the user type (see Consumer/Business APIs).

If no account type of checking or savings is found, the service will return HTTP 400 Bad Request.

This is a premium service, billable per every successful API call for non-testing customers. A successful call to this API will generate analytics report which can be retrieved via Get Report by Customer or Get Report by Consumer.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_report_response = mastercard.balance_analytics.generate_report(
    customer_id="1005061234",
    user_type="personal",
    analytics_report_data={
        "for_cra_purpose": True,
        "applicant_is_personal_guarantor": True,
        "time_interval_types": ["MONTHLY_CALENDAR"],
    },
    account_ids="5011648377 5011648378 5011648379",
    report_custom_fields=[
        {
            "label": "loanID",
            "value": "123456",
            "shown": True,
        }
    ],
    from_date=1607450357,
    callback_url="https://finicity-test/webhook",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### user_type: `str`<a id="user_type-str"></a>

UserType indicates if the request is for a business or personal use case, Allowed values: business/personal.

##### analytics_report_data: [`AnalyticsReportData`](./mastercard_python_sdk/type/analytics_report_data.py)<a id="analytics_report_data-analyticsreportdatamastercard_python_sdktypeanalytics_report_datapy"></a>


##### account_ids: `str`<a id="account_ids-str"></a>

A whitespace-separated list of account IDs to be included in the report (all accounts will be included if not set)

##### report_custom_fields: [`ReportCustomFields`](./mastercard_python_sdk/type/report_custom_fields.py)<a id="report_custom_fields-reportcustomfieldsmastercard_python_sdktypereport_custom_fieldspy"></a>

##### from_date: `int`<a id="from_date-int"></a>

A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).

##### callback_url: `str`<a id="callback_url-str"></a>

A Report Listener URL to receive notifications. The webhook must respond to the Finicity API with a 2xx HTTP status code.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AnalyticsReportConstraints`](./mastercard_python_sdk/type/analytics_report_constraints.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AnalyticsReportAck`](./mastercard_python_sdk/pydantic/analytics_report_ack.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/decisioning/v2/customers/{customerId}/reports/balance-analytics/userTypes/{userType}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.balance_analytics.get_report_data`<a id="mastercardbalance_analyticsget_report_data"></a>

Retrieve the report saved by _Generate Balance Analytics_, _Generate Cash Flow Analytics_, or _Generate Payment History_. Requires the report ID generated by the previous call.

Report data can either be retrieved as a JSON document or PDF file.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_report_data_response = mastercard.balance_analytics.get_report_data(
    obb_report_id="bcab9592-e032-4e7b-b737-0380619a0573",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### obb_report_id: `str`<a id="obb_report_id-str"></a>

Report ID generated and returned by OBB products

#### 🔄 Return<a id="🔄-return"></a>

[`ObbAnalyticsReport`](./mastercard_python_sdk/pydantic/obb_analytics_report.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/analytics/data/v1/{obb_report_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.balance_analytics.get_report_data_fcra`<a id="mastercardbalance_analyticsget_report_data_fcra"></a>

Retrieve the report saved by _Generate Balance Analytics - FCRA_, _Generate Cash Flow Analytics - FCRA_, or _Generate Payment History - FCRA_. Requires the report ID generated by the previous call.

Report data can either be retrieved as a JSON document or PDF file.

*Note:* this is a premium service, billable per every successful API call for non-testing customers.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_report_data_fcra_response = mastercard.balance_analytics.get_report_data_fcra(
    obb_report_id="bcab9592-e032-4e7b-b737-0380619a0573",
    purpose="3F",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### obb_report_id: `str`<a id="obb_report_id-str"></a>

Report ID generated and returned by OBB products

##### purpose: `str`<a id="purpose-str"></a>

2-digit code from [Permissible Purpose Codes](https://developer.mastercard.com/open-banking-us/documentation/products/lend/report-handling/permissible-purpose-codes/), specifying the reason for retrieving this report. Required for retrieving some reports.

#### 🔄 Return<a id="🔄-return"></a>

[`ObbAnalyticsReport`](./mastercard_python_sdk/pydantic/obb_analytics_report.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/analytics/data/v1/{obb_report_id}/fcra` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.bank_statements.generate_report`<a id="mastercardbank_statementsgenerate_report"></a>

Generate a Statement Report for the given accounts under the given customer.

This is a premium service. A billable event will be created upon the successful generation of the Statement Report.

Before calling this API, a consumer must be created for the given customer ID (see Consumers APIs).

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_report_response = mastercard.bank_statements.generate_report(
    statement_report_data={
        "account_id": 5011648377,
        "statement_index": 1,
    },
    customer_id="1005061234",
    report_custom_fields=[
        {
            "label": "loanID",
            "value": "123456",
            "shown": True,
        }
    ],
    callback_url="https://finicity-test/webhook",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### statement_report_data: [`StatementData`](./mastercard_python_sdk/type/statement_data.py)<a id="statement_report_data-statementdatamastercard_python_sdktypestatement_datapy"></a>


##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### report_custom_fields: [`ReportCustomFields`](./mastercard_python_sdk/type/report_custom_fields.py)<a id="report_custom_fields-reportcustomfieldsmastercard_python_sdktypereport_custom_fieldspy"></a>

##### callback_url: `str`<a id="callback_url-str"></a>

A Report Listener URL to receive notifications. The webhook must respond to the Finicity API with a 2xx HTTP status code.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`StatementReportConstraints`](./mastercard_python_sdk/type/statement_report_constraints.py)
#### 🔄 Return<a id="🔄-return"></a>

[`StatementReportAck`](./mastercard_python_sdk/pydantic/statement_report_ack.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/decisioning/v2/customers/{customerId}/statement` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.bank_statements.get_customer_statement_in_pdf`<a id="mastercardbank_statementsget_customer_statement_in_pdf"></a>

Retrieve the customer's bank statements in PDF format. Up to 24 months of history is available depending on the financial institution. Since this is a premium service, charges incur per each successful statement retrieved.

For certified financial institutions, statements are available for the following account types:
* Checking
* Savings
* Money market
* CDs
* Investments
* Mortgage
* Credit cards
* Loans
* Line of credit
* Student Loans

Note: setting the timeout to 180 seconds is recommended to allow enough time for a response.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_customer_statement_in_pdf_response = mastercard.bank_statements.get_customer_statement_in_pdf(
    customer_id="1005061234",
    account_id="5011648377",
    index=1,
    type="taxStatement",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### account_id: `str`<a id="account_id-str"></a>

The account ID

##### index: `int`<a id="index-int"></a>

Request statements from 1-24. By default, 1 is the most recent statement. Increase the index value to count back (by month) and retrieve its most recent statement.

##### type: `str`<a id="type-str"></a>

The type of statement to retrieve

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/aggregation/v1/customers/{customerId}/accounts/{accountId}/statement` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.bank_statements.get_multiple_statements`<a id="mastercardbank_statementsget_multiple_statements"></a>

This endpoint is retrieving the account statement for a given customer. The maximum number of indexes it will fetch for a single login is 24.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_multiple_statements_response = mastercard.bank_statements.get_multiple_statements(
    customer_id="1005061234",
    account_id="5011648377",
    index="1,2,3,4,5,6",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### account_id: `str`<a id="account_id-str"></a>

The account ID

##### index: `str`<a id="index-str"></a>

Request statements with comma-separated indexes ranged between 1-24. The default value is 1 and it will return the most recent statement. Increasing the index will return older statements, for example, setting the index value to 6 will return a statement from six months ago.

#### 🔄 Return<a id="🔄-return"></a>

[`CustomerAccountMultipleStatements`](./mastercard_python_sdk/pydantic/customer_account_multiple_statements.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/aggregation/v3/customers/{customerId}/accounts/{accountId}/statement` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.businesses_api.create_new_business`<a id="mastercardbusinesses_apicreate_new_business"></a>

Create a new business record for the associated customer.
A customer can have one business record associated.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_business_response = mastercard.businesses_api.create_new_business(
    name="ABC Tires Inc",
    personally_liable=True,
    address={
        "address_line1": "434 W Ascension Way",
        "address_line2": "Suite #200",
        "city": "Murray",
        "state": "UT",
        "country": "US",
        "postal_code": "84123",
    },
    phone_number={
        "country_code": "1",
        "phone_no": "8042221111",
    },
    customer_id="1005061234",
    url="https://www.finicity.com/",
    email="myname@mycompany.com",
    type="Nonprofit",
    tax_id="A1234561Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

The legal name of the business

##### personally_liable: `bool`<a id="personally_liable-bool"></a>

Indicates whether a business owner is personally liable for a loan

##### address: [`NewAddress`](./mastercard_python_sdk/type/new_address.py)<a id="address-newaddressmastercard_python_sdktypenew_addresspy"></a>


##### phone_number: [`PhoneNumberFormat`](./mastercard_python_sdk/type/phone_number_format.py)<a id="phone_number-phonenumberformatmastercard_python_sdktypephone_number_formatpy"></a>


##### customer_id: `str`<a id="customer_id-str"></a>

Unique identifier of the customer

##### url: `str`<a id="url-str"></a>

A URL for the business website

##### email: `str`<a id="email-str"></a>

An email address

##### type: `str`<a id="type-str"></a>

The business type eg LLC, Corp, S Corp, C Corp, B Corp, Sole Propriertorship, Nonprofit, etc.

##### tax_id: `str`<a id="tax_id-str"></a>

Provide details of the tax id for the business

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`NewBusiness`](./mastercard_python_sdk/type/new_business.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Business`](./mastercard_python_sdk/pydantic/business.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/business-services/customers/{customer_id}/businesses` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.businesses_api.get_details_by_customer_id`<a id="mastercardbusinesses_apiget_details_by_customer_id"></a>

Retrieve business details associated with a specific customer. By providing the unique customer identifier, details about the associated business can be accessed.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_by_customer_id_response = mastercard.businesses_api.get_details_by_customer_id(
    customer_id="1005061234",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

Unique identifier of the customer

#### 🔄 Return<a id="🔄-return"></a>

[`BusinessList`](./mastercard_python_sdk/pydantic/business_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/business-services/customers/{customer_id}/businesses` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.businesses_api.get_details_by_id`<a id="mastercardbusinesses_apiget_details_by_id"></a>

Retrieve business details.

_Supported regions_: ![\U0001F1FA\U0001F1F8](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_by_id_response = mastercard.businesses_api.get_details_by_id(
    customer_id="1005061234",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

Unique identifier of the customer

#### 🔄 Return<a id="🔄-return"></a>

[`BusinessList`](./mastercard_python_sdk/pydantic/business_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/business-services/businesses/{business_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.businesses_api.update_by_id`<a id="mastercardbusinesses_apiupdate_by_id"></a>

Update the details of a business based on its unique identifier. By providing the specific business ID and the updated information in the request, modifications can be made to the business's profile.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_by_id_response = mastercard.businesses_api.update_by_id(
    name="ABC Tires Inc",
    personally_liable=True,
    address={
        "address_line1": "434 W Ascension Way",
        "address_line2": "Suite #200",
        "city": "Murray",
        "state": "UT",
        "country": "US",
        "postal_code": "84123",
    },
    phone_number={
        "country_code": "1",
        "phone_no": "8042221111",
    },
    customer_id="1005061234",
    url="https://www.finicity.com/",
    email="myname@mycompany.com",
    type="Nonprofit",
    tax_id="A1234561Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

The legal name of the business

##### personally_liable: `bool`<a id="personally_liable-bool"></a>

Indicates whether a business owner is personally liable for a loan

##### address: [`NewAddress`](./mastercard_python_sdk/type/new_address.py)<a id="address-newaddressmastercard_python_sdktypenew_addresspy"></a>


##### phone_number: [`PhoneNumberFormat`](./mastercard_python_sdk/type/phone_number_format.py)<a id="phone_number-phonenumberformatmastercard_python_sdktypephone_number_formatpy"></a>


##### customer_id: `str`<a id="customer_id-str"></a>

Unique identifier of the customer

##### url: `str`<a id="url-str"></a>

A URL for the business website

##### email: `str`<a id="email-str"></a>

An email address

##### type: `str`<a id="type-str"></a>

The business type eg LLC, Corp, S Corp, C Corp, B Corp, Sole Propriertorship, Nonprofit, etc.

##### tax_id: `str`<a id="tax_id-str"></a>

Provide details of the tax id for the business

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`NewBusiness`](./mastercard_python_sdk/type/new_business.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Business`](./mastercard_python_sdk/pydantic/business.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/business-services/businesses/{business_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.cash_flow.generate_personal_report`<a id="mastercardcash_flowgenerate_personal_report"></a>

Generate a Cash Flow Report (Personal) report for all checking and savings under the given customer. This service retrieves up to two years of transaction history for the given account. It then uses this information to generate the CFR report.

This report is provided under FCRA rules, with Finicity acting as the CRA (Consumer Reporting Agency). If an individual account is included in the report - for example, with an individual acting as an personal guarantor on the loan - then this version of the report should be used. In case of an adverse action on the loan where the decision was based on this report, then the borrower can be referred to the [Finicity Consumer Portal](https://consumer.finicityreports.com) where they can view this report and submit a dispute if they feel any information in this report is inaccurate.

Before calling this API, a consumer must be created for the given customer ID (see Consumers APIs).

If no account type of checking or savings is found, the service will return HTTP 400 Bad Request.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_personal_report_response = mastercard.cash_flow.generate_personal_report(
    customer_id="1005061234",
    account_ids="5011648377 5011648378 5011648379",
    report_custom_fields=[
        {
            "label": "loanID",
            "value": "123456",
            "shown": True,
        }
    ],
    show_nsf=False,
    from_date=1607450357,
    income_stream_confidence_minimum=50,
    callback_url="https://finicity-test/webhook",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### account_ids: `str`<a id="account_ids-str"></a>

A whitespace-separated list of account IDs to be included in the report (all accounts will be included if not set)

##### report_custom_fields: [`ReportCustomFields`](./mastercard_python_sdk/type/report_custom_fields.py)<a id="report_custom_fields-reportcustomfieldsmastercard_python_sdktypereport_custom_fieldspy"></a>

##### show_nsf: `bool`<a id="show_nsf-bool"></a>

Include the non-sufficient funds (NSF) summary JSON and the NSF summary PDF section in the report. Data included: * Account  * Total number of NSF funds  * Days since the most recent NFS funds fee

##### from_date: `int`<a id="from_date-int"></a>

A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).

##### income_stream_confidence_minimum: `int`<a id="income_stream_confidence_minimum-int"></a>

Include income streams in the report, based on the income stream's confidence score. For example, Use the value 50 to include only income streams with a confidence score of 50 or higher.

##### callback_url: `str`<a id="callback_url-str"></a>

A Report Listener URL to receive notifications. The webhook must respond to the Finicity API with a 2xx HTTP status code.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CashFlowReportConstraints`](./mastercard_python_sdk/type/cash_flow_report_constraints.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CashFlowReportAck`](./mastercard_python_sdk/pydantic/cash_flow_report_ack.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/decisioning/v2/customers/{customerId}/cashFlowPersonal` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.cash_flow.generate_report_business`<a id="mastercardcash_flowgenerate_report_business"></a>

Generate a Cash Flow Report (Business) report for all checking and savings under the given customer. This service retrieves up to two years of transaction history for the given account. It then uses this information to generate the CFR report. A consumer is not required to generate this report.

This report is not provided under FCRA rules, and this report is not available in the Finicity Consumer Portal for the borrower to view.

If no account type of checking or savings is found, the service will return HTTP 400 Bad Request.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_report_business_response = mastercard.cash_flow.generate_report_business(
    customer_id="1005061234",
    account_ids="5011648377 5011648378 5011648379",
    report_custom_fields=[
        {
            "label": "loanID",
            "value": "123456",
            "shown": True,
        }
    ],
    show_nsf=False,
    from_date=1607450357,
    income_stream_confidence_minimum=50,
    callback_url="https://finicity-test/webhook",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### account_ids: `str`<a id="account_ids-str"></a>

A whitespace-separated list of account IDs to be included in the report (all accounts will be included if not set)

##### report_custom_fields: [`ReportCustomFields`](./mastercard_python_sdk/type/report_custom_fields.py)<a id="report_custom_fields-reportcustomfieldsmastercard_python_sdktypereport_custom_fieldspy"></a>

##### show_nsf: `bool`<a id="show_nsf-bool"></a>

Include the non-sufficient funds (NSF) summary JSON and the NSF summary PDF section in the report. Data included: * Account  * Total number of NSF funds  * Days since the most recent NFS funds fee

##### from_date: `int`<a id="from_date-int"></a>

A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).

##### income_stream_confidence_minimum: `int`<a id="income_stream_confidence_minimum-int"></a>

Include income streams in the report, based on the income stream's confidence score. For example, Use the value 50 to include only income streams with a confidence score of 50 or higher.

##### callback_url: `str`<a id="callback_url-str"></a>

A Report Listener URL to receive notifications. The webhook must respond to the Finicity API with a 2xx HTTP status code.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CashFlowReportConstraints`](./mastercard_python_sdk/type/cash_flow_report_constraints.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CashFlowReportAck`](./mastercard_python_sdk/pydantic/cash_flow_report_ack.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/decisioning/v2/customers/{customerId}/cashFlowBusiness` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.cash_flow_analytics.generate_analytics`<a id="mastercardcash_flow_analyticsgenerate_analytics"></a>

Cash Flow Analytics for Business analyzes cash flow over time to report metrics and identify behavior that may indicate risk.

Calculated metrics include:
* Average transaction value by month over the requested time period
* Net cash flow over the requested time period and broken down by month
* Count and report of weeks in the requested time period where there
  were zero transactions posted to the customer's accounts

* Minimum/maximum/average/sum/count of deposits by month
* Minimum/maximum/average/sum/count of withdrawals by month
* Estimated amount of deposits that can be classified as business
  revenue

* Number of transactions posted incurring a non-sufficient funds (NSF)
  fee, and net amount charged in NSF fees


This version of the API is intended for piloting and integration testing your application with the Cash Flow Analytics product. It does not adhere to FCRA requirements, and should not be used for production/lending purposes. See _Generate Cash Flow Analytics - FCRA_ for the FCRA compliant version of this API.

A successful call to this API will generate analytics and store a report within Finicity. The report can be retrieved via _Get Cash Flow Analytics Report_ (operation: _GetCashFlowAnalyticsReport_).

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_analytics_response = mastercard.cash_flow_analytics.generate_analytics(
    customer_id="1005061234",
    account_ids=[
        1
    ],
    length_of_report=730,
    reference_number="abc123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### account_ids: List[`int`]<a id="account_ids-listint"></a>

The list of account IDs to include in the report. If omitted, all accounts on record for the customer will be used.

##### length_of_report: `int`<a id="length_of_report-int"></a>

Number of days to search for transactions. Must be one of 30, 90, 180, 270, 365, or 730. If omitted, defaults to 2 years from current time at which the request was received (730 days).

##### reference_number: `str`<a id="reference_number-str"></a>

Partner-provided reference number to correlate reports.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BalanceAndCashFlowAnalyticsReportConstraints`](./mastercard_python_sdk/type/balance_and_cash_flow_analytics_report_constraints.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ObbAnalyticsReportAck`](./mastercard_python_sdk/pydantic/obb_analytics_report_ack.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/analytics/cashflow/v1/customer/{customerId}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.cash_flow_analytics.generate_fcra_analytics_report`<a id="mastercardcash_flow_analyticsgenerate_fcra_analytics_report"></a>

Cash Flow Analytics for Business analyzes cash flow over time to report metrics and identify behavior that may indicate risk.

Calculated metrics include:
* Average transaction value by month over the requested time period
* Net cash flow over the requested time period and broken down by month
* Count and report of weeks in the requested time period where there
  were zero transactions posted to the customer's accounts

* Minimum/maximum/average/sum/count of deposits by month
* Minimum/maximum/average/sum/count of withdrawals by month
* Estimated amount of deposits that can be classified as business
  revenue

* Number of transactions posted incurring a non-sufficient funds (NSF)
  fee, and net amount charged in NSF fees


This version of the API is intended for production use. It maintains and enforces all compliance with FCRA rules and requirements.

*Note:* this is a premium service, billable per every successful API call for non-testing customers.

A successful call to this API will generate analytics and store a report within Finicity. The report can be retrieved via _Get Cash Flow Analytics Report - FCRA_ (operation: _GetCashFlowAnalyticsReportFCRA_).

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_fcra_analytics_report_response = mastercard.cash_flow_analytics.generate_fcra_analytics_report(
    customer_id="1005061234",
    account_ids=[
        1
    ],
    length_of_report=730,
    reference_number="abc123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### account_ids: List[`int`]<a id="account_ids-listint"></a>

The list of account IDs to include in the report. If omitted, all accounts on record for the customer will be used.

##### length_of_report: `int`<a id="length_of_report-int"></a>

Number of days to search for transactions. Must be one of 30, 90, 180, 270, 365, or 730. If omitted, defaults to 2 years from current time at which the request was received (730 days).

##### reference_number: `str`<a id="reference_number-str"></a>

Partner-provided reference number to correlate reports.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BalanceAndCashFlowAnalyticsReportConstraints`](./mastercard_python_sdk/type/balance_and_cash_flow_analytics_report_constraints.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ObbAnalyticsReportAck`](./mastercard_python_sdk/pydantic/obb_analytics_report_ack.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/analytics/cashflow/v1/customer/{customerId}/fcra` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.cash_flow_analytics.generate_report`<a id="mastercardcash_flow_analyticsgenerate_report"></a>

Generate a Cashflow Analytics Report for a given customer. This service retrieves up to two years of transaction history from connected accounts.

Cashflow Analytics analyzes transaction over time to report metrics and identify behavior that may indicate risk.

Before calling this API, A consumer or business may need to be created for the given customer ID based on the user type (see Consumer/Business APIs).

If no account type of checking or savings is found, the service will return HTTP 400 Bad Request.

This is a premium service, billable per every successful API call for non-testing customers. A successful call to this API will generate analytics report which can be retrieved via Get Report by Customer or Get Report by Consumer.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_report_response = mastercard.cash_flow_analytics.generate_report(
    customer_id="1005061234",
    user_type="personal",
    analytics_report_data={
        "for_cra_purpose": True,
        "applicant_is_personal_guarantor": True,
        "time_interval_types": ["MONTHLY_CALENDAR"],
    },
    account_ids="5011648377 5011648378 5011648379",
    report_custom_fields=[
        {
            "label": "loanID",
            "value": "123456",
            "shown": True,
        }
    ],
    from_date=1607450357,
    callback_url="https://finicity-test/webhook",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### user_type: `str`<a id="user_type-str"></a>

UserType indicates if the request is for a business or personal use case, Allowed values: business/personal.

##### analytics_report_data: [`AnalyticsReportData`](./mastercard_python_sdk/type/analytics_report_data.py)<a id="analytics_report_data-analyticsreportdatamastercard_python_sdktypeanalytics_report_datapy"></a>


##### account_ids: `str`<a id="account_ids-str"></a>

A whitespace-separated list of account IDs to be included in the report (all accounts will be included if not set)

##### report_custom_fields: [`ReportCustomFields`](./mastercard_python_sdk/type/report_custom_fields.py)<a id="report_custom_fields-reportcustomfieldsmastercard_python_sdktypereport_custom_fieldspy"></a>

##### from_date: `int`<a id="from_date-int"></a>

A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).

##### callback_url: `str`<a id="callback_url-str"></a>

A Report Listener URL to receive notifications. The webhook must respond to the Finicity API with a 2xx HTTP status code.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AnalyticsReportConstraints`](./mastercard_python_sdk/type/analytics_report_constraints.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AnalyticsReportAck`](./mastercard_python_sdk/pydantic/analytics_report_ack.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/decisioning/v2/customers/{customerId}/reports/cashflow-analytics/userTypes/{userType}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.cash_flow_analytics.get_report_data`<a id="mastercardcash_flow_analyticsget_report_data"></a>

Retrieve the report saved by _Generate Balance Analytics_, _Generate Cash Flow Analytics_, or _Generate Payment History_. Requires the report ID generated by the previous call.

Report data can either be retrieved as a JSON document or PDF file.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_report_data_response = mastercard.cash_flow_analytics.get_report_data(
    obb_report_id="bcab9592-e032-4e7b-b737-0380619a0573",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### obb_report_id: `str`<a id="obb_report_id-str"></a>

Report ID generated and returned by OBB products

#### 🔄 Return<a id="🔄-return"></a>

[`ObbAnalyticsReport`](./mastercard_python_sdk/pydantic/obb_analytics_report.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/analytics/data/v1/{obb_report_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.cash_flow_analytics.get_report_data_fcra`<a id="mastercardcash_flow_analyticsget_report_data_fcra"></a>

Retrieve the report saved by _Generate Balance Analytics - FCRA_, _Generate Cash Flow Analytics - FCRA_, or _Generate Payment History - FCRA_. Requires the report ID generated by the previous call.

Report data can either be retrieved as a JSON document or PDF file.

*Note:* this is a premium service, billable per every successful API call for non-testing customers.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_report_data_fcra_response = mastercard.cash_flow_analytics.get_report_data_fcra(
    obb_report_id="bcab9592-e032-4e7b-b737-0380619a0573",
    purpose="3F",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### obb_report_id: `str`<a id="obb_report_id-str"></a>

Report ID generated and returned by OBB products

##### purpose: `str`<a id="purpose-str"></a>

2-digit code from [Permissible Purpose Codes](https://developer.mastercard.com/open-banking-us/documentation/products/lend/report-handling/permissible-purpose-codes/), specifying the reason for retrieving this report. Required for retrieving some reports.

#### 🔄 Return<a id="🔄-return"></a>

[`ObbAnalyticsReport`](./mastercard_python_sdk/pydantic/obb_analytics_report.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/analytics/data/v1/{obb_report_id}/fcra` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.connect_🔗.fix_url_generation`<a id="mastercardconnect_🔗fix_url_generation"></a>

Use the Connect Fix API when the following conditions occur:
* The connection to the user's financial institution is lost
* The user's credentials were updated (for any number of reasons)
* The user's MFA challenge has expired

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
fix_url_generation_response = mastercard.connect_🔗.fix_url_generation(
    partner_id="1234583871234",
    customer_id="1005061234",
    institution_login_id="1007302745",
    language="es",
    redirect_uri="https://www.finicity.com/connect/",
    webhook="https://webhook.site/8d4421a7-d1d1-4f01-bb08-5370aff0321b",
    webhook_content_type="application/json",
    webhook_data={},
    webhook_headers={},
    experience="default",
    single_use_url=True,
    is_web_view=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### partner_id: `str`<a id="partner_id-str"></a>

Your Partner ID displayed in the [Developer Dashboard](https://developer.mastercard.com/account/log-in)

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID. See Add Customer API for how to create a customer ID.

##### institution_login_id: `str`<a id="institution_login_id-str"></a>

An institution login ID (from the account record)

##### language: `str`<a id="language-str"></a>

By default, the Connect application is in English. You don't need to pass this parameter unless you want to translate Connect into one of our supported languages.  * Spanish (United States): `es` * French (Canada): `fr` 

##### redirect_uri: `str`<a id="redirect_uri-str"></a>

The URL that customers will be redirected to after completing Finicity Connect. Required unless Connect is embedded inside our application (iframe).

##### webhook: `str`<a id="webhook-str"></a>

The publicly available URL you want to be notified with events as the user progresses through the application. See [Connect Webhook Event](https://developer.mastercard.com/open-banking-us/documentation/webhooks/webhooks-connect/) for event details.

##### webhook_content_type: `str`<a id="webhook_content_type-str"></a>

The content type the webhook events will be sent in. Supported types: \\\"application/json\\\" and \\\"application/xml\\\".

##### webhook_data: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="webhook_data-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Allows additional identifiable information to be inserted into the payload of connect webhook events. See: [Custom Webhooks](https://developer.mastercard.com/open-banking-us/documentation/webhooks/webhooks-custom/).

##### webhook_headers: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="webhook_headers-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Allows additional identifiable information to be included as headers of connect webhook event. See: [Custom Webhooks](https://developer.mastercard.com/open-banking-us/documentation/webhooks/webhooks-custom/).

##### experience: `str`<a id="experience-str"></a>

The `experience` field allows you to customize: * Brand: color and logo * Icon: displayed on the \\\"Share your data\\\" page * Popular institutions: displayed on the Bank Search page * Report: the credit decisioning report to send when Connect completes. * MVS modules: financial, payroll, paystub  Note: the Finicity sales engineers (SE) help you set up a default experience for your company when you migrate to Connect 2.0. For each additional experience you create thereafter, they'll give you a unique ID. See [Generate Connect URL](https://developer.mastercard.com/open-banking-us/documentation/connect/generate-2-connect-url-apis/).  Experience values options: * \\\"default\\\": your default experience (must be defined) * GUID: the code for a different experience * Not defined: If you don't pass the experience parameter, then Connect's out of the box default experience (add accounts but no branding) is used, and the MVS modules will not run.

##### single_use_url: `bool`<a id="single_use_url-bool"></a>

\\\"true\\\": The URL link expires after a Connect session successfully completes.  Note: when the `singleUseUrl` and the `experience` parameters are passed in the same call, the `singleUseUrl` value overrides the `singleUseUrl` value configured in the `experience` parameter.

##### is_web_view: `bool`<a id="is_web_view-bool"></a>

\\\"true\\\": Indicates that the Connect Session will be displayed within a WebView. Note: when the `isWebView` parameter is `true` the `redirectUri` parameter is required.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FixConnectParameters`](./mastercard_python_sdk/type/fix_connect_parameters.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ConnectUrl`](./mastercard_python_sdk/pydantic/connect_url.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/connect/v2/generate/fix` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.connect_🔗.generate_joint_borrower_url`<a id="mastercardconnect_🔗generate_joint_borrower_url"></a>

Same as Connect Full (`POST /connect/v2/generate`) but for joint borrowers.

MVS prompts both the primary and joint borrower to enter each of their financial, payroll, and paystub information in the same Connect session.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_joint_borrower_url_response = mastercard.connect_🔗.generate_joint_borrower_url(
    partner_id="1234583871234",
    borrowers=[
        {
            "customer_id": "1005061234",
            "consumer_id": "0bf46322c167b562e6cbed9d40e19a4c",
            "type": "primary",
        }
    ],
    language="es",
    redirect_uri="https://www.finicity.com/connect/",
    webhook="https://webhook.site/8d4421a7-d1d1-4f01-bb08-5370aff0321b",
    webhook_content_type="application/json",
    webhook_data={},
    webhook_headers={},
    institution_settings={},
    experience="default",
    from_date=1607450357,
    report_custom_fields=[
        {
            "label": "loanID",
            "value": "123456",
            "shown": True,
        }
    ],
    single_use_url=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### partner_id: `str`<a id="partner_id-str"></a>

Your Partner ID displayed in the [Developer Dashboard](https://developer.mastercard.com/account/log-in)

##### borrowers: [`Borrowers`](./mastercard_python_sdk/type/borrowers.py)<a id="borrowers-borrowersmastercard_python_sdktypeborrowerspy"></a>

##### language: `str`<a id="language-str"></a>

By default, the Connect application is in English. You don't need to pass this parameter unless you want to translate Connect into one of our supported languages.  * Spanish (United States): `es` * French (Canada): `fr` 

##### redirect_uri: `str`<a id="redirect_uri-str"></a>

The URL that customers will be redirected to after completing Finicity Connect. Required unless Connect is embedded inside our application (iframe).

##### webhook: `str`<a id="webhook-str"></a>

The publicly available URL you want to be notified with events as the user progresses through the application. See [Connect Webhook Event](https://developer.mastercard.com/open-banking-us/documentation/webhooks/webhooks-connect/) for event details.

##### webhook_content_type: `str`<a id="webhook_content_type-str"></a>

The content type the webhook events will be sent in. Supported types: \\\"application/json\\\" and \\\"application/xml\\\".

##### webhook_data: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="webhook_data-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Allows additional identifiable information to be inserted into the payload of connect webhook events. See: [Custom Webhooks](https://developer.mastercard.com/open-banking-us/documentation/webhooks/webhooks-custom/).

##### webhook_headers: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="webhook_headers-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Allows additional identifiable information to be included as headers of connect webhook event. See: [Custom Webhooks](https://developer.mastercard.com/open-banking-us/documentation/webhooks/webhooks-custom/).

##### institution_settings: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="institution_settings-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Advanced options for configuration of which institutions to display in. See [Institution Settings](https://developer.mastercard.com/open-banking-us/documentation/connect/connect-institutions-settings/).

##### experience: `str`<a id="experience-str"></a>

The `experience` field allows you to customize: * Brand: color and logo * Icon: displayed on the \\\"Share your data\\\" page * Popular institutions: displayed on the Bank Search page * Report: the credit decisioning report to send when Connect completes. * MVS modules: financial, payroll, paystub  Note: the Finicity sales engineers (SE) help you set up a default experience for your company when you migrate to Connect 2.0. For each additional experience you create thereafter, they'll give you a unique ID. See [Generate Connect URL](https://developer.mastercard.com/open-banking-us/documentation/connect/generate-2-connect-url-apis/).  Experience values options: * \\\"default\\\": your default experience (must be defined) * GUID: the code for a different experience * Not defined: If you don't pass the experience parameter, then Connect's out of the box default experience (add accounts but no branding) is used, and the MVS modules will not run.

##### from_date: `int`<a id="from_date-int"></a>

The `fromDate` parameter is used when experiences are associated with a credit decisioning report and any other reports with transaction data. The value is in epoch time and must be 10 digits. Example: 1494449017. If it's greater than 10 digits, then the `fromDate` is set to the credit decisioning report's default `fromDate`.  For an experience that generates multiple reports, the `fromDate` gets passed to the reports that support it.  However, Connect doesn't pass this parameter to the following reports: * Pay Statement Extraction Report * VOIE - Paystub (with TXVerify) Report * Statement Report * Verification of Income Report * VOIE - Payroll Report  Note: this field isn't used if you're only collecting transaction data without a report.

##### report_custom_fields: [`ReportCustomFields`](./mastercard_python_sdk/type/report_custom_fields.py)<a id="report_custom_fields-reportcustomfieldsmastercard_python_sdktypereport_custom_fieldspy"></a>

##### single_use_url: `bool`<a id="single_use_url-bool"></a>

\\\"true\\\": The URL link expires after a Connect session successfully completes.  Note: when the `singleUseUrl` and the `experience` parameters are passed in the same call, the `singleUseUrl` value overrides the `singleUseUrl` value configured in the `experience` parameter.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ConnectJointBorrowerParameters`](./mastercard_python_sdk/type/connect_joint_borrower_parameters.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ConnectUrl`](./mastercard_python_sdk/pydantic/connect_url.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/connect/v2/generate/jointBorrower` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.connect_🔗.generate_lite_url`<a id="mastercardconnect_🔗generate_lite_url"></a>

Connect Lite is a variation of Connect Full (`POST /connect/v2/generate`), which has a limited set of features.
* Sign in, user's credentials, and Multi-Factor Authentication (MFA)
* No user account management

The Connect Web SDK isn't a requirement when using Connect lite. However, if you want to use the SDK events, routes, and user events, then you must integrate with the Connect Web SDK.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_lite_url_response = mastercard.connect_🔗.generate_lite_url(
    partner_id="1234583871234",
    customer_id="1005061234",
    institution_id=4222,
    language="es",
    redirect_uri="https://www.finicity.com/connect/",
    webhook="https://webhook.site/8d4421a7-d1d1-4f01-bb08-5370aff0321b",
    webhook_content_type="application/json",
    webhook_data={},
    webhook_headers={},
    experience="default",
    single_use_url=True,
    is_web_view=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### partner_id: `str`<a id="partner_id-str"></a>

Your Partner ID displayed in the [Developer Dashboard](https://developer.mastercard.com/account/log-in)

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID. See Add Customer API for how to create a customer ID.

##### institution_id: `int`<a id="institution_id-int"></a>

The ID of a financial institution, represented as a number

##### language: `str`<a id="language-str"></a>

By default, the Connect application is in English. You don't need to pass this parameter unless you want to translate Connect into one of our supported languages.  * Spanish (United States): `es` * French (Canada): `fr` 

##### redirect_uri: `str`<a id="redirect_uri-str"></a>

The URL that customers will be redirected to after completing Finicity Connect. Required unless Connect is embedded inside our application (iframe).

##### webhook: `str`<a id="webhook-str"></a>

The publicly available URL you want to be notified with events as the user progresses through the application. See [Connect Webhook Event](https://developer.mastercard.com/open-banking-us/documentation/webhooks/webhooks-connect/) for event details.

##### webhook_content_type: `str`<a id="webhook_content_type-str"></a>

The content type the webhook events will be sent in. Supported types: \\\"application/json\\\" and \\\"application/xml\\\".

##### webhook_data: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="webhook_data-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Allows additional identifiable information to be inserted into the payload of connect webhook events. See: [Custom Webhooks](https://developer.mastercard.com/open-banking-us/documentation/webhooks/webhooks-custom/).

##### webhook_headers: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="webhook_headers-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Allows additional identifiable information to be included as headers of connect webhook event. See: [Custom Webhooks](https://developer.mastercard.com/open-banking-us/documentation/webhooks/webhooks-custom/).

##### experience: `str`<a id="experience-str"></a>

The `experience` field allows you to customize: * Brand: color and logo * Icon: displayed on the \\\"Share your data\\\" page * Popular institutions: displayed on the Bank Search page * Report: the credit decisioning report to send when Connect completes. * MVS modules: financial, payroll, paystub  Note: the Finicity sales engineers (SE) help you set up a default experience for your company when you migrate to Connect 2.0. For each additional experience you create thereafter, they'll give you a unique ID. See [Generate Connect URL](https://developer.mastercard.com/open-banking-us/documentation/connect/generate-2-connect-url-apis/).  Experience values options: * \\\"default\\\": your default experience (must be defined) * GUID: the code for a different experience * Not defined: If you don't pass the experience parameter, then Connect's out of the box default experience (add accounts but no branding) is used, and the MVS modules will not run.

##### single_use_url: `bool`<a id="single_use_url-bool"></a>

\\\"true\\\": The URL link expires after a Connect session successfully completes.  Note: when the `singleUseUrl` and the `experience` parameters are passed in the same call, the `singleUseUrl` value overrides the `singleUseUrl` value configured in the `experience` parameter.

##### is_web_view: `bool`<a id="is_web_view-bool"></a>

\\\"true\\\": Indicates that the Connect Session will be displayed within a WebView. Note: when the `isWebView` parameter is `true` the `redirectUri` parameter is required.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LiteConnectParameters`](./mastercard_python_sdk/type/lite_connect_parameters.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ConnectUrl`](./mastercard_python_sdk/pydantic/connect_url.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/connect/v2/generate/lite` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.connect_🔗.generate_url`<a id="mastercardconnect_🔗generate_url"></a>

Generate a Connect 2.0 URL link to add within your own applications.

Optional Parameters:
* `experience`: Configure different customer experiences per Connect session by changing the brand, color, logo, icon, the type of credit decisioning report to generate after the session ends, and more.
* `language`: By default, the Connect application is in English. You don't need to pass  this parameter unless you want to translate Connect into one of our supported languages.

  * Spanish (United States)
  * French (Canada)


MVS Developers: You can pre-populate the consumer's SSN on the Find employment records page at the beginning of the MVS payroll app. Pass the SSN value for the consumer in the body of the request call.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_url_response = mastercard.connect_🔗.generate_url(
    partner_id="1234583871234",
    customer_id="1005061234",
    language="es",
    consumer_id="0bf46322c167b562e6cbed9d40e19a4c",
    redirect_uri="https://www.finicity.com/connect/",
    webhook="https://webhook.site/8d4421a7-d1d1-4f01-bb08-5370aff0321b",
    webhook_content_type="application/json",
    webhook_data={},
    webhook_headers={},
    optional_consumer_info={
        "ssn": "999999999",
        "dob": 1607450357,
    },
    single_use_url=True,
    experience="default",
    institution_settings={},
    from_date=1607450357,
    report_custom_fields=[
        {
            "label": "loanID",
            "value": "123456",
            "shown": True,
        }
    ],
    is_web_view=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### partner_id: `str`<a id="partner_id-str"></a>

Your Partner ID displayed in the [Developer Dashboard](https://developer.mastercard.com/account/log-in)

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID. See Add Customer API for how to create a customer ID.

##### language: `str`<a id="language-str"></a>

By default, the Connect application is in English. You don't need to pass this parameter unless you want to translate Connect into one of our supported languages.  * Spanish (United States): `es` * French (Canada): `fr` 

##### consumer_id: `str`<a id="consumer_id-str"></a>

A consumer ID. See Create Consumer API for how to create a consumer ID.

##### redirect_uri: `str`<a id="redirect_uri-str"></a>

The URL that customers will be redirected to after completing Finicity Connect. Required unless Connect is embedded inside our application (iframe).

##### webhook: `str`<a id="webhook-str"></a>

The publicly available URL you want to be notified with events as the user progresses through the application. See [Connect Webhook Event](https://developer.mastercard.com/open-banking-us/documentation/webhooks/webhooks-connect/) for event details.

##### webhook_content_type: `str`<a id="webhook_content_type-str"></a>

The content type the webhook events will be sent in. Supported types: \\\"application/json\\\" and \\\"application/xml\\\".

##### webhook_data: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="webhook_data-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Allows additional identifiable information to be inserted into the payload of connect webhook events. See: [Custom Webhooks](https://developer.mastercard.com/open-banking-us/documentation/webhooks/webhooks-custom/).

##### webhook_headers: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="webhook_headers-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Allows additional identifiable information to be included as headers of connect webhook event. See: [Custom Webhooks](https://developer.mastercard.com/open-banking-us/documentation/webhooks/webhooks-custom/).

##### optional_consumer_info: [`ConsumerInfo`](./mastercard_python_sdk/type/consumer_info.py)<a id="optional_consumer_info-consumerinfomastercard_python_sdktypeconsumer_infopy"></a>


##### single_use_url: `bool`<a id="single_use_url-bool"></a>

\\\"true\\\": The URL link expires after a Connect session successfully completes.  Note: when the `singleUseUrl` and the `experience` parameters are passed in the same call, the `singleUseUrl` value overrides the `singleUseUrl` value configured in the `experience` parameter.

##### experience: `str`<a id="experience-str"></a>

The `experience` field allows you to customize: * Brand: color and logo * Icon: displayed on the \\\"Share your data\\\" page * Popular institutions: displayed on the Bank Search page * Report: the credit decisioning report to send when Connect completes. * MVS modules: financial, payroll, paystub  Note: the Finicity sales engineers (SE) help you set up a default experience for your company when you migrate to Connect 2.0. For each additional experience you create thereafter, they'll give you a unique ID. See [Generate Connect URL](https://developer.mastercard.com/open-banking-us/documentation/connect/generate-2-connect-url-apis/).  Experience values options: * \\\"default\\\": your default experience (must be defined) * GUID: the code for a different experience * Not defined: If you don't pass the experience parameter, then Connect's out of the box default experience (add accounts but no branding) is used, and the MVS modules will not run.

##### institution_settings: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="institution_settings-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Advanced options for configuration of which institutions to display in. See [Institution Settings](https://developer.mastercard.com/open-banking-us/documentation/connect/connect-institutions-settings/).

##### from_date: `int`<a id="from_date-int"></a>

The `fromDate` parameter is used when experiences are associated with a credit decisioning report and any other reports with transaction data. The value is in epoch time and must be 10 digits. Example: 1494449017. If it's greater than 10 digits, then the `fromDate` is set to the credit decisioning report's default `fromDate`.  For an experience that generates multiple reports, the `fromDate` gets passed to the reports that support it.  However, Connect doesn't pass this parameter to the following reports: * Pay Statement Extraction Report * VOIE - Paystub (with TXVerify) Report * Statement Report * Verification of Income Report * VOIE - Payroll Report  Note: this field isn't used if you're only collecting transaction data without a report.

##### report_custom_fields: [`ReportCustomFields`](./mastercard_python_sdk/type/report_custom_fields.py)<a id="report_custom_fields-reportcustomfieldsmastercard_python_sdktypereport_custom_fieldspy"></a>

##### is_web_view: `bool`<a id="is_web_view-bool"></a>

\\\"true\\\": Indicates that the Connect Session will be displayed within a WebView. Note: when the `isWebView` parameter is `true` the `redirectUri` parameter is required.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ConnectParameters`](./mastercard_python_sdk/type/connect_parameters.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ConnectUrl`](./mastercard_python_sdk/pydantic/connect_url.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/connect/v2/generate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.connect_🔗.send_connect_email`<a id="mastercardconnect_🔗send_connect_email"></a>

Same as Connect Full (`POST /connect/v2/generate`) but send a Connect email to a consumer.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
send_connect_email_response = mastercard.connect_🔗.send_connect_email(
    partner_id="1234583871234",
    customer_id="1005061234",
    consumer_id="0bf46322c167b562e6cbed9d40e19a4c",
    email={
        "to": "bob@example.com",
        "_from": "test.lender@test.com",
        "support_phone": "800-555-5555",
        "subject": "Verify your income",
        "first_name": "Bob",
        "institution_name": "Acme Lending",
        "institution_address": "222 Winnipeg Drive SLC UT, 84109",
        "signature": ["Cindy Mayfield", "Senior Loan Officer", "Direct 123-456-7890"],
    },
    language="es",
    redirect_uri="https://www.finicity.com/connect/",
    webhook="https://webhook.site/8d4421a7-d1d1-4f01-bb08-5370aff0321b",
    webhook_content_type="application/json",
    webhook_data={},
    webhook_headers={},
    institution_settings={},
    experience="default",
    single_use_url=True,
    from_date=1607450357,
    report_custom_fields=[
        {
            "label": "loanID",
            "value": "123456",
            "shown": True,
        }
    ],
    optional_consumer_info={
        "ssn": "999999999",
        "dob": 1607450357,
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### partner_id: `str`<a id="partner_id-str"></a>

Your Partner ID displayed in the [Developer Dashboard](https://developer.mastercard.com/account/log-in)

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID. See Add Customer API for how to create a customer ID.

##### consumer_id: `str`<a id="consumer_id-str"></a>

A consumer ID. See Create Consumer API for how to create a consumer ID.

##### email: [`EmailOptions`](./mastercard_python_sdk/type/email_options.py)<a id="email-emailoptionsmastercard_python_sdktypeemail_optionspy"></a>


##### language: `str`<a id="language-str"></a>

By default, the Connect application is in English. You don't need to pass this parameter unless you want to translate Connect into one of our supported languages.  * Spanish (United States): `es` * French (Canada): `fr` 

##### redirect_uri: `str`<a id="redirect_uri-str"></a>

The URL that customers will be redirected to after completing Finicity Connect. Required unless Connect is embedded inside our application (iframe).

##### webhook: `str`<a id="webhook-str"></a>

The publicly available URL you want to be notified with events as the user progresses through the application. See [Connect Webhook Event](https://developer.mastercard.com/open-banking-us/documentation/webhooks/webhooks-connect/) for event details.

##### webhook_content_type: `str`<a id="webhook_content_type-str"></a>

The content type the webhook events will be sent in. Supported types: \\\"application/json\\\" and \\\"application/xml\\\".

##### webhook_data: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="webhook_data-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Allows additional identifiable information to be inserted into the payload of connect webhook events. See: [Custom Webhooks](https://developer.mastercard.com/open-banking-us/documentation/webhooks/webhooks-custom/).

##### webhook_headers: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="webhook_headers-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Allows additional identifiable information to be included as headers of connect webhook event. See: [Custom Webhooks](https://developer.mastercard.com/open-banking-us/documentation/webhooks/webhooks-custom/).

##### institution_settings: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="institution_settings-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Advanced options for configuration of which institutions to display in. See [Institution Settings](https://developer.mastercard.com/open-banking-us/documentation/connect/connect-institutions-settings/).

##### experience: `str`<a id="experience-str"></a>

The `experience` field allows you to customize: * Brand: color and logo * Icon: displayed on the \\\"Share your data\\\" page * Popular institutions: displayed on the Bank Search page * Report: the credit decisioning report to send when Connect completes. * MVS modules: financial, payroll, paystub  Note: the Finicity sales engineers (SE) help you set up a default experience for your company when you migrate to Connect 2.0. For each additional experience you create thereafter, they'll give you a unique ID. See [Generate Connect URL](https://developer.mastercard.com/open-banking-us/documentation/connect/generate-2-connect-url-apis/).  Experience values options: * \\\"default\\\": your default experience (must be defined) * GUID: the code for a different experience * Not defined: If you don't pass the experience parameter, then Connect's out of the box default experience (add accounts but no branding) is used, and the MVS modules will not run.

##### single_use_url: `bool`<a id="single_use_url-bool"></a>

\\\"true\\\": The URL link expires after a Connect session successfully completes.  Note: when the `singleUseUrl` and the `experience` parameters are passed in the same call, the `singleUseUrl` value overrides the `singleUseUrl` value configured in the `experience` parameter.

##### from_date: `int`<a id="from_date-int"></a>

The `fromDate` parameter is used when experiences are associated with a credit decisioning report and any other reports with transaction data. The value is in epoch time and must be 10 digits. Example: 1494449017. If it's greater than 10 digits, then the `fromDate` is set to the credit decisioning report's default `fromDate`.  For an experience that generates multiple reports, the `fromDate` gets passed to the reports that support it.  However, Connect doesn't pass this parameter to the following reports: * Pay Statement Extraction Report * VOIE - Paystub (with TXVerify) Report * Statement Report * Verification of Income Report * VOIE - Payroll Report  Note: this field isn't used if you're only collecting transaction data without a report.

##### report_custom_fields: [`ReportCustomFields`](./mastercard_python_sdk/type/report_custom_fields.py)<a id="report_custom_fields-reportcustomfieldsmastercard_python_sdktypereport_custom_fieldspy"></a>

##### optional_consumer_info: [`ConsumerInfo`](./mastercard_python_sdk/type/consumer_info.py)<a id="optional_consumer_info-consumerinfomastercard_python_sdktypeconsumer_infopy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ConnectEmailParameters`](./mastercard_python_sdk/type/connect_email_parameters.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ConnectEmailUrl`](./mastercard_python_sdk/pydantic/connect_email_url.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/connect/v2/send/email` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.connect_🔗.send_email_joint_borrower`<a id="mastercardconnect_🔗send_email_joint_borrower"></a>

Same as Connect Joint Borrower (`POST /connect/v2/generate/jointBorrower`) but send a Connect email  to at least one of the joint borrower's email addresses.

When the consumer opens the email, MVS prompts both the primary and joint borrower to enter each of their financial, payroll, and paystub information in the same Connect session.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
send_email_joint_borrower_response = mastercard.connect_🔗.send_email_joint_borrower(
    partner_id="1234583871234",
    borrowers=[
        {
            "customer_id": "1005061234",
            "consumer_id": "0bf46322c167b562e6cbed9d40e19a4c",
            "type": "primary",
        }
    ],
    email={
        "to": "bob@example.com",
        "_from": "test.lender@test.com",
        "support_phone": "800-555-5555",
        "subject": "Verify your income",
        "first_name": "Bob",
        "institution_name": "Acme Lending",
        "institution_address": "222 Winnipeg Drive SLC UT, 84109",
        "signature": ["Cindy Mayfield", "Senior Loan Officer", "Direct 123-456-7890"],
    },
    experience="default",
    language="es",
    redirect_uri="https://www.finicity.com/connect/",
    webhook="https://webhook.site/8d4421a7-d1d1-4f01-bb08-5370aff0321b",
    webhook_content_type="application/json",
    webhook_data={},
    webhook_headers={},
    institution_settings={},
    from_date=1607450357,
    report_custom_fields=[
        {
            "label": "loanID",
            "value": "123456",
            "shown": True,
        }
    ],
    single_use_url=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### partner_id: `str`<a id="partner_id-str"></a>

Your Partner ID displayed in the [Developer Dashboard](https://developer.mastercard.com/account/log-in)

##### borrowers: [`Borrowers`](./mastercard_python_sdk/type/borrowers.py)<a id="borrowers-borrowersmastercard_python_sdktypeborrowerspy"></a>

##### email: [`EmailOptions`](./mastercard_python_sdk/type/email_options.py)<a id="email-emailoptionsmastercard_python_sdktypeemail_optionspy"></a>


##### experience: `str`<a id="experience-str"></a>

The `experience` field allows you to customize: * Brand: color and logo * Icon: displayed on the \\\"Share your data\\\" page * Popular institutions: displayed on the Bank Search page * Report: the credit decisioning report to send when Connect completes. * MVS modules: financial, payroll, paystub  Note: the Finicity sales engineers (SE) help you set up a default experience for your company when you migrate to Connect 2.0. For each additional experience you create thereafter, they'll give you a unique ID. See [Generate Connect URL](https://developer.mastercard.com/open-banking-us/documentation/connect/generate-2-connect-url-apis/).  Experience values options: * \\\"default\\\": your default experience (must be defined) * GUID: the code for a different experience * Not defined: If you don't pass the experience parameter, then Connect's out of the box default experience (add accounts but no branding) is used, and the MVS modules will not run.

##### language: `str`<a id="language-str"></a>

By default, the Connect application is in English. You don't need to pass this parameter unless you want to translate Connect into one of our supported languages.  * Spanish (United States): `es` * French (Canada): `fr` 

##### redirect_uri: `str`<a id="redirect_uri-str"></a>

The URL that customers will be redirected to after completing Finicity Connect. Required unless Connect is embedded inside our application (iframe).

##### webhook: `str`<a id="webhook-str"></a>

The publicly available URL you want to be notified with events as the user progresses through the application. See [Connect Webhook Event](https://developer.mastercard.com/open-banking-us/documentation/webhooks/webhooks-connect/) for event details.

##### webhook_content_type: `str`<a id="webhook_content_type-str"></a>

The content type the webhook events will be sent in. Supported types: \\\"application/json\\\" and \\\"application/xml\\\".

##### webhook_data: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="webhook_data-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Allows additional identifiable information to be inserted into the payload of connect webhook events. See: [Custom Webhooks](https://developer.mastercard.com/open-banking-us/documentation/webhooks/webhooks-custom/).

##### webhook_headers: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="webhook_headers-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Allows additional identifiable information to be included as headers of connect webhook event. See: [Custom Webhooks](https://developer.mastercard.com/open-banking-us/documentation/webhooks/webhooks-custom/).

##### institution_settings: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="institution_settings-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Advanced options for configuration of which institutions to display in. See [Institution Settings](https://developer.mastercard.com/open-banking-us/documentation/connect/connect-institutions-settings/).

##### from_date: `int`<a id="from_date-int"></a>

The `fromDate` parameter is used when experiences are associated with a credit decisioning report and any other reports with transaction data. The value is in epoch time and must be 10 digits. Example: 1494449017. If it's greater than 10 digits, then the `fromDate` is set to the credit decisioning report's default `fromDate`.  For an experience that generates multiple reports, the `fromDate` gets passed to the reports that support it.  However, Connect doesn't pass this parameter to the following reports: * Pay Statement Extraction Report * VOIE - Paystub (with TXVerify) Report * Statement Report * Verification of Income Report * VOIE - Payroll Report  Note: this field isn't used if you're only collecting transaction data without a report.

##### report_custom_fields: [`ReportCustomFields`](./mastercard_python_sdk/type/report_custom_fields.py)<a id="report_custom_fields-reportcustomfieldsmastercard_python_sdktypereport_custom_fieldspy"></a>

##### single_use_url: `bool`<a id="single_use_url-bool"></a>

\\\"true\\\": The URL link expires after a Connect session successfully completes.  Note: when the `singleUseUrl` and the `experience` parameters are passed in the same call, the `singleUseUrl` value overrides the `singleUseUrl` value configured in the `experience` parameter.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ConnectJointBorrowerEmailParameters`](./mastercard_python_sdk/type/connect_joint_borrower_email_parameters.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ConnectEmailUrl`](./mastercard_python_sdk/pydantic/connect_email_url.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/connect/v2/send/email/jointBorrower` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.connect_🔗.verify_micro_entry_microdeposits`<a id="mastercardconnect_🔗verify_micro_entry_microdeposits"></a>

The UI re-engages the consumer to enter two microdeposit amounts found in their account and validates them.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
verify_micro_entry_microdeposits_response = mastercard.connect_🔗.verify_micro_entry_microdeposits(
    partner_id="1234583871234",
    customer_id="1005061234",
    redirect_uri="https://www.finicity.com/connect/",
    webhook="https://webhook.site/8d4421a7-d1d1-4f01-bb08-5370aff0321b",
    webhook_content_type="application/json",
    webhook_data={},
    webhook_headers={},
    experience="default",
    account_id="5011648377",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### partner_id: `str`<a id="partner_id-str"></a>

Your Partner ID displayed in the [Developer Dashboard](https://developer.mastercard.com/account/log-in)

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID. See Add Customer API for how to create a customer ID.

##### redirect_uri: `str`<a id="redirect_uri-str"></a>

The URL that customers will be redirected to after completing Finicity Connect. Required unless Connect is embedded inside our application (iframe).

##### webhook: `str`<a id="webhook-str"></a>

The publicly available URL you want to be notified with events as the user progresses through the application. See [Connect Webhook Event](https://developer.mastercard.com/open-banking-us/documentation/webhooks/webhooks-connect/) for event details.

##### webhook_content_type: `str`<a id="webhook_content_type-str"></a>

The content type the webhook events will be sent in. Supported types: \\\"application/json\\\" and \\\"application/xml\\\".

##### webhook_data: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="webhook_data-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Allows additional identifiable information to be inserted into the payload of connect webhook events. See: [Custom Webhooks](https://developer.mastercard.com/open-banking-us/documentation/webhooks/webhooks-custom/).

##### webhook_headers: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="webhook_headers-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Allows additional identifiable information to be included as headers of connect webhook event. See: [Custom Webhooks](https://developer.mastercard.com/open-banking-us/documentation/webhooks/webhooks-custom/).

##### experience: `str`<a id="experience-str"></a>

The `experience` field allows you to customize: * Brand: color and logo * Icon: displayed on the \\\"Share your data\\\" page * Popular institutions: displayed on the Bank Search page * Report: the credit decisioning report to send when Connect completes. * MVS modules: financial, payroll, paystub  Note: the Finicity sales engineers (SE) help you set up a default experience for your company when you migrate to Connect 2.0. For each additional experience you create thereafter, they'll give you a unique ID. See [Generate Connect URL](https://developer.mastercard.com/open-banking-us/documentation/connect/generate-2-connect-url-apis/).  Experience values options: * \\\"default\\\": your default experience (must be defined) * GUID: the code for a different experience * Not defined: If you don't pass the experience parameter, then Connect's out of the box default experience (add accounts but no branding) is used, and the MVS modules will not run.

##### account_id: `str`<a id="account_id-str"></a>

An account ID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MicroEntryVerifyRequestParameter`](./mastercard_python_sdk/type/micro_entry_verify_request_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ConnectUrl`](./mastercard_python_sdk/pydantic/connect_url.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/connect/v2/generate/microentry/verify` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.consumers.create_consumer_record`<a id="mastercardconsumerscreate_consumer_record"></a>

Create a consumer record associated with the given customer. A consumer persists as the owner of any reports that are generated, even after the original customer is deleted from the system.

A consumer must be created for the given customer before calling any of the Generate Report services.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_consumer_record_response = mastercard.consumers.create_consumer_record(
    first_name="John",
    last_name="Smith",
    address="434 W Ascension Way",
    city="Murray",
    state="UT",
    zip="84123",
    phone="1-801-984-4200",
    ssn="999-99-9999",
    birthday={
        "year": 1989,
        "month": 8,
        "day_of_month": 13,
    },
    customer_id="1005061234",
    email="myname@mycompany.com",
    suffix="PhD",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### first_name: `str`<a id="first_name-str"></a>

The first name of the account holder

##### last_name: `str`<a id="last_name-str"></a>

The last name of the account holder

##### address: `str`<a id="address-str"></a>

A street address

##### city: `str`<a id="city-str"></a>

City

##### state: `str`<a id="state-str"></a>

State

##### zip: `str`<a id="zip-str"></a>

A ZIP code

##### phone: `str`<a id="phone-str"></a>

A phone number (max length 15).

##### ssn: `str`<a id="ssn-str"></a>

A full SSN with or without hyphens

##### birthday: [`Birthday`](./mastercard_python_sdk/type/birthday.py)<a id="birthday-birthdaymastercard_python_sdktypebirthdaypy"></a>


##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### email: `str`<a id="email-str"></a>

An email address

##### suffix: `str`<a id="suffix-str"></a>

A generational or academic suffix

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`NewConsumer`](./mastercard_python_sdk/type/new_consumer.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CreatedConsumer`](./mastercard_python_sdk/pydantic/created_consumer.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/decisioning/v1/customers/{customerId}/consumer` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.consumers.get_by_customer_id`<a id="mastercardconsumersget_by_customer_id"></a>

Get the details of a consumer record by customer ID.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_customer_id_response = mastercard.consumers.get_by_customer_id(
    customer_id="1005061234",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

#### 🔄 Return<a id="🔄-return"></a>

[`Consumer`](./mastercard_python_sdk/pydantic/consumer.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/decisioning/v1/customers/{customerId}/consumer` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.consumers.get_by_id`<a id="mastercardconsumersget_by_id"></a>

Get the details of a consumer record by consumer ID.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = mastercard.consumers.get_by_id(
    consumer_id="0bf46322c167b562e6cbed9d40e19a4c",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### consumer_id: `str`<a id="consumer_id-str"></a>

The consumer ID

#### 🔄 Return<a id="🔄-return"></a>

[`Consumer`](./mastercard_python_sdk/pydantic/consumer.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/decisioning/v1/consumers/{consumerId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.consumers.modify_by_id`<a id="mastercardconsumersmodify_by_id"></a>

Modify an existing consumer. All fields are required for a consumer record, but individual fields for this call are optional because fields that are not specified will be left unchanged.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
mastercard.consumers.modify_by_id(
    consumer_id="0bf46322c167b562e6cbed9d40e19a4c",
    first_name="John",
    last_name="Smith",
    address="434 W Ascension Way",
    city="Murray",
    state="UT",
    zip="84123",
    phone="1-801-984-4200",
    ssn="999-99-9999",
    birthday={
        "year": 1989,
        "month": 8,
        "day_of_month": 13,
    },
    email="myname@mycompany.com",
    suffix="PhD",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### consumer_id: `str`<a id="consumer_id-str"></a>

The consumer ID

##### first_name: `str`<a id="first_name-str"></a>

The first name of the account holder

##### last_name: `str`<a id="last_name-str"></a>

The last name of the account holder

##### address: `str`<a id="address-str"></a>

A street address

##### city: `str`<a id="city-str"></a>

City

##### state: `str`<a id="state-str"></a>

State

##### zip: `str`<a id="zip-str"></a>

A ZIP code

##### phone: `str`<a id="phone-str"></a>

A phone number (max length 15).

##### ssn: `str`<a id="ssn-str"></a>

A full SSN with or without hyphens

##### birthday: [`Birthday`](./mastercard_python_sdk/type/birthday.py)<a id="birthday-birthdaymastercard_python_sdktypebirthdaypy"></a>


##### email: `str`<a id="email-str"></a>

An email address

##### suffix: `str`<a id="suffix-str"></a>

A generational or academic suffix

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ConsumerUpdate`](./mastercard_python_sdk/type/consumer_update.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/decisioning/v1/consumers/{consumerId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.customer_authorization_details.get_authorization_details`<a id="mastercardcustomer_authorization_detailsget_authorization_details"></a>

The endpoint provides customer authorization details like authorization start date, authorization end date against the requested institution login id

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_authorization_details_response = mastercard.customer_authorization_details.get_authorization_details(
    institution_login_id=7008461438,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### institution_login_id: `int`<a id="institution_login_id-int"></a>

Institution login id of the customer.

#### 🔄 Return<a id="🔄-return"></a>

[`CustomerAuthorizationDetails`](./mastercard_python_sdk/pydantic/customer_authorization_details.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/customers/institution-logins/{institution_login_id}/authorization-details` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.customers.enroll_active_customer`<a id="mastercardcustomersenroll_active_customer"></a>

Enroll an active customer, which is the actual owner of one or more real-world accounts. This is a billable customer.

Active customers must use the "FinBank Billable" profiles for testing purposes.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
enroll_active_customer_response = mastercard.customers.enroll_active_customer(
    username="customerusername1",
    first_name="John",
    last_name="Smith",
    application_id="123456789",
    phone="1-801-984-4200",
    email="myname@mycompany.com",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### username: `str`<a id="username-str"></a>

The customer's username, assigned by the partner (a unique identifier), following these rules: minimum 6 characters maximum 255 characters any mix of uppercase, lowercase, numeric, and non-alphabet special characters ! @ . # $ % & * _ - + the use of email in this field is discouraged it is recommended to use a unique non-email identifier. Use of special characters may result in an error (e.g. í, ü, etc.). Usernames are unique. A username used in Test Drive can't be reused in other plans.

##### first_name: `str`<a id="first_name-str"></a>

The first name of the account holder

##### last_name: `str`<a id="last_name-str"></a>

The last name of the account holder

##### application_id: `str`<a id="application_id-str"></a>

`applicationId` value returned from the Get App Registration Status API and the partner assign the customers to. This cannot be changed once set. Only applicable in cases of partners with multiple registered applications. If the partner only has one app, this can usually be omitted. This field is populated after the app is in a status approved.

##### phone: `str`<a id="phone-str"></a>

A phone number (max length 15).

##### email: `str`<a id="email-str"></a>

An email address

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`NewCustomer`](./mastercard_python_sdk/type/new_customer.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CreatedCustomer`](./mastercard_python_sdk/pydantic/created_customer.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/aggregation/v2/customers/active` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.customers.enroll_testing_customer`<a id="mastercardcustomersenroll_testing_customer"></a>

Enroll a testing customer (Test Drive accounts).

For using testing customers with FinBank OAuth, you must register a test application with your systems engineer or account manager. Then, use that testing `applicationId` when creating testing customers.

Testing Customers can access FinBank profiles (except "FinBank Billable" profiles), and cannot access live financial institutions.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
enroll_testing_customer_response = mastercard.customers.enroll_testing_customer(
    username="customerusername1",
    first_name="John",
    last_name="Smith",
    application_id="123456789",
    phone="1-801-984-4200",
    email="myname@mycompany.com",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### username: `str`<a id="username-str"></a>

The customer's username, assigned by the partner (a unique identifier), following these rules: minimum 6 characters maximum 255 characters any mix of uppercase, lowercase, numeric, and non-alphabet special characters ! @ . # $ % & * _ - + the use of email in this field is discouraged it is recommended to use a unique non-email identifier. Use of special characters may result in an error (e.g. í, ü, etc.). Usernames are unique. A username used in Test Drive can't be reused in other plans.

##### first_name: `str`<a id="first_name-str"></a>

The first name of the account holder

##### last_name: `str`<a id="last_name-str"></a>

The last name of the account holder

##### application_id: `str`<a id="application_id-str"></a>

`applicationId` value returned from the Get App Registration Status API and the partner assign the customers to. This cannot be changed once set. Only applicable in cases of partners with multiple registered applications. If the partner only has one app, this can usually be omitted. This field is populated after the app is in a status approved.

##### phone: `str`<a id="phone-str"></a>

A phone number (max length 15).

##### email: `str`<a id="email-str"></a>

An email address

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`NewCustomer`](./mastercard_python_sdk/type/new_customer.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CreatedCustomer`](./mastercard_python_sdk/pydantic/created_customer.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/aggregation/v2/customers/testing` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.customers.find_enrolled_users`<a id="mastercardcustomersfind_enrolled_users"></a>

Find all customers enrolled by the current partner, where the search text is found in the customer's username or any combination of `firstName` and `lastName` fields. If no search text is provided, all customers will be returned.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_enrolled_users_response = mastercard.customers.find_enrolled_users(
    username="customerusername1",
    type="active",
    search="Search Value",
    start=1,
    limit=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### username: `str`<a id="username-str"></a>

Username for exact match (will return 0 or 1 record)

##### type: `str`<a id="type-str"></a>

\"testing\" or \"active\" to return only customers of that type, or leave empty to return all customers

##### search: `str`<a id="search-str"></a>

The text you wish to match. Leave this empty if you wish to return all customers. Must be URL-encoded (see: [Handling Spaces in Queries](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/)).

##### start: `int`<a id="start-int"></a>

Index of the page of results to return

##### limit: `int`<a id="limit-int"></a>

Maximum number of results per page

#### 🔄 Return<a id="🔄-return"></a>

[`Customers`](./mastercard_python_sdk/pydantic/customers.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/aggregation/v1/customers` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.customers.get_by_id`<a id="mastercardcustomersget_by_id"></a>

Retrieve a customer by ID.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = mastercard.customers.get_by_id(
    customer_id="1005061234",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

#### 🔄 Return<a id="🔄-return"></a>

[`Customer`](./mastercard_python_sdk/pydantic/customer.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/aggregation/v1/customers/{customerId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.customers.get_with_app_data_by_id`<a id="mastercardcustomersget_with_app_data_by_id"></a>

Retrieve a customer along with additional details about the OAuth application.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_with_app_data_by_id_response = mastercard.customers.get_with_app_data_by_id(
    customer_id="1005061234",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

#### 🔄 Return<a id="🔄-return"></a>

[`CustomerWithAppData`](./mastercard_python_sdk/pydantic/customer_with_app_data.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/aggregation/v1/customers/{customerId}/application` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.customers.modify_by_id`<a id="mastercardcustomersmodify_by_id"></a>

Modify an enrolled customer by ID.

You must specify either `firstName`, `lastName`, or both in the request.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
mastercard.customers.modify_by_id(
    customer_id="1005061234",
    first_name="John",
    last_name="Smith",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### first_name: `str`<a id="first_name-str"></a>

The first name of the account holder

##### last_name: `str`<a id="last_name-str"></a>

The last name of the account holder

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CustomerUpdate`](./mastercard_python_sdk/type/customer_update.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/aggregation/v1/customers/{customerId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.customers.remove_by_id`<a id="mastercardcustomersremove_by_id"></a>

Completely remove a customer from the system. This will remove the customer and all associated accounts and transactions.

⚠️ Use this service carefully! It will not pause for confirmation before performing the operation!

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
mastercard.customers.remove_by_id(
    customer_id="1005061234",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/aggregation/v1/customers/{customerId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.institutions.get_branding_by_id`<a id="mastercardinstitutionsget_branding_by_id"></a>

Return the branding information for a financial institution.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_branding_by_id_response = mastercard.institutions.get_branding_by_id(
    institution_id=4222,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### institution_id: `int`<a id="institution_id-int"></a>

The institution ID

#### 🔄 Return<a id="🔄-return"></a>

[`BrandingWrapper`](./mastercard_python_sdk/pydantic/branding_wrapper.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/institution/v2/institutions/{institutionId}/branding` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.institutions.get_by_id_details`<a id="mastercardinstitutionsget_by_id_details"></a>

Get financial institution details by ID.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_details_response = mastercard.institutions.get_by_id_details(
    institution_id=4222,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### institution_id: `int`<a id="institution_id-int"></a>

The institution ID

#### 🔄 Return<a id="🔄-return"></a>

[`InstitutionWrapper`](./mastercard_python_sdk/pydantic/institution_wrapper.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/institution/v2/institutions/{institutionId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.institutions.get_certified_institutions_with_rssd`<a id="mastercardinstitutionsget_certified_institutions_with_rssd"></a>

Search for certified financial institutions w/RSSD.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_certified_institutions_with_rssd_response = mastercard.institutions.get_certified_institutions_with_rssd(
    search="finbank",
    start=1,
    limit=1,
    type="voa",
    supported_countries=[
        "us"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### search: `str`<a id="search-str"></a>

Search term (financial institution `name` field). Leave empty for all FIs.

##### start: `int`<a id="start-int"></a>

Index of the page of results to return

##### limit: `int`<a id="limit-int"></a>

Maximum number of results per page

##### type: `str`<a id="type-str"></a>

A product type: \"transAgg\", \"ach\", \"stateAgg\", \"voi\", \"voa\", \"aha\", \"availBalance\", \"accountOwner\"

##### supported_countries: List[`str`]<a id="supported_countries-liststr"></a>

A list of country codes, '*' for all countries.

#### 🔄 Return<a id="🔄-return"></a>

[`CertifiedInstitutions`](./mastercard_python_sdk/pydantic/certified_institutions.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/institution/v2/certifiedInstitutions/rssd` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.institutions.list_certified_institutions`<a id="mastercardinstitutionslist_certified_institutions"></a>

Search for financial institutions by certified product.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_certified_institutions_response = mastercard.institutions.list_certified_institutions(
    search="finbank",
    start=1,
    limit=1,
    type="voa",
    supported_countries=[
        "us"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### search: `str`<a id="search-str"></a>

Search term (financial institution `name` field). Leave empty for all FIs.

##### start: `int`<a id="start-int"></a>

Index of the page of results to return

##### limit: `int`<a id="limit-int"></a>

Maximum number of results per page

##### type: `str`<a id="type-str"></a>

A product type: \"transAgg\", \"ach\", \"stateAgg\", \"voi\", \"voa\", \"aha\", \"availBalance\", \"accountOwner\"

##### supported_countries: List[`str`]<a id="supported_countries-liststr"></a>

A list of country codes, '*' for all countries.

#### 🔄 Return<a id="🔄-return"></a>

[`CertifiedInstitutions`](./mastercard_python_sdk/pydantic/certified_institutions.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/institution/v2/certifiedInstitutions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.institutions.search_financial_institutions`<a id="mastercardinstitutionssearch_financial_institutions"></a>

Search for financial institutions.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
search_financial_institutions_response = mastercard.institutions.search_financial_institutions(
    search="finbank",
    start=1,
    limit=1,
    type="voa",
    supported_countries=[
        "us"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### search: `str`<a id="search-str"></a>

Search term (financial institution `name` field). Leave empty for all FIs.

##### start: `int`<a id="start-int"></a>

Index of the page of results to return

##### limit: `int`<a id="limit-int"></a>

Maximum number of results per page

##### type: `str`<a id="type-str"></a>

A product type: \"transAgg\", \"ach\", \"stateAgg\", \"voi\", \"voa\", \"aha\", \"availBalance\", \"accountOwner\"

##### supported_countries: List[`str`]<a id="supported_countries-liststr"></a>

A list of country codes, '*' for all countries.

#### 🔄 Return<a id="🔄-return"></a>

[`Institutions`](./mastercard_python_sdk/pydantic/institutions.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/institution/v2/institutions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.pay_statements.upload_for_customer`<a id="mastercardpay_statementsupload_for_customer"></a>

Upload pay statements for a customer.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
upload_for_customer_response = mastercard.pay_statements.upload_for_customer(
    label="lastPayPeriod",
    statement="VGhpcyBtdXN0IGJlIGFuIGltYWdl",
    customer_id="1005061234",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### label: `str`<a id="label-str"></a>

The label to be associated with the pay statement. This label will allow the paystub to go through data extraction. * `lastPayPeriod`: default label that should be used for the VOIE - Paystub products * `lastPayPeriodMinusOne`: the second most recent pay statement * `lastPayPeriodMinusTwo`: the third most recent pay statement * `previousYearLastPayPeriod` Last pay statement of the previous calendar year * `previousYear2LastPayPeriod`: last pay statement of the calendar year 2 years prior * `earliestPayPeriod`: the earliest pay statement

##### statement: `str`<a id="statement-str"></a>

A Base64 encoded pay statement file. Finicity supports PDF, JPG, or PNG files.

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PayStatement`](./mastercard_python_sdk/type/pay_statement.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Asset`](./mastercard_python_sdk/pydantic/asset.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/aggregation/v1/customers/{customerId}/payStatements` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.payment_history.generate_customer_payment_report`<a id="mastercardpayment_historygenerate_customer_payment_report"></a>

Payment history report analyzes up to 12-months of transactions and predicts the probability that a SMB will experience a payment risk event, such as NSF/Overdraft or missed recurring payments, in the near future when making a payment. The Risk Score provided in the report is a 2-digit ranking with four levels of risk going from low to high.

Some of the highlights of calculated risk present in the report include:
* Risk Score representing the likelihood of a missed payment
  based on analysis of permissioned open-banking data

* Monthly average balance for all accounts by month in the requested
  time period

* Total deposit amount by month for all accounts in the requested time
  period

* Total withdrawal amounts by month for all accounts in the requested
  time period

* Number of NSF counts and aggregate amount per month in the requested
  time period

* Recurring loan payment amounts per month in the requested time period
* Insurance payment amount per month in the requested time period
* Tax payment amounts per month in the requested time period

This version of the API is intended for piloting and integration testing your application with the Payment History product. It does not adhere to FCRA requirements, and should not be used for production/lending purposes. See _Generate Payment History - FCRA_ for the FCRA compliant version of this API.

*Note:* this is a premium service, billable per every successful API call for non-testing customers.

A successful call to this API will generate analytics and store a report within Finicity. The report can be retrieved via _Get OBB Analytics Report_ (operation: _GetObbAnalyticsReport_).
*Note:* this is a premium service, billable per every successful API call for non-testing customers.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_customer_payment_report_response = mastercard.payment_history.generate_customer_payment_report(
    customer_id="1005061234",
    reference_number="abc123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### reference_number: `str`<a id="reference_number-str"></a>

Partner-provided reference number to correlate reports.

#### 🔄 Return<a id="🔄-return"></a>

[`ObbAnalyticsReportAck`](./mastercard_python_sdk/pydantic/obb_analytics_report_ack.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/analytics/payment-history/v1/customer/{customerId}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.payment_history.generate_fcra_payment_report`<a id="mastercardpayment_historygenerate_fcra_payment_report"></a>

Payment history report analyzes up to 12-months of transactions and predicts the probability that a SMB will experience a payment risk event, such as NSF/Overdraft or missed recurring payments, in the near future when making a payment. The Risk Score provided in the report is a 2-digit ranking with four levels of risk going from low to high.

Some of the highlights of calculated risk present in the report include:
* Risk Score representing the likelihood of a missed payment
  based on analysis of permissioned open-banking data

* Monthly average balance for all accounts by month in the requested
  time period

* Total deposit amount by month for all accounts in the requested time
  period

* Total withdrawal amounts by month for all accounts in the requested
  time period

* Number of NSF counts and aggregate amount per month in the requested
  time period

* Recurring loan payment amounts per month in the requested time period
* Insurance payment amount per month in the requested time period
* Tax payment amounts per month in the requested time period

This version of the API is intended for production use. It maintains and
 enforces all compliance with FCRA rules and requirements.


*Note:* this is a premium service, billable per every successful API call for non-testing customers.

A successful call to this API will generate analytics and store a report within Finicity. The report can be retrieved via _Get OBB Analytics Report - FCRA_  (operation: _GetObbAnalyticsReportFcra_).

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_fcra_payment_report_response = mastercard.payment_history.generate_fcra_payment_report(
    customer_id="1005061234",
    reference_number="abc123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### reference_number: `str`<a id="reference_number-str"></a>

Partner-provided reference number to correlate reports.

#### 🔄 Return<a id="🔄-return"></a>

[`ObbAnalyticsReportAck`](./mastercard_python_sdk/pydantic/obb_analytics_report_ack.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/analytics/payment-history/v1/customer/{customerId}/fcra` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.payment_history.get_report_data`<a id="mastercardpayment_historyget_report_data"></a>

Retrieve the report saved by _Generate Balance Analytics_, _Generate Cash Flow Analytics_, or _Generate Payment History_. Requires the report ID generated by the previous call.

Report data can either be retrieved as a JSON document or PDF file.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_report_data_response = mastercard.payment_history.get_report_data(
    obb_report_id="bcab9592-e032-4e7b-b737-0380619a0573",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### obb_report_id: `str`<a id="obb_report_id-str"></a>

Report ID generated and returned by OBB products

#### 🔄 Return<a id="🔄-return"></a>

[`ObbAnalyticsReport`](./mastercard_python_sdk/pydantic/obb_analytics_report.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/analytics/data/v1/{obb_report_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.payment_history.get_report_data_fcra`<a id="mastercardpayment_historyget_report_data_fcra"></a>

Retrieve the report saved by _Generate Balance Analytics - FCRA_, _Generate Cash Flow Analytics - FCRA_, or _Generate Payment History - FCRA_. Requires the report ID generated by the previous call.

Report data can either be retrieved as a JSON document or PDF file.

*Note:* this is a premium service, billable per every successful API call for non-testing customers.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_report_data_fcra_response = mastercard.payment_history.get_report_data_fcra(
    obb_report_id="bcab9592-e032-4e7b-b737-0380619a0573",
    purpose="3F",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### obb_report_id: `str`<a id="obb_report_id-str"></a>

Report ID generated and returned by OBB products

##### purpose: `str`<a id="purpose-str"></a>

2-digit code from [Permissible Purpose Codes](https://developer.mastercard.com/open-banking-us/documentation/products/lend/report-handling/permissible-purpose-codes/), specifying the reason for retrieving this report. Required for retrieving some reports.

#### 🔄 Return<a id="🔄-return"></a>

[`ObbAnalyticsReport`](./mastercard_python_sdk/pydantic/obb_analytics_report.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/analytics/data/v1/{obb_report_id}/fcra` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.payments.get_account_owner_details`<a id="mastercardpaymentsget_account_owner_details"></a>

Retrieve the names and addresses of the account owner from a financial institution.

Note: this is a premium service, billable per every successful API call.

This service retrieves account data from the institution. This usually returns quickly, but in some scenarios may take a few minutes to complete. In the event of a timeout condition, retry the call.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_account_owner_details_response = mastercard.payments.get_account_owner_details(
    customer_id="1005061234",
    account_id="5011648377",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### account_id: `str`<a id="account_id-str"></a>

The account ID

#### 🔄 Return<a id="🔄-return"></a>

[`AccountOwner`](./mastercard_python_sdk/pydantic/account_owner.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/aggregation/v1/customers/{customerId}/accounts/{accountId}/owner` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.payments.get_account_owner_details_0`<a id="mastercardpaymentsget_account_owner_details_0"></a>

This service retrieves the account details for an account holder from an institution. The following data objects are available.

* Account holders

* Addresses

* Emails

* Phones

* Documentations

* Identity Insights


Note: The data returned varies from institution to institution as not all of them make the same data available. This is a premium service, billable per each successful API call.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_account_owner_details_0_response = mastercard.payments.get_account_owner_details_0(
    customer_id="1005061234",
    account_id="5011648377",
    with_insights=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### account_id: `str`<a id="account_id-str"></a>

The account ID

##### with_insights: `bool`<a id="with_insights-bool"></a>

If this parameter is true, Identity Insights data will be returned along with the account owner information

#### 🔄 Return<a id="🔄-return"></a>

[`AccountOwnerHolders`](./mastercard_python_sdk/pydantic/account_owner_holders.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/aggregation/v3/customers/{customerId}/accounts/{accountId}/owner` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.payments.get_ach_details`<a id="mastercardpaymentsget_ach_details"></a>

Return the real account number and routing number details for an ACH payment.

Note: this is a premium service, billable per every successful API call.

_Supported account types_: "checking", "savings", "moneyMarket", "cd"

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_ach_details_response = mastercard.payments.get_ach_details(
    customer_id="1005061234",
    account_id="5011648377",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### account_id: `str`<a id="account_id-str"></a>

The account ID

#### 🔄 Return<a id="🔄-return"></a>

[`ACHDetails`](./mastercard_python_sdk/pydantic/ach_details.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/aggregation/v1/customers/{customerId}/accounts/{accountId}/details` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.payments.get_available_balance_live`<a id="mastercardpaymentsget_available_balance_live"></a>

Retrieve the available and cleared account balances for a single account in real-time directly from a financial institution.

Note: this is a premium service, billable per every successful API call.

_Supported account types_: "checking", "savings", "moneyMarket", "cd"

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_available_balance_live_response = mastercard.payments.get_available_balance_live(
    customer_id="1005061234",
    account_id="5011648377",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### account_id: `str`<a id="account_id-str"></a>

The account ID

#### 🔄 Return<a id="🔄-return"></a>

[`AvailableBalance`](./mastercard_python_sdk/pydantic/available_balance.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/aggregation/v1/customers/{customerId}/accounts/{accountId}/availableBalance/live` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.payments.get_latest_cached_balance`<a id="mastercardpaymentsget_latest_cached_balance"></a>

Retrieve the latest cached available and cleared account balances for a customer. Since we update and store balances throughout the day, this is the most accurate balance information available when a connection to a financial institution is unavailable or when a faster response is needed. Only deposit account types are supported: Checking, Savings, Money Market, and CD.

Note: this is a premium service, billable per every successful API call. Enrollment is required.

_Supported account types_: "checking", "savings", "moneyMarket", "cd"

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_latest_cached_balance_response = mastercard.payments.get_latest_cached_balance(
    customer_id="1005061234",
    account_id="5011648377",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### account_id: `str`<a id="account_id-str"></a>

The account ID

#### 🔄 Return<a id="🔄-return"></a>

[`AvailableBalance`](./mastercard_python_sdk/pydantic/available_balance.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/aggregation/v1/customers/{customerId}/accounts/{accountId}/availableBalance` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.payments.get_loan_payment_details`<a id="mastercardpaymentsget_loan_payment_details"></a>

Return the loan payment details of the customer for a loan-type account.

Note: this is a premium service, billable per every successful API call.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_loan_payment_details_response = mastercard.payments.get_loan_payment_details(
    customer_id="1005061234",
    account_id="5011648377",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### account_id: `str`<a id="account_id-str"></a>

The account ID

#### 🔄 Return<a id="🔄-return"></a>

[`LoanPaymentDetails`](./mastercard_python_sdk/pydantic/loan_payment_details.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/aggregation/v2/customers/{customerId}/accounts/{accountId}/loanDetails` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.portfolios.get_most_recent_reports`<a id="mastercardportfoliosget_most_recent_reports"></a>

Return a portfolio of most recently generated reports for each report type for the given customer. If there are multiple reports that were generated for a report type (VOA, VOI, etc.), only the most recently generated report for the type will be returned.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_most_recent_reports_response = mastercard.portfolios.get_most_recent_reports(
    customer_id="1005061234",
    portfolio_id="y4zsgccj4xpw-6-port",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### portfolio_id: `str`<a id="portfolio_id-str"></a>

A portfolio ID with the portfolio version number. Using the portfolio number without a version number will return the most recently generated reports.

#### 🔄 Return<a id="🔄-return"></a>

[`PortfolioSummary`](./mastercard_python_sdk/pydantic/portfolio_summary.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/decisioning/v1/customers/{customerId}/portfolios/{portfolioId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.portfolios.get_portfolio_by_consumer`<a id="mastercardportfoliosget_portfolio_by_consumer"></a>

Return a portfolio of most recently generated reports for each report type for a given consumer. If there are multiple reports that were generated for a report type (VOA, VOI, etc.), only the most recently generated report for the type will be returned.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_portfolio_by_consumer_response = mastercard.portfolios.get_portfolio_by_consumer(
    consumer_id="0bf46322c167b562e6cbed9d40e19a4c",
    portfolio_id="y4zsgccj4xpw-6-port",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### consumer_id: `str`<a id="consumer_id-str"></a>

The consumer ID

##### portfolio_id: `str`<a id="portfolio_id-str"></a>

A portfolio ID with the portfolio version number. Using the portfolio number without a version number will return the most recently generated reports.

#### 🔄 Return<a id="🔄-return"></a>

[`PortfolioWithConsumerSummary`](./mastercard_python_sdk/pydantic/portfolio_with_consumer_summary.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/decisioning/v1/consumers/{consumerId}/portfolios/{portfolioId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.reports.by_consumer_id`<a id="mastercardreportsby_consumer_id"></a>

Get all reports that have been generated by previous calls to Generate Report services for the given consumer.

The `status` fields in the returned list contain "inProgress", "failure", or "success". If the status shows "inProgress", the client app should wait 20 seconds and then call this API again.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
by_consumer_id_response = mastercard.reports.by_consumer_id(
    consumer_id="0bf46322c167b562e6cbed9d40e19a4c",
    purpose="3F",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### consumer_id: `str`<a id="consumer_id-str"></a>

The consumer ID

##### purpose: `str`<a id="purpose-str"></a>

2-digit code from [Permissible Purpose Codes](https://developer.mastercard.com/open-banking-us/documentation/products/lend/report-handling/permissible-purpose-codes/), specifying the reason for retrieving this report. Required for retrieving some reports.

#### 🔄 Return<a id="🔄-return"></a>

[`ReportSummaries`](./mastercard_python_sdk/pydantic/report_summaries.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/decisioning/v1/consumers/{consumerId}/reports` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.reports.by_customer_id`<a id="mastercardreportsby_customer_id"></a>

Get all reports that have been generated by previous calls to Generate Report services for the given customer.

The `status` fields in the returned list contain "inProgress", "failure", or "success". If the status shows "inProgress", the client app should wait 20 seconds and then call this API again.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
by_customer_id_response = mastercard.reports.by_customer_id(
    customer_id="1005061234",
    purpose="3F",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### purpose: `str`<a id="purpose-str"></a>

2-digit code from [Permissible Purpose Codes](https://developer.mastercard.com/open-banking-us/documentation/products/lend/report-handling/permissible-purpose-codes/), specifying the reason for retrieving this report. Required for retrieving some reports.

#### 🔄 Return<a id="🔄-return"></a>

[`ReportSummaries`](./mastercard_python_sdk/pydantic/report_summaries.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/decisioning/v1/customers/{customerId}/reports` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.reports.get_by_consumer_and_id`<a id="mastercardreportsget_by_consumer_and_id"></a>

Get a report that has been generated by a previous call to one of the Generate Report services.

The report's `status` field contains "inProgress", "failure", or "success". If the status shows "inProgress", the client app should wait 20 seconds and then call this API again.

Report data can either be retrieved as a JSON document or a PDF file.  To specify the format required, set the _Accept request header_ to either **application/json** or **application/pdf**. If neither is set, the report format will be returned as a JSON document.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_consumer_and_id_response = mastercard.reports.get_by_consumer_and_id(
    consumer_id="0bf46322c167b562e6cbed9d40e19a4c",
    report_id="u4hstnnak45g",
    purpose="3F",
    on_behalf_of="Some entity",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### consumer_id: `str`<a id="consumer_id-str"></a>

The consumer ID

##### report_id: `str`<a id="report_id-str"></a>

ID of the report

##### purpose: `str`<a id="purpose-str"></a>

2-digit code from [Permissible Purpose Codes](https://developer.mastercard.com/open-banking-us/documentation/products/lend/report-handling/permissible-purpose-codes/), specifying the reason for retrieving this report. Required for retrieving some reports.

##### on_behalf_of: `str`<a id="on_behalf_of-str"></a>

The name of the entity you are retrieving the report on behalf of

#### 🔄 Return<a id="🔄-return"></a>

[`Report`](./mastercard_python_sdk/pydantic/report.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/decisioning/v3/consumers/{consumerId}/reports/{reportId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.reports.get_status`<a id="mastercardreportsget_status"></a>

Get a report that has been generated by a previous call to one of the Generate Report services.

The report's `status` field contains "inProgress", "failure", or "success". If the status shows "inProgress", the client app should wait 20 seconds and then call this API again.

Report data can either be retrieved as a JSON document or a PDF file.  To specify the format required, set the _Accept request header_ to either **application/json** or **application/pdf**. If neither is set, the report format will be returned as a JSON document.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_status_response = mastercard.reports.get_status(
    customer_id="1005061234",
    report_id="u4hstnnak45g",
    on_behalf_of="Some entity",
    purpose="3F",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### report_id: `str`<a id="report_id-str"></a>

ID of the report

##### on_behalf_of: `str`<a id="on_behalf_of-str"></a>

The name of the entity you are retrieving the report on behalf of

##### purpose: `str`<a id="purpose-str"></a>

2-digit code from [Permissible Purpose Codes](https://developer.mastercard.com/open-banking-us/documentation/products/lend/report-handling/permissible-purpose-codes/), specifying the reason for retrieving this report. Required for retrieving some reports.

#### 🔄 Return<a id="🔄-return"></a>

[`Report`](./mastercard_python_sdk/pydantic/report.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/decisioning/v3/customers/{customerId}/reports/{reportId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.third_party_access.generate_key`<a id="mastercardthird_party_accessgenerate_key"></a>

Generate access key for third party partners.
A partner can provide access to third party partners with this access key.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_key_response = mastercard.third_party_access.generate_key(
    customer_id="1005061234",
    partner_id="1234583871234",
    third_party_partner_id="1234583871234",
    products=[
        {
            "product": "moneyTransferDetails",
            "payor_id": "2445581559892",
            "max_calls": 200,
            "account_id": "5011648377",
            "access_period": {
                "type": "timeframe",
                "start_time": "2022-03-10T06:06:20.042584549Z",
                "end_time": "2022-03-10T06:06:20.042584549Z",
            },
        }
    ],
    provenance={
        "client_fingerprint": "LU9ZYxcDNQCwEmAxH52XFzaRiGMAAAAABclSKxW5S9P8pUMDV4fbpg",
        "ip_address": "8.8.8.8",
        "token": "P9YbR+srNVyQI35893d+BzPrhGMAAAAAuacVUt+3m4svbaFjVSbHEA==",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID. See Add Customer API for how to create a customer ID.

##### partner_id: `str`<a id="partner_id-str"></a>

Your Partner ID displayed in the [Developer Dashboard](https://developer.mastercard.com/account/log-in)

##### third_party_partner_id: `str`<a id="third_party_partner_id-str"></a>

Your Partner ID displayed in the [Developer Dashboard](https://developer.mastercard.com/account/log-in)

##### products: List[`ThirdPartyAccessProduct`]<a id="products-listthirdpartyaccessproduct"></a>

##### provenance: [`ThirdPartyAccessProvenance`](./mastercard_python_sdk/type/third_party_access_provenance.py)<a id="provenance-thirdpartyaccessprovenancemastercard_python_sdktypethird_party_access_provenancepy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ThirdPartyAccessKeyData`](./mastercard_python_sdk/type/third_party_access_key_data.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ThirdPartyAccessKeyReceiptData`](./mastercard_python_sdk/pydantic/third_party_access_key_receipt_data.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/aggregation/v1/partners/accessKey` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.third_party_access.revoke_partners_access`<a id="mastercardthird_party_accessrevoke_partners_access"></a>

Revoke access of third party partners

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
mastercard.third_party_access.revoke_partners_access(
    consent_receipt_id="cr_4pfI3r1X8aOHrDDwrwC01NHFxOXlT1",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### consent_receipt_id: `str`<a id="consent_receipt_id-str"></a>

Third party access key receipt ID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/aggregation/v1/partners/accessKey/{consentReceiptId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.third_party_access.update_access`<a id="mastercardthird_party_accessupdate_access"></a>

Update access for third party partners

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_access_response = mastercard.third_party_access.update_access(
    customer_id="1005061234",
    partner_id="1234583871234",
    third_party_partner_id="1234583871234",
    products=[
        {
            "product": "moneyTransferDetails",
            "payor_id": "2445581559892",
            "max_calls": 200,
            "account_id": "5011648377",
            "access_period": {
                "type": "timeframe",
                "start_time": "2022-03-10T06:06:20.042584549Z",
                "end_time": "2022-03-10T06:06:20.042584549Z",
            },
        }
    ],
    consent_receipt_id="cr_4pfI3r1X8aOHrDDwrwC01NHFxOXlT1",
    provenance={
        "client_fingerprint": "LU9ZYxcDNQCwEmAxH52XFzaRiGMAAAAABclSKxW5S9P8pUMDV4fbpg",
        "ip_address": "8.8.8.8",
        "token": "P9YbR+srNVyQI35893d+BzPrhGMAAAAAuacVUt+3m4svbaFjVSbHEA==",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID. See Add Customer API for how to create a customer ID.

##### partner_id: `str`<a id="partner_id-str"></a>

Your Partner ID displayed in the [Developer Dashboard](https://developer.mastercard.com/account/log-in)

##### third_party_partner_id: `str`<a id="third_party_partner_id-str"></a>

Your Partner ID displayed in the [Developer Dashboard](https://developer.mastercard.com/account/log-in)

##### products: List[`ThirdPartyAccessProduct`]<a id="products-listthirdpartyaccessproduct"></a>

##### consent_receipt_id: `str`<a id="consent_receipt_id-str"></a>

Third party access key receipt ID

##### provenance: [`ThirdPartyAccessProvenance`](./mastercard_python_sdk/type/third_party_access_provenance.py)<a id="provenance-thirdpartyaccessprovenancemastercard_python_sdktypethird_party_access_provenancepy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ThirdPartyAccessKeyData`](./mastercard_python_sdk/type/third_party_access_key_data.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ThirdPartyAccessKeyReceiptData`](./mastercard_python_sdk/pydantic/third_party_access_key_receipt_data.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/aggregation/v1/partners/accessKey/{consentReceiptId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.transactions.get24_months_history_and_generate_report`<a id="mastercardtransactionsget24_months_history_and_generate_report"></a>

Generate a Transaction Report for the given accounts under the given customer. This service retrieves up to 24 months of transaction history for the given customer. It then uses this information to generate the Transaction Report.

This is a premium service. A billable event will be created upon the successful generation of the Transactions Report.

Before calling this API, a consumer must be created for the given customer ID (see Consumers APIs).

There cannot be more than 24 months between `fromDate` and `toDate`.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get24_months_history_and_generate_report_response = mastercard.transactions.get24_months_history_and_generate_report(
    customer_id="1005061234",
    to_date=1607450357,
    account_ids="5011648377 5011648378 5011648379",
    from_date=1607450357,
    report_custom_fields=[
        {
            "label": "loanID",
            "value": "123456",
            "shown": True,
        }
    ],
    callback_url="https://finicity-test/webhook",
    include_pending=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### to_date: `int`<a id="to_date-int"></a>

A end date

##### account_ids: `str`<a id="account_ids-str"></a>

A whitespace-separated list of account IDs to be included in the report (all accounts will be included if not set)

##### from_date: `int`<a id="from_date-int"></a>

A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).

##### report_custom_fields: [`ReportCustomFields`](./mastercard_python_sdk/type/report_custom_fields.py)<a id="report_custom_fields-reportcustomfieldsmastercard_python_sdktypereport_custom_fieldspy"></a>

##### callback_url: `str`<a id="callback_url-str"></a>

A Report Listener URL to receive notifications. The webhook must respond to the Finicity API with a 2xx HTTP status code.

##### include_pending: `bool`<a id="include_pending-bool"></a>

If pending transactions must be included

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TransactionsReportConstraints`](./mastercard_python_sdk/type/transactions_report_constraints.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TransactionsReportAck`](./mastercard_python_sdk/pydantic/transactions_report_ack.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/decisioning/v2/customers/{customerId}/transactions` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.transactions.get_all_customer_transactions`<a id="mastercardtransactionsget_all_customer_transactions"></a>

Get all transactions available for this customer within the given date range, across all accounts. This service supports paging and sorting by `transactionDate` (or `postedDate` if no transaction date is provided), with a maximum of 1000 transactions per request.

Standard consumer aggregation provides up to 180 days of transactions prior to the date each account was added to the Finicity system. To access older transactions, you must first call the service Load Historic Transactions for Account.

There is no limit for the size of the window between `fromDate` and `toDate`, however, the maximum number of transactions returned on one page is 1000.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_customer_transactions_response = mastercard.transactions.get_all_customer_transactions(
    customer_id="1005061234",
    from_date=1607450357,
    to_date=1607450357,
    start=1,
    limit=1,
    sort="desc",
    include_pending=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### from_date: `int`<a id="from_date-int"></a>

A start date

##### to_date: `int`<a id="to_date-int"></a>

A end date

##### start: `int`<a id="start-int"></a>

Index of the page of results to return

##### limit: `int`<a id="limit-int"></a>

Maximum number of results per page

##### sort: `str`<a id="sort-str"></a>

Date sort order: \"asc\" for ascending, \"desc\" for descending

##### include_pending: `bool`<a id="include_pending-bool"></a>

If pending transactions must be included

#### 🔄 Return<a id="🔄-return"></a>

[`Transactions`](./mastercard_python_sdk/pydantic/transactions.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/aggregation/v3/customers/{customerId}/transactions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.transactions.get_by_id`<a id="mastercardtransactionsget_by_id"></a>

Get details for the given transaction.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = mastercard.transactions.get_by_id(
    customer_id="1005061234",
    transaction_id=21284820852,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### transaction_id: `int`<a id="transaction_id-int"></a>

A transaction ID

#### 🔄 Return<a id="🔄-return"></a>

[`Transaction`](./mastercard_python_sdk/pydantic/transaction.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/aggregation/v2/customers/{customerId}/transactions/{transactionId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.transactions.get_customer_account_transactions`<a id="mastercardtransactionsget_customer_account_transactions"></a>

Get all transactions available for this customer account within the given date range. This service supports paging and sorting by `transactionDate` (or `postedDate` if no transaction date is provided), with a maximum of 1000 transactions per request.

Standard consumer aggregation provides up to 180 days of transactions prior to the date each account was added to the Finicity system. To access older transactions, you must first call the Cash Flow Verification service Load Historic Transactions for Account.

There is no limit for the size of the window between `fromDate` and `toDate`, however, the maximum number of transactions returned on one page is 1000.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_customer_account_transactions_response = mastercard.transactions.get_customer_account_transactions(
    customer_id="1005061234",
    account_id="5011648377",
    from_date=1607450357,
    to_date=1607450357,
    start=1,
    limit=1,
    sort="desc",
    include_pending=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### account_id: `str`<a id="account_id-str"></a>

The account ID

##### from_date: `int`<a id="from_date-int"></a>

A start date

##### to_date: `int`<a id="to_date-int"></a>

A end date

##### start: `int`<a id="start-int"></a>

Index of the page of results to return

##### limit: `int`<a id="limit-int"></a>

Maximum number of results per page

##### sort: `str`<a id="sort-str"></a>

Date sort order: \"asc\" for ascending, \"desc\" for descending

##### include_pending: `bool`<a id="include_pending-bool"></a>

If pending transactions must be included

#### 🔄 Return<a id="🔄-return"></a>

[`Transactions`](./mastercard_python_sdk/pydantic/transactions.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/aggregation/v4/customers/{customerId}/accounts/{accountId}/transactions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.transactions.load_historic_transactions_for_customer_account`<a id="mastercardtransactionsload_historic_transactions_for_customer_account"></a>

Connect to the account's financial institution and load up to 24 months of historic transactions for the account. Length of history varies by institution.

This is a premium service. The billable event is a call to this service specifying a customer ID that has not been seen before by this service. (If this service is called multiple times with the same customer ID, to load transactions from multiple accounts, only one billable event has occurred.)

The recommended timeout setting for this request is 180 seconds in order to receive a response. However, you can terminate the connection after making the call the operation will still complete. You will have to pull the account records to check for an updated aggregation attempt date to know when the refresh is complete.

The date range sent to the institution is calculated from the account's `createdDate`. This means that calling this service a second time for the same account normally will not add any new transactions for the account. For this reason, a second call to this service for a known account ID will usually return immediately.

In a few specific scenarios, it may be desirable to force a second connection to the institution for a known account ID. Some examples are:

* The institution's policy has changed, making more transactions available
* Finicity has now added a longer transaction history support for the institution
* The first call encountered an error, and the resulting Aggregation Ticket has now been fixed by the Finicity Support Team

In these cases, the POST request can contain the parameter `force=true` in the request body to force the second connection.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
mastercard.transactions.load_historic_transactions_for_customer_account(
    customer_id="1005061234",
    account_id="5011648377",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### account_id: `str`<a id="account_id-str"></a>

The account ID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/aggregation/v1/customers/{customerId}/accounts/{accountId}/transactions/historic` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.tx_push.delete_subscription`<a id="mastercardtx_pushdelete_subscription"></a>

Delete a specific subscription to TxPush notifications for the given account. This could be individual deleting the account or transactions events. No more events will be sent for that specific subscription.

For additional details on this process, see [TxPush Listener Service](https://developer.mastercard.com/open-banking-us/documentation/products/manage/tx-push/#setting-up-the-txpush-listener-service).

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
mastercard.tx_push.delete_subscription(
    customer_id="1005061234",
    subscription_id=17554874,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### subscription_id: `int`<a id="subscription_id-int"></a>

The subscription ID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/aggregation/v1/customers/{customerId}/subscriptions/{subscriptionId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.tx_push.disable_notifications`<a id="mastercardtx_pushdisable_notifications"></a>

Delete all TxPush subscriptions with their notifications for the given account. No more notifications will be sent for account or transaction events.

For additional details on this process, see [TxPush Listener Service](https://developer.mastercard.com/open-banking-us/documentation/products/manage/tx-push/#setting-up-the-txpush-listener-service).

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
mastercard.tx_push.disable_notifications(
    customer_id="1005061234",
    account_id="5011648377",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### account_id: `str`<a id="account_id-str"></a>

The account ID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/aggregation/v1/customers/{customerId}/accounts/{accountId}/txpush` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.tx_push.inject_test_transaction`<a id="mastercardtx_pushinject_test_transaction"></a>

Inject a transaction into the transaction list for a testing account. This allows an app to trigger TxPush notifications for the account in order to test the app's TxPush Listener service. This causes the platform to send one transaction event and one account event (showing that the account balance has changed). This service is only supported for testing accounts.

For additional details on this process, see [TxPush Listener Service](https://developer.mastercard.com/open-banking-us/documentation/products/manage/tx-push/#setting-up-the-txpush-listener-service).

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
inject_test_transaction_response = mastercard.tx_push.inject_test_transaction(
    description="a testing transaction description",
    amount=-4.25,
    transaction_date=1607450357,
    customer_id="1005061234",
    account_id="5011648377",
    status="pending",
    posted_date=1607450357,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### description: `str`<a id="description-str"></a>

The description of the transaction

##### amount: `Union[int, float]`<a id="amount-unionint-float"></a>

The amount of the transaction

##### transaction_date: `int`<a id="transaction_date-int"></a>

A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### account_id: `str`<a id="account_id-str"></a>

The account ID

##### status: `str`<a id="status-str"></a>

\\\"active\\\" or \\\"pending\\\" (optional)

##### posted_date: `int`<a id="posted_date-int"></a>

A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TestTxPushTransaction`](./mastercard_python_sdk/type/test_tx_push_transaction.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CreatedTestTxPushTransaction`](./mastercard_python_sdk/pydantic/created_test_tx_push_transaction.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/aggregation/v1/customers/{customerId}/accounts/{accountId}/transactions` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.tx_push.subscribe_notifications`<a id="mastercardtx_pushsubscribe_notifications"></a>

Register a client app's TxPush Listener to receive TxPush notifications related to the given account.

Each call to this service will return two records, one with class account and one with class transaction. Account events are sent when values change in the account's fields (such as `balance` or `interestRate`). Transaction events are sent whenever a new transaction is posted for the account. For institutions that do not provide TxPush services, notifications are sent as soon as Finicity finds a new transaction or new account data through regular aggregation processes.

The listener's URL must be secure (HTTPS) for any real-world account. In addition, the client's TxPush Listener will need to be verified. HTTP and HTTPS connections are only allowed on the standard ports 80 (HTTP) and 443 (HTTPS). The use of other ports will result with the call failing.

For additional details on this process, see [TxPush Listener Service](https://developer.mastercard.com/open-banking-us/documentation/products/manage/tx-push/#setting-up-the-txpush-listener-service).

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
subscribe_notifications_response = mastercard.tx_push.subscribe_notifications(
    callback_url="https://www.mydomain.com/txpush/listener",
    customer_id="1005061234",
    account_id="5011648377",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### callback_url: `str`<a id="callback_url-str"></a>

A callback URL where to receive TxPush notifications

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### account_id: `str`<a id="account_id-str"></a>

The account ID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TxPushSubscriptionParameters`](./mastercard_python_sdk/type/tx_push_subscription_parameters.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TxPushSubscriptions`](./mastercard_python_sdk/pydantic/tx_push_subscriptions.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/aggregation/v1/customers/{customerId}/accounts/{accountId}/txpush` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.verify_assets.customer_voa_report`<a id="mastercardverify_assetscustomer_voa_report"></a>

Generate a Verification of Assets (VOA) report for all checking, savings, money market, and investment accounts for the given customer. This service retrieves up to twelve months of transaction history for each account and uses this information to generate the VOA report.

This is a premium service. The billing rate is the variable rate for Verification of Assets under the current subscription plan. The billable event is the successful generation of a VOA report.

Before calling this API, a consumer must be created for the given customer ID (see Consumers APIs).

If no account of type checking, savings, money market, or investment is found, the service will return HTTP 400 Bad Request.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
customer_voa_report_response = mastercard.verify_assets.customer_voa_report(
    customer_id="1005061234",
    account_ids="5011648377 5011648378 5011648379",
    report_custom_fields=[
        {
            "label": "loanID",
            "value": "123456",
            "shown": True,
        }
    ],
    show_nsf=False,
    from_date=1607450357,
    callback_url="https://finicity-test/webhook",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### account_ids: `str`<a id="account_ids-str"></a>

A whitespace-separated list of account IDs to be included in the report (all accounts will be included if not set)

##### report_custom_fields: [`ReportCustomFields`](./mastercard_python_sdk/type/report_custom_fields.py)<a id="report_custom_fields-reportcustomfieldsmastercard_python_sdktypereport_custom_fieldspy"></a>

##### show_nsf: `bool`<a id="show_nsf-bool"></a>

Include the non-sufficient funds (NSF) summary JSON and the NSF summary PDF section in the report. Data included: * Account  * Total number of NSF funds  * Days since the most recent NFS funds fee

##### from_date: `int`<a id="from_date-int"></a>

A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).

##### callback_url: `str`<a id="callback_url-str"></a>

A Report Listener URL to receive notifications. The webhook must respond to the Finicity API with a 2xx HTTP status code.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`VOAReportConstraints`](./mastercard_python_sdk/type/voa_report_constraints.py)
#### 🔄 Return<a id="🔄-return"></a>

[`VOAReportAck`](./mastercard_python_sdk/pydantic/voa_report_ack.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/decisioning/v2/customers/{customerId}/voa` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.verify_assets.generate_voa_with_income_report`<a id="mastercardverify_assetsgenerate_voa_with_income_report"></a>

Generate a Verification of Assets with Income (VOAI) report for all checking, savings, money market, and investment accounts for the given customer. This service retrieves up to 24 months of transaction history for each account and uses this information to generate the VOAI report. The report includes 1 - 6 months of all debit and credit transactions for asset verification. By default, the history is set to 61 days, however, you can change the transaction history in this section by setting the `fromDate` parameter. The report also includes up to 24 months of income credit transactions (ordered by account and confidence level) regardless of `fromDate` for income verification.

This is a premium service. The billable event is the successful generation of a VOAI report.

Before calling this API, a consumer must be created for the given customer ID (see Consumers APIs).

If no account of type checking, savings, money market, or investment is found, the service will return HTTP 400 Bad Request.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_voa_with_income_report_response = mastercard.verify_assets.generate_voa_with_income_report(
    customer_id="1005061234",
    account_ids="5011648377 5011648378 5011648379",
    report_custom_fields=[
        {
            "label": "loanID",
            "value": "123456",
            "shown": True,
        }
    ],
    show_nsf=False,
    from_date=1607450357,
    income_stream_confidence_minimum=50,
    callback_url="https://finicity-test/webhook",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### account_ids: `str`<a id="account_ids-str"></a>

A whitespace-separated list of account IDs to be included in the report (all accounts will be included if not set)

##### report_custom_fields: [`ReportCustomFields`](./mastercard_python_sdk/type/report_custom_fields.py)<a id="report_custom_fields-reportcustomfieldsmastercard_python_sdktypereport_custom_fieldspy"></a>

##### show_nsf: `bool`<a id="show_nsf-bool"></a>

Include the non-sufficient funds (NSF) summary JSON and the NSF summary PDF section in the report. Data included: * Account  * Total number of NSF funds  * Days since the most recent NFS funds fee

##### from_date: `int`<a id="from_date-int"></a>

A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).

##### income_stream_confidence_minimum: `int`<a id="income_stream_confidence_minimum-int"></a>

Include income streams in the report, based on the income stream's confidence score. For example, Use the value 50 to include only income streams with a confidence score of 50 or higher.

##### callback_url: `str`<a id="callback_url-str"></a>

A Report Listener URL to receive notifications. The webhook must respond to the Finicity API with a 2xx HTTP status code.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`VOAWithIncomeReportConstraints`](./mastercard_python_sdk/type/voa_with_income_report_constraints.py)
#### 🔄 Return<a id="🔄-return"></a>

[`VOAWithIncomeReportAck`](./mastercard_python_sdk/pydantic/voa_with_income_report_ack.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/decisioning/v2/customers/{customerId}/voaHistory` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.verify_assets.get_asset_summary`<a id="mastercardverify_assetsget_asset_summary"></a>

Retrieve all checking, savings, money market, and investment accounts for a customer. The account, owner information, and the number of insufficient funds (NSFs) for checking accounts are also provided.

If no account type of checking, savings, money market, or investment is found, the service will return HTTP 400 Bad Request.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_asset_summary_response = mastercard.verify_assets.get_asset_summary(
    customer_id="1005061234",
    account_ids="5011648377 5011648378 5011648379",
    report_custom_fields=[
        {
            "label": "loanID",
            "value": "123456",
            "shown": True,
        }
    ],
    show_nsf=False,
    from_date=1607450357,
    callback_url="https://finicity-test/webhook",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### account_ids: `str`<a id="account_ids-str"></a>

A whitespace-separated list of account IDs to be included in the report (all accounts will be included if not set)

##### report_custom_fields: [`ReportCustomFields`](./mastercard_python_sdk/type/report_custom_fields.py)<a id="report_custom_fields-reportcustomfieldsmastercard_python_sdktypereport_custom_fieldspy"></a>

##### show_nsf: `bool`<a id="show_nsf-bool"></a>

Include the non-sufficient funds (NSF) summary JSON and the NSF summary PDF section in the report. Data included: * Account  * Total number of NSF funds  * Days since the most recent NFS funds fee

##### from_date: `int`<a id="from_date-int"></a>

A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).

##### callback_url: `str`<a id="callback_url-str"></a>

A Report Listener URL to receive notifications. The webhook must respond to the Finicity API with a 2xx HTTP status code.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PrequalificationReportConstraints`](./mastercard_python_sdk/type/prequalification_report_constraints.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PrequalificationReportAck`](./mastercard_python_sdk/pydantic/prequalification_report_ack.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/decisioning/v2/customers/{customerId}/assetSummary` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.verify_assets.get_checking_savings_investment_accounts`<a id="mastercardverify_assetsget_checking_savings_investment_accounts"></a>

Retrieve all checking, savings, money market, and investment accounts for a consumer. The account, owner information, and the number of insufficient funds (NSFs) for checking accounts are also provided.

If no account of type checking, savings, money market, or investment is found, the service will return HTTP 400 Bad Request.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_checking_savings_investment_accounts_response = mastercard.verify_assets.get_checking_savings_investment_accounts(
    customer_id="1005061234",
    account_ids="5011648377 5011648378 5011648379",
    report_custom_fields=[
        {
            "label": "loanID",
            "value": "123456",
            "shown": True,
        }
    ],
    show_nsf=False,
    from_date=1607450357,
    callback_url="https://finicity-test/webhook",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### account_ids: `str`<a id="account_ids-str"></a>

A whitespace-separated list of account IDs to be included in the report (all accounts will be included if not set)

##### report_custom_fields: [`ReportCustomFields`](./mastercard_python_sdk/type/report_custom_fields.py)<a id="report_custom_fields-reportcustomfieldsmastercard_python_sdktypereport_custom_fieldspy"></a>

##### show_nsf: `bool`<a id="show_nsf-bool"></a>

Include the non-sufficient funds (NSF) summary JSON and the NSF summary PDF section in the report. Data included: * Account  * Total number of NSF funds  * Days since the most recent NFS funds fee

##### from_date: `int`<a id="from_date-int"></a>

A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).

##### callback_url: `str`<a id="callback_url-str"></a>

A Report Listener URL to receive notifications. The webhook must respond to the Finicity API with a 2xx HTTP status code.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PrequalificationReportConstraints`](./mastercard_python_sdk/type/prequalification_report_constraints.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PrequalificationReportAck`](./mastercard_python_sdk/pydantic/prequalification_report_ack.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/decisioning/v2/customers/{customerId}/preQualVoa` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.verify_income_and_employment.create_voi_report`<a id="mastercardverify_income_and_employmentcreate_voi_report"></a>

Generate a Verification of Income (VOI) report for all checking, savings, and money market accounts for the given customer. This service retrieves up to two years of transaction history for each account and uses this information to generate the VOI report.

This is a premium service. The billing rate is the variable rate for Verification of Income under the current subscription plan. The billable event is the successful generation of a VOI report.

If no account of type checking, savings, or money market is found, the service will return HTTP 400 Bad Request.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_voi_report_response = mastercard.verify_income_and_employment.create_voi_report(
    customer_id="1005061234",
    account_ids="5011648377 5011648378 5011648379",
    report_custom_fields=[
        {
            "label": "loanID",
            "value": "123456",
            "shown": True,
        }
    ],
    from_date=1607450357,
    income_stream_confidence_minimum=50,
    callback_url="https://finicity-test/webhook",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### account_ids: `str`<a id="account_ids-str"></a>

A whitespace-separated list of account IDs to be included in the report (all accounts will be included if not set)

##### report_custom_fields: [`ReportCustomFields`](./mastercard_python_sdk/type/report_custom_fields.py)<a id="report_custom_fields-reportcustomfieldsmastercard_python_sdktypereport_custom_fieldspy"></a>

##### from_date: `int`<a id="from_date-int"></a>

A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).

##### income_stream_confidence_minimum: `int`<a id="income_stream_confidence_minimum-int"></a>

Include income streams in the report, based on the income stream's confidence score. For example, Use the value 50 to include only income streams with a confidence score of 50 or higher.

##### callback_url: `str`<a id="callback_url-str"></a>

A Report Listener URL to receive notifications. The webhook must respond to the Finicity API with a 2xx HTTP status code.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`VOIReportConstraints`](./mastercard_python_sdk/type/voi_report_constraints.py)
#### 🔄 Return<a id="🔄-return"></a>

[`VOIReportAck`](./mastercard_python_sdk/pydantic/voi_report_ack.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/decisioning/v2/customers/{customerId}/voi` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.verify_income_and_employment.generate_pay_statement_report`<a id="mastercardverify_income_and_employmentgenerate_pay_statement_report"></a>

Generate Pay Statement Extraction Report for the given customer. This service accepts asset IDs of the stored pay statements to generate a Pay Statement Extraction Report.

This is a premium service. The billing rate is the variable rate for Pay Statement Extraction Report under the current subscription plan. The billable event is the successful generation of a Pay Statement Extraction Report.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_pay_statement_report_response = mastercard.verify_income_and_employment.generate_pay_statement_report(
    paystatement_report={
        "asset_ids": [
            "097545c5-1c2a-4f20-a5ef-77f0820344c9-2018601178"
        ],
        "extract_earnings": True,
        "extract_deductions": True,
        "extract_direct_deposit": True,
    },
    customer_id="1005061234",
    report_custom_fields=[
        {
            "label": "loanID",
            "value": "123456",
            "shown": True,
        }
    ],
    callback_url="https://finicity-test/webhook",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### paystatement_report: [`PayStatementData`](./mastercard_python_sdk/type/pay_statement_data.py)<a id="paystatement_report-paystatementdatamastercard_python_sdktypepay_statement_datapy"></a>


##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### report_custom_fields: [`ReportCustomFields`](./mastercard_python_sdk/type/report_custom_fields.py)<a id="report_custom_fields-reportcustomfieldsmastercard_python_sdktypereport_custom_fieldspy"></a>

##### callback_url: `str`<a id="callback_url-str"></a>

A Report Listener URL to receive notifications. The webhook must respond to the Finicity API with a 2xx HTTP status code.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PayStatementReportConstraints`](./mastercard_python_sdk/type/pay_statement_report_constraints.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PayStatementReportAck`](./mastercard_python_sdk/pydantic/pay_statement_report_ack.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/decisioning/v2/customers/{customerId}/payStatement` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.verify_income_and_employment.generate_voe_payroll_report`<a id="mastercardverify_income_and_employmentgenerate_voe_payroll_report"></a>

Generate or refresh a VOE - Payroll report. Often used as a complementary report to the VOIE-Payroll report to fulfill the pre-close VOE requirements. It retrieves the customer's employment details and employment status through the payroll source without any income information.

This is a premium service. The billable event is the successful generation of a VOE - Payroll report.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_voe_payroll_report_response = mastercard.verify_income_and_employment.generate_voe_payroll_report(
    payroll_data={
        "ssn": "999999999",
        "dob": 1607450357,
        "report_id": "u4hstnnak45g-voiepayroll",
    },
    customer_id="1005061234",
    report_custom_fields=[
        {
            "label": "loanID",
            "value": "123456",
            "shown": True,
        }
    ],
    pay_statements_from_date=1607450357,
    market_segment="Mortgage",
    exclude_emp_info=False,
    purpose="31",
    callback_url="https://finicity-test/webhook",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payroll_data: [`PayrollData`](./mastercard_python_sdk/type/payroll_data.py)<a id="payroll_data-payrolldatamastercard_python_sdktypepayroll_datapy"></a>


##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### report_custom_fields: [`ReportCustomFields`](./mastercard_python_sdk/type/report_custom_fields.py)<a id="report_custom_fields-reportcustomfieldsmastercard_python_sdktypereport_custom_fieldspy"></a>

##### pay_statements_from_date: `int`<a id="pay_statements_from_date-int"></a>

Limits the pay statement history in the VOIE - Payroll report income record. Pay statements are only included if the payDate of the statement is equal to or greater than the start date requested. Date should be in Unix epoch time (in seconds). See: Handling Epoch Dates and Times.

##### market_segment: `str`<a id="market_segment-str"></a>

Use case for requesting the consumer's data. Current supported enumerations are \\\"Mortgage\\\" and \\\"KYC\\\". If your use case doesn't match one of these please reach out to your technical point of contact.

##### exclude_emp_info: `bool`<a id="exclude_emp_info-bool"></a>

Only used on an exception basis for clients that need to exclude EmpInfo data from the VOE-Payroll or VOIE-Payroll report. If true is passed EmpInfo payroll provider's data will not be searched or returned.

##### purpose: `str`<a id="purpose-str"></a>

FCRA required 2-digit Permissible Purpose Code, specifying the reason for retrieving this report.

##### callback_url: `str`<a id="callback_url-str"></a>

A Report Listener URL to receive notifications. The webhook must respond to the Finicity API with a 2xx HTTP status code.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PayrollReportConstraints`](./mastercard_python_sdk/type/payroll_report_constraints.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PayrollReportAck`](./mastercard_python_sdk/pydantic/payroll_report_ack.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/decisioning/v2/customers/{customerId}/voePayroll` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.verify_income_and_employment.generate_voe_transactions_report`<a id="mastercardverify_income_and_employmentgenerate_voe_transactions_report"></a>

Premium Service: A billable event when the API response is successful.

MVS-Direct integration developers only.

Used as a complimentary report to the VOA with Income and VOIE - Paystub (with TXVerify) reports and used to fulfill the pre-close VOE requirements.

Retrieve the latest credit transaction information from the borrower's connected bank accounts and groups them into income streams so that you can view their payment history to ensure a direct deport was made within the expected cadence. The report displays transaction descriptions without any dollar amounts so that income re-verification isn't necessary.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_voe_transactions_report_response = mastercard.verify_income_and_employment.generate_voe_transactions_report(
    customer_id="1005061234",
    report_id="u4hstnnak45g",
    account_ids="5011648377 5011648378 5011648379",
    report_custom_fields=[
        {
            "label": "loanID",
            "value": "123456",
            "shown": True,
        }
    ],
    from_date=1607450357,
    income_stream_confidence_minimum=50,
    callback_url="https://finicity-test/webhook",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### report_id: `str`<a id="report_id-str"></a>

A report ID

##### account_ids: `str`<a id="account_ids-str"></a>

A whitespace-separated list of account IDs to be included in the report (all accounts will be included if not set)

##### report_custom_fields: [`ReportCustomFields`](./mastercard_python_sdk/type/report_custom_fields.py)<a id="report_custom_fields-reportcustomfieldsmastercard_python_sdktypereport_custom_fieldspy"></a>

##### from_date: `int`<a id="from_date-int"></a>

A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).

##### income_stream_confidence_minimum: `int`<a id="income_stream_confidence_minimum-int"></a>

Include income streams in the report, based on the income stream's confidence score. For example, Use the value 50 to include only income streams with a confidence score of 50 or higher.

##### callback_url: `str`<a id="callback_url-str"></a>

A Report Listener URL to receive notifications. The webhook must respond to the Finicity API with a 2xx HTTP status code.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`VOETransactionsReportConstraints`](./mastercard_python_sdk/type/voe_transactions_report_constraints.py)
#### 🔄 Return<a id="🔄-return"></a>

[`VOETransactionsReportAck`](./mastercard_python_sdk/pydantic/voe_transactions_report_ack.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/decisioning/v2/customers/{customerId}/voeTransactions` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.verify_income_and_employment.generate_voie_paystub_report`<a id="mastercardverify_income_and_employmentgenerate_voie_paystub_report"></a>

Generate a VOIE - Paystub report. This service uses the provided paystub(s), which are passed into the request body as asset IDs (generated using the Store Customer Pay Statement API) to generate the VOIE - Paystub report with digitized paystub details.

This is a premium service. The billing rate is the variable rate for VOIE - Paystub under the current subscription plan. The billable event is the successful generation of a VOIE - Paystub Report.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_voie_paystub_report_response = mastercard.verify_income_and_employment.generate_voie_paystub_report(
    voie_with_statement_data={
        "asset_ids": [
            "097545c5-1c2a-4f20-a5ef-77f0820344c9-2018601178"
        ],
        "extract_earnings": True,
        "extract_deductions": True,
        "extract_direct_deposit": True,
    },
    customer_id="1005061234",
    report_custom_fields=[
        {
            "label": "loanID",
            "value": "123456",
            "shown": True,
        }
    ],
    callback_url="https://finicity-test/webhook",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### voie_with_statement_data: [`VOIEWithStatementData`](./mastercard_python_sdk/type/voie_with_statement_data.py)<a id="voie_with_statement_data-voiewithstatementdatamastercard_python_sdktypevoie_with_statement_datapy"></a>


##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### report_custom_fields: [`ReportCustomFields`](./mastercard_python_sdk/type/report_custom_fields.py)<a id="report_custom_fields-reportcustomfieldsmastercard_python_sdktypereport_custom_fieldspy"></a>

##### callback_url: `str`<a id="callback_url-str"></a>

A Report Listener URL to receive notifications. The webhook must respond to the Finicity API with a 2xx HTTP status code.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`VOIEReportConstraints`](./mastercard_python_sdk/type/voie_report_constraints.py)
#### 🔄 Return<a id="🔄-return"></a>

[`VOIEPaystubReportAck`](./mastercard_python_sdk/pydantic/voie_paystub_report_ack.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/decisioning/v2/customers/{customerId}/voieTxVerify/withStatement` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.verify_income_and_employment.generate_voie_paystub_with_tx_verify_report`<a id="mastercardverify_income_and_employmentgenerate_voie_paystub_with_tx_verify_report"></a>

Generate a VOIE - Paystub (with TXVerify) report for all checking and savings under the given customer. This service retrieves up to two years of transaction history for the given accounts. It then uses this information as well as the provided paystub(s), which are passed into the request body as asset IDs (generated using the Store Customer Pay Statement API) to generate the VOIE - Paystub (with TXVerify) report.

Note: if you are using this API to refresh the bank transactions, use the same asset ID from the first report. A new paystub is not required unless the paystub is too old for underwriting requirements. Using the same asset ID that was on the original report and the previously extracted details will be used to speed up report generation response time.

This is a premium service. The billing rate is the variable rate for VOIE TXVerify under the current subscription plan. The billable event is the successful generation of a VOIE TXVerify Report.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_voie_paystub_with_tx_verify_report_response = mastercard.verify_income_and_employment.generate_voie_paystub_with_tx_verify_report(
    voie_with_interview_data={
        "tx_verify_interview": [
            {
                "asset_id": "097545c5-1c2a-4f20-a5ef-77f0820344c9-2018601178",
                "accounts": ["5011648377", "5011648378", "5011648379"],
            }
        ],
        "extract_earnings": True,
        "extract_deductions": True,
        "extract_direct_deposit": True,
    },
    customer_id="1005061234",
    account_ids="5011648377 5011648378 5011648379",
    report_custom_fields=[
        {
            "label": "loanID",
            "value": "123456",
            "shown": True,
        }
    ],
    from_date=1607450357,
    income_stream_confidence_minimum=50,
    callback_url="https://finicity-test/webhook",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### voie_with_interview_data: [`VOIEWithInterviewData`](./mastercard_python_sdk/type/voie_with_interview_data.py)<a id="voie_with_interview_data-voiewithinterviewdatamastercard_python_sdktypevoie_with_interview_datapy"></a>


##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### account_ids: `str`<a id="account_ids-str"></a>

A whitespace-separated list of account IDs to be included in the report (all accounts will be included if not set)

##### report_custom_fields: [`ReportCustomFields`](./mastercard_python_sdk/type/report_custom_fields.py)<a id="report_custom_fields-reportcustomfieldsmastercard_python_sdktypereport_custom_fieldspy"></a>

##### from_date: `int`<a id="from_date-int"></a>

A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).

##### income_stream_confidence_minimum: `int`<a id="income_stream_confidence_minimum-int"></a>

Include income streams in the report, based on the income stream's confidence score. For example, Use the value 50 to include only income streams with a confidence score of 50 or higher.

##### callback_url: `str`<a id="callback_url-str"></a>

A Report Listener URL to receive notifications. The webhook must respond to the Finicity API with a 2xx HTTP status code.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`VOIEWithTXVerifyReportConstraints`](./mastercard_python_sdk/type/voie_with_tx_verify_report_constraints.py)
#### 🔄 Return<a id="🔄-return"></a>

[`VOIEPaystubWithTXVerifyReportAck`](./mastercard_python_sdk/pydantic/voie_paystub_with_tx_verify_report_ack.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/decisioning/v2/customers/{customerId}/voieTxVerify/withInterview` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `mastercard.verify_income_and_employment.refresh_voie_payroll_report`<a id="mastercardverify_income_and_employmentrefresh_voie_payroll_report"></a>

Generate or refresh a VOIE - Payroll report. For clients using the product via a consumer permissioning experience via Connect, the original VOIE - Payroll report generates when the consumer completes the Connect experience, and this API is only used for future report refreshes without reengaging the consumer.

This is a premium service. The billable event is the successful generation of a VOIE - Payroll report.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
refresh_voie_payroll_report_response = mastercard.verify_income_and_employment.refresh_voie_payroll_report(
    payroll_data={
        "ssn": "999999999",
        "dob": 1607450357,
        "report_id": "u4hstnnak45g-voiepayroll",
    },
    customer_id="1005061234",
    report_custom_fields=[
        {
            "label": "loanID",
            "value": "123456",
            "shown": True,
        }
    ],
    pay_statements_from_date=1607450357,
    market_segment="Mortgage",
    exclude_emp_info=False,
    purpose="31",
    callback_url="https://finicity-test/webhook",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payroll_data: [`PayrollData`](./mastercard_python_sdk/type/payroll_data.py)<a id="payroll_data-payrolldatamastercard_python_sdktypepayroll_datapy"></a>


##### customer_id: `str`<a id="customer_id-str"></a>

A customer ID

##### report_custom_fields: [`ReportCustomFields`](./mastercard_python_sdk/type/report_custom_fields.py)<a id="report_custom_fields-reportcustomfieldsmastercard_python_sdktypereport_custom_fieldspy"></a>

##### pay_statements_from_date: `int`<a id="pay_statements_from_date-int"></a>

Limits the pay statement history in the VOIE - Payroll report income record. Pay statements are only included if the payDate of the statement is equal to or greater than the start date requested. Date should be in Unix epoch time (in seconds). See: Handling Epoch Dates and Times.

##### market_segment: `str`<a id="market_segment-str"></a>

Use case for requesting the consumer's data. Current supported enumerations are \\\"Mortgage\\\" and \\\"KYC\\\". If your use case doesn't match one of these please reach out to your technical point of contact.

##### exclude_emp_info: `bool`<a id="exclude_emp_info-bool"></a>

Only used on an exception basis for clients that need to exclude EmpInfo data from the VOE-Payroll or VOIE-Payroll report. If true is passed EmpInfo payroll provider's data will not be searched or returned.

##### purpose: `str`<a id="purpose-str"></a>

FCRA required 2-digit Permissible Purpose Code, specifying the reason for retrieving this report.

##### callback_url: `str`<a id="callback_url-str"></a>

A Report Listener URL to receive notifications. The webhook must respond to the Finicity API with a 2xx HTTP status code.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PayrollReportConstraints`](./mastercard_python_sdk/type/payroll_report_constraints.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PayrollReportAck`](./mastercard_python_sdk/pydantic/payroll_report_ack.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/decisioning/v2/customers/{customerId}/voiePayroll` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
