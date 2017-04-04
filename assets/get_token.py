import requests
import requests.auth
CLIENT_ID = '209d8e5101794540bb6bdd7a0aa91ba8'
CLIENT_SECRET = 'a477f40d5939427ba260b3179032f2c5'
REDIRECT_URI = 'https://github.com/wipaweeeeee'
code = 'AQCgpgtnY_WewgHOKeInidme8sUqXINy03KdCD1w8Lv2Q7UeYn4luksnP83WZ8VRxq5p9VDX3Cyjt8I6M8xhzNy-IVcFqjxs4IXQxPlY9_WIFSgesMZNAlV8LOjA3QMTW5-Gb_W9P5CzSang0FzQMoUNXu_Hx4M_mq_zE7D9DnbjDRrLP1YtJtLu-NmFB99wGU2QGjiavfMzlJfwPHFi7W_M8GGOIprac-pvUKIiNiSpBPXnZ7xwJA'

def get_token(code):
    client_auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    post_data = {"grant_type": "authorization_code",
                 "code": code,
                 "redirect_uri": REDIRECT_URI}
    response = requests.post("https://accounts.spotify.com/api/token",
                             auth=client_auth,
                             data=post_data)
    token_json = response.json()
    return token_json

get_token(code)
