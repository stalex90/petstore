import os

import allure
import requests

from utils.attachment import attach_request_url_and_response_body, attach_request_and_response_body


class PetApi:

    def __init__(self, base_url):
        self.base_url = base_url

    @allure.step('Sending a request for get information about a pet by id')
    def get_pet(self, id: int):
        response = requests.get(f'{self.base_url}/v2/pet/{str(id)}',
                                headers={'accept': 'application/json', 'Content-Type': 'application/json'})
        attach_request_url_and_response_body(response)
        return response

    @allure.step('Sending a request to add information about a pet')
    def add_pet(self, body: dict):
        response = requests.post(f'{self.base_url}/v2/pet', json=body,
                                 headers={'accept': 'application/json', 'Content-Type': 'application/json'})
        attach_request_and_response_body(response)
        return response

    @allure.step('Sending a request to change pet information')
    def change_pet(self, body: dict):
        response = requests.put(f'{self.base_url}/v2/pet', json=body,
                                headers={'accept': 'application/json', 'Content-Type': 'application/json'})
        attach_request_and_response_body(response)
        return response

    @allure.step('Sending a request to delete pet information')
    def delete_pet(self, id: int):
        response = requests.delete(f'{self.base_url}/v2/pet/{str(id)}',
                                   headers={'accept': 'application/json', 'Content-Type': 'application/json'})
        attach_request_url_and_response_body(response)
        return response
