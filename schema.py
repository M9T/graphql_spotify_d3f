from graphene import ObjectType, String, Boolean, ID, List, Field, Int
import json
import os
from collections import namedtuple
from api import *

# Setup Authorization Object
sp = create_access_object()


def _json_object_hook(d):
    return namedtuple('X', d.keys())(*d.values())


def json2obj(data):
    ''' Convert json dictionary to objects
    '''
    return json.loads(data, object_hook=_json_object_hook)


class Artist(ObjectType):
    ''' class for artist structure
    api output
                    "external_urls": {
                        "spotify": "https://open.spotify.com/artist/3meJIgRw7YleJrmbpbJK6S"
                    },
                    "href": "https://api.spotify.com/v1/artists/3meJIgRw7YleJrmbpbJK6S",
                    "id": "3meJIgRw7YleJrmbpbJK6S",
                    "name": "Die drei ???",
                    "type": "artist",
                    "uri": "spotify:artist:3meJIgRw7YleJrmbpbJK6S"
    '''
    external_urls = String(
    )  #"https://api.spotify.com/v1/artists/3meJIgRw7YleJrmbpbJK6S",
    href = String(
    )  #"https://api.spotify.com/v1/artists/3meJIgRw7YleJrmbpbJK6S",
    id = ID()  #"3meJIgRw7YleJrmbpbJK6S",
    name = String()  #"Die drei ???",
    type = String()  #"artist",
    uri = String()  #"spotify:artist:3meJIgRw7YleJrmbpbJK6S"


class Query(ObjectType):
    artist = Field(Artist)
    # album = Field(Album)

    # albums = List(Album)
    artist = List(Artist)

    def resolve_artist(self, info):
        artist_id = get_artist_id(sp)
        result = get_artist_album(sp)

        # consider only subset
        result = result['items'][0]['artists']

        ret = json2obj(json.dumps(result))
        return ret


'''To see results directly in the console, remove the comments here.
'''
import graphene
schema = graphene.Schema(query=Query)
query = """
    {
      artist{
          id
          href
      }
    }
"""

if __name__ == "__main__":
    result = schema.execute(query)
    items = dict(result.data.items())
    print(json.dumps(items, indent=2))
