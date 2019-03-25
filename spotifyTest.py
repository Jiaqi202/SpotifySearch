import os
import sys
import json
import spotipy
import webbrowser
import csv
import spotipy.util as util


def write_csv(data):
    with open('haha.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for line in data:
            csvwriter.writerow(line)

def write_spotify_search_response_to_csv(response):
    albumResults = response['albums']['items']

    datas = []
    for item in albumResults:
        data = []
        data.append(item['name'])
        data.append(item['artists'][0]['name'])
        data.append(item['release_date'])
        datas.append(data)

    write_csv(datas)


#Get the username from the terminal
if len(sys.argv)>1:
    username = sys.argv[1]
    print("UserName: " + username)
else:
    print("Usage: %username" %(sys.argv[0],))
    sys.exit()

#Erase cache and prompt for user permission

try:
    token = util.prompt_for_user_token(username)
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username)

# Create our sportifyObject
spotifyObject = spotipy.Spotify(auth=token)

# User information
user = spotifyObject.current_user()
displayName = user['display_name']
followers = user['followers']['total']

# Loop to get information
while True:
    print()
    print(">>> Welcome to Spotify!" + displayName + "!")
    print(">>> You have " + str(followers) + " followers.")
    print()
    print("1 - Search for an artist")
    print("2 - Search for an album")
    print("3 - List your recent playlist")
    print("4 - New release playlist")
    print("0 - exit")
    print()
    choice = input("Your choice:")

    # Search for the artist
    if choice == "1":
        searchQuery = input("OK, what is artist name?: ")
        print()

        # Get search results
        searchResult = spotifyObject.search(searchQuery, 1,0,"artist")
        # print(json.dumps(searchResult, sort_keys=True, indent=4))

        # Artist details
        artist = searchResult['artists']['items'][0]
        artistID = artist['id']

        # Extract album data
        albumResults = spotifyObject.artist_albums(artistID)

        datas = []
        for item in albumResults['items']:
            print("ALBUM " + item['name'])
            albumID = item['id']

            # Extract track data
            trackResults = spotifyObject.album_tracks(albumID)

            for item in trackResults['items']:
                data = [albumID, item['name']]
                datas.append(data)
            print()

        write_csv(datas)

    # Search by key word
    if choice == "2":
        print()
        searchQuery = input("OK, what is the key word?: ")
        print()

        # get search result
        searchResult = spotifyObject.search(q=searchQuery, limit=50, offset=0, type='album')

        write_spotify_search_response_to_csv(searchResult)

    # Get current user's playlist
    if choice == "3":
        scope = ' '
        if token:
            spotifyObject.trace = False
            results = spotifyObject.current_user_playlists(limit = 50)
            print(json.dumps(results, sort_keys=True, indent=4))

            for i, item in enumerate(results['items']):
                print("%d %s" %(i, item['name']))
        else:
            print("can't get token for", username)

    # Get new released playlist
    if choice == "4":
        response = spotifyObject.new_releases()
        write_spotify_search_response_to_csv(response)


    # Exit program
    if choice == "0":
        break

