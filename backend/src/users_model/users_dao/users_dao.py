import sqlite3
import uuid
from sqlite3 import Error
from backend.src.constants.constants import database_name


class UsersDao:
    def __init__(self):
        """ create a connection to the spotilytics database """
        self.__db_connection = sqlite3.connect(database_name)
        self.__db_cursor = self.__db_connection.cursor()

    def store_user(self, user_name, name, profile):
        """ store in the Users table """
        try:
            # Create a new UUID for the respective user
            user_id = str(uuid.uuid1())
            self.__db_cursor.execute("INSERT INTO users VALUES (?,?,?,?)",
                      (user_id, user_name, name, profile))
            self.__db_connection.commit()

            return {
                        'name': name,
                        'display_picture': profile,
                        'id': user_id
                    }

        except Error as e:
            print(e)
            raise e

    def __del__(self):
        """ close the connection """
        self.__db_connection.close()
