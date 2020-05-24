from backend.User.PlaylistModel.PlaylistDao.PlaylistDao import PlaylistDao

class PlaylistModel:
    @staticmethod
    def create(sp, playlist_name, user_id):
        new_playlist = sp.user_playlist_create("ernest.lian97", playlist_name)

        playlist_uris = PlaylistDao.create_connection(user_id)

        sp.user_playlist_add_tracks("ernest.lian97", new_playlist['id'], playlist_uris)

        return { 'response': 200 }