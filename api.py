import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os


def create_access_object():
    """ Creates object to access the Spotify API

    Reads env variables for client id and client secret to establish
    Spotipy access object
    """
    client_id = os.environ['SPOTIPY_CLIENT_ID']
    client_secret = os.environ['SPOTIPY_CLIENT_SECRET']

    client_credentials_manager = SpotifyClientCredentials(
        client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    return sp


def get_artist_id(sp):
    """ Search the unique artist id for Die drei Fragezeichen
    """
    artist_name = "Die drei ???"
    # search query
    search_result = sp.search(artist_name, limit=1, type='artist', market="DE")
    artist_id = search_result['artists']['items'][0]['id']
    return artist_id


def get_artist_album(sp):
    """ Get Spotify catalog information about an artist’s albums
    """
    artist_id = "3meJIgRw7YleJrmbpbJK6S"
    api_result = sp.artist_albums(artist_id)
    return api_result