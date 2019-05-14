from graphene import ObjectType, String, Boolean, ID, List, Field, Int
import json
import os
from collections import namedtuple
from api import *

# Setup Authorization Object
sp = create_access_object()
# fetch album information
artist_name = "Die drei ???"
artist_id = get_artist_id(sp, artist_name)
api_album_output = get_artist_album(sp, artist_id)


def _json_object_hook(d):
    tuples = namedtuple('X', d.keys())(*d.values())
    return tuples


def json2obj(data):
    ''' Convert json into a Python object
    '''
    converted = json.loads(data, object_hook=_json_object_hook)
    return converted


class Artist(ObjectType):
    ''' class for artist structure
        api output
        "artists": [
            "external_urls": {
                "spotify": "https://open.spotify.com/artist/3meJIgRw7YleJrmbpbJK6S"
            },
            "href": "https://api.spotify.com/v1/artists/3meJIgRw7YleJrmbpbJK6S",
            "id": "3meJIgRw7YleJrmbpbJK6S",
            "name": "Die drei ???",
            "type": "artist",
            "uri": "spotify:artist:3meJIgRw7YleJrmbpbJK6S"
        ]
    '''
    # external_urls = String()
    href = String()
    id = ID()
    name = String()
    # type = String()
    uri = String()


class Image(ObjectType):
    ''' class for image structure
        api output
        "images": [
            {
                "height": 640,
                "url": "https://i.scdn.co/image/7c37a296848832ecaef8e65392c156ac2a568afe",
                "width": 640
            },
            {
                "height": 300,
                "url": "https://i.scdn.co/image/25e6bff8227efb48e405bb0b4e399a3034ab75ae",
                "width": 300
            },
            {
                "height": 64,
                "url": "https://i.scdn.co/image/f5c64f391a782b08cddefe72e283a51c3bfa4cd6",
                "width": 64
            }
        ],
    '''
    # height = Int()
    url = String()
    # width = Int()


class Album(ObjectType):
    ''' class for image structure
        api output
        "items": [
        {
            "album_group": "album",
            "album_type": "album",
            "artists": [...],
            "available_markets": [...],
            "external_urls": {
                "spotify": "https://open.spotify.com/album/39K0Sczt1mIbW33lB5RNer"
            },
            "href": "https://api.spotify.com/v1/albums/39K0Sczt1mIbW33lB5RNer",
            "id": "39K0Sczt1mIbW33lB5RNer",
            "images": [...],
            "name": "Und die schwarze Katze",
            "release_date": "2019-02-15",
            "release_date_precision": "day",
            "total_tracks": 60,
            "type": "album",
            "uri": "spotify:album:39K0Sczt1mIbW33lB5RNer"
        },
    '''
    album_group = String()
    album_type = String()
    # artists = Field(Artist)
    # available_markets = List(String)
    # external_urls = String()
    href = String()
    id = ID()
    # images = Field(Image)
    name = String()
    release_date = String()
    # release_date_precision = Int()
    total_tracks = Int()
    type = String()
    uri = String()


class Query(ObjectType):

    artist = List(Artist)
    image = List(Image)
    album = List(Album)

    def resolve_artist(self, info):
        # consider only artist subset
        artist_json = api_album_output['items'][0]['artists']
        return json2obj(json.dumps(artist_json))

    def resolve_image(self, info):
        # consider only image subset
        image_json = api_album_output['items'][0]['images']
        return json2obj(json.dumps(image_json))

    def resolve_album(self, info):
        # consider only album subset
        album_json = api_album_output['items']
        return json2obj(json.dumps(album_json))


'''To see results directly in the console, remove the comments here.
'''
import graphene
schema = graphene.Schema(query=Query)
query = """
    {
        album{
            name
            type
        }
    }
"""

if __name__ == "__main__":
    result = schema.execute(query)
    items = dict(result.data.items())
    print(json.dumps(items, indent=2))
