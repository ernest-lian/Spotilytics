import sqlite3
from sqlite3 import Error

class AnalyticsDao:
    @staticmethod
    def create_connection(user_id, analytics):
        """ create a database connection to a SQLite database """
        conn = None
        try:
            conn = sqlite3.connect('spotilytics.db')
            c = conn.cursor()

            c.execute('''CREATE TABLE IF NOT EXISTS Analytics( 
                                user_id text PRIMARY KEY,
                                popular_title text NOT NULL,
                                popular_artist text NOT NULL,
                                popular_cover text NOT NULL,
                                popular_greatest text NOT NULL,
                                popular_average text NOT NULL,
                                longest_title text NOT NULL,
                                longest_artist text NOT NULL,
                                longest_cover text NOT NULL,
                                longest_greatest text NOT NULL,
                                longest_average text NOT NULL,
                                fastest_title text NOT NULL,
                                fastest_artist text NOT NULL,
                                fastest_cover text NOT NULL,
                                fastest_greatest text NOT NULL,
                                fastest_average text NOT NULL,
                                energetic_title text NOT NULL,
                                energetic_artist text NOT NULL,
                                energetic_cover text NOT NULL,
                                energetic_greatest text NOT NULL,
                                energetic_average text NOT NULL,
                                FOREIGN KEY (user_id) REFERENCES User (user_id)
                            )''')

            c.execute("DELETE FROM Analytics")
            conn.commit()

            popular_title = analytics['popular_track']['title']
            popular_artist = analytics['popular_track']['artist']
            popular_cover = analytics['popular_track']['cover']
            popular_greatest = analytics['popular_track']['popular']
            popular_average = analytics['popular_track']['average']

            longest_title = analytics['longest_track']['title']
            longest_artist = analytics['longest_track']['artist']
            longest_cover = analytics['longest_track']['cover']
            longest_greatest = analytics['longest_track']['duration']
            longest_average = analytics['longest_track']['average']

            fastest_title = analytics['fastest_track']['title']
            fastest_artist = analytics['fastest_track']['artist']
            fastest_cover = analytics['fastest_track']['cover']
            fastest_greatest = analytics['fastest_track']['speed']
            fastest_average = analytics['fastest_track']['average']

            energetic_title = analytics['energetic_track']['title']
            energetic_artist = analytics['energetic_track']['artist']
            energetic_cover = analytics['energetic_track']['cover']
            energetic_greatest = analytics['energetic_track']['energy']
            energetic_average = analytics['energetic_track']['average']

            c.execute("INSERT INTO Analytics VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (
                user_id,
                popular_title, popular_artist, popular_cover, popular_greatest, popular_average,
                longest_title, longest_artist, longest_cover, longest_greatest, longest_average,
                fastest_title, fastest_artist, fastest_cover, fastest_greatest, fastest_average,
                energetic_title, energetic_artist, energetic_cover, energetic_greatest, energetic_average
            ))
            conn.commit()

            return analytics

        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()
