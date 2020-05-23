import sqlite3
import base64
import simplejson as simplejson

class TopSongsDao:
    @staticmethod
    def store(user_id, title, artist, cover, rank):

        conn = sqlite3.connect('spotilytics.db')
        c = conn.cursor()

        c.execute('''CREATE TABLE IF NOT EXISTS TopSongs
                                            (user_id text, title text, artist text, cover text, rank integer)''')

        c.execute("INSERT INTO TopSongs VALUES (?,?,?,?,?)",
                  (user_id, title, artist, cover, rank))
        conn.commit()

        return {'response': 200, 'body': {
                                    'title': title,
                                    'artist': artist,
                                    'cover': cover,
                                    'rank': rank
                                    }
                }


