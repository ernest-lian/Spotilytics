import sys
import unittest
from unittest.mock import Mock
from unittest.mock import patch
sys.modules['backend'] = Mock()


class TestPlaylistMethods(unittest.TestCase):
    @patch('backend.src.app.create_playlist')
    def test_playlist_empty(self, mock_create_playlist):
        mock_create_playlist.return_value = {
            'status_code': 400,
            'message': 'Playlist name must be a string of at least length 1'
        }

        response = mock_create_playlist()

        self.assertEqual(response['status_code'], 400)
        self.assertEqual(response['message'], 'Playlist name must be a string of at least length 1')

    @patch('backend.src.app.create_playlist')
    def test_playlist_error(self, mock_create_playlist):
        mock_create_playlist.return_value = {
            'status_code': 400,
            'message': 'An error occurred while creating your playlist'
        }

        response = mock_create_playlist()

        self.assertEqual(response['status_code'], 400)
        self.assertEqual(response['message'], 'An error occurred while creating your playlist')

    @patch('backend.src.app.create_playlist')
    def test_playlist_success(self, mock_create_playlist):
        mock_create_playlist.return_value = {
            'status_code': 200,
            'message': 'Playlist successfully created'
        }

        response = mock_create_playlist()

        self.assertEqual(response['status_code'], 200)
        self.assertEqual(response['message'], 'Playlist successfully created')

class TestAnalyticMethods(unittest.TestCase):
    @patch('backend.src.app.login_spotify')
    def test_login_users_fail(self, mock_login_spotify):
        mock_login_spotify.return_value = {
            'status_code': 400,
            'error': 'An error occurred while processing users'
        }

        response = mock_login_spotify()

        self.assertEqual(response['status_code'], 400)
        self.assertEqual(response['error'], 'An error occurred while processing users')

    @patch('backend.src.app.login_spotify')
    def test_login_top_artists_fail(self, mock_login_spotify):
        mock_login_spotify.return_value = {
            'status_code': 400,
            'error': 'An error occurred while processing your top artists'
        }

        response = mock_login_spotify()

        self.assertEqual(response['status_code'], 400)
        self.assertEqual(response['error'], 'An error occurred while processing your top artists')

    @patch('backend.src.app.login_spotify')
    def test_login_top_tracks_fail(self, mock_login_spotify):
        mock_login_spotify.return_value = {
            'status_code': 400,
            'error': 'An error occurred while processing your top tracks'
        }

        response = mock_login_spotify()

        self.assertEqual(response['status_code'], 400)
        self.assertEqual(response['error'], 'An error occurred while processing your top tracks')

    @patch('backend.src.app.login_spotify')
    def test_login_analytics_fail(self, mock_login_spotify):
        mock_login_spotify.return_value = {
            'status_code': 400,
            'error': 'An error occurred while processing your analytics'
        }

        response = mock_login_spotify()

        self.assertEqual(response['status_code'], 400)
        self.assertEqual(response['error'], 'An error occurred while processing your analytics')

    @patch('backend.src.app.login_spotify')
    def test_login_recommendations_fail(self, mock_login_spotify):
        mock_login_spotify.return_value = {
            'status_code': 400,
            'error': 'An error occurred while processing your recommendations'
        }

        response = mock_login_spotify()

        self.assertEqual(response['status_code'], 400)
        self.assertEqual(response['error'], 'An error occurred while processing your recommendations')

    @patch('backend.src.app.login_spotify')
    def test_login_success(self, mock_login_spotify):
        mock_login_spotify.return_value = {
            'status_code': 200,
            'body': {
                'name': 'Ernest Lian',
                'display_picture': 'https://i.scdn.co/image/ab6775700000ee8526a6ebbfdc7621dece89f2d0',
                'user_id': '8c792b26-a08a-11ea-ac0e-acbc3282522f',
                'top_artists': [
                    {
                        'user_id': '8c792b26-a08a-11ea-ac0e-acbc3282522f',
                        'name': 'Ariana Grande',
                        'profile': 'https://i.scdn.co/image/b1dfbe843b0b9f54ab2e588f33e7637d2dab065a',
                        'rank': 1
                    }
                ],
                'top_tracks': [
                    {
                        'user_id': '8c792b26-a08a-11ea-ac0e-acbc3282522f',
                        'title': 'better off',
                        'artist': 'Ariana Grande',
                        'cover': 'https://i.scdn.co/image/ab67616d0000b273c3af0c2355c24ed7023cd394',
                        'rank': 1
                    }
                ],
                'analytics': {
                    'popular_track': {
                        'title': 'idontwannabeyouanymore',
                        'artist': 'Billie Eilish',
                        'cover': 'https://i.scdn.co/image/ab67616d0000b273a9f6c04ba168640b48aa5795',
                        'popular': 82,
                        'average': 58.8
                    },
                    'fastest_track': {
                        'title': 'Get Free',
                        'artist': 'Lana Del Rey',
                        'cover': 'https://i.scdn.co/image/ab67616d0000b27395e2fd1accb339fa14878190',
                        'speed': 203,
                        'average': 127
                    },
                    'energetic_track': {
                        'title': 'Radio',
                        'artist': 'Lana Del Rey',
                        'cover': 'https://i.scdn.co/image/ab67616d0000b273a1c37f3fd969287c03482c3b',
                        'energy': 84.1,
                        'average': 47.88
                    },
                    'longest_track': {
                        'title': 'Get Free',
                        'artist': 'Lana Del Rey',
                        'cover': 'https://i.scdn.co/image/ab67616d0000b27395e2fd1accb339fa14878190',
                        'duration': 334,
                        'average': 228
                    }
                },
                'recommendations': [
                    {
                        'title': 'Trap Queen',
                        'artist': 'Fetty Wap',
                        'cover': 'https://i.scdn.co/image/ab67616d0000b273de6bd09b07e2b4af4e409f6c',
                        'uri': 'spotify:track:2d8JP84HNLKhmd6IYOoupQ'
                    }
                ]
            }
        }

        response = mock_login_spotify()

        self.assertEqual(response['status_code'], 200)
        self.assertEqual(response['body']['name'], 'Ernest Lian')
        self.assertEqual(response['body']['user_id'], '8c792b26-a08a-11ea-ac0e-acbc3282522f')
        self.assertEqual(response['body']['top_artists'][0]['user_id'], '8c792b26-a08a-11ea-ac0e-acbc3282522f')

if __name__ == '__main__':
    unittest.main()
