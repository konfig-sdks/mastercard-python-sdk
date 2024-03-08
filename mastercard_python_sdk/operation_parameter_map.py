operation_parameter_map = {
    '/microentry/v1/customers/{customerId}/accounts/{accountId}-GET': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'accountId'
            },
        ]
    },
    '/microentry/v1/customers/{customerId}-POST': {
        'parameters': [
            {
                'name': 'receiver'
            },
            {
                'name': 'customerId'
            },
            {
                'name': 'institutionLoginId'
            },
            {
                'name': 'callbackUrl'
            },
        ]
    },
    '/microentry/v1/customers/{customerId}/accounts/{accountId}/amounts-POST': {
        'parameters': [
            {
                'name': 'amounts'
            },
            {
                'name': 'customerId'
            },
            {
                'name': 'accountId'
            },
        ]
    },
    '/aggregation/v2/customers/{customerId}/accounts/{accountId}-GET': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'accountId'
            },
        ]
    },
    '/aggregation/v1/customers/{customerId}/institutionLogins/{institutionLoginId}/accounts-GET': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'institutionLoginId'
            },
        ]
    },
    '/aggregation/v1/customers/{customerId}/accounts-GET': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'status'
            },
            {
                'name': 'account_type'
            },
        ]
    },
    '/aggregation/v1/customers/{customerId}/institutions/{institutionId}/accounts-GET': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'institutionId'
            },
        ]
    },
    '/aggregation/v2/customers/{customerId}/institutionLogins/{institutionLoginId}/accounts-POST': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'institutionLoginId'
            },
        ]
    },
    '/aggregation/v1/customers/{customerId}/accounts-POST': {
        'parameters': [
            {
                'name': 'customerId'
            },
        ]
    },
    '/aggregation/v1/customers/{customerId}/institutionLogins/{institutionLoginId}/accounts-POST': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'institutionLoginId'
            },
        ]
    },
    '/aggregation/v2/customers/{customerId}/accounts-POST': {
        'parameters': [
            {
                'name': 'customerId'
            },
        ]
    },
    '/aggregation/v1/customers/{customerId}/accounts/{accountId}-DELETE': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'accountId'
            },
        ]
    },
    '/aggregation/v1/customers/{customerId}/institutionLogins/{institutionLoginId}-DELETE': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'institutionLoginId'
            },
        ]
    },
    '/aggregation/v1/customers/{customerId}/institutions/{institutionId}/accounts/simple-GET': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'institutionId'
            },
        ]
    },
    '/aggregation/v1/customers/{customerId}/institutionLogins/{institutionLoginId}/accounts/simple-GET': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'institutionLoginId'
            },
        ]
    },
    '/aggregation/v1/customers/{customerId}/accounts/{accountId}/simple-GET': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'accountId'
            },
        ]
    },
    '/aggregation/v1/customers/{customerId}/accounts/simple-GET': {
        'parameters': [
            {
                'name': 'customerId'
            },
        ]
    },
    '/aggregation/v1/customers/{customerId}/applications/{applicationId}-PUT': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'applicationId'
            },
        ]
    },
    '/aggregation/v1/partners/applications-POST': {
        'parameters': [
            {
                'name': 'appDescription'
            },
            {
                'name': 'appName'
            },
            {
                'name': 'appUrl'
            },
            {
                'name': 'ownerAddressLine1'
            },
            {
                'name': 'ownerAddressLine2'
            },
            {
                'name': 'ownerCity'
            },
            {
                'name': 'ownerCountry'
            },
            {
                'name': 'ownerName'
            },
            {
                'name': 'ownerPostalCode'
            },
            {
                'name': 'ownerState'
            },
            {
                'name': 'image'
            },
        ]
    },
    '/aggregation/v2/partners/applications-GET': {
        'parameters': [
            {
                'name': 'preAppId'
            },
            {
                'name': 'applicationId'
            },
            {
                'name': 'status'
            },
            {
                'name': 'appName'
            },
            {
                'name': 'submittedDate'
            },
            {
                'name': 'modifiedDate'
            },
            {
                'name': 'page'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/aggregation/v2/customers/{customerId}/institutionLogins/{institutionLoginId}/migration-PUT': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'institutionLoginId'
            },
        ]
    },
    '/aggregation/v1/partners/applications/{preAppId}-PUT': {
        'parameters': [
            {
                'name': 'appDescription'
            },
            {
                'name': 'appName'
            },
            {
                'name': 'appUrl'
            },
            {
                'name': 'ownerAddressLine1'
            },
            {
                'name': 'ownerAddressLine2'
            },
            {
                'name': 'ownerCity'
            },
            {
                'name': 'ownerCountry'
            },
            {
                'name': 'ownerName'
            },
            {
                'name': 'ownerPostalCode'
            },
            {
                'name': 'ownerState'
            },
            {
                'name': 'image'
            },
            {
                'name': 'preAppId'
            },
        ]
    },
    '/aggregation/v1/customers/{customerId}/assets/{assetId}-GET': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'assetId'
            },
        ]
    },
    '/aggregation/v2/partners/authentication-POST': {
        'parameters': [
            {
                'name': 'partnerId'
            },
            {
                'name': 'partnerSecret'
            },
        ]
    },
    '/aggregation/v2/partners/authentication-PUT': {
        'parameters': [
            {
                'name': 'partnerId'
            },
            {
                'name': 'partnerSecret'
            },
            {
                'name': 'newPartnerSecret'
            },
        ]
    },
    '/analytics/balance/v1/customer/{customerId}-POST': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'accountIds'
            },
            {
                'name': 'lengthOfReport'
            },
            {
                'name': 'reference-number'
            },
        ]
    },
    '/analytics/balance/v1/customer/{customerId}/fcra-POST': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'accountIds'
            },
            {
                'name': 'lengthOfReport'
            },
            {
                'name': 'reference-number'
            },
        ]
    },
    '/decisioning/v2/customers/{customerId}/reports/balance-analytics/userTypes/{userType}-POST': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'userType'
            },
            {
                'name': 'analyticsReportData'
            },
            {
                'name': 'accountIds'
            },
            {
                'name': 'reportCustomFields'
            },
            {
                'name': 'fromDate'
            },
            {
                'name': 'callbackUrl'
            },
        ]
    },
    '/analytics/data/v1/{obb_report_id}-GET': {
        'parameters': [
            {
                'name': 'obb_report_id'
            },
        ]
    },
    '/analytics/data/v1/{obb_report_id}/fcra-GET': {
        'parameters': [
            {
                'name': 'obb_report_id'
            },
            {
                'name': 'purpose'
            },
        ]
    },
    '/decisioning/v2/customers/{customerId}/statement-POST': {
        'parameters': [
            {
                'name': 'statementReportData'
            },
            {
                'name': 'customerId'
            },
            {
                'name': 'reportCustomFields'
            },
            {
                'name': 'callbackUrl'
            },
        ]
    },
    '/aggregation/v1/customers/{customerId}/accounts/{accountId}/statement-GET': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'accountId'
            },
            {
                'name': 'index'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/aggregation/v3/customers/{customerId}/accounts/{accountId}/statement-GET': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'accountId'
            },
            {
                'name': 'index'
            },
        ]
    },
    '/business-services/customers/{customer_id}/businesses-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'personallyLiable'
            },
            {
                'name': 'address'
            },
            {
                'name': 'phoneNumber'
            },
            {
                'name': 'customer_id'
            },
            {
                'name': 'url'
            },
            {
                'name': 'email'
            },
            {
                'name': 'type'
            },
            {
                'name': 'taxId'
            },
        ]
    },
    '/business-services/customers/{customer_id}/businesses-GET': {
        'parameters': [
            {
                'name': 'customer_id'
            },
        ]
    },
    '/business-services/businesses/{business_id}-GET': {
        'parameters': [
            {
                'name': 'customer_id'
            },
        ]
    },
    '/business-services/businesses/{business_id}-PUT': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'personallyLiable'
            },
            {
                'name': 'address'
            },
            {
                'name': 'phoneNumber'
            },
            {
                'name': 'customer_id'
            },
            {
                'name': 'url'
            },
            {
                'name': 'email'
            },
            {
                'name': 'type'
            },
            {
                'name': 'taxId'
            },
        ]
    },
    '/decisioning/v2/customers/{customerId}/cashFlowPersonal-POST': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'accountIds'
            },
            {
                'name': 'reportCustomFields'
            },
            {
                'name': 'showNsf'
            },
            {
                'name': 'fromDate'
            },
            {
                'name': 'incomeStreamConfidenceMinimum'
            },
            {
                'name': 'callbackUrl'
            },
        ]
    },
    '/decisioning/v2/customers/{customerId}/cashFlowBusiness-POST': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'accountIds'
            },
            {
                'name': 'reportCustomFields'
            },
            {
                'name': 'showNsf'
            },
            {
                'name': 'fromDate'
            },
            {
                'name': 'incomeStreamConfidenceMinimum'
            },
            {
                'name': 'callbackUrl'
            },
        ]
    },
    '/analytics/cashflow/v1/customer/{customerId}-POST': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'accountIds'
            },
            {
                'name': 'lengthOfReport'
            },
            {
                'name': 'reference-number'
            },
        ]
    },
    '/analytics/cashflow/v1/customer/{customerId}/fcra-POST': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'accountIds'
            },
            {
                'name': 'lengthOfReport'
            },
            {
                'name': 'reference-number'
            },
        ]
    },
    '/decisioning/v2/customers/{customerId}/reports/cashflow-analytics/userTypes/{userType}-POST': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'userType'
            },
            {
                'name': 'analyticsReportData'
            },
            {
                'name': 'accountIds'
            },
            {
                'name': 'reportCustomFields'
            },
            {
                'name': 'fromDate'
            },
            {
                'name': 'callbackUrl'
            },
        ]
    },
    '/analytics/data/v1/{obb_report_id}-GET': {
        'parameters': [
            {
                'name': 'obb_report_id'
            },
        ]
    },
    '/analytics/data/v1/{obb_report_id}/fcra-GET': {
        'parameters': [
            {
                'name': 'obb_report_id'
            },
            {
                'name': 'purpose'
            },
        ]
    },
    '/connect/v2/generate/fix-POST': {
        'parameters': [
            {
                'name': 'partnerId'
            },
            {
                'name': 'customerId'
            },
            {
                'name': 'institutionLoginId'
            },
            {
                'name': 'language'
            },
            {
                'name': 'redirectUri'
            },
            {
                'name': 'webhook'
            },
            {
                'name': 'webhookContentType'
            },
            {
                'name': 'webhookData'
            },
            {
                'name': 'webhookHeaders'
            },
            {
                'name': 'experience'
            },
            {
                'name': 'singleUseUrl'
            },
            {
                'name': 'isWebView'
            },
        ]
    },
    '/connect/v2/generate/jointBorrower-POST': {
        'parameters': [
            {
                'name': 'partnerId'
            },
            {
                'name': 'borrowers'
            },
            {
                'name': 'language'
            },
            {
                'name': 'redirectUri'
            },
            {
                'name': 'webhook'
            },
            {
                'name': 'webhookContentType'
            },
            {
                'name': 'webhookData'
            },
            {
                'name': 'webhookHeaders'
            },
            {
                'name': 'institutionSettings'
            },
            {
                'name': 'experience'
            },
            {
                'name': 'fromDate'
            },
            {
                'name': 'reportCustomFields'
            },
            {
                'name': 'singleUseUrl'
            },
        ]
    },
    '/connect/v2/generate/lite-POST': {
        'parameters': [
            {
                'name': 'partnerId'
            },
            {
                'name': 'customerId'
            },
            {
                'name': 'institutionId'
            },
            {
                'name': 'language'
            },
            {
                'name': 'redirectUri'
            },
            {
                'name': 'webhook'
            },
            {
                'name': 'webhookContentType'
            },
            {
                'name': 'webhookData'
            },
            {
                'name': 'webhookHeaders'
            },
            {
                'name': 'experience'
            },
            {
                'name': 'singleUseUrl'
            },
            {
                'name': 'isWebView'
            },
        ]
    },
    '/connect/v2/generate-POST': {
        'parameters': [
            {
                'name': 'partnerId'
            },
            {
                'name': 'customerId'
            },
            {
                'name': 'language'
            },
            {
                'name': 'consumerId'
            },
            {
                'name': 'redirectUri'
            },
            {
                'name': 'webhook'
            },
            {
                'name': 'webhookContentType'
            },
            {
                'name': 'webhookData'
            },
            {
                'name': 'webhookHeaders'
            },
            {
                'name': 'optionalConsumerInfo'
            },
            {
                'name': 'singleUseUrl'
            },
            {
                'name': 'experience'
            },
            {
                'name': 'institutionSettings'
            },
            {
                'name': 'fromDate'
            },
            {
                'name': 'reportCustomFields'
            },
            {
                'name': 'isWebView'
            },
        ]
    },
    '/connect/v2/send/email-POST': {
        'parameters': [
            {
                'name': 'partnerId'
            },
            {
                'name': 'customerId'
            },
            {
                'name': 'consumerId'
            },
            {
                'name': 'email'
            },
            {
                'name': 'language'
            },
            {
                'name': 'redirectUri'
            },
            {
                'name': 'webhook'
            },
            {
                'name': 'webhookContentType'
            },
            {
                'name': 'webhookData'
            },
            {
                'name': 'webhookHeaders'
            },
            {
                'name': 'institutionSettings'
            },
            {
                'name': 'experience'
            },
            {
                'name': 'singleUseUrl'
            },
            {
                'name': 'fromDate'
            },
            {
                'name': 'reportCustomFields'
            },
            {
                'name': 'optionalConsumerInfo'
            },
        ]
    },
    '/connect/v2/send/email/jointBorrower-POST': {
        'parameters': [
            {
                'name': 'partnerId'
            },
            {
                'name': 'borrowers'
            },
            {
                'name': 'email'
            },
            {
                'name': 'experience'
            },
            {
                'name': 'language'
            },
            {
                'name': 'redirectUri'
            },
            {
                'name': 'webhook'
            },
            {
                'name': 'webhookContentType'
            },
            {
                'name': 'webhookData'
            },
            {
                'name': 'webhookHeaders'
            },
            {
                'name': 'institutionSettings'
            },
            {
                'name': 'fromDate'
            },
            {
                'name': 'reportCustomFields'
            },
            {
                'name': 'singleUseUrl'
            },
        ]
    },
    '/connect/v2/generate/microentry/verify-POST': {
        'parameters': [
            {
                'name': 'partnerId'
            },
            {
                'name': 'customerId'
            },
            {
                'name': 'redirectUri'
            },
            {
                'name': 'webhook'
            },
            {
                'name': 'webhookContentType'
            },
            {
                'name': 'webhookData'
            },
            {
                'name': 'webhookHeaders'
            },
            {
                'name': 'experience'
            },
            {
                'name': 'accountId'
            },
        ]
    },
    '/decisioning/v1/customers/{customerId}/consumer-POST': {
        'parameters': [
            {
                'name': 'firstName'
            },
            {
                'name': 'lastName'
            },
            {
                'name': 'address'
            },
            {
                'name': 'city'
            },
            {
                'name': 'state'
            },
            {
                'name': 'zip'
            },
            {
                'name': 'phone'
            },
            {
                'name': 'ssn'
            },
            {
                'name': 'birthday'
            },
            {
                'name': 'customerId'
            },
            {
                'name': 'email'
            },
            {
                'name': 'suffix'
            },
        ]
    },
    '/decisioning/v1/customers/{customerId}/consumer-GET': {
        'parameters': [
            {
                'name': 'customerId'
            },
        ]
    },
    '/decisioning/v1/consumers/{consumerId}-GET': {
        'parameters': [
            {
                'name': 'consumerId'
            },
        ]
    },
    '/decisioning/v1/consumers/{consumerId}-PUT': {
        'parameters': [
            {
                'name': 'consumerId'
            },
            {
                'name': 'firstName'
            },
            {
                'name': 'lastName'
            },
            {
                'name': 'address'
            },
            {
                'name': 'city'
            },
            {
                'name': 'state'
            },
            {
                'name': 'zip'
            },
            {
                'name': 'phone'
            },
            {
                'name': 'ssn'
            },
            {
                'name': 'birthday'
            },
            {
                'name': 'email'
            },
            {
                'name': 'suffix'
            },
        ]
    },
    '/customers/institution-logins/{institution_login_id}/authorization-details-GET': {
        'parameters': [
            {
                'name': 'institution_login_id'
            },
        ]
    },
    '/aggregation/v2/customers/active-POST': {
        'parameters': [
            {
                'name': 'username'
            },
            {
                'name': 'firstName'
            },
            {
                'name': 'lastName'
            },
            {
                'name': 'applicationId'
            },
            {
                'name': 'phone'
            },
            {
                'name': 'email'
            },
        ]
    },
    '/aggregation/v2/customers/testing-POST': {
        'parameters': [
            {
                'name': 'username'
            },
            {
                'name': 'firstName'
            },
            {
                'name': 'lastName'
            },
            {
                'name': 'applicationId'
            },
            {
                'name': 'phone'
            },
            {
                'name': 'email'
            },
        ]
    },
    '/aggregation/v1/customers-GET': {
        'parameters': [
            {
                'name': 'username'
            },
            {
                'name': 'type'
            },
            {
                'name': 'search'
            },
            {
                'name': 'start'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/aggregation/v1/customers/{customerId}-GET': {
        'parameters': [
            {
                'name': 'customerId'
            },
        ]
    },
    '/aggregation/v1/customers/{customerId}/application-GET': {
        'parameters': [
            {
                'name': 'customerId'
            },
        ]
    },
    '/aggregation/v1/customers/{customerId}-PUT': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'firstName'
            },
            {
                'name': 'lastName'
            },
        ]
    },
    '/aggregation/v1/customers/{customerId}-DELETE': {
        'parameters': [
            {
                'name': 'customerId'
            },
        ]
    },
    '/institution/v2/institutions/{institutionId}/branding-GET': {
        'parameters': [
            {
                'name': 'institutionId'
            },
        ]
    },
    '/institution/v2/institutions/{institutionId}-GET': {
        'parameters': [
            {
                'name': 'institutionId'
            },
        ]
    },
    '/institution/v2/certifiedInstitutions/rssd-GET': {
        'parameters': [
            {
                'name': 'search'
            },
            {
                'name': 'start'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'type'
            },
            {
                'name': 'supportedCountries'
            },
        ]
    },
    '/institution/v2/certifiedInstitutions-GET': {
        'parameters': [
            {
                'name': 'search'
            },
            {
                'name': 'start'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'type'
            },
            {
                'name': 'supportedCountries'
            },
        ]
    },
    '/institution/v2/institutions-GET': {
        'parameters': [
            {
                'name': 'search'
            },
            {
                'name': 'start'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'type'
            },
            {
                'name': 'supportedCountries'
            },
        ]
    },
    '/aggregation/v1/customers/{customerId}/payStatements-POST': {
        'parameters': [
            {
                'name': 'label'
            },
            {
                'name': 'statement'
            },
            {
                'name': 'customerId'
            },
        ]
    },
    '/analytics/payment-history/v1/customer/{customerId}-POST': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'reference-number'
            },
        ]
    },
    '/analytics/payment-history/v1/customer/{customerId}/fcra-POST': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'reference-number'
            },
        ]
    },
    '/analytics/data/v1/{obb_report_id}-GET': {
        'parameters': [
            {
                'name': 'obb_report_id'
            },
        ]
    },
    '/analytics/data/v1/{obb_report_id}/fcra-GET': {
        'parameters': [
            {
                'name': 'obb_report_id'
            },
            {
                'name': 'purpose'
            },
        ]
    },
    '/aggregation/v1/customers/{customerId}/accounts/{accountId}/owner-GET': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'accountId'
            },
        ]
    },
    '/aggregation/v3/customers/{customerId}/accounts/{accountId}/owner-GET': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'accountId'
            },
            {
                'name': 'withInsights'
            },
        ]
    },
    '/aggregation/v1/customers/{customerId}/accounts/{accountId}/details-GET': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'accountId'
            },
        ]
    },
    '/aggregation/v1/customers/{customerId}/accounts/{accountId}/availableBalance/live-GET': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'accountId'
            },
        ]
    },
    '/aggregation/v1/customers/{customerId}/accounts/{accountId}/availableBalance-GET': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'accountId'
            },
        ]
    },
    '/aggregation/v2/customers/{customerId}/accounts/{accountId}/loanDetails-GET': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'accountId'
            },
        ]
    },
    '/decisioning/v1/customers/{customerId}/portfolios/{portfolioId}-GET': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'portfolioId'
            },
        ]
    },
    '/decisioning/v1/consumers/{consumerId}/portfolios/{portfolioId}-GET': {
        'parameters': [
            {
                'name': 'consumerId'
            },
            {
                'name': 'portfolioId'
            },
        ]
    },
    '/decisioning/v1/consumers/{consumerId}/reports-GET': {
        'parameters': [
            {
                'name': 'consumerId'
            },
            {
                'name': 'purpose'
            },
        ]
    },
    '/decisioning/v1/customers/{customerId}/reports-GET': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'purpose'
            },
        ]
    },
    '/decisioning/v3/consumers/{consumerId}/reports/{reportId}-GET': {
        'parameters': [
            {
                'name': 'consumerId'
            },
            {
                'name': 'reportId'
            },
            {
                'name': 'purpose'
            },
            {
                'name': 'onBehalfOf'
            },
        ]
    },
    '/decisioning/v3/customers/{customerId}/reports/{reportId}-GET': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'reportId'
            },
            {
                'name': 'onBehalfOf'
            },
            {
                'name': 'purpose'
            },
        ]
    },
    '/aggregation/v1/partners/accessKey-POST': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'partnerId'
            },
            {
                'name': 'thirdPartyPartnerId'
            },
            {
                'name': 'products'
            },
            {
                'name': 'provenance'
            },
        ]
    },
    '/aggregation/v1/partners/accessKey/{consentReceiptId}-DELETE': {
        'parameters': [
            {
                'name': 'consentReceiptId'
            },
        ]
    },
    '/aggregation/v1/partners/accessKey/{consentReceiptId}-PUT': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'partnerId'
            },
            {
                'name': 'thirdPartyPartnerId'
            },
            {
                'name': 'products'
            },
            {
                'name': 'consentReceiptId'
            },
            {
                'name': 'provenance'
            },
        ]
    },
    '/decisioning/v2/customers/{customerId}/transactions-POST': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'toDate'
            },
            {
                'name': 'accountIds'
            },
            {
                'name': 'fromDate'
            },
            {
                'name': 'reportCustomFields'
            },
            {
                'name': 'callbackUrl'
            },
            {
                'name': 'includePending'
            },
        ]
    },
    '/aggregation/v3/customers/{customerId}/transactions-GET': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'fromDate'
            },
            {
                'name': 'toDate'
            },
            {
                'name': 'start'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'includePending'
            },
        ]
    },
    '/aggregation/v2/customers/{customerId}/transactions/{transactionId}-GET': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'transactionId'
            },
        ]
    },
    '/aggregation/v4/customers/{customerId}/accounts/{accountId}/transactions-GET': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'accountId'
            },
            {
                'name': 'fromDate'
            },
            {
                'name': 'toDate'
            },
            {
                'name': 'start'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'includePending'
            },
        ]
    },
    '/aggregation/v1/customers/{customerId}/accounts/{accountId}/transactions/historic-POST': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'accountId'
            },
        ]
    },
    '/aggregation/v1/customers/{customerId}/subscriptions/{subscriptionId}-DELETE': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'subscriptionId'
            },
        ]
    },
    '/aggregation/v1/customers/{customerId}/accounts/{accountId}/txpush-DELETE': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'accountId'
            },
        ]
    },
    '/aggregation/v1/customers/{customerId}/accounts/{accountId}/transactions-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'transactionDate'
            },
            {
                'name': 'customerId'
            },
            {
                'name': 'accountId'
            },
            {
                'name': 'status'
            },
            {
                'name': 'postedDate'
            },
        ]
    },
    '/aggregation/v1/customers/{customerId}/accounts/{accountId}/txpush-POST': {
        'parameters': [
            {
                'name': 'callbackUrl'
            },
            {
                'name': 'customerId'
            },
            {
                'name': 'accountId'
            },
        ]
    },
    '/decisioning/v2/customers/{customerId}/voa-POST': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'accountIds'
            },
            {
                'name': 'reportCustomFields'
            },
            {
                'name': 'showNsf'
            },
            {
                'name': 'fromDate'
            },
            {
                'name': 'callbackUrl'
            },
        ]
    },
    '/decisioning/v2/customers/{customerId}/voaHistory-POST': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'accountIds'
            },
            {
                'name': 'reportCustomFields'
            },
            {
                'name': 'showNsf'
            },
            {
                'name': 'fromDate'
            },
            {
                'name': 'incomeStreamConfidenceMinimum'
            },
            {
                'name': 'callbackUrl'
            },
        ]
    },
    '/decisioning/v2/customers/{customerId}/assetSummary-POST': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'accountIds'
            },
            {
                'name': 'reportCustomFields'
            },
            {
                'name': 'showNsf'
            },
            {
                'name': 'fromDate'
            },
            {
                'name': 'callbackUrl'
            },
        ]
    },
    '/decisioning/v2/customers/{customerId}/preQualVoa-POST': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'accountIds'
            },
            {
                'name': 'reportCustomFields'
            },
            {
                'name': 'showNsf'
            },
            {
                'name': 'fromDate'
            },
            {
                'name': 'callbackUrl'
            },
        ]
    },
    '/decisioning/v2/customers/{customerId}/voi-POST': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'accountIds'
            },
            {
                'name': 'reportCustomFields'
            },
            {
                'name': 'fromDate'
            },
            {
                'name': 'incomeStreamConfidenceMinimum'
            },
            {
                'name': 'callbackUrl'
            },
        ]
    },
    '/decisioning/v2/customers/{customerId}/payStatement-POST': {
        'parameters': [
            {
                'name': 'paystatementReport'
            },
            {
                'name': 'customerId'
            },
            {
                'name': 'reportCustomFields'
            },
            {
                'name': 'callbackUrl'
            },
        ]
    },
    '/decisioning/v2/customers/{customerId}/voePayroll-POST': {
        'parameters': [
            {
                'name': 'payrollData'
            },
            {
                'name': 'customerId'
            },
            {
                'name': 'reportCustomFields'
            },
            {
                'name': 'payStatementsFromDate'
            },
            {
                'name': 'marketSegment'
            },
            {
                'name': 'excludeEmpInfo'
            },
            {
                'name': 'purpose'
            },
            {
                'name': 'callbackUrl'
            },
        ]
    },
    '/decisioning/v2/customers/{customerId}/voeTransactions-POST': {
        'parameters': [
            {
                'name': 'customerId'
            },
            {
                'name': 'reportId'
            },
            {
                'name': 'accountIds'
            },
            {
                'name': 'reportCustomFields'
            },
            {
                'name': 'fromDate'
            },
            {
                'name': 'incomeStreamConfidenceMinimum'
            },
            {
                'name': 'callbackUrl'
            },
        ]
    },
    '/decisioning/v2/customers/{customerId}/voieTxVerify/withStatement-POST': {
        'parameters': [
            {
                'name': 'voieWithStatementData'
            },
            {
                'name': 'customerId'
            },
            {
                'name': 'reportCustomFields'
            },
            {
                'name': 'callbackUrl'
            },
        ]
    },
    '/decisioning/v2/customers/{customerId}/voieTxVerify/withInterview-POST': {
        'parameters': [
            {
                'name': 'voieWithInterviewData'
            },
            {
                'name': 'customerId'
            },
            {
                'name': 'accountIds'
            },
            {
                'name': 'reportCustomFields'
            },
            {
                'name': 'fromDate'
            },
            {
                'name': 'incomeStreamConfidenceMinimum'
            },
            {
                'name': 'callbackUrl'
            },
        ]
    },
    '/decisioning/v2/customers/{customerId}/voiePayroll-POST': {
        'parameters': [
            {
                'name': 'payrollData'
            },
            {
                'name': 'customerId'
            },
            {
                'name': 'reportCustomFields'
            },
            {
                'name': 'payStatementsFromDate'
            },
            {
                'name': 'marketSegment'
            },
            {
                'name': 'excludeEmpInfo'
            },
            {
                'name': 'purpose'
            },
            {
                'name': 'callbackUrl'
            },
        ]
    },
};