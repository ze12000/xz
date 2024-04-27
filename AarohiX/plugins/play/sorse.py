import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from AarohiX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AarohiX import app
from random import  choice, randint

@app.on_message(
    filters.command(["سورس مين","سورس","السورس","سورسي", "افتار"], ""))
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/4fda78aaf200bf313be62.jpg",
        caption=f"""𝙎𝙊𝙐𝙍𝘾𝙀 𝘼𝙑𝘼𝙏𝘼𝙍""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                text="𝚂𝙾𝚄𝚁𝙲𝙴⁩", url=f"https://t.me/source_av"
                        ),
           InlineKeyboardButton(
                text="𝙶𝚁𝙾𝚄𝙿", url=f"https://t.me/S1SO0"
            ),
        ],

            ]

        ),

    )


@app.on_message(filters.command(["غنيلي", "غني", "غ", "🎙 ¦ غـنيـلي"], ""))
async def ihd(client: Client, message: Message):
    rl = random.randint(3,267)
    url = f"https://t.me/bsmaatt/{rl}"
    await client.send_voice(message.chat.id,url,caption="🔥 ¦ تـم اختيـار الاغـنـية لـك",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
                           )
