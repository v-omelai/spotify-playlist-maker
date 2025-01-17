import json

from spotify import Spotify


if __name__ == '__main__':
    with open('config.json', 'r') as file:
        config = json.load(file)

    playlist = config.get('playlist', {})
    items = config.get('items', [])

    spotify = Spotify()
    spotify.delete(playlist=playlist, items=items)
