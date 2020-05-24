import sys

# Flask imports
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, jwt_refresh_token_required, get_jwt_identity

# Spotipy imports
import spotipy
import spotipy.util as util

# Model imports
from backend.User.TopArtistsModel.TopArtistsModel import TopArtistsModel
from backend.User.TopSongsModel.TopSongsModel import TopSongsModel
from backend.User.AnalyticsModel.AnalyticsModel import AnalyticsModel
from backend.User.PredictModel.PredictModel import PredictModel
from backend.machine_learning.model import predict_genre

# Dao imports
from backend.User.UserDao.UserDao import UserDao

app = Flask(__name__)
CORS(app)
app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
jwt = JWTManager(app)


@app.route('/login', methods = ['POST'])
# @jwt_required
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
        'response': 400,
    }

    '''

    response = login_spotify()

    return response

# @jwt_required
def login_spotify():
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

        # Logs in the user
        me = sp.me()
        user_name = me['id']
        name = me['display_name']
        user_profile = me['images'][0]['url']
        user_response = UserDao.create_connection(user_name, name, user_profile)
        user_id = user_response['body']['user_id']


        # Processes the user's most played artists
        top_artists_response = TopArtistsModel.store(user_id, sp.current_user_top_artists(5,0,'long_term'))
        user_response['body']['top_artists'] = top_artists_response

        # Process the user's most played tracks
        top_tracks_response = TopSongsModel.store(user_id, sp.current_user_top_tracks(5,0,'long_term'))
        user_response['body']['top_tracks'] = top_tracks_response

        # Fetch the user's top played tracks
        top_tracks = []
        for entry in sp.current_user_top_tracks(20, 0, 'long_term')['items']:
            top_tracks.append(entry['uri'])

        # Process the user's most played tracks analytics
        user_response['body']['analytics'] = AnalyticsModel.store_analytics(user_id, sp, top_tracks)

        # Get the user's predictions
        user_response['body']['recommendations'] = PredictModel.store_predictions(user_id, sp, top_tracks)

        return user_response


@app.route('/playlist', methods = ['POST'])
def create_playlist():
    '''
    This method will create a playlist for the user
    :return:
    200 Response OK

    {
        'response': 200,
        'user_id': '2fae1640-e821-492c-8003-6b1e7ad98311'
    }

    400 Response BAD REQUEST
    {
        'response': 400,
    }

    '''


    return {'response': 200}


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
    login_spotify()
