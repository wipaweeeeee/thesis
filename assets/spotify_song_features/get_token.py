import requests
import requests.auth
import config

def get_token(code):
    client_auth = requests.auth.HTTPBasicAuth(config.CLIENT_ID, config.CLIENT_SECRET)
    post_data = {"grant_type": "authorization_code",
                 "code": config.code,
                 "redirect_uri": config.REDIRECT_URI}
    response = requests.post("https://accounts.spotify.com/api/token",
                             auth=client_auth,
                             data=post_data)
    token_json = response.json()
    return token_json

get_token(config.code)
