from flask import (
    Flask,
    session,
    redirect,
    url_for,
    request,
    render_template,
    jsonify,
    Blueprint,
)
import requests
from config import config_petfinder

api_petfinder = Blueprint("api_petfinder", __name__)


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


def search_breeds(search):
    pass


"""
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST','GET'])
def login()

@app.route("/dog/breeds/", methods=["POST","GET"])
def dog_breeds():
    access_token = get_access_token()
    dogs = get_dog_breeds(access_token)
    if request.method == "POST":
        breeds_search = request.form["search"]
        session["breeds_search"] = breeds_search
        return redirect("/")
    else:
        return render_template('test.html', content=['1','2'])


"""
