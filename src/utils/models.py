from enum import Enum
from pydantic import BaseModel
from integration.spotify import Spotify
from integration.youtube_music import YoutubeMusic


class Apps(Enum):
    YOUTUBE_MUSIC = YoutubeMusic
    SPOTIFY = Spotify


class App(BaseModel):
    app: Apps
    pl_code: str
    token: str
