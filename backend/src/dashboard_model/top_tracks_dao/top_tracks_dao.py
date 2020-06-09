import sqlite3
from sqlite3 import Error
from backend.src.constants.constants import database_name


class TopTracksDao:
    def __init__(self):
        """ create a connection to the spotilytics database """
        self.__db_connection = sqlite3.connect(database_name)
        self.__db_cursor = self.__db_connection.cursor()

    def store_tracks(self, tracks):
        """ store in the TopTracks table """
        try:
            tracks_rows = list(map(lambda x: (x['user_id'], x['title'], x['artist'], x['cover']), tracks))
            self.__db_cursor.executemany('INSERT INTO TopTracks VALUES(?,?,?,?)', tracks_rows)
            self.__db_connection.commit()

            return tracks

        except Error as e:
            print(e)
            raise e

    def __del__(self):
        """ close the connection """
        self.__db_connection.close()
