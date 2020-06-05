import sqlite3
from sqlite3 import Error

class PlaylistDao:
    @staticmethod
    def create_connection(user_name):
        """ create a database connection to a SQLite database """
        conn = None
        try:
            conn = sqlite3.connect('spotilytics.db')
            c = conn.cursor()

            c.execute("SELECT id FROM Users WHERE user_name =?", (user_name,))
            user_id = c.fetchone()[0]

            c.execute("SELECT uri FROM Recommendations WHERE user_id =?", (user_id,))
            rows = c.fetchall()

            return [track[0] for track in rows]
        except Error as e:
            print(e)
            raise e
        finally:
            if conn:
                conn.close()