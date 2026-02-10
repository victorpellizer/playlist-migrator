import tkinter as tk

import frontend
from integration.spotify import Spotify
from integration.youtube_music import YoutubeMusic
from utils.functions import extract_yt_pl_code
from utils.models import App, Apps


class PlaylistMigrator:
    def __init__(self, destination: App, source: App) -> None:
        self.destination = destination
        self.source = source

    def exec(self) -> None:
        source_app: Spotify = self.source.app.value(pl_code=self.source.pl_code, token=self.source.token)
        source_app.fill_song_list()
        if source_app.song_list:
            destination_app: YoutubeMusic = self.destination.app.value(
                pl_code=self.destination.pl_code, token=self.destination.token
            )
            destination_app.save_songs_on_pl(song_list=source_app.song_list)


def submit():
    SPOTIFY_TOKEN = frontend.spotify_token_entry.get()
    YOUTUBE_TOKEN = frontend.ytm_token1_entry.get()
    SAPISID = frontend.ytm_token2_entry.get()
    PSID = frontend.ytm_token3_entry.get()
    PSIDTS = frontend.ytm_token4_entry.get()

    your_source_spotify_playlist = frontend.source_playlist_entry.get()
    your_destination_ytm_playlist = frontend.destination_playlist_entry.get()

    spotify_pl_code = your_source_spotify_playlist.split("/")[-1]
    ytm_pl_code = extract_yt_pl_code(your_destination_ytm_playlist)

    source = App(app=Apps.SPOTIFY, pl_code=spotify_pl_code, token=SPOTIFY_TOKEN)
    destination = App(app=Apps.YOUTUBE_MUSIC, pl_code=ytm_pl_code, token=YOUTUBE_TOKEN)

    app = PlaylistMigrator(destination=destination, source=source)
    app.exec()


submit_button = tk.Button(frontend.root, text="Start", command=submit)
submit_button.pack(pady=20)
frontend.root.mainloop()
