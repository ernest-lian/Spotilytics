import sqlite3
from sqlite3 import Error
from backend.src.constants.constants import database_name


class TopArtistsDao:
    def __init__(self):
        """ create a connection to the spotilytics database """
        self.__db_connection = sqlite3.connect(database_name)
        self.__db_cursor = self.__db_connection.cursor()

    def store_artists(self, artists):
        """ store in the TopArtists table """
        try:
            artists_rows = list(map(lambda x: (x['user_id'], x['name'], x['profile']), artists))
            self.__db_cursor.executemany('INSERT INTO TopArtists VALUES(?,?,?)', artists_rows)
            self.__db_connection.commit()

            return artists

        except Error as e:
            print(e)
            raise e

    def __del__(self):
        """ close the connection """
        self.__db_connection.close()
