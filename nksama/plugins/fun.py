from pyrogram.types import Message
from pyrogram import filters
from nksama import bot, BOT_ID
import random

dnote = [ ]

deathnote_img = "https://telegra.ph/file/9e220eb59606f8435eafe.mp4"

@bot.on_message(filters.command('adddeathnote'))
def adddeathnote(_, m: Message):
    reply = m.reply_to_message
    if reply:
        dnote.append(reply.from_user.first_name)
        reply.reply_animation(deathnote_img,
                              caption="{} Added Death Note List!".format(reply.from_user.mention))
        
    else:
        m.reply_animation(deathnote_img,
                              caption="{} Added Death Note List!".format(m.from_user.mention))
  
@bot.on_message(filters.command('removedeathnote'))
def removedeathnote(_, m: Message):
    reply = m.reply_to_message
    if reply:
        dnote.remove(reply.from_user.first_name)
        reply.reply_animation(deathnote_img,
                              caption="{} Removed Death Note List!".format(reply.from_user.mention))
        
    else:
        m.reply("reply to Death Note list added person!")
  

@bot.on_message(filters.command('deathnotelist'))
def deathnotelist(_, m):
    reply = m.reply_to_message
    if reply:
        reply(str(dnote))
    else:
        m.reply(str(dnote))
        
        
@bot.on_message(filters.regex('good morning'))
def gm(_, m: Message):
    reply = m.reply_to_message
    if reply:
        m.reply(f"good morning! {reply.from_user.mention}")
    else:
        m.reply(f"good morning! {m.from_user.mention}")
 

@bot.on_message(filters.regex('good night'))
def gn(_, m: Message):
    reply = m.reply_to_message
    if reply:
        m.reply(f"good night! {reply.from_user.mention}")
    else:
        m.reply(f"good night! {m.from_user.mention}")
    
gbam_text = """
#GBANNED
**Froma Chat:** `{}`
**Admin:** {}
**User :** {}
**Reason:** `{}`
**Chat Count:** `{}`
"""
reason_text = [ "abusing",
                "spamming",
                "NSFW Spam",
                "no respecting",
                "gban me so I'm gbanned",
                "aasf friend",
                "aunty lover",
                "gang tag",
                "abuse pfp"
                "hentai pfp",
                "trolling" ]

@bot.on_message(filters.command(["gban", "gbam"]))
async def gbams(_, m: Message):
      reply = m.reply_to_message
      if not reply:
      await m.reply("reply someone: /gban or /gbam")
      user1 = m.from_user
      reason = random.choice(reason_text)
      count = random.randint(10,30)
      user2 = reply.from_user
      chat = m.chat
    if m.from_user == BOT_ID:
      await m.reply_text("nigga I can't gban myself")
      gbam = await m.reply("Gbaning...")
      await gbam.edit_text(gbam_text.format(chat.username,user1.mention,
                                            user2.mention,reason,count))
       
