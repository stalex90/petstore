import allure
import pytest

from datas.pet_data import random_pet
from utils.validation import assert_request_response_by_oas3, assert_status_code, assert_field_equals

ID = 'id'
NAME = 'name'
STATUS = 'status'
MESSAGE = 'message'
PET_NOT_FOUND = 'Pet not found'


@allure.suite('Pet store tests')
class TestClass:

    @allure.title('Getting information about a pet by id')
    @pytest.mark.get_pet
    def test_get(self, client):
        pet_data = random_pet()
        client.add_pet(pet_data)
        response = client.get_pet(pet_data[ID])

        assert_status_code(response, 200)
        assert_request_response_by_oas3(response)
        assert_field_equals(response.json()[ID], pet_data[ID])

    @allure.title('Adding pet information')
    @pytest.mark.post_pet
    def test_post(self, client):
        pet_data = random_pet()
        response = client.add_pet(pet_data)

        assert_status_code(response, 200)
        assert_request_response_by_oas3(response)
        assert_field_equals(response.json()[ID], pet_data[ID])

    @allure.title('Changing pet information')
    @pytest.mark.put_pet
    def test_put(self, client):
        pet_data = random_pet()
        client.add_pet(pet_data)
        pet_data[NAME] = 'Zhuchka'
        pet_data[STATUS] = 'pending'
        response = client.change_pet(pet_data)

        assert_status_code(response, 200)
        assert_request_response_by_oas3(response)
        assert_field_equals(response.json()[ID], pet_data[ID])
        assert_field_equals(response.json()[NAME], pet_data[NAME])
        assert_field_equals(response.json()[STATUS], pet_data[STATUS])

    @allure.title('Deleting pet information')
    @pytest.mark.delete_pet
    def test_delete(self, client):
        pet_data = random_pet()
        client.add_pet(pet_data)
        response = client.delete_pet(pet_data[ID])
        response_get = client.get_pet(pet_data[ID])

        assert_status_code(response, 200)
        assert_request_response_by_oas3(response)
        assert_field_equals(response.json()[MESSAGE], str(pet_data[ID]))
        assert_status_code(response_get, 404)
        assert_field_equals(response_get.json()[MESSAGE], PET_NOT_FOUND)
