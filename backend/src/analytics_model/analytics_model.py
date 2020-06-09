from backend.src.analytics_model.analytics_dao.analytics_dao import AnalyticsDao
from backend.src.constants.constants import number_of_tracks, long_term, duration, speed, energy, popular


def fetch_popular(sp):
    popular_track = {}
    most_popular = 0
    average_popularity = 0

    # Pre-process the most popular tracks
    for entry in sp.current_user_top_tracks(number_of_tracks, 0, long_term)['items']:
        current_popularity = sp.track(entry['id'])['popularity']
        average_popularity += current_popularity
        if current_popularity >= most_popular:
            most_popular = current_popularity
            popular_track['title'] = entry['name']
            popular_track['artist'] = entry['album']['artists'][0]['name']
            popular_track['cover'] = entry['album']['images'][0]['url']

    popular_track['popular'] = most_popular
    popular_track['analytic_type'] = popular
    popular_track['average'] = (average_popularity / number_of_tracks)

    return popular_track


def fetch_analytics(sp, top_tracks):
    longest_duration = 0
    longest_song_id = ''
    average_duration = 0

    fastest_tempo = 0
    fastest_song_id = ''
    average_tempo = 0

    most_energetic = 0
    energetic_song_id = ''
    average_energy = 0

    # Pre-process the longest, fastest, and most energetic tracks
    for entry in sp.audio_features(top_tracks):
        if entry['duration_ms'] >= longest_duration:
            longest_duration = entry['duration_ms']
            longest_song_id = entry['id']

        if entry['tempo'] >= fastest_tempo:
            fastest_tempo = entry['tempo']
            fastest_song_id = entry['id']

        if entry['energy'] >= most_energetic:
            most_energetic = entry['energy']
            energetic_song_id = entry['id']

        average_duration += entry['duration_ms']
        average_tempo += entry['tempo']
        average_energy += entry['energy']

    longest_track = dict()
    longest_track['analytic_type'] = duration
    longest_track['title'] = sp.track(longest_song_id)['name']
    longest_track['artist'] = sp.track(longest_song_id)['artists'][0]['name']
    longest_track['cover'] = sp.track(longest_song_id)['album']['images'][0]['url']
    longest_track['duration'] = int(longest_duration / 1000)
    longest_track['average'] = int((average_duration / number_of_tracks) / 1000)

    fastest_track = dict()
    fastest_track['analytic_type'] = speed
    fastest_track['title'] = sp.track(fastest_song_id)['name']
    fastest_track['artist'] = sp.track(fastest_song_id)['artists'][0]['name']
    fastest_track['cover'] = sp.track(fastest_song_id)['album']['images'][0]['url']
    fastest_track['speed'] = int(fastest_tempo)
    fastest_track['average'] = int(average_tempo / number_of_tracks)

    energetic_track = dict()
    energetic_track['analytic_type'] = energy
    energetic_track['title'] = sp.track(energetic_song_id)['name']
    energetic_track['artist'] = sp.track(energetic_song_id)['artists'][0]['name']
    energetic_track['cover'] = sp.track(energetic_song_id)['album']['images'][0]['url']
    energetic_track['energy'] = most_energetic * 100
    energetic_track['average'] = round((average_energy / number_of_tracks) * 100, 2)

    return {
        'longest_track': longest_track,
        'fastest_track': fastest_track,
        'energetic_track': energetic_track
    }


def store_analytics(user_id, sp, top_tracks):
    response = dict()
    analytics = fetch_analytics(sp, top_tracks)
    analytics['popular_track'] = fetch_popular(sp)

    try:
        # Store the collected track analytics
        analytics_dao = AnalyticsDao()
        analytics_response = analytics_dao.store_track(user_id, analytics)
        response['longest_track'] = analytics_response['longest_track']
        response['popular_track'] = analytics_response['popular_track']
        response['fastest_track'] = analytics_response['fastest_track']
        response['energetic_track'] = analytics_response['energetic_track']
        return response
    except Exception as e:
        raise e
