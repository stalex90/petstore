from dataclasses import asdict

from faker import Faker

from models.category import Category
from models.pet import Pet
from models.tag import Tag

fake = Faker()


def random_pet():
    category = Category(fake.random_digit(), fake.first_name())
    tag = Tag(fake.random_digit(), "test")
    pet = Pet(fake.random_number(digits=10, fix_len=False), category, fake.language_name(), [fake.url()], [tag],
              "available")
    body = asdict(pet)
    return body


def create_pet(pet_id: int, pet_category: Category, pet_name: str, pet_photo_urls: str, pet_tags: str, pet_status: str):
    pet = Pet(pet_id, pet_category, pet_name, pet_photo_urls, pet_tags, pet_status)
    body = asdict(pet)
    return body
