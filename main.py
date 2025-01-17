from pathlib import Path

from cdktf import TerraformStack, TerraformVariable, Fn, TerraformOutput, App
from cdktf_cdktf_provider_null.provider import NullProvider
from cdktf_cdktf_provider_null.resource import Resource as NullResource
from constructs import Construct


BASE_DIR = Path(__file__).resolve().parent

COMMAND_CREATE = 'pipenv run python create.py'
COMMAND_DESTROY = 'pipenv run python destroy.py'


class SpotifyPlaylistStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):  # noqa
        super().__init__(scope, id)

        NullProvider(self, 'null')

        name = TerraformVariable(
            self,
            'name',
            type='string',
            description='Your Spotify playlist name',
        )

        description = TerraformVariable(
            self,
            'description',
            type='string',
            description='Your Spotify playlist description',
        )

        keywords = TerraformVariable(
            self,
            'keywords',
            type='list(string)',
            description='A list of keywords to search for songs',
        )

        joined = Fn.join(separator=', ', list=keywords.list_value)

        resource = NullResource(self, 'SpotifyPlaylist',
                                triggers={
                                    'name': name.string_value,
                                    'description': description.string_value,
                                    'keywords': joined,
                                })

        parameters = {'working_dir': str(BASE_DIR)}

        resource.add_override('provisioner.local-exec', [
            {'command': COMMAND_CREATE, 'environment': {
                'name': name.string_value,
                'description': description.string_value,
                'keywords': joined,
            }, 'when': 'create', **parameters},
            {'command': COMMAND_DESTROY, 'when': 'destroy', **parameters},
        ])

        TerraformOutput(self, 'created-name', value=name.string_value)
        TerraformOutput(self, 'created-description', value=description.string_value)
        TerraformOutput(self, 'created-keywords', value=joined)


if __name__ == '__main__':
    app = App()
    SpotifyPlaylistStack(app, 'spotify-playlist-maker')
    app.synth()
