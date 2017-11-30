import sys

import datetime
import time

# music api imports
import spotipy
import spotipy.util as util
import billboard

import requests
import re
from bs4 import BeautifulSoup
from time import sleep
import pickle

#Spotify
client_id='11b4ed2d522742c9b810543286e0ab87'
client_secret='efd4da3bd97c4a5f99d2e9fad766e82f'
redirect_uri='https://github.com/MSicard/MusicMoodRecommendation/blob/master/SpotifyTest.py'
SCOPE = 'user-library-read'
CACHE = '.spotipyoauthcache'


if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print "Usage: %s username" % (sys.argv[0],)
    sys.exit()

token = util.prompt_for_user_token(username, SCOPE,
                                   client_id,
                                   client_secret,
                                   redirect_uri)

spotify = spotipy.Spotify(auth=token)


# Gracenote
clientid='1959581114'
userid = pygn.register(clientid)

# last.fm
apikey = 'ca15f24b7dd16b1d8f4f9f3d82b6c466'
apisecret = '4982e3c940522f4155171708fc34c3bf'
username = 'Mude_poet'
password_hash = pylast.md5(<INSERT YOUR PASSWORD>)

lastfm = pylast.LastFMNetwork(api_key = apikey, api_secret = apisecret,
                               username = username, password_hash = password_hash)

# timing function
def timefunc(f):
    def f_timer(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print f.__name__, 'took', end - start, 'seconds'
        return result
    return f_timer
	

@timefunc
# get categories 
def get_categories():
    category_ids = []
    for i in spotify.categories(limit = 50)['categories']['items']:
        category_ids.append(i.get('id'))
    return category_ids

@timefunc
# get playlists from list of categories
def get_playlists(categories):
    playlist_ids = []
    for i in categories:
        for j in spotify.category_playlists(i, limit = 50)['playlists']['items']:
            playlist_ids.append(j.get('id'))
    return playlist_ids

# get song ids from list of playlist ids
@timefunc
def get_songs(playlists):
    song_ids = []
    for i in playlists:
        try:
            for j in spotify.user_playlist('spotify', i)['tracks']['items']:
                song_ids.append(j['track']['id'])
        except:
            pass
        time.sleep(.1)
    return song_ids

categories = get_categories()
playlists = get_playlists(categories)
songs = get_songs(playlists)

