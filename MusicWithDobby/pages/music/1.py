import json 
import spotipy 
import webbrowser 
# https://accounts.spotify.com/en/login?continue=https%3A%2F%2Faccounts.spotify.com%2Fauthorize%3Fclient_id%3Dyour%2Bclient%2BID%26response_type%3Dcode%26redirect_uri%3Dhttp%253A%252F%252Fgoogle.com%252Fcallback%252F
username = '315iylipwytjrmrtx7cj3hfecxsi'
clientID = '786b703a4f3c4f7da2582611b7c9b471'
clientSecret = 'e60fe38eeebf42b7a37632e8fb117851'
redirect_uri = 'http://google.com/callback/'

oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirect_uri) 
token_dict = oauth_object.get_access_token() 
token = token_dict['access_token'] 
spotifyObject = spotipy.Spotify(auth=token) 
user_name = spotifyObject.current_user() 

# To print the JSON response from 
# browser in a readable format. 
# optional can be removed 
print(json.dumps(user_name, sort_keys=True, indent=4)) 
# https://accounts.spotify.com/authorize?client_id=786b703a4f3c4f7da2582611b7c9b471&response_type=code&redirect_uri=http%3A%2F%2Fgoogle.com%2Fcallback%2F
while True: 
	print("Welcome to the project, " + user_name['display_name']) 
	print("0 - Exit the console") 
	print("1 - Search for a Song") 
	user_input = int(input("Enter Your Choice: ")) 
	if user_input == 1: 
		search_song = input("Enter the song name: ") 
		results = spotifyObject.search(search_song, 1, 0, "track") 
		songs_dict = results['tracks'] 
		song_items = songs_dict['items'] 
		song = song_items[0]['external_urls']['spotify'] 
		webbrowser.open(song) 
		print('Song has opened in your browser.') 
	elif user_input == 0: 
		print("Good Bye, Have a great day!") 
		break
	else: 
		print("Please enter valid user-input.") 
