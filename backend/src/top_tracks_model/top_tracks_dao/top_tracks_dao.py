import sqlite3
from sqlite3 import Error

class TopTracksDao:
    @staticmethod
    def create_connection(tracks):
        """ create a database connection to a SQLite database """
        conn = None
        try:
            conn = sqlite3.connect('spotilytics.db')
            c = conn.cursor()

            c.execute('''CREATE TABLE IF NOT EXISTS TopTracks (
                            user_id text NOT NULL, 
                            title text NOT NULL,
                            artist text NOT NULL,
                            cover text NOT NULL,
                            FOREIGN KEY (user_id) REFERENCES Users (user_id)
                        )''')

            c.execute("DELETE FROM TopTracks")
            conn.commit()

            tracks_rows = list(map(lambda x: (x['user_id'], x['title'], x['artist'], x['cover']), tracks))
            c.executemany('INSERT INTO TopTracks VALUES(?,?,?,?)', tracks_rows)
            conn.commit()

            return tracks

        except Error as e:
            print(e)
            raise e
        finally:
            if conn:
                conn.close()

