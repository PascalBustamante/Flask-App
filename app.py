from flask import Flask, session, redirect, url_for, request, render_template,jsonify
import requests

app = Flask(__name__)

def get_access_token():
    token_url= 'https://api.petfinder.com/v2/oauth2/token'
    oauth_data = {
        "grant_type": "client_credentials",
        "client_id": "I9W61HSD43LqdvfdyoeLaYFvD76OZuKma8wfs0f0yeddur54Gg",
        "client_secret": "zEibYWOgIPGwZk058QT21Xfzx67OGgpNAQfeYQcl"
    }
    response = requests.post(url=token_url, data=oauth_data)
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

if __name__ == '__main__':
    app.run(debug=True)

