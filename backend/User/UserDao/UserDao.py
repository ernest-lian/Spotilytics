import sqlite3
import base64
import simplejson as simplejson
import uuid

class UserDao:

    @staticmethod
    def login(user_name, name, user_profile):
        # Connect to the Spotilytics database
        conn = sqlite3.connect('spotilytics.db')
        c = conn.cursor()

        c.execute('''CREATE TABLE IF NOT EXISTS Users
                                    (user_id text, user_name text, name text, user_profile text)''')

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

        # Insert a user into the database
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
