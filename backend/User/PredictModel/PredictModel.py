import operator
from backend.machine_learning.model import predict_genre
from backend.User.PredictModel.PredictDao.PredictDao import PredictDao

class PredictModel:
    @staticmethod
    def store_predictions(user_id, sp, top_tracks):
        predict_matrix = []
        genre_dict = {}
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

        # Move to constants
        all_genres = {1: 'pop', 2: 'r-n-b', 3: 'k-pop', 4: 'hip-hop', 5: 'classical', 6: 'indie', 7: 'country'}

        store_tracks = []
        for track in sp.recommendations(seed_genres=[all_genres[max(genre_dict, key=genre_dict.get)]])['tracks']:
            store_tracks.append(
                {
                    'title': track['name'],
                    'artist': track['artists'][0]['name'],
                    'cover': track['album']['images'][0]['url']
                })

        recommended_tracks = PredictDao.create_connection(user_id, store_tracks)
        return recommended_tracks