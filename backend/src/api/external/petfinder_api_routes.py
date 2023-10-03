from flask import Blueprint
import requests


from api.external.dto import DogDto
from api.external.config import config_petfinder


petfinder_api_routes = Blueprint(
    "petfinder_api_routes", __name__
)  ##this might not be needed


def get_access_token():
    config = [config_petfinder.token_url, config_petfinder.oauth_data]
    response = requests.post(url=config[0], data=config[1])
    access_token = response.json()["access_token"]
    return access_token


def get_dog_breeds(access_token):
    url = "https://api.petfinder.com/v2/types/dog/breeds"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    data = response.json()
    _breeds = data["breeds"]
    breed = []

    for x in _breeds:
        breed.append(x["name"])

    return breed


def fetch_dogs(access_token):
    url = "https://api.petfinder.com/v2/types/dog"
    headers = {"Authorization": f"Bearer {access_token}"}

    response = requests.get(url, headers=headers)
    data = response.json()

    dogs = []

    for animal in data["animals"]:
        if animal["type"] != "Dog":
            continue

        dog = DogDto(
            id=animal["id"],
            type=animal["type"],
            breeds=animal["breeds"],
            colors=animal["colors"],
            age=animal["age"],
            gender=animal["gender"],
            size=animal["size"],
            photos=[photo["url"] for photo in animal["photos"]],
            contact=animal["contact"],
        )
        dogs.append(dog)

    return dogs


def search_breeds(search):
    pass
