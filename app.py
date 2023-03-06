# This example uses the Evervault Python SDK.
import evervault
from flask import Flask, request, render_template, jsonify
import os
from dotenv import load_dotenv, find_dotenv
import requests

load_dotenv(find_dotenv())

app = Flask(__name__)

@app.route("/")
def index():
    '''
    A function that returns the index page and passes in the Ev credentials.
    '''
    github_client_id=os.environ.get("GITHUB_CLIENT_ID")

    return render_template('index.html', github_client_id=github_client_id)

if __name__ == '__main__':
   app.run()

@app.route("/callback", methods=['POST', 'GET'])
def decrypt():
    '''
    A function that calls the Evervault Function and returns the decrypted data.
    '''
    evervault.init(
	api_key=os.environ.get("EVERVAULT_API_KEY"),
	enable_outbound_relay=True
    )

    print(os.environ.get("EVERVAULT_API_KEY"))
    
    session_code = request.args.get('code')
    data = {'client_id': os.environ.get("GITHUB_CLIENT_ID"), 'client_secret': os.environ.get("GITHUB_CLIENT_SECRET"), 'code': session_code}
    headers = {'accept': 'application/json'}
    ACCESS_TOKEN_URL='https://github.com/login/oauth/access_token'
    result = requests.post(ACCESS_TOKEN_URL, data=data, headers=headers)
    access_token = result.json()["access_token"]

    email_headers={"Authorization": "Bearer " + access_token}
    params = {"accept": "application/vnd.github+json"}
    get_user_data = requests.get('https://api.github.com/user', params=params, headers=email_headers)
    user_data = get_user_data.json()

    return jsonify({'name': user_data['name'], 'email': user_data['email'], 'token': access_token})