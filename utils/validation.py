import allure
from openapi_core.contrib.requests import RequestsOpenAPIRequest
from openapi_core.contrib.requests import RequestsOpenAPIResponse
from openapi_core.validation.request.validators import RequestValidator
from openapi_core.validation.response.validators import ResponseValidator
from requests import Response, Request

import specification


@allure.step('Checking the status of the response code - {status_code}')
def assert_status_code(response, status_code):
    assert response.status_code == status_code


@allure.step('Checking the expected value of the field {expectedField} with actual {responseField}')
def assert_field_equals(responseField, expectedField):
    assert responseField == expectedField


@allure.step('Checking the request schema by OAS3')
def validate_request_by_oas3(request: Request):
    openapi_request = RequestsOpenAPIRequest(request)
    validator_request = RequestValidator(specification.spec)
    result = validator_request.validate(openapi_request)
    result.raise_for_errors()
    return result.errors


@allure.step('Checking the response scheme by OAS3')
def validate_response_by_oas3(response: Response):
    openapi_request = RequestsOpenAPIRequest(response.request)
    openapi_response = RequestsOpenAPIResponse(response)
    validator_response = ResponseValidator(specification.spec)
    result = validator_response.validate(openapi_request, openapi_response)
    result.raise_for_errors()
    return result.errors


@allure.step('Checking request and response scheme by OAS3')
def assert_request_response_by_oas3(response: Response):
    validate_request_by_oas3(response.request)
    validate_response_by_oas3(response)
