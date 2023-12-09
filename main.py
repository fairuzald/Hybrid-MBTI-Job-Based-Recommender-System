from dotenv import load_dotenv
import os
import base64
from requests import post, get

import json
load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_string_bytes = auth_string.encode('utf-8')
    auth_base64_bytes = str(base64.b64encode(auth_string_bytes),"utf-8")
    
    url = "https://accounts.spotify.com/api/token"
    
    headers ={
        "Authorization": "Basic " + auth_base64_bytes,
        "Content-Type" : "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    jsons = json.loads(result.content)
    token = jsons["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}    

def search_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=1"
    query_url = url + query
    result = get(query_url, headers=headers)
    jsons = json.loads(result.content)["artists"]["items"]
    if len(jsons) == 0:
        return print("Artist not found")
    return jsons

def get_songs_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks"
    headers = get_auth_header(token)
    query = "?country=US"
    query_url = url + query
    result = get(query_url, headers=headers)
    jsons = json.loads(result.content)["tracks"]
    return jsons


token = get_token()
tes =search_artist(token, "BTS")
song = get_songs_by_artist(token, tes[0]["id"])

for idx, son in enumerate(song):
    print(f"{idx+1}. {son['name']}")
