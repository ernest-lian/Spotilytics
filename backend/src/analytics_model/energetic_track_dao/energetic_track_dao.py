import sqlite3
from sqlite3 import Error

class EnergeticTrackDao:
    @staticmethod
    def create_connection(user_id, analytics):
        """ create a database connection to a SQLite database """
        conn = None
        try:
            conn = sqlite3.connect('spotilytics.db')
            c = conn.cursor()

            c.execute('''CREATE TABLE IF NOT EXISTS EnergeticTrack( 
                                user_id text PRIMARY KEY,
                                energetic_title text NOT NULL,
                                energetic_artist text NOT NULL,
                                energetic_cover text NOT NULL,
                                energetic_greatest real NOT NULL,
                                energetic_average real NOT NULL,
                                FOREIGN KEY (user_id) REFERENCES Users (user_id)
                            )''')

            c.execute("DELETE FROM EnergeticTrack")
            conn.commit()

            energetic_title = analytics['title']
            energetic_artist = analytics['artist']
            energetic_cover = analytics['cover']
            energetic_greatest = analytics['energy']
            energetic_average = analytics['average']

            c.execute("INSERT INTO EnergeticTrack VALUES (?,?,?,?,?,?)", (
                user_id,
                energetic_title, energetic_artist, energetic_cover, energetic_greatest, energetic_average
            ))
            conn.commit()

            return analytics

        except Error as e:
            print(e)
            raise e
        finally:
            if conn:
                conn.close()
