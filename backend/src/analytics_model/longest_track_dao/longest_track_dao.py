import sqlite3
from sqlite3 import Error

class LongestTrackDao:
    @staticmethod
    def create_connection(user_id, analytics):
        """ create a database connection to a SQLite database """
        conn = None
        try:
            conn = sqlite3.connect('spotilytics.db')
            c = conn.cursor()

            c.execute('''CREATE TABLE IF NOT EXISTS LongestTrack( 
                                user_id text PRIMARY KEY,
                                longest_title text NOT NULL,
                                longest_artist text NOT NULL,
                                longest_cover text NOT NULL,
                                longest_greatest integer NOT NULL,
                                longest_average integer NOT NULL,
                                FOREIGN KEY (user_id) REFERENCES Users (user_id)
                            )''')

            c.execute("DELETE FROM LongestTrack")
            conn.commit()

            longest_title = analytics['title']
            longest_artist = analytics['artist']
            longest_cover = analytics['cover']
            longest_greatest = analytics['duration']
            longest_average = analytics['average']

            c.execute("INSERT INTO LongestTrack VALUES (?,?,?,?,?,?)", (
                user_id,
                longest_title, longest_artist, longest_cover, longest_greatest, longest_average
            ))
            conn.commit()

            return analytics

        except Error as e:
            print(e)
            raise e
        finally:
            if conn:
                conn.close()
