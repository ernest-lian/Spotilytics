import sqlite3
from sqlite3 import Error
from backend.src.constants.constants import database_name


class AnalyticsDao:
    def __init__(self):
        """ create a connection to the spotilytics database """
        self.__db_connection = sqlite3.connect(database_name)
        self.__db_cursor = self.__db_connection.cursor()

    def store_track(self, user_id, analytics):
        """ store in the Analytics table """
        try:
            analytics_rows = list(map(lambda x: (user_id,
                                                 analytics[x]['analytic_type'],
                                                 analytics[x]['title'],
                                                 analytics[x]['artist'],
                                                 analytics[x]['cover'],
                                                 analytics[x][analytics[x]['analytic_type']],
                                                 analytics[x]['average']), analytics))
            self.__db_cursor.executemany('INSERT INTO Analytics VALUES(?,?,?,?,?,?,?)', analytics_rows)
            self.__db_connection.commit()

            return analytics

        except Error as e:
            print(e)
            raise e

    def __del__(self):
        """ close the connection """
        self.__db_connection.close()
