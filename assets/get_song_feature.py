#grabbing valence of each song

import requests
import requests.auth
import sys
import config

song_name = sys.argv[1]
artist = sys.argv[2]

def get_song_id(token, song_name):
    url = 'https://api.spotify.com/v1/search'
    params = {'q': song_name, 'type': 'track'}
    headers = {'Authorization': 'Bearer ' + token}

    response = requests.get(url, headers=headers, params=params)
    json = response.json()

    for index, item in enumerate(json["tracks"]["items"]):
        artist_name = item["artists"][0]["name"]
        if artist_name == artist:
            # print index
            song_id = json["tracks"]["items"][index]["id"]
            song_name = json["tracks"]["items"][index]["name"]
            print song_name

    get_song_feature(token, song_id)

def get_song_feature(token, song_id):
    base_url = "https://api.spotify.com/v1/audio-features/"
    url = base_url + song_id
    headers = {'Authorization': 'Bearer ' + token}

    response = requests.get(url, headers=headers)
    json = response.json()
    print json["valence"]


def get_token(code):
    client_auth = requests.auth.HTTPBasicAuth(config.CLIENT_ID, config.CLIENT_SECRET)
    post_data = {"grant_type": "refresh_token",
                 "refresh_token": config.refresh_token
                 }
    response = requests.post("https://accounts.spotify.com/api/token",
                             auth=client_auth,
                             data=post_data)
    token_json = response.json()
    fresh_token = token_json["access_token"]
    # return fresh_token

    get_song_id(fresh_token, song_name)

get_token(config.code)
