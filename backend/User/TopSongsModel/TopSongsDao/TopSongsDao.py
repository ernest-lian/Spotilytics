import sqlite3
from sqlite3 import Error

class TopSongsDao:
    @staticmethod
    def create_connection(tracks):
        """ create a database connection to a SQLite database """
        conn = None
        try:
            conn = sqlite3.connect('spotilytics.db')
            c = conn.cursor()

            c.execute('''CREATE TABLE IF NOT EXISTS TopSongs (
                            user_id text NOT NULL, 
                            title text NOT NULL,
                            artist text NOT NULL,
                            cover text NOT NULL,
                            rank integer NOT NULL,
                            FOREIGN KEY (user_id) REFERENCES User (user_id)
                        )''')

            c.execute("DELETE FROM TopSongs")
            conn.commit()

            for track in tracks:
                user_id = track['user_id']
                title = track['title']
                artist = track['artist']
                cover = track['cover']
                rank = track['rank']

                c.execute("INSERT INTO TopSongs VALUES (?,?,?,?,?)",
                          (user_id, title, artist, cover, rank))
                conn.commit()
            return tracks

        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()

