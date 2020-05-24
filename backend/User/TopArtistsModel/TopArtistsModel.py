import sqlite3
import base64
import simplejson as simplejson

from backend.User.TopArtistsModel.TopArtistsDao.TopArtistsDao import TopArtistsDao

class TopArtistsModel:
    @staticmethod
    def store(user_id, top_artists):
        rank = 1
        artists = []

        for entry in top_artists['items']:
            name = entry['name']
            profile = entry['images'][0]['url']

            artists.append(
                {
                    'user_id': user_id,
                    'name': name,
                    'profile': profile,
                    'rank': rank
                }
            )
            rank += 1

        stored_artists = TopArtistsDao.create_connection(artists)
        return stored_artists

