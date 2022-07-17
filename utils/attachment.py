import allure
from requests import Response


def attach_request_url_and_response_body(response: Response):
    allure.attach(f'{response.request.url}\n\n{response.request.headers}', 'Request', allure.attachment_type.TEXT)
    allure.attach(f'{response.headers}\n\n{response.text}', 'Response', allure.attachment_type.TEXT)


def attach_request_and_response_body(response: Response):
    allure.attach(f'{response.request.url}\n\n{response.request.headers}\n\n{response.request.body}', 'Request',
                  allure.attachment_type.TEXT)
    allure.attach(f'{response.headers}\n\n{response.text}', 'Response', allure.attachment_type.TEXT)
