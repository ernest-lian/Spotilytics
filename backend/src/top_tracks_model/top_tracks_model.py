import sqlite3
import base64
import simplejson as simplejson

from backend.src.top_tracks_model.top_tracks_dao.top_tracks_dao import TopTracksDao

class TopTracksModel:
    @staticmethod
    def store(user_id, top_tracks):
        tracks = []

        for entry in top_tracks['items']:
            title = entry['name']
            artist = entry['artists'][0]['name']
            cover = entry['album']['images'][0]['url']
            tracks.append({
                'user_id': user_id,
                'title': title,
                'artist': artist,
                'cover': cover
            })

        try:
            return TopTracksDao.create_connection(tracks)
        except Exception as e:
            raise e
