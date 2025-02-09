import os

from integration.spotify import Spotify
from integration.youtube_music import YoutubeMusic
from models import App, Apps


class PlaylistMigrator:
    def __init__(self, destination: App, source: App) -> None:
        self.destination = destination
        self.source = source

    def exec(self) -> None:
        source_app: Spotify = source.app.value(pl_code=self.source.pl_code, token=self.source.token)
        source_app.fill_song_list()
        if source_app.song_list:
            destination_app: YoutubeMusic = destination.app.value(
                pl_code=self.destination.pl_code, token=self.destination.token
            )
            destination_app.save_songs_on_pl(song_list=source_app.song_list)


your_source_spotify_playlist="https://open.spotify.com/playlist/0cSPaVnSIJNoAdZ9dBCtii" # awesome sample
your_destination_ytm_playlist="https://music.youtube.com/browse/VLPLYw2qF2LaIHkFnW8vjQoilpSjKWg-sxvg" # awesome sample

spotify_pl_code = your_source_spotify_playlist.split("/")[-1]
ytm_pl_code = your_destination_ytm_playlist.split("/")[-1][2:]

source = App(app=Apps.SPOTIFY, pl_code=spotify_pl_code, token=os.getenv("SPOTIFY_TOKEN"))
destination = App(app=Apps.YOUTUBE_MUSIC, pl_code=ytm_pl_code, token=os.getenv("YOUTUBE_TOKEN"))

app = PlaylistMigrator(destination=destination, source=source)
app.exec()
