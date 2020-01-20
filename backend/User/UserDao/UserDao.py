import sqlite3
import base64
import simplejson as simplejson

class UserDao:
    def __init__(self, user_name=None, user_password=None):
        '''
        This method will construct a new UserDao object
        :param user_name: The user name of the user
        :param user_password: The password of the user
        '''

        self.user_name = user_name
        self.user_password = user_password

    def login(self):
        conn = sqlite3.connect('spotilytics.db')

        # Query the database for the user_id that matches the given user_name and password
        c = conn.cursor()
        c.execute("SELECT user_name, user_password FROM users WHERE user_name =?", (self.user_name,))
        rows = c.fetchone()


    def register(self):
        conn = sqlite3.connect('spotilytics.db')

        c = conn.cursor()

