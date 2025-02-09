# Playlist Migrator
## Just for fun (and because I really need it)
### The free migrator you desperately need so you can stop paying for Spotify Premium and YouTube Premium at the same time


To use:
1. create your virtual environment
```bash
python -m venv .venv
```
2. install environment packages
```bash
pip install -r requirements.txt
```
3. open YoutubeMusic (must be authenticated) and Spotify and grab the cookies needed to fill your .env (they can be found at .env.example)
- [ ] SPOTIFY_TOKEN - Authorization: Bearer xxxxxxxx
- [ ] YOUTUBE_TOKEN - Authorization: SAPISIDHASH xxxxxxx
- [ ] SAPISID - SAPISID=xxxxxxx"
- [ ] PSID - __Secure-1PSID=xxxxxxx"
- [ ] PSIDTS -  __Secure-1PSIDTS=xxxxxxx"
4. on main.py fill the variables with the url from the Spotify playlist that you want to grab songs from and the url from the YoutubeMusic playlist that you want to store your songs at
- [ ] your_source_spotify_playlist
- [ ] your_destination_ytm_playlist
