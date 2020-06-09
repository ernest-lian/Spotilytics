from backend.src.dashboard_model.top_artists_dao.top_artists_dao import TopArtistsDao
from backend.src.dashboard_model.top_tracks_dao.top_tracks_dao import TopTracksDao


def store_top_artists(user_id, top_artists):
    artists = []

    # Pre-process top artists before storing
    for entry in top_artists['items']:
        name = entry['name']
        profile = entry['images'][0]['url']

        artists.append(
            {
                'user_id': user_id,
                'name': name,
                'profile': profile
            }
        )
    try:
        top_artists_dao = TopArtistsDao()
        return top_artists_dao.store_artists(artists)
    except Exception as e:
        raise e


def store_top_tracks(user_id, top_tracks):
    tracks = []

    # Pre-process top tracks before storing
    for entry in top_tracks['items']:
        title = entry['name']
        artist = entry['artists'][0]['name']
        cover = entry['album']['images'][0]['url']
        tracks.append({
            'user_id': user_id,
            'title': title,
            'artist': artist,
            'cover': cover
        })

    try:
        top_tracks_dao = TopTracksDao()
        return top_tracks_dao.store_tracks(tracks)
    except Exception as e:
        raise e