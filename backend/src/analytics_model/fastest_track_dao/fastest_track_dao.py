import sqlite3
from sqlite3 import Error

class FastestTrackDao:
    @staticmethod
    def create_connection(user_id, analytics):
        """ create a database connection to a SQLite database """
        conn = None
        try:
            conn = sqlite3.connect('spotilytics.db')
            c = conn.cursor()

            c.execute('''CREATE TABLE IF NOT EXISTS FastestTrack( 
                                user_id text PRIMARY KEY,
                                fastest_title text NOT NULL,
                                fastest_artist text NOT NULL,
                                fastest_cover text NOT NULL,
                                fastest_greatest integer NOT NULL,
                                fastest_average integer NOT NULL,
                                FOREIGN KEY (user_id) REFERENCES Users (user_id)
                            )''')

            c.execute("DELETE FROM FastestTrack")
            conn.commit()

            fastest_title = analytics['title']
            fastest_artist = analytics['artist']
            fastest_cover = analytics['cover']
            fastest_greatest = analytics['speed']
            fastest_average = analytics['average']

            c.execute("INSERT INTO FastestTrack VALUES (?,?,?,?,?,?)", (
                user_id,
                fastest_title, fastest_artist, fastest_cover, fastest_greatest, fastest_average
            ))
            conn.commit()

            return analytics

        except Error as e:
            print(e)
            raise e
        finally:
            if conn:
                conn.close()
