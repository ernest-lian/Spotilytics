import sqlite3
from sqlite3 import Error
import uuid

class UserDao:
    @staticmethod
    def create_connection(user_name, name, profile):
        """ create a database connection to a SQLite database """
        conn = None
        try:
            conn = sqlite3.connect('spotilytics.db')
            
            c = conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS Users (
                            id text PRIMARY KEY, 
                            user_name text NOT NULL, 
                            name text NOT NULL, 
                            profile text NOT NULL
                        )''')

            c.execute("SELECT * FROM users WHERE user_name =?", (user_name,))
            row = c.fetchone()

            if row:
                return {
                            'name': row[2],
                            'display_picture': row[3],
                            'id': row[0]
                        }

            user_id = str(uuid.uuid1())
            c.execute("INSERT INTO users VALUES (?,?,?,?)",
                      (user_id, user_name, name, profile))
            conn.commit()

            return {
                        'name': name,
                        'display_picture': profile,
                        'id': user_id
                    }

        except Error as e:
            print(e)
            raise e
        finally:
            if conn:
                conn.close()
