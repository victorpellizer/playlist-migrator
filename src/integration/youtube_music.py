import requests
import json
import os


class YoutubeMusic:
    def __init__(self, pl_code: str, token: str) -> None:
        self._pl_code = pl_code
        self._token = token

    def save_songs_on_pl(self, song_list: list) -> None:
        cookies = get_yt_cookies()
        for song in song_list:
            search_response = requests.post(
                url="https://music.youtube.com/youtubei/v1/search?prettyPrint=false",
                json={
                    "query": song,
                    "params": "EgWKAQIIAWoKEAoQCRADEAQQBQ==",
                    "context": {"client": {"clientName": "WEB_REMIX", "clientVersion": "1.20240201.01.00"}},
                },
                headers={
                    "Content-Type": "application/json",
                    "Origin": "https://music.youtube.com",
                    "Referer": "https://music.youtube.com/",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                },
            )
            response_dict = json.loads(search_response.text)
            try:
                video_id = response_dict["contents"]["tabbedSearchResultsRenderer"]["tabs"][0]["tabRenderer"][
                    "content"
                ]["sectionListRenderer"]["contents"][0]["musicShelfRenderer"]["contents"][0][
                    "musicResponsiveListItemRenderer"
                ]["overlay"]["musicItemThumbnailOverlayRenderer"]["content"]["musicPlayButtonRenderer"][
                    "playNavigationEndpoint"
                ]["watchEndpoint"]["videoId"]
            except:
                continue

            append_response = requests.post(
                url="https://music.youtube.com/youtubei/v1/browse/edit_playlist?prettyPrint=false",
                json={
                    "playlistId": self._pl_code,
                    "actions": [{"action": "ACTION_ADD_VIDEO", "addedVideoId": video_id}],
                    "context": {"client": {"clientName": "WEB_REMIX", "clientVersion": "1.20250204.03.00"}},
                },
                headers={
                    "Authorization": self._token,
                    "Content-Type": "application/json",
                    "Origin": "https://music.youtube.com",
                    "Referer": "https://music.youtube.com/",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                    "Cookie": cookies,
                },
            )
            if append_response.status_code == 200:
                print(f"A música {song} foi adicionada com sucesso!")
            else:
                print(f"Erro ao adicionar a música {song}!")


def get_yt_cookies() -> str:
    cookies = f"SAPISID={os.getenv('SAPISID')};"
    cookies += f"__Secure-1PAPISID={os.getenv('SAPISID')};"
    cookies += f"__Secure-1PSIDTS={os.getenv('PSIDTS')};"
    cookies += f"__Secure-1PSID={os.getenv('PSID')};"
    return cookies
