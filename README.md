This is a simple music recommendation tool that finds similar tracks using the Spotify Web API.

**Overview**  

This project is a small python program that takes a user-entered song and suggests similar tracks by the same artist.  
It uses the Spotify Web API and Spotipy library to authenticate, search for a track, and generate recommendations.   
My goal was to learn API usage, authentication, and practice data parsing in Python.  

**Tech Stack**  
Python 3.12, Spotipy (Web API Wrapper), and Spotify Developer Dashboard   

**Instructions** 
1. Install the required libraries
2. For security reasons **this project does not include spotify API credentials** To run the app locally:
     a. create a spotify developer account (free)  
     b. create an app and copy your client ID, client secret, and set your redirect URI to http://127.0.0.1:8080  
     c. create a .env file with the following variables (replace with your info)  
       SPOTIPY_CLIENT_ID=your_client_id_here  
       SPOTIPY_CLIENT_SECRET=your_client_secret_here  
       SPOTIPY_REDIRECT_URI=http://127.0.0.1:8080/callback  
3. Run the app from the terminal using: python recommend.py  

**What I Learned**  
- How to authenticate with OAuth  
- Using REST APIs in Python  
- How to handle user input and errors  

**Future V2 Improvements**    
- Better recommendation logic that recommends based on song makeup  
- Save results into a playlist  
- Allow user to confirm that the matched song was the song they intended   
