import sqlite3
from sqlite3 import Error

class TopArtistsDao:
    @staticmethod
    def create_connection(artists):
        """ create a database connection to a SQLite database """
        conn = None
        try:
            conn = sqlite3.connect('spotilytics.db')
            c = conn.cursor()

            c.execute('''CREATE TABLE IF NOT EXISTS TopArtists( 
                            user_id text NOT NULL,
                            name text NOT NULL,
                            profile text NOT NULL,
                            FOREIGN KEY (user_id) REFERENCES Users (user_id)
                        )''')

            c.execute("DELETE FROM TopArtists")
            conn.commit()

            artists_rows = list(map(lambda x: (x['user_id'], x['name'], x['profile']), artists))
            c.executemany('INSERT INTO TopArtists VALUES(?,?,?)', artists_rows)
            conn.commit()

            return artists

        except Error as e:
            print(e)
            raise e
        finally:
            if conn:
                conn.close()
