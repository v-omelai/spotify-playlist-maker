import spotipy
from decouple import config


class Spotify:
    def __init__(self,
                 client_id: str = config('SPOTIFY_CLIENT_ID'),
                 client_secret: str = config('SPOTIFY_CLIENT_SECRET'),
                 redirect_uri: str = config('SPOTIFY_REDIRECT_URI'),
                 scope: tuple[str] = (
                         'user-library-read',
                         'playlist-modify-public',
                         'playlist-modify-private',
                 )):
        self.s = spotipy.Spotify(auth_manager=spotipy.SpotifyOAuth(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            scope=scope
        ))

    def search(self, query: str) -> str:
        results = self.s.search(q=query, limit=1)
        [track] = results.get('tracks', {}).get('items', [])
        return track['uri']

    def create(self, name: str, description: str, items: list) -> dict:
        user = self.s.current_user()['id']
        playlist = self.s.user_playlist_create(user=user, name=name, description=description)
        self.s.playlist_add_items(playlist_id=playlist['id'], items=items)
        return playlist

    def delete(self, playlist: dict, items: list = None) -> dict:
        if items:
            self.s.playlist_remove_all_occurrences_of_items(playlist_id=playlist['id'], items=items)
        return self.s.current_user_unfollow_playlist(playlist_id=playlist['id'])
