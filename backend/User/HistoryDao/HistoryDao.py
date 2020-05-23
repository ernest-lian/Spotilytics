import sqlite3
import base64
import simplejson as simplejson

class HistoryDao:
    @staticmethod
    def login(user_id, song_title, song_artists, song_album_title, song_album_cover, song_uri, song_artist_cover, song_artist_uri):

        conn = sqlite3.connect('spotilytics.db')
        c = conn.cursor()

        c.execute('''CREATE TABLE IF NOT EXISTS History
                                            (user_id text, title text, artist text, album_title text, album_cover text, song_uri text, song_artist_cover text, song_artist_uri text)''')

        c.execute("INSERT INTO history VALUES (?,?,?,?,?,?,?,?)",
                  (user_id, song_title, song_artists, song_album_title, song_album_cover, song_uri, song_artist_cover, song_artist_uri))
        conn.commit()

        return {'response': 200, 'body': {
                                    'song_uri': song_uri,
                                    'song_title': song_title,
                                    'song_artist': song_artists,
                                    'song_album_title': song_album_title,
                                    'song_album_cover': song_album_cover,
                                    'song_artist_cover': song_artist_cover,
                                    'song_artist_uri': song_artist_uri
                                    }
                }


