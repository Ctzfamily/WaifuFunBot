from pyrogram import filters
import random 
from pyrogram.types import Message
from pyrogram.types.bots_and_keyboards.inline_keyboard_button import InlineKeyboardButton
from pyrogram.types.bots_and_keyboards.inline_keyboard_markup import InlineKeyboardMarkup
from nksama import bot

BOT_IMG = [ "https://telegra.ph/file/b3fbf990e0b67ede241a3.jpg",
           "https://telegra.ph/file/94865dae2576a2fa52732.jpg" ]

@bot.on_message(filters.command(["start"], ["/", ".", "?"]))
async def start(bot, m: Message):
    buttons = [
        [
            InlineKeyboardButton(
                "ADD ME", url="t.me/VegetaRobot?startgroup=true"
            ),
            InlineKeyboardButton(
                "Support", url=f"{SUPPORT_CHAT}"
            ),
        ]
    ]
    await m.reply_photo(
        random.choice(BOT_IMG),
        caption=text.format(m.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(buttons),
    )