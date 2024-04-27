from pyromod import listen
from random import choice, randint 
from pyrogram import Client, filters 
from AarohiX import app
from pyrogram.types import (
  InlineKeyboardMarkup,
  InlineKeyboardButton,
  CallbackQuery
)


   
AUT = [
  "https://telegra.ph/file/5c0875dfcffe3e9a5df8b.jpgZAIDاصالة",
  "https://telegra.ph/file/6eb251808382289632226.jpgZAIDتامر حسني",
  "https://telegra.ph/file/94131da89e97781e08772.jpgZAIDنانسي عجرم",
  "https://telegra.ph/file/eed0d7ff96194a8f8c2d7.jpgZAIDاليسا",
  "https://telegra.ph/file/79de290d7131bd2343c50.jpgZAIDهيفاء وهبي",
  "https://telegra.ph/file/47b584756e5c7c84e0bad.jpgZAIDشيرين",
  "https://telegra.ph/file/56def78a3f3b78b3515ac.jpgZAIDحسين الجسمي",
  "https://telegra.ph/file/478423ba1b724269b71ab.jpgZAIDعمرو دياب",
  "https://telegra.ph/file/2364efe0dd00116830480.jpgZAIDكاظم الساهر",
  "https://telegra.ph/file/5f0de633a64e7b28d2b46.jpgZAIDناصيف زيتون",
  "https://telegra.ph/file/5b3abd2874d41d8d3bbc8.jpgZAIDتامر عاشور",
  "https://telegra.ph/file/a06b89e8e3a9c66707e78.jpgZAIDمحمد صلاح",
  "https://telegra.ph/file/6f6622b0e345a624e94e9.jpgZAIDكرستيانو رونالدو",
  "https://telegra.ph/file/2c11bfdab09589eddb542.jpgZAIDمحمد رمضان",
  "https://telegra.ph/file/10f7ddbd1779f6bcc9df8.jpgZAIDوائل جسار"
]

@app.on_message(filters.regex("مشاهير"))
async def game_2(client, message):
   photoo = choice(AUT)
   photo = photoo.split("ZAID")[0]
   print(photo)
   author = photoo.split("ZAID")[1]
   print(author)
   x = await message.reply_photo(
     photo
   )
   re = f"^{author}$"
   ASK = await app.ask(
     message.chat.id,
     "اسرع واحد يرسل أسم الفنان",
     reply_to_message_id=x.id,
     filters=filters.regex(re)
   )
   await ASK.reply(
    f"كفو {ASK.from_user.mention} اجابتك صحيحة"
   )
   
EMO = [
  "👞:حذاء",
  "⭐:نجمة",
  "🕞:ساعة",
  "🍑:خوخ",
  "🛢️:نفط",
  "🎂:كيكة",
  "⚽:كورة",
  "🩳:شورت",
  "📒:دفتر",
  "🌹:وردة",
  "✏️:قلم",
  "🔥:نار",
  "💸:فلوس",
  "💻:لاب"
]
@app.on_message(filters.regex("معاني"))
async def game_3(client, message):
   A = choice(EMO)
   emo = A.split(":")[0]
   print(emo)
   ans = A.split(":")[1]
   print(ans)
   re = f"^{ans}$"
   ASK = await app.ask(
     message.chat.id,
     "اسرع واحد يرسل معنى الايموجي {}".format(emo),
     reply_to_message_id=message.id,
     filters=filters.regex(re)
   )
   await ASK.reply(
    f"كفو {ASK.from_user.mention} اجابتك صحيحة"
   )
   
FLAGS = [
  "🇦🇪:الامارات",
  "🇧🇭:البحرين",
  "🇪🇬:مصر",
  "🇮🇶:العراق",
  "🇱🇧️:لبنان",
  "🇱🇺:لوكسمبورغ",
  "🇵🇰:باكستان",
  "🇹🇷:تركيا",
  "🇾🇪:اليمن",
  "🇸🇩:السودان",
  "🇸🇦:السعودية",
  "🇵🇸:فلسطين",
  "🇴🇲:سلطنة عمان",
  "🇯🇵:اليابان"
]
@app.on_message(filters.regex("اعلام دول"))
async def game_4(client, message):
   A = choice(FLAGS)
   emo = A.split(":")[0]
   print(emo)
   ans = A.split(":")[1]
   print(ans)
   re = f"^{ans}$"
   ASK = await app.ask(
     message.chat.id,
     "اسرع واحد يرسل اسم الدولة {}".format(emo),
     reply_to_message_id=message.id,
     filters=filters.regex(re)
   )
   await ASK.reply(
    f"كفو {ASK.from_user.mention} اجابتك صحيحة"
   )
