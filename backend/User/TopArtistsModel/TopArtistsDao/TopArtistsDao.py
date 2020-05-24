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
                            rank integer NOT NULL,
                            FOREIGN KEY (user_id) REFERENCES User (user_id)
                        )''')

            c.execute("DELETE FROM TopArtists")
            conn.commit()

            for entry in artists:
                user_id = entry['user_id']
                name = entry['name']
                profile = entry['profile']
                rank = entry['rank']
                c.execute("INSERT INTO TopArtists VALUES (?,?,?,?)", (
                                user_id, name, profile, rank
                            ))
                conn.commit()

            return artists

        except Error as e:
                print(e)
        finally:
            if conn:
                conn.close()
