import spotipy
import spotipy.util as util

scope = 'user-library-read'

util.prompt_for_user_token('Maritza Sicard',scope,client_id='11b4ed2d522742c9b810543286e0ab87',client_secret='efd4da3bd97c4a5f99d2e9fad766e82fl',redirect_uri='http://localhost/?code=C:\Users\maris\Documents\Escuela\ITESO5\AprendizajeMaquina\Proyecto\SpotifyTest.py')
spotify = spotipy.Spotify()
results = spotify.search(q='artist:' + 'Led Zeppelin', type='artist')
print results