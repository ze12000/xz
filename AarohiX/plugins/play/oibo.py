import asyncio
import os
import time
import requests
import aiohttp
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from AarohiX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AarohiX import app


@app.on_message(filters.command(["قول", "كول"], ""))
def elko(client: Client, message: Message):
    tet = message.text.split(None, 1)[1]
    message.reply(tet) 
