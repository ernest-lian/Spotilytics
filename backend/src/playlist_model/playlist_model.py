from backend.src.playlist_model.playlist_dao.playlist_dao import PlaylistDao


class PlaylistModel:
    @staticmethod
    def create(sp, validated_data, user_id):
        playlist_name = 'Spotilytics - ' + validated_data['body']['playlist_name']
        new_playlist = sp.user_playlist_create("ernest.lian97", playlist_name)

        playlist_response = PlaylistDao.create_connection(user_id)

        try:
            sp.user_playlist_add_tracks("ernest.lian97", new_playlist['id'], playlist_response)
            return {'status_code': 200, 'message': 'Playlist successfully created'}
        except Exception as e:
            raise e
