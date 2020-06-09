from backend.machine_learning.model import predict_genre
from backend.src.recommendations_model.recommendations_dao.recommendations_dao import RecommendationsDao
from backend.src.constants.constants import all_genres


def store_recommendations(user_id, sp, top_tracks):
    predict_matrix = []
    genre_dict = {}
    store_tracks = []

    # Pre-processing data to train the model
    audio_features = sp.audio_features(top_tracks)
    for track in audio_features:
        track_info = [track['tempo'], track['energy']]
        predict_matrix.append(track_info)

    # Accumulate the most common genre from the model's result
    for genre in predict_genre(predict_matrix):
        current_genre = round(genre)
        if current_genre in genre_dict.keys():
            genre_dict[current_genre]+=1
        else:
            genre_dict[current_genre]=1

    # Fetch the tracks classified under the specific genre
    for track in sp.recommendations(seed_genres=[all_genres[max(genre_dict, key=genre_dict.get)]])['tracks']:
        store_tracks.append(
            {
                'title': track['name'],
                'artist': track['artists'][0]['name'],
                'cover': track['album']['images'][0]['url'],
                'uri': track['uri']
            })

    try:
        # Store the recommendations
        recommendations_dao = RecommendationsDao()
        return recommendations_dao.store_recommendations(user_id, store_tracks)
    except Exception as e:
        raise e


def store_playlist(sp, validated_data, user_name):
    # Create a new playlist based on the user's input
    playlist_name = 'Spotilytics - ' + validated_data['playlist_name']
    new_playlist = sp.user_playlist_create("ernest.lian97", playlist_name)

    try:
        # Fetch the recommendations and store them in the playlist
        recommendations_dao = RecommendationsDao()
        recommendations_response = recommendations_dao.fetch_recommendations(user_name)
        sp.user_playlist_add_tracks("ernest.lian97", new_playlist['id'], recommendations_response)
        return {'status_code': 200, 'message': 'Playlist successfully created'}
    except Exception as e:
        raise e
