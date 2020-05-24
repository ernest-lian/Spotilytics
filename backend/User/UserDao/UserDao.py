import sqlite3
from sqlite3 import Error
import uuid

class UserDao:
    @staticmethod
    def create_connection(user_name, name, user_profile):
        """ create a database connection to a SQLite database """
        conn = None
        try:
            conn = sqlite3.connect('spotilytics.db')
            # print(sqlite3.version)
            
            c = conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS Users (
                            user_id text PRIMARY KEY, 
                            user_name text NOT NULL, 
                            name text NOT NULL, 
                            user_profile text NOT NULL
                        )''')

            c.execute("SELECT * FROM users WHERE user_name =?", (user_name,))
            row = c.fetchone()

            if row:
                return {'response': 200, 'body': {
                                            'message': 'User already registered',
                                            'name': row[2],
                                            'display_picture': row[3],
                                            'user_id': row[0]
                                            }
                        }

            user_id = str(uuid.uuid1())
            c.execute("INSERT INTO users VALUES (?,?,?,?)",
                    (user_id, user_name, name, user_profile))
            conn.commit()

            return {'response': 200, 'body': {
                                        'message': 'Successful registration',
                                        'name': name,
                                        'display_picture': user_profile,
                                        'user_id': user_id
                                        }
                    }

        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()
