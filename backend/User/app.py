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

# Dao imports
from backend.User.UserDao.UserDao import UserDao

app = Flask(__name__)
CORS(app)
app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
jwt = JWTManager(app)

@app.route('/', methods = ['get'])
def hello_world():
    return 'Hello, World!'


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
        'response': 200,
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
        user_response = UserDao.login(user_name, name, user_profile)
        user_id = user_response['body']['user_id']


        # Processes the user's most played artists
        top_artists_response = TopArtistsModel.store(user_id, sp.current_user_top_artists(5,0,'long_term'))
        user_response['body']['top_artists'] = top_artists_response

        # Process the user's most played songs
        top_tracks_response = TopSongsModel.store(user_id, sp.current_user_top_tracks(5,0,'long_term'))
        user_response['body']['top_tracks'] = top_tracks_response




        most_played_tracks = []

        popular_track = {}
        most_popular = 0
        average_popularity = 0

        for entry in sp.current_user_top_tracks(20, 0, 'long_term')['items']:
            # print('entry: ', entry)
            most_played_tracks.append(entry['uri'])
            current_popularity = sp.track(entry['id'])['popularity']
            average_popularity+= current_popularity
            if current_popularity >= most_popular:
                most_popular = current_popularity
                popular_track['title']= entry['name']
                popular_track['artist'] = entry['album']['artists'][0]['name']
                popular_track['cover'] = entry['album']['images'][0]['url']


        popular_track['popular'] = most_popular
        popular_track['average'] = (average_popularity / 20)


        analytics = {}
        longest_duration = 0
        longest_song_uri = ''
        average_duration = 0

        fastest_tempo = 0
        fastest_song_uri = ''
        average_tempo = 0

        most_energetic = 0
        energetic_song_uri = ''
        average_energy = 0

        for entry in sp.audio_features(most_played_tracks):
            if entry['duration_ms'] >= longest_duration:
                longest_duration = entry['duration_ms']
                longest_song_uri = entry['id']

            if entry['tempo'] >= fastest_tempo:
                fastest_tempo = entry['tempo']
                fastest_song_uri = entry['id']

            if entry['energy'] >= most_energetic:
                most_energetic = entry['energy']
                energetic_song_uri = entry['id']

            average_duration+=entry['duration_ms']
            average_tempo+=entry['tempo']
            average_energy+=entry['energy']

        longest_track = {}
        longest_track['title'] = sp.track(longest_song_uri)['name']
        longest_track['artist'] = sp.track(longest_song_uri)['artists'][0]['name']
        longest_track['cover'] = sp.track(longest_song_uri)['album']['images'][0]['url']
        longest_track['duration'] = int(longest_duration/1000)
        longest_track['average'] = int((average_duration/20)/1000)

        fastest_track = {}
        fastest_track['title'] = sp.track(fastest_song_uri)['name']
        fastest_track['artist'] = sp.track(fastest_song_uri)['artists'][0]['name']
        fastest_track['cover'] = sp.track(fastest_song_uri)['album']['images'][0]['url']
        fastest_track['speed'] = int(fastest_tempo)
        fastest_track['average'] = int(average_tempo/20)

        energetic_track = {}
        energetic_track['title'] = sp.track(energetic_song_uri)['name']
        energetic_track['artist'] = sp.track(energetic_song_uri)['artists'][0]['name']
        energetic_track['cover'] = sp.track(energetic_song_uri)['album']['images'][0]['url']
        energetic_track['energy'] = most_energetic*100
        energetic_track['average'] = (average_energy/20)*100

        analytics['longest_track'] = longest_track
        analytics['energetic_track'] = energetic_track
        analytics['fastest_track'] = fastest_track
        analytics['popular_track'] = popular_track

        user_response['body']['analytics'] = analytics

        print('user_response')
        print(user_response)
        return user_response

# https://www.musical-u.com/learn/rhythm-tips-for-identifying-music-genres-by-ear/

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
