import sqlite3
from sqlite3 import Error
from backend.src.constants.constants import database_name


class RecommendationsDao:
    def __init__(self):
        """ create a connection to the spotilytics database """
        self.__db_connection = sqlite3.connect(database_name)
        self.__db_cursor = self.__db_connection.cursor()

    def store_recommendations(self, user_id, recommended_tracks):
        """ store in the Recommendations table """
        try:
            recommended_tracks_rows = list(map(lambda track: (
                user_id, track['title'], track['artist'], track['cover'], track['uri']
            ), recommended_tracks))
            self.__db_cursor.executemany('INSERT INTO Recommendations VALUES(?,?,?,?,?)', recommended_tracks_rows)
            self.__db_connection.commit()

            return recommended_tracks
        except Error as e:
            print(e)
            raise e

    def fetch_recommendations(self, user_name):
        """ fetch playlist from the Recommendations table """
        try:
            self.__db_cursor.execute("SELECT id FROM Users WHERE user_name =?", (user_name,))
            user_id = self.__db_cursor.fetchone()[0]

            self.__db_cursor.execute("SELECT uri FROM Recommendations WHERE user_id =?", (user_id,))
            rows = self.__db_cursor.fetchall()

            return [track[0] for track in rows]
        except Error as e:
            print(e)
            raise e

    def __del__(self):
        """ close the connection """
        self.__db_connection.close()