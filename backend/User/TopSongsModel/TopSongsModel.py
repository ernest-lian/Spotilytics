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
            tracks.append({
                'user_id': user_id,
                'title': title,
                'artist': artist,
                'cover': cover,
                'rank': rank
            })
            rank += 1

        stored_tracks = TopSongsDao.create_connection(tracks)

        return stored_tracks
