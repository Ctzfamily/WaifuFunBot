from pyrogram import filters
import random 
from pyrogram.types import Message
from pyrogram.types.bots_and_keyboards.inline_keyboard_button import InlineKeyboardButton
from pyrogram.types.bots_and_keyboards.inline_keyboard_markup import InlineKeyboardMarkup
from nksama import bot, SUPPORT_CHAT
from pyrogram.types import CallbackQuery


           
BOT_IMG = [ "https://telegra.ph/file/b3fbf990e0b67ede241a3.jpg",
           "https://telegra.ph/file/94865dae2576a2fa52732.jpg" ]
text = """
Hello! Dear {}

I'm An Anime themed Smart VegetaRobot make your group's
joyful Using /help commands!!

powered by @PegaBots
"""


@bot.on_message(filters.command(["start"], ["/", ".", "?"]))
async def start(_, m: Message):
    buttons = [
        [
            InlineKeyboardButton(
                "ADD ME", url="t.me/VegetaRobot?startgroup=true"),
            InlineKeyboardButton(
                "HELP", callback_data='help_back'),]]

    await m.reply_photo(
        random.choice(BOT_IMG),
        caption=text.format(m.from_user.mention),
        reply_markup=InlineKeyboardMarkup(buttons),
    )

          
HELP_TEXT = """
Hello! Dear {}

here my:\n**help and commands!**
"""

HELP_BUTTON = [[
        InlineKeyboardButton('Anime', callback_data='anime_help'),
        InlineKeyboardButton('Admin', callback_data='admin_help'),
        InlineKeyboardButton('Userinfo', callback_data='userinfo_help')]]

         
@bot.on_message(filters.command(["help"], ["/", ".", "?"]))
async def start(_, m: Message):
   await m.reply_text(HELP_TEXT.format(m.from_user.mention),
                      reply_markup=InlineKeyboardMarkup(HELP_BUTTON),)
           
  
@bot.on_callback_query(filters.regex("help_back"))
async def help(_, query: CallbackQuery):
    await query.message.edit_caption(HELP_TEXT.format(query.message.reply_to_message.from_user.mention),
                                    reply_markup=InlineKeyboardMarkup(HELP_BUTTON),)
               
        
