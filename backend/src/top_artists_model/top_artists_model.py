import sqlite3
import base64
import simplejson as simplejson

from backend.src.top_artists_model.top_artists_dao.top_artists_dao import TopArtistsDao

class TopArtistsModel:
    @staticmethod
    def store(user_id, top_artists):
        artists = []

        for entry in top_artists['items']:
            name = entry['name']
            profile = entry['images'][0]['url']

            artists.append(
                {
                    'user_id': user_id,
                    'name': name,
                    'profile': profile
                }
            )

        try:
            return TopArtistsDao.create_connection(artists)
        except Exception as e:
            raise e
