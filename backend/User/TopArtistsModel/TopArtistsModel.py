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

            response = TopArtistsDao.store(user_id, name, profile, rank)
            rank+=1
            artists.append(response['body'])

        return artists

