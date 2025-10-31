import spotipy
from spotipy import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials

client_id = "2f81e9c9d3f84c559ba818d9522ba93f"
client_secret = "248207d57c5a4cb09ce5c4912e4fcc6f"
redirect_uri = "http://127.0.0.1:8080"
scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id,client_secret, redirect_uri, scope))

user_input = input("Enter the name of the song you'd like to get recommendations for?")

result = sp.search(q=user_input, type="track", limit=10,) #search returns dictionary w multiple layers
first_match = result["tracks"]["items"][0]["name"] #dictionary tracks contains dictionary items which contains track info
match_artist = result["tracks"]["items"][0]["artists"][0]["name"] #artists returns second array for each artist, get first index's name
match_uri = result["tracks"]["items"][0]["id"]

print("Getting recommendations for ", first_match, "by", match_artist)

recommendations = sp.search(q=f"{match_artist} radio", type="track", limit=10)
for i, t in enumerate(recommendations["tracks"]["items"]):
    print(t["name"], t["artists"][0]["name"])
