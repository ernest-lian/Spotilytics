import sqlite3
from sqlite3 import Error

class PredictDao:
    @staticmethod
    def create_connection(user_id, store_tracks):
        """ create a database connection to a SQLite database """
        conn = None
        try:
            conn = sqlite3.connect('spotilytics.db')
            c = conn.cursor()

            c.execute('''CREATE TABLE IF NOT EXISTS Recommendations( 
                                    user_id text NOT NULL,
                                    title text NOT NULL,
                                    artist text NOT NULL,
                                    cover integer NOT NULL,
                                    FOREIGN KEY (user_id) REFERENCES User (user_id)
                                )''')

            c.execute("DELETE FROM Recommendations")
            conn.commit()

            for track in store_tracks:
                title = track['title']
                artist = track['artist']
                cover = track['cover']

                c.execute("INSERT INTO Recommendations VALUES (?,?,?,?)", (
                    user_id, title, artist, cover
                ))
                conn.commit()

            return store_tracks

        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()