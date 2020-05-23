import sqlite3
import base64
import simplejson as simplejson

class TopArtistsDao:
    @staticmethod
    def store(user_id, name, profile, rank):

        conn = sqlite3.connect('spotilytics.db')
        c = conn.cursor()

        c.execute('''CREATE TABLE IF NOT EXISTS TopArtists
                                            (user_id text, name text, profile text, rank integer)''')

        c.execute("INSERT INTO TopArtists VALUES (?,?,?,?)",
                  (user_id, name, profile, rank))
        conn.commit()

        return {'response': 200, 'body': {
                                    'name': name,
                                    'profile': profile,
                                    'rank': rank
                                    }
                }


