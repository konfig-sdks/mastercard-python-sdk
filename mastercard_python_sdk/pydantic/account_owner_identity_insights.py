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


class AccountOwnerIdentityInsights(BaseModel):
    # True if the email address is valid.
    is_email_valid: typing.Optional[bool] = Field(None, alias='isEmailValid')

    # Count of days since the email was first observed in Ekata's Identity Network. If the email has not been observed before, first_seen_days will be 0.
    email_first_seen_days: typing.Optional[typing.Union[int, float]] = Field(None, alias='emailFirstSeenDays')

    # Returns a date that the email domain was created.
    email_domain_creation_date: typing.Optional[str] = Field(None, alias='emailDomainCreationDate')

    # The match status between the input name and the queried entity. * not found * match * no-match
    email_to_name: typing.Optional[str] = Field(None, alias='emailToName')

    # True if the IP address is considered risky, based on multiple IP data points and velocity calculations.
    ip_risk: typing.Optional[typing.Union[int, float]] = Field(None, alias='ipRisk')

    # Comprehensive risk score associated with an IP address, with a higher score indicating a riskier IP address. A number between 0 and 1 rounded to three decimal places.
    ip_risk_score: typing.Optional[typing.Union[int, float]] = Field(None, alias='ipRiskScore')

    # Count of days since the IP address was last observed in Ekata's Identity Network. If the IP address has not been observed before, IpLastSeenDays will be 0.
    ip_last_seen_days: typing.Optional[typing.Union[int, float]] = Field(None, alias='ipLastSeenDays')

    # The ISO-3166 alpha-2 country code associated with the geolocation of the IP address.
    ip_geolocation_country_code: typing.Optional[str] = Field(None, alias='ipGeolocationCountryCode')

    # More granular detail about the IP address location.
    ip_geolocation_subdivision: typing.Optional[str] = Field(None, alias='ipGeolocationSubdivision')

    # The distance (in miles) between the IP address and the closest physical address associated with the phone number.
    ip_phone_distance: typing.Optional[typing.Union[int, float]] = Field(None, alias='ipPhoneDistance')

    # The distance (in miles) between the IP address and the physical address.
    ip_address_distance: typing.Optional[typing.Union[int, float]] = Field(None, alias='ipAddressDistance')

    # True if the phone number is valid.
    is_phone_valid: typing.Optional[bool] = Field(None, alias='isPhoneValid')

    # The line type of the phone number. * landline - traditional wired phone line. * fixed-voip - VoIP-based fixed line phones. * mobile - wireless phone line. * voicemail - voicemail-only service. * toll-free - callee pays for call. * premium - caller pays a premium for the call-e.g., 976 area code. * non-fixed-voip - Skype, for example * other - anything that does not match the previous categories.
    phone_line_type: typing.Optional[str] = Field(None, alias='phoneLineType')

    # The company that provides voice and/or data services for the phone number. Carriers are returned at the MVNO level.
    phone_carrier: typing.Optional[str] = Field(None, alias='phoneCarrier')

    # The ISO-3166 alpha-2 country code associated with the phone number.
    phone_country_code: typing.Optional[str] = Field(None, alias='phoneCountryCode')

    # Count of days since the phone was last observed in Ekata's Identity Network. If the phone has not been observed before, `phoneLastSeenDays` will be 0.
    phone_last_seen_days: typing.Optional[typing.Union[int, float]] = Field(None, alias='phoneLastSeenDays')

    # Count of days since the combination of phone and email was first observed in Ekata's Identity Network. If that combination has not been observed before, `phoneEmailFirstSeenDays` will be 0.
    phone_email_first_seen_days: typing.Optional[typing.Union[int, float]] = Field(None, alias='phoneEmailFirstSeenDays')

    # The match status between the input name and the queried entity.  * not-found  * match  * no-match
    phone_to_name: typing.Optional[str] = Field(None, alias='phoneToName')

    # The match status between the input phone and the queried entity. * match - Phone location matches input address line 1, address line 2, city, state, and postal code.  * postal-match - Phone location postal code matches input address postal code.  * zip4-match - Phone location postal code zip+4 matches input address postal code zip+4.  * city-state-match - Phone location city and state matches input address city and state. * metro-match - Phone location is in the same metro area as input address.  * country-match - Phone location country matches input address country.  * no-match - Phone location does not match input address.
    phone_to_address: typing.Optional[str] = Field(None, alias='phoneToAddress')

    # The most granular level to which the address could be validated. Ex. If the address was only valid to the city level (but not to the house level), it would return “valid_to_city”.   * missing_address - An input address was not provided.    * invalid - The input address is not valid.    * valid - The input address is valid.    * valid_to_country - The input address could only be validated to the country level. This means the country of the input address is valid, but the other elements of the input address were unable to be confirmed as valid or invalid.    * valid_to_city - The input address was validated to the city level. This means the country, state, city, and postal code of the input address are valid, but the street, house number, and subpremise of the input address were unable to be confirmed as valid or invalid.    * valid_to_street - The input address was validated to the street level. This means the country, state, city, postal code, and street of the input address are valid, but the house number and subpremise of the input address were unable to be confirmed as valid or invalid.      * valid_to_house_number - The input address was validated to the street and house number level. This means the country, state, city, postal code, street, and house number of the input address are valid, but the subpremise of the input address was unable to be confirmed as valid or invalid.      * valid_to_house_number_missing_apt - The input address was validated to the street and house number level. This means the country, state, city, postal code, street, and house number of the input address are valid, but the subpremise of the input address was missing and thus unable to be confirmed as valid or invalid.
    address_validity_level: typing.Optional[typing.Union[int, float]] = Field(None, alias='addressValidityLevel')

    # The match status between the input name and the queried entity. * not-found * match * no-match
    address_to_name: typing.Optional[str] = Field(None, alias='addressToName')

    # Comprehensive network score built on behavioral insights such as velocity, popularity, volatility, and age of an attribute, with a higher score indicating a riskier account sign-up. A number between 0 and 1 rounded to three decimal places.
    identity_network_score: typing.Optional[typing.Union[int, float]] = Field(None, alias='identityNetworkScore')

    # Comprehensive identity risk score with a higher score indicating a riskier account sign-up.
    identity_risk_score: typing.Optional[typing.Union[int, float]] = Field(None, alias='identityRiskScore')

    warnings: typing.Optional[typing.List[str]] = Field(None, alias='warnings')
    class Config:
        arbitrary_types_allowed = True
