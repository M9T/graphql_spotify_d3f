from api import *
import json
from schema import *
# Setup Authorization Object
sp = create_access_object()

artist_id = get_artist_id(sp)

# print(sp.artist_albums(artist_id))

artist_name = "Die drei ???"
result = sp.search(artist_name, limit=1, type='artist', market="DE")

# output = json2obj(json.dumps(result['artists']['items'][0]['id']))
# print(output)

res = json2obj(json.dumps(result["artists"]['items'][0], indent=2))

# print(json.dumps(get_artist_albumsm(sp), indent=2))

import json
with open('artist_album.json', 'w') as outfile:
    json.dump(get_artist_albumsm(sp), outfile)