import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "12696592"))

API_HASH = getenv("API_HASH","de5edd6a410e89ba6c3fc85604fc3b57")

BOT_TOKEN = getenv("BOT_TOKEN","5636013818:AAF1Zco5j-j9Kl7TXmkYrDpJi4yxGv8rduI")

MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(
    getenv("DURATION_LIMIT", "90")
)

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180")
)

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001717661886"))

MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "UTOPIA'S MELODY")

OWNER_ID = list(
    map(int, getenv("OWNER_ID", "5358294860").split())
)

HEROKU_API_KEY = getenv("HEROKU_API_KEY")

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/otakubinge/VIVI-MUSIC-ROBOT",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")

GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv(
    "SUPPORT_CHANNEL", "https://t.me/kakashi_bots_updates")
SUPPORT_GROUP = getenv(
    "SUPPORT_GROUP", "https://t.me/kakashi_bots_support")

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")

AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))

TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "6"))

GITHUB_REPO = getenv("GITHUB_REPO", "https://github.com/otakubinge/VIVI-MUSIC-ROBOT")

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))

SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))

PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "7")
)

TG_AUDIO_FILESIZE_LIMIT = int(
    getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600")
)

TG_VIDEO_FILESIZE_LIMIT = int(
    getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824")
)
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION", "BQCpq4tJSqJeoZ1fcOqFhlBrxPjmCXLWsx2ODkaWGBvA3olT8t5dOhbmJDJxBww_Np0HFaCn5zUtpNy1LMOChSBOj37G_AsFcmy1SPsQxiA7q8VeeSwCoBuSUKx39Va9tCOuP1zTzJ-YzYPQAfuqXyUg-D_jX42AomWKWui6A01W7Ip3OzUaOOHtqzTnreQL7Jfd_wBkdZpR7PbcmsJSIrHR21K8EFxHJFGlb00nTzF0eAuQF8GjAR0VlSjQWA0RRlskVNu9nkSME41OUoT1yah_efFu9hAw6UiQAYIj10YYSvPlXxujYj6AYgQThCkV3AeiHzsKi_ehCCLOVgyR_LK1AAAAAT9hF0wA")
STRING2 = getenv("STRING_SESSION2", "BQAPGNCdu6TBm4p72RS0BSSaXUrr_HqviRlaGryNCm0hluU5lIOo6R5uOa73qxF88vzxAZZ0BWYxcL8cmIF0aW7OIkpv0R7Coh2OmQhIQZvAmm6TZAnBYfxTwVOn-cyXCByww3jrwMHjnsH3MpF-ZezPj-TsVNFT2SJEMuoKNCcaZicbL0ujoKGYv5fuInqp8J5MruBoPWYFisnW1Ajb3r0NM0gT6VXqgrznUGAAIT21FPvXDz70bgKw6YbZ303c2gUevsSC70xfi2NeF7pt-H5fnfczySjSbfWGxs-BBrOBYWWruwkxBfsw3fuOWgmRteQhVWH5hnMx3yb_fiV9iyxMAAAAAT9hF0wA")
STRING3 = getenv("STRING_SESSION3", "BQDDbdgoWlRz-e7czHVCXgcWNyd867N3NE4Xduv4gsWAzBcXxNtglKsBLJW7C3Mxfm1TJz9g2sJjFaKG7FYR3qKzGKrLMIaCaW0jybTrjFL4RU7VNtYxhALNwfAECiYcJujQ_u_ClJhczBHRJb_snxwoMlhbKI1IxgrwqLJBBqVI8whpV83-2N4H99XrzTrwsJF4XjamtaOiFYOgBmtd6jx4BmkLxC9myeNq4AixSJAqyRrfvZb3vnPmX8ltxR_CV_wo1m_kUpwsFmMlA1aQjeVIWXwrM8-tfvsOnvdE1L_PLyyGADYoMVMjB4FZo5SVmgViEjf8Zd6qQT0lGbllPTrVAAAAAT9hF0wA")
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "VIVIlogs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = getenv("START_IMG_URL", "https://telegra.ph/file/4a8ab226fba0b46a1f33e.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://telegra.ph/file/1fb934326ef84ffd7f322.jpg",
)

PLAYLIST_IMG_URL = getenv(
    "PLAYLIST_IMG_URL",
    "assets/Playlist.jpeg",
)

GLOBAL_IMG_URL = getenv(
    "GLOBAL_IMG_URL",
    "assets/Global.jpeg",
)

STATS_IMG_URL = getenv(
    "STATS_IMG_URL",
    "assets/Stats.jpeg",
)

TELEGRAM_AUDIO_URL = getenv(
    "TELEGRAM_AUDIO_URL",
    "assets/Audio.jpeg",
)

TELEGRAM_VIDEO_URL = getenv(
    "TELEGRAM_VIDEO_URL",
    "assets/Video.jpeg",
)

STREAM_IMG_URL = getenv(
    "STREAM_IMG_URL",
    "assets/Stream.jpeg",
)

SOUNCLOUD_IMG_URL = getenv(
    "SOUNCLOUD_IMG_URL",
    "assets/Soundcloud.jpeg",
)

YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL",
    "assets/Youtube.jpeg",
)

SPOTIFY_ARTIST_IMG_URL = getenv(
    "SPOTIFY_ARTIST_IMG_URL",
    "assets/SpotifyArtist.jpeg",
)

SPOTIFY_ALBUM_IMG_URL = getenv(
    "SPOTIFY_ALBUM_IMG_URL",
    "assets/SpotifyAlbum.jpeg",
)

SPOTIFY_PLAYLIST_IMG_URL = getenv(
    "SPOTIFY_PLAYLIST_IMG_URL",
    "assets/SpotifyPlaylist.jpeg",
)


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)

SUPPORT_HEHE = SUPPORT_GROUP.split("me/")[1]


if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            print(
                "[ERROR] - Your PING_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if PLAYLIST_IMG_URL:
    if PLAYLIST_IMG_URL != "assets/Playlist.jpeg":
        if not re.match("(?:http|https)://", PLAYLIST_IMG_URL):
            print(
                "[ERROR] - Your PLAYLIST_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if GLOBAL_IMG_URL:
    if GLOBAL_IMG_URL != "assets/Global.jpeg":
        if not re.match("(?:http|https)://", GLOBAL_IMG_URL):
            print(
                "[ERROR] - Your GLOBAL_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if STATS_IMG_URL:
    if STATS_IMG_URL != "assets/Stats.jpeg":
        if not re.match("(?:http|https)://", STATS_IMG_URL):
            print(
                "[ERROR] - Your STATS_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if TELEGRAM_AUDIO_URL:
    if TELEGRAM_AUDIO_URL != "assets/Audio.jpeg":
        if not re.match("(?:http|https)://", TELEGRAM_AUDIO_URL):
            print(
                "[ERROR] - Your TELEGRAM_AUDIO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if STREAM_IMG_URL:
    if STREAM_IMG_URL != "assets/Stream.jpeg":
        if not re.match("(?:http|https)://", STREAM_IMG_URL):
            print(
                "[ERROR] - Your STREAM_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if SOUNCLOUD_IMG_URL:
    if SOUNCLOUD_IMG_URL != "assets/Soundcloud.jpeg":
        if not re.match("(?:http|https)://", SOUNCLOUD_IMG_URL):
            print(
                "[ERROR] - Your SOUNCLOUD_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if YOUTUBE_IMG_URL:
    if YOUTUBE_IMG_URL != "assets/Youtube.jpeg":
        if not re.match("(?:http|https)://", YOUTUBE_IMG_URL):
            print(
                "[ERROR] - Your YOUTUBE_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if TELEGRAM_VIDEO_URL:
    if TELEGRAM_VIDEO_URL != "assets/Video.jpeg":
        if not re.match("(?:http|https)://", TELEGRAM_VIDEO_URL):
            print(
                "[ERROR] - Your TELEGRAM_VIDEO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()
