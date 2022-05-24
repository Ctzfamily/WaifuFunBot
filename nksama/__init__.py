from pyrogram import filters , Client
import os , time
from aiohttp import ClientSession
from Python_ARQ import ARQ
from telegraph import Telegraph
StartTime = time.time()

from nksama.config import *

#edit yourself nksama/config.py
OWNER_ID = OWNER_ID
LOG_GROUP_ID = LOG_GROUP_ID
BOT_USERNAME = BOT_USERNAME
SUPPORT_CHAT = SUPPORT_CHAT
UPDATES_CHANNEL = UPDATES_CHANNEL
ARQ_API_KEY = ARQ_API_KEY
ARQ_API_URL = ARQ_API_URL



#main vars set your deploying app
API_ID = os.environ.get("API_ID", None)
API_HASH = os.environ.get("API_HASH", None)
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
bot = Client("nksama", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, plugins=dict(root="{}/plugins".format(__name__)))


print("Bot is Working")

help_message = []
aiohttpsession = ClientSession()
arq = ARQ(ARQ_API_URL, ARQ_API_KEY, aiohttpsession)
telegraph = Telegraph()
telegraph.create_account(short_name=BOT_USERNAME)


dev_user = [1491497760]

