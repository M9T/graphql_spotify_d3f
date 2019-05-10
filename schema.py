from graphene import ObjectType, String, Boolean, ID, List, Field, Int
import json
import os
from collections import namedtuple
from api import *


def _json_object_hook(d):
    print(d)
    print(namedtuple('X', d.keys())(*d.values()))
    return namedtuple('X', d.keys())(*d.values())


def json2obj(data):
    print(data)
    print(json.loads(data, object_hook=_json_object_hook))
    return json.loads(data, object_hook=_json_object_hook)


#https://github.com/wittydeveloper/spotify-graphql/blob/master/lib/schema.ts
# class Track(ObjectType):
#     id = ID()
#     album = Field(Album)
#     artists = Field(Artist)
#     available_markets = String()
#     disc_number = Int()
#     duration_ms = Int()
#     explicit: Boolean
#     href = String()
#     is_playable = Boolean()
#     name = String()
#     popularity = Int()
#     preview_url = String()
#     track_number = Int()
#     type = String()
#     uri = String()


class Artist(ObjectType):
    id = ID()
    genres = String()
    # href = String()
    name = String()
    # popularity = Int()
    # type = String()
    # uri = String()

    @property
    def description(self):
        return 'Description for Artist'


class Album(ObjectType):
    #     id = String()
    #     album_type = String()
    artists = Field(Artist)
    #     available_markets = String()
    #     genres = String()
    #     href = String()
    #     label = String()
    name = String()


#     popularity = Int()
#     release_date = String()
#     release_date_precision = String()
#     type = String()
#     uri = String()
#     #images = Image()
#     tracks = Field(Track)


class Query(ObjectType):
    artist = Field(Artist)
    album = Field(Album)

    albums = List(Album)
    artist = List(Artist)

    def resolve_albums(self, info):
        #  return json2obj(json.dumps(api.get_reviews(id)["reviews"]))
        return [Album('Album 1'), Album('Album 2')]

    def resolve_artist(self, info):

        # # Setup Authorization Object
        # sp = create_access_object()
        # artist_id = get_artist_id(sp)

        # artist_name = "Die drei ???"
        # # search query
        # result = sp.search(artist_name, limit=1, type='artist', market="DE")
        # #artist_id = result['artists']

        # output = json.dumps(result['artists'])
        # print(output)
        return [
            Artist(123, 'HipHop', 'Mark'),
            Artist(234, 'RnB', 'Mark2'),
            Artist(345, '', 'Mark3')
        ]


### TEST
import graphene
schema = graphene.Schema(query=Query)
query = """
    {
      album {
        artists
        name
        }
      artist {
        name
        genres
      }
    }
"""

if __name__ == "__main__":
    result = schema.execute(query)
    items = dict(result.data.items())
    print(json.dumps(items, indent=2))
