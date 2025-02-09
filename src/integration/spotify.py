import requests
import urllib.parse
from bs4 import BeautifulSoup
import json


class Spotify:
    def __init__(self, pl_code: str, token: str) -> None:
        self._pl_code = pl_code
        self._token = token
        self.song_list = []

    def fill_song_list(self) -> bool:
        spotify_response = requests.get(
            url="https://open.spotify.com/playlist/" + self._pl_code,
            headers={"Content-Type": "application/json"},
        )
        site_html = BeautifulSoup(spotify_response.text, "html.parser")
        song_count = int(site_html.find("meta", attrs={"name": "music:song_count"}).get("content"))

        base_url = "https://api-partner.spotify.com/pathfinder/v1/query?"

        params = {
            "operationName": "fetchPlaylist",
            "variables": json.dumps(
                {
                    "uri": f"spotify:playlist:{self._pl_code}",
                    "offset": 0,
                    "limit": song_count,
                    "enableWatchFeedEntrypoint": False,
                },
                separators=(",", ":"),
            ),
            "extensions": json.dumps(
                {
                    "persistedQuery": {
                        "version": 1,
                        "sha256Hash": "2c2c2a14cfa3a338a68af8010f0b044aa0d06a696035689f977b0f228d243ffc",
                    }
                },
                separators=(",", ":"),
            ),
        }

        api_response = requests.get(
            url=base_url + urllib.parse.urlencode(params),
            headers={"Content-Type": "application/json", "Authorization": self._token},
        )
        pl_data = json.loads(api_response.text)

        songs = []
        try:
            songs = pl_data["data"]["playlistV2"]["content"]["items"]
        except:
            print("Erro ao extrair músicas da playlist do Spotify")
            return False

        for song in songs:
            try:
                self.song_list.append(song["itemV2"]["data"]["name"])
            except:
                continue
        return True
