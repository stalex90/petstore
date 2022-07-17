from yaml import load
from openapi_core import create_spec

with open('petstore.yaml', 'r') as spec_file:
    spec_dict = load(spec_file)

spec = create_spec(spec_dict)
