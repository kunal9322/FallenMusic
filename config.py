from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID","16743442"))
API_HASH = getenv("API_HASH","12bbd720f4097ba7713c5e40a11dfd2a")

BOT_TOKEN = getenv("BOT_TOKEN", "5935778941:AAG_Sn9YGJQnklXJ4M4KUcihXOSMeQ7TuwY")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://graph.org/file/391572b9bf7b02bbb7b2e.jpg")
START_IMG = getenv("START_IMG", "https://graph.org/file/391572b9bf7b02bbb7b2e.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Anime_Krew")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Anime_Campus")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5885920877").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
