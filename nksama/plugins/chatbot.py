import re
import aiohttp
import requests
import asyncio


from pyrogram import filters
from time import time
from nksama import bot, SUPPORT_CHAT, BOT_ID
import nksama.plugins.sql.kuki_sql as sql



@bot.on_message(
    filters.command(["addchat", f"addchat@KomiSanRobot"])
)
async def addchat(_, message):
    chid = message.chat.id
    is_kuki = sql.is_kuki(chid)
    if not is_kuki:
        sql.set_kuki(int(message.chat.id))
        m.reply_text(
            f"kuki AI Successfully {message.chat.id}"
        )
    await asyncio.sleep(5)

@bot.on_message(
    filters.command(["rmchat", f"rmchat@KomiSanRobot"])
)
async def rmchat(_, message):
    chid = message.chat.id
    is_kuki = sql.is_kuki(chid)
    if not is_kuki:
        sql.rm_kuki(int(message.chat.id))
        m.reply_text(
            f" AI disabled successfully {message.chat.id}"
        )
    await asyncio.sleep(5)


@bot.on_message(
    filters.text
    & filters.reply
    & ~filters.bot
    & ~filters.edited
    & ~filters.via_bot
    & ~filters.forwarded,
    group=2,
)
async def kuki(_, message):
    try:
        chid = message.chat.id
        is_kuki = sql.is_kuki(chid)
        if not is_kuki:
            return
        if not message.reply_to_message:
            return
        try:
            moe = message.reply_to_message.from_user.id
        except:
            return
        if moe != BOT_ID:
            return
        text = message.text
        Kuki = requests.get(f"https://www.kukiapi.xyz/api/apikey=KUKIwrLK87gL6/kuki/moezilla/message={text}").json()
        nksamax = f"{Kuki['reply']}"
        if "Komi" in text or "komi" in text or "KOMI" in text:
            await bot.send_chat_action(chid, "typing")
        
        await message.reply_text(nksamax)
    
    except Exception as e:
        await bot.send_message(@{SUPPORT_CHAT}, f"error in chatbot:\n\n{e}")
