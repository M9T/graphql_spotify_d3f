'''
With this you can save the Spotify API output as a json file for testing purposes.
'''
from api import *
import json
from schema import *

# Setup Authorization Object
sp = create_access_object()

# Write api results for artist albums
with open('json/artist_album.json', 'w') as outfile:
    json.dump(get_artist_album(sp), outfile)

# Write api results for artist id search
with open('json/artist_id.json', 'w') as outfile:
    json.dump(get_artist_id(sp), outfile)
