import requests
from bs4 import BeautifulSoup
import urllib.parse
import json


class Spotify2YtMusic:
    def __init__(
        self,
        ytm_pl_code: str,
        ytm_token: str,
        spotify_pl_code: str,
        spotify_token: str,
    ) -> None:
        self.ytm_pl_code = ytm_pl_code
        self.ytm_token = ytm_token
        self.spotify_pl_code = spotify_pl_code
        self.spotify_token = spotify_token
        self.song_list = []

    def get_spotify_data(self) -> list:
        spotify_response = requests.get(
            url="https://open.spotify.com/playlist/" + self.spotify_pl_code,
            headers={"Content-Type": "application/json"},
        )
        site_html = BeautifulSoup(spotify_response.text, "html.parser")
        song_count = int(site_html.find("meta", attrs={"name": "music:song_count"}).get("content"))

        base_url = "https://api-partner.spotify.com/pathfinder/v1/query?"

        params = {
            "operationName": "fetchPlaylist",
            "variables": json.dumps(
                {
                    "uri": f"spotify:playlist:{self.spotify_pl_code}",
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
            headers={"Content-Type": "application/json", "Authorization": self.spotify_token},
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

        print(f"Conseguimos extrair estas musicas da sua playlist: {self.song_list}")
        return True

    def store_on_ytm(self) -> dict:
        for song in self.song_list:
            yt_search_response = requests.post(
                url="https://music.youtube.com/youtubei/v1/search?prettyPrint=false",
                data={
                    "query": song,
                    "params": "EgWKAQIIAWoKEAoQCRADEAQQBQ==",
                    "context": {"client": {"clientName": "WEB_REMIX", "clientVersion": "1.20240201.01.00"}},
                },
                headers={
                    "Content-Type": "application/json",
                    "Origin": "https://music.youtube.com",
                    "Referer": "https://music.youtube.com/",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
                }
            )
            site_html = BeautifulSoup(yt_search_response.text, "html.parser")
            url = site_html.select("obter o token da musica para inserir na playlist desejada")
            yt_append_response = requests.post(url=self.ytm_pl_url, headers={"Cookie": self.ytm_token})


def main():
    pls_spotify = {
        "bananamente": "https://open.spotify.com/playlist/0cSPaVnSIJNoAdZ9dBCtii",
        "latinoamericano": "https://open.spotify.com/playlist/1ekDXNNDveNj0sV4UR1CfF",
        "otaku": "https://open.spotify.com/playlist/6U6hclhZ7nefxZIh0gQfed",
        "tchuras": "https://open.spotify.com/playlist/7kOR9YoujNx4pwKdywLoxx",
    }
    pls_youtube = {"latinoamericano": "https://music.youtube.com/browse/VLPLYw2qF2LaIHkcDyYkoU2jLJYQGuDzT-Se"}

    spotify_pl = pls_spotify["tchuras"]
    ytm_pl = "https://music.youtube.com/browse/VLPLYw2qF2LaIHkcDyYkoU2jLJYQGuDzT-Se"
    spotify_pl_code = spotify_pl.split("/")[-1]
    ytm_pl_code = ytm_pl.split("/")[-1]
    ytm_token = ""
    spotify_token = "Bearer BQBTA9R0bxcibSG0YPUfswsQTCWDcIDpSvethudq-ItXfZlu0YtUGB9SGPIFmqcLHZoybMgABLbIHRSNmlKnw1BS8D6q36NtApY6WTcB3xOPulTDSD7zuwd6_tEz037-J38bNaRZHLc"
    app = Spotify2YtMusic(
        ytm_pl_code=ytm_pl_code, ytm_token=ytm_token, spotify_pl_code=spotify_pl_code, spotify_token=spotify_token
    )
    # extraction_success = app.get_spotify_data()
    # if extraction_success:
    app.store_on_ytm()


main()

# Mãe To na Balada - Ao Vivo
# botao de salvar
# ToDoList
# > buscar musica no ytm
# > inserir a musica na playlist desejada do ytm
