'''
With this you can save the Spotify API output as a json file for testing purposes.
'''
from api import *
import json
from schema import *

# Setup Authorization Object
sp = create_access_object()

# fetch album information
artist_name = "Die drei ???"
artist_id = get_artist_id(sp, artist_name)
album_id = "5B7w9vkfh979tEyzwkLk9k"

# Write api results for artist albums
with open('json/artist_album.json', 'w') as outfile:
    json.dump(get_artist_album(sp, artist_id), outfile)

# Write api results for artist id search
with open('json/artist_id.json', 'w') as outfile:
    json.dump(get_artist_id(sp, artist_name), outfile)
