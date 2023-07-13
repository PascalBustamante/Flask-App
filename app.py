from flask import Flask, session, redirect, url_for, request, render_template
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

def get_german_shepherds(access_token):
    url = "https://api.petfinder.com/v2/types/dog/breeds"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    data = response.json()
    breeds = data["breeds"]


    return breeds

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/german-shepherds")
def german_shepherds():
    access_token = get_access_token()
    dogs = get_german_shepherds(access_token)
    return {"dogs": dogs}


if __name__ == '__main__':
    app.run(debug=True)

