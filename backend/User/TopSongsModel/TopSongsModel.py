import sqlite3
import base64
import simplejson as simplejson

from backend.User.TopSongsModel.TopSongsDao.TopSongsDao import TopSongsDao

class TopSongsModel:
    @staticmethod
    def store(user_id, top_tracks):
        rank = 1
        tracks = []

        for entry in top_tracks['items']:
            title = entry['name']
            artist = entry['artists'][0]['name']
            cover = entry['album']['images'][0]['url']
            response = TopSongsDao.store(user_id, title, artist, cover, rank)

            rank += 1
            tracks.append(response['body'])

        return tracks
