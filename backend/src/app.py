import sys
import json
import sqlite3

from flask import Flask, request
from flask_cors import CORS

import spotipy
import spotipy.util as util

import backend.src.dashboard_model.dashboard_model as DashboardModel
import backend.src.analytics_model.analytics_model as AnalyticsModel
import backend.src.recommendations_model.recommendations_model as RecommendationsModel
import backend.src.users_model.users_model as UsersModel
from backend.src.validations.validations import validate_playlist
from backend.src.constants.constants import database_name, number_of_tracks, number_of_artists, long_term

app = Flask(__name__)
CORS(app)


def init_db():
    conn = sqlite3.connect(database_name)
    with app.open_resource('schema.sql') as f:
        conn.executescript(f.read().decode('utf8'))

@app.route('/login', methods=['POST'])
def login_spotify():
    """
    This method will log the user in and process all analytics and recommendations
    :return:
    200 Response OK

    {
        'status_code': 200,
        'body': {
            'message': 'User already registered',
            'name': 'Ernest Lian',
            'display_picture': 'https://i.scdn.co/image/ab6775700000ee8526a6ebbfdc7621dece89f2d0',
            'user_id': '8c792b26-a08a-11ea-ac0e-acbc3282522f',
            'top_artists': [
                {
                    'user_id': '8c792b26-a08a-11ea-ac0e-acbc3282522f',
                    'name': 'Ariana Grande',
                    'profile': 'https://i.scdn.co/image/b1dfbe843b0b9f54ab2e588f33e7637d2dab065a',
                    'rank': 1
                }
            ],
            'top_tracks': [
                {
                    'user_id': '8c792b26-a08a-11ea-ac0e-acbc3282522f',
                    'title': 'better off',
                    'artist': 'Ariana Grande',
                    'cover': 'https://i.scdn.co/image/ab67616d0000b273c3af0c2355c24ed7023cd394',
                    'rank': 1
                }
            'analytics': {
                'popular_track': {
                    'title': 'idontwannabeyouanymore',
                    'artist': 'Billie Eilish',
                    'cover': 'https://i.scdn.co/image/ab67616d0000b273a9f6c04ba168640b48aa5795',
                    'popular': 82,
                    'average': 58.8
                },
                'fastest_track': {
                    'title': 'Get Free',
                    'artist': 'Lana Del Rey',
                    'cover': 'https://i.scdn.co/image/ab67616d0000b27395e2fd1accb339fa14878190',
                    'speed': 203,
                    'average': 127
                },
                'energetic_track': {
                    'title': 'Radio',
                    'artist': 'Lana Del Rey',
                    'cover': 'https://i.scdn.co/image/ab67616d0000b273a1c37f3fd969287c03482c3b',
                    'energy': 84.1,
                    'average': 47.88
                },
                'longest_track': {
                    'title': 'Get Free',
                    'artist': 'Lana Del Rey',
                    'cover': 'https://i.scdn.co/image/ab67616d0000b27395e2fd1accb339fa14878190',
                    'duration': 334,
                    'average': 228
                }
            },
            'recommendations': [
                {
                    'title': 'Trap Queen',
                    'artist': 'Fetty Wap',
                    'cover': 'https://i.scdn.co/image/ab67616d0000b273de6bd09b07e2b4af4e409f6c',
                    'uri': 'spotify:track:2d8JP84HNLKhmd6IYOoupQ'
                }
            ]
        }
    }
    """

    init_db()
    scope = 'user-read-recently-played user-top-read'

    with app.app_context():

        if len(sys.argv) > 1:
            username = sys.argv[1]
        else:
            print("Usage: %s username" % (sys.argv[0],))
            sys.exit()

        token = util.prompt_for_user_token(username, scope, client_id='CLIENT_ID_HERE',
                                           client_secret='CLIENT_SECRET_HERE',
                                           redirect_uri='https://example.com/callback/')

        sp = spotipy.Spotify(auth=token)
        sp.trace = False

        try:

            # Logs in the user
            me = sp.me()
            response = UsersModel.create_user(me)
            user_id = response['body']['id']

            # Processes the user's most played artists
            top_artists_response = DashboardModel.store_top_artists(user_id, sp.current_user_top_artists(number_of_artists, 0, long_term))
            response['body']['top_artists'] = top_artists_response

            # Process the user's most played tracks
            top_tracks_response = DashboardModel.store_top_tracks(user_id, sp.current_user_top_tracks(number_of_artists, 0, long_term))
            response['body']['top_tracks'] = top_tracks_response

            # Fetch the user's top played tracks
            top_tracks = []
            for entry in sp.current_user_top_tracks(number_of_tracks, 0, long_term)['items']:
                top_tracks.append(entry['uri'])

            # Process the user's most played tracks analytics
            response['body']['analytics'] = AnalyticsModel.store_analytics(user_id, sp, top_tracks)

            # Get the user's recommendations
            response['body']['recommendations'] = RecommendationsModel.store_recommendations(user_id, sp, top_tracks)
        except Exception:
            return {
                        'status_code': 400,
                        'error': 'An error occurred'
                    }

        response['response'] = 200
        return response


@app.route('/playlist', methods=['POST'])
def create_playlist():
    """
    This method will create a playlist for the user
    :return:
    200 Response OK

    {
        'response': 200,
        'message': 'Playlist successfully created'
    }

    400 Response BAD REQUEST
    {
        'response': 400,
        'message': 'Please enter a valid string of at least length 1'
    }

    """

    scope = 'user-read-recently-played user-top-read'

    with app.app_context():
        username = 'USERNAME_HERE'

        token = util.prompt_for_user_token(username, scope, client_id='CLIENT_ID_HERE',
                                           client_secret='CLIENT_SECRET_HERE',
                                           redirect_uri='https://example.com/callback/')

        sp = spotipy.Spotify(auth=token)

        data = request.data.decode('utf-8')

        # Validate playlist payload
        try:
            validated_data = validate_playlist(json.loads(data))
        except Exception:
            return {'status_code': 400, 'message': 'Playlist name must be a string of at least length 1'}

        # Create and store playlist
        try:
            response = RecommendationsModel.store_playlist(sp, validated_data, username)
        except Exception:
            return {'status_code': 400, 'error': 'An error occurred while creating your playlist'}

        return response


if __name__ == '__main__':
    login_spotify()
