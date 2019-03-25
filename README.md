# SpotifySearch
This is a project to get records from spotify by artist, keyword, or new relase

**A. Set your Spotify Account and Developer Application**

1. At first, you have to register an account at : https://developer.spotify.com
2. Then get into the dashboard, create a new app, give it a name. There are *client ID* and *client Secret*, that will be access key.
3. In the Edit setting, change the RedirectURIs to : http://google.com/ (or localhost), save it.
4. In the your local Spotify player, get into your personal account, find profile link, and see unique User ID : xxxxx in the link "https://open.spotify.com/user/xxxxxxxxx"
5. Then in the terminal, get into your project folder (the folder includes this spotifyTest.py)
6. In the terminal, input :
        $ export SPOTIPY_CLIENT_ID = '(Input your *client ID*)'
        $ export SPOTIPY_CLIENT_SECRET = '(Input your *client Secret*)'
        $ export SPOTIPY_REDIRECT_URI='http://google.com/'

**B. Running project : Four options**

7. In the terminal, after authentication, run this project by:
        $ python3 spotifyTest.py
   Then you will be redirect to a web page.
   Click OK, give permission to spotify.
   Copy the link "https://google.com/xxxxxxxxxx" and paste to the terminal
        $ Enter the URL you were redirected to: (Paste here)
8. There are five options:
    * a. search an artist's all album list
    * b. search albums have a key word (input)
    * c. get yourself recent playlist
    * d. new released playlist
    * e. exit 
9. For the option a, b, d, the result will be saved as a ".csv" file
    * a. The name you input must be as same as spotify has. such as : Tylor Swift, Katy Perry
    * b. It is better to be a "complex" word, not only "he ,she, love, cat, dog...", but something special
    * c. Sometimes, people don't have recent playlist(like me, because I use other player)
    * d. the raw data will have 500 rows, but I cut 100 rows
    * e. noting, just exit it

**C. Note**

* sometimes, you have to try twice to get connection
* you can edit the limitation to control the rows you like
* you can edit the output content as you like
