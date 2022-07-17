import pytest
from utils.api import PetApi
import os


@pytest.fixture(scope="module")
def client():
    return PetApi(os.environ.get("BASE_URL", "https://petstore.swagger.io"))
