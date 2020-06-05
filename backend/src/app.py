import sys
import json

# Flask imports
from flask import Flask, request
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, jwt_refresh_token_required, get_jwt_identity

# Spotipy imports
import spotipy
import spotipy.util as util

# Model imports
from backend.src.top_artists_model.top_artists_model import TopArtistsModel
from backend.src.top_tracks_model.top_tracks_model import TopTracksModel
from backend.src.analytics_model.analytics_model import AnalyticsModel
from backend.src.recommendations_model.recommendations_model import RecommendationsModel
from backend.src.playlist_model.playlist_model import PlaylistModel
from backend.src.user_model.user_model import UserModel

# Validation imports
from backend.src.validations.validations import validate_playlist

app = Flask(__name__)
CORS(app)
app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
jwt = JWTManager(app)


@app.route('/login', methods = ['POST'])
def login_spotify():
    '''
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

    '''
    scope = 'user-read-recently-played user-top-read'

    with app.app_context():

        if len(sys.argv) > 1:
            username = sys.argv[1]
        else:
            print("Usage: %s username" % (sys.argv[0],))
            sys.exit()

        token = util.prompt_for_user_token("ernest.lian97", scope, client_id='db3cb208eea947b9b5115eaba840402e',
                                           client_secret='7b4727b89b3f463985624fe4c145bc97',
                                           redirect_uri='https://example.com/callback/')

        sp = spotipy.Spotify(auth=token)
        sp.trace = False

        try:
            # Logs in the user
            me = sp.me()
            response = UserModel.create_user(me)
            user_id = response['body']['id']

            # Processes the user's most played artists
            top_artists_response = TopArtistsModel.store(user_id, sp.current_user_top_artists(5, 0, 'long_term'))
            response['body']['top_artists'] = top_artists_response

            # Process the user's most played tracks
            top_tracks_response = TopTracksModel.store(user_id, sp.current_user_top_tracks(5, 0, 'long_term'))
            response['body']['top_tracks'] = top_tracks_response

            # Fetch the user's top played tracks
            top_tracks = []
            for entry in sp.current_user_top_tracks(20, 0, 'long_term')['items']:
                top_tracks.append(entry['uri'])

            # Process the user's most played tracks analytics
            response['body']['analytics'] = AnalyticsModel.store_analytics(user_id, sp, top_tracks)

            # Get the user's recommendations
            response['body']['recommendations'] = RecommendationsModel.store_predictions(user_id, sp, top_tracks)
        except Exception:
            return {'status_code': 400, 'error': 'An error occurred'}

        response['response'] = 200

        print('response: ', response)
        return response


@app.route('/playlist', methods=['POST'])
def create_playlist():
    '''
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

    '''
    scope = 'user-read-recently-played user-top-read'

    with app.app_context():

        if len(sys.argv) > 1:
            username = sys.argv[1]
        else:
            print("Usage: %s username" % (sys.argv[0],))
            sys.exit()

        user_name = 'ernest.lian97'

        token = util.prompt_for_user_token("ernest.lian97", scope, client_id='db3cb208eea947b9b5115eaba840402e',
                                           client_secret='7b4727b89b3f463985624fe4c145bc97',
                                           redirect_uri='https://example.com/callback/')

        sp = spotipy.Spotify(auth=token)


        data = request.data.decode('utf-8')

        # Validate playlist information
        try:
            validated_data = validate_playlist(json.loads(data))
        except Exception:
            return {'status_code': 400, 'message': 'Playlist name must be a string of at least length 1'}

        # Create playlist
        try:
            response = PlaylistModel.create(sp, validated_data, user_name)
        except Exception:
            return {'status_code': 400, 'error': 'An error occurred while creating your playlist'}

        return response


if __name__ == '__main__':
    login_spotify()
