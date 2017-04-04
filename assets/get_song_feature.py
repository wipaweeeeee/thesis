#grabbing valence of each song

import requests
import requests.auth
import sys

CLIENT_ID = '209d8e5101794540bb6bdd7a0aa91ba8'
CLIENT_SECRET = 'a477f40d5939427ba260b3179032f2c5'
REDIRECT_URI = 'https://github.com/wipaweeeeee'
refresh_token = 'AQA89EzMnQBG1Zu09RtN-xLwbOAf6PhrvMrLowdxT0rz8WI26WzFyQmOiEHLcNxuygyOkfd5WJ3O2PnzM5gY6-fUUc-HpRDRvzkYMaKnv3w0eJ_h4npT6_afjnXPpbQiz-M'
code = 'AQCgpgtnY_WewgHOKeInidme8sUqXINy03KdCD1w8Lv2Q7UeYn4luksnP83WZ8VRxq5p9VDX3Cyjt8I6M8xhzNy-IVcFqjxs4IXQxPlY9_WIFSgesMZNAlV8LOjA3QMTW5-Gb_W9P5CzSang0FzQMoUNXu_Hx4M_mq_zE7D9DnbjDRrLP1YtJtLu-NmFB99wGU2QGjiavfMzlJfwPHFi7W_M8GGOIprac-pvUKIiNiSpBPXnZ7xwJA'

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
    client_auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    post_data = {"grant_type": "refresh_token",
                 "refresh_token": refresh_token
                 }
    response = requests.post("https://accounts.spotify.com/api/token",
                             auth=client_auth,
                             data=post_data)
    token_json = response.json()
    fresh_token = token_json["access_token"]
    # return fresh_token

    get_song_id(fresh_token, song_name)

get_token(code)
