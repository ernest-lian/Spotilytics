import operator
from backend.machine_learning.model import predict_genre
from backend.src.recommendations_model.recommendations_dao.recommendations_dao import RecommendationsDao
from backend.src.constants.constants import all_genres

class RecommendationsModel:
    @staticmethod
    def store_predictions(user_id, sp, top_tracks):
        predict_matrix = []
        genre_dict = {}
        store_tracks = []

        audio_features = sp.audio_features(top_tracks)

        for track in audio_features:
            track_info = [track['tempo'], track['energy']]
            predict_matrix.append(track_info)

        for genre in predict_genre(predict_matrix):
            current_genre = round(genre)
            if current_genre  in genre_dict.keys():
                genre_dict[current_genre ]+=1
            else:
                genre_dict[current_genre ]=1

        for track in sp.recommendations(seed_genres=[all_genres[max(genre_dict, key=genre_dict.get)]])['tracks']:
            store_tracks.append(
                {
                    'title': track['name'],
                    'artist': track['artists'][0]['name'],
                    'cover': track['album']['images'][0]['url'],
                    'uri': track['uri']
                })

        try:
            return RecommendationsDao.create_connection(user_id, store_tracks)
        except Exception as e:
            raise e
