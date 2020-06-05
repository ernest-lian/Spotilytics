import sqlite3
from sqlite3 import Error

class RecommendationsDao:
    @staticmethod
    def create_connection(user_id, recommended_tracks):
        """ create a database connection to a SQLite database """
        conn = None
        try:
            conn = sqlite3.connect('spotilytics.db')
            c = conn.cursor()

            c.execute('''CREATE TABLE IF NOT EXISTS Recommendations( 
                                    user_id text NOT NULL,
                                    title text NOT NULL,
                                    artist text NOT NULL,
                                    cover text NOT NULL,
                                    uri text NOT NULL,
                                    FOREIGN KEY (user_id) REFERENCES Users (user_id)
                                )''')

            c.execute("DELETE FROM Recommendations")
            conn.commit()

            recommended_tracks_rows = list(map(lambda x: (user_id, x['title'], x['artist'], x['cover'], x['uri']), recommended_tracks))
            c.executemany('INSERT INTO Recommendations VALUES(?,?,?,?,?)', recommended_tracks_rows)
            conn.commit()

            return recommended_tracks

        except Error as e:
            print(e)
            raise e
        finally:
            if conn:
                conn.close()