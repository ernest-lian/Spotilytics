import json
import base64
import os

from flask import Flask, request, make_response, jsonify
from flask_cors import CORS, cross_origin
from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt
from datetime import date, datetime

from UserDao import UserDao

app = Flask(__name__)
CORS(app)
app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
jwt = JWTManager(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/login', methods = ['POST'])
def login():
    '''
    This method will log a user into the system
    :return:
    200 Response OK

    {
        'response': 200,
        'user_id': '2fae1640-e821-492c-8003-6b1e7ad98311'
    }

    400 Response BAD REQUEST
    {
        'response': 200,
    }

    '''

    # Extracts the user_name and user_password from the payload body
    data = request.data.decode('utf-8')
    user_name = json.loads(data)['user_name']
    user_password = json.loads(data)['user_password']

    # Validates the user_name and user_password values from the payload body

    # Validates if the user exists
    user_dao = UserDao(user_name, user_password)
    user_dao.login()

    print('user_name: ' + user_name)
    print('user_password: ' + user_password)

    response = jsonify({'response': 200})

    return response

@app.route('/dashboard', methods = ['GET'])
def get_dashboard():
    '''

    '''

    # Extracts the user_name from the query parameters
    user_name = request.args.get('user_name')

    # Validate the user_name from the query parameters
    print(user_name)

    # Return the user_name, last 5 played spotify songs, lsat 5 played spotify artist

    response = jsonify({'response': 200})

    return response

@app.route('/analytics/all', methods = ['GET'])
def get_all_analytics():
    '''

    :return:
    '''

    # Extracts the user_name from the query parameters
    user_name = request.args.get('user_name')


    # Return their total play time

    response = jsonify({'response': 200})

    return response

@app.route('/analytics/all', methods = ['GET'])
def get_predictions():
    '''

    :return:
    '''

    response = jsonify({'response': 200})

    return response


@app.route('/secret', methods = ['GET'])
@jwt_required
def get_secret():
    '''
    This method will test the access token implementation
    :return:
    200 Response OK

    {
        'response': 10
    }

    '''

    return {
        'response': 10
    }

@app.route('/token/refresh', methods = ['POST'])
@jwt_refresh_token_required
def token_refresh():
    '''
    This method will renew the access token given a refresh token
    :return:
    200 Response OK

    {
        'response': 10
    }

    '''

    current_user = get_jwt_identity()
    access_token = create_access_token(identity=current_user)
    return {'access_token': access_token}


if __name__ == '__main__':
    app.run()