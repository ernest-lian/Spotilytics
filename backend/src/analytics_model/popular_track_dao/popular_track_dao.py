import sqlite3
from sqlite3 import Error

class PopularTrackDao:
    @staticmethod
    def create_connection(user_id, analytics):
        """ create a database connection to a SQLite database """
        conn = None
        try:
            conn = sqlite3.connect('spotilytics.db')
            c = conn.cursor()

            c.execute('''CREATE TABLE IF NOT EXISTS PopularTrack( 
                                user_id text PRIMARY KEY,
                                popular_title text NOT NULL,
                                popular_artist text NOT NULL,
                                popular_cover text NOT NULL,
                                popular_greatest real NOT NULL,
                                popular_average real NOT NULL,
                                FOREIGN KEY (user_id) REFERENCES Users (user_id)
                            )''')

            c.execute("DELETE FROM PopularTrack")
            conn.commit()

            popular_title = analytics['title']
            popular_artist = analytics['artist']
            popular_cover = analytics['cover']
            popular_greatest = analytics['popular']
            popular_average = analytics['average']

            c.execute("INSERT INTO PopularTrack VALUES (?,?,?,?,?,?)", (
                user_id,
                popular_title, popular_artist, popular_cover, popular_greatest, popular_average
            ))
            conn.commit()

            return analytics

        except Error as e:
            print(e)
            raise e
        finally:
            if conn:
                conn.close()
