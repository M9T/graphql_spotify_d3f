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
    search = sp.search(artist_name, limit=1, type='artist', market="DE")
    return search['artists']['items'][0]


def get_album(sp):
    """ returns a single album
    """
    album_id = "39K0Sczt1mIbW33lB5RNer"
    # get album
    album = sp.album(album_id)
    return album


def get_artist_albumsm(sp):
    """ Get Spotify catalog information about an artist’s albums
    """
    artist_id = "3meJIgRw7YleJrmbpbJK6S"
    result = sp.get_artist_albumsm(artist_id)
    return result