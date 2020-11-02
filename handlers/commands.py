import random
from time import sleep

from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from pyrogram.types import ChatPermissions



@Client.on_message(filters.command("start"))
def start(bot: Client, message: Message):
    #await message.reply_text(f"Hello MOTHER FUCKERS {message.from_user.mention}")
    tg_id = message.from_user.id
    print(message.text)
    msg = "HI HI HI "
    bot.send_message(tg_id, msg)


