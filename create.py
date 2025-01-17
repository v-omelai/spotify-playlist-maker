import json
import os

from spotify import Spotify


if __name__ == '__main__':
    name = os.getenv('name', '')
    description = os.getenv('description', '')
    keywords = os.getenv('keywords', '').split(', ')

    spotify = Spotify()

    items = []
    for keyword in keywords:
        items.append(spotify.search(query=keyword))  # noqa

    playlist = spotify.create(name=name, description=description, items=items)

    config = {'name': name, 'description': description, 'keywords': keywords, 'playlist': playlist, 'items': items}

    with open('config.json', 'w') as file:
        json.dump(config, file, indent=4)  # noqa
