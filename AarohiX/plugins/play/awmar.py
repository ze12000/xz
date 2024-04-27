import asyncio
import config
from pyrogram import Client, filters
from pyrogram import filters
from strings import get_command
from strings.filters import command
from AarohiX import app
from config.config import OWNER_ID
from AarohiX.misc import SUDOERS
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,InlineKeyboardMarkup, Message)
from AarohiX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AarohiX.misc import SUDOERS

@app.on_message(command(["الاوامر","اوامر البوت"]))
async def abrag(c: Client, m: Message):
    global mid
    mid = m.message_id
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("اوامر التشغيل", callback_data="awamry1" + str(m.from_user.id))] +
        [InlineKeyboardButton("اوامر البوت", callback_data="tasalyhh1 " + str(m.from_user.id))],
        [InlineKeyboardButton("تسليه١", callback_data="tasaly2 " + str(m.from_user.id))] +
        [InlineKeyboardButton("تسليه٢", callback_data="tslyaaa3 " + str(m.from_user.id))],
        [InlineKeyboardButton("التحشيش١", callback_data="tahsehh1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التحشيش٢", callback_data="tahshh2 " + str(m.from_user.id))],
        [InlineKeyboardButton("البنك", callback_data="bankkky " + str(m.from_user.id))],
        
        

    ])
    await m.reply_text("• مرحبآ بك عزيزي × قسم ( الزخرفه الجاهزه ) آنقر علي الازرار لآختيار برجك - 💠\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^awamry1 (\\d+)$"))
async def bioo1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    abrag_text = """♻️ | اليك اوامر المستخدمين
╼════⦗ ᥲ️᥎ᥲ️ƚᥲ️ᖇ ⦘════╾
✅ | تشغيل - لتشغيل ملف صوتي في القنوات  ، 

🎥 | /yt - تنزيل ملف صوتي من اليوتيوب  ، 

🔊 | مين في الكول - اضهار الموجودين في المكالمة ، 

🎞 | فيديو - تنزيل فيديو من اليوتيوب الجديد  ، 

🔇 | ايقاف - ايقاف الملف الصوتي المشغل الجديد  ، 

🐉 | تخطي - تخطي الملف الصوتي المشغل الجديد  ، 

🔢 | تكرار - عمل تكرار الى الملف الصوتي المشغل  ، 

🔰 | عشوائي - تشغيل الطابور عشوائياً المكالمة  ، 

📣 | يرجى دخول قناة السورس لمتابعة التحديثات ✓ ، 

╼═════⦗ ᥲ️᥎ᥲ️ƚᥲ️ᖇ ⦘═════╾
"""
    await m.message.reply_text(abrag_text, reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^tasalyhh1 (\\d+)$"))
async def bioo2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    abrag_text = """    
╼══════⦗ ᥲ️᥎ᥲ️ƚᥲ️ᖇ ⦘══════╾
🔇 | كتم ، 
🔊 | الغاء كتم ، 
🚫 | حظر ، 
✅ | الغاء حظر ، 
🔢 | احسب ، 
🐉 | زخارف ، 
📣 | انذار ، 
📿 | قران ، 
🕸 | الاسرع ،
╼══════⦗ ᥲ️᥎ᥲ️ƚᥲ️ᖇ ⦘══════╾"""
    await m.message.reply_text(abrag_text, reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^tasaly2 (\\d+)$"))
async def knwat1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    abrag_text = """╔━━━※ 𝙎𝙊𝙐𝙍𝘾𝙀 𝘼𝙑𝘼𝙏𝘼𝙍  ※━━━╗

🧊 | حجره  ، 
🍯 | احرف ، 
🥮 | انصحني  ، 
🍪 | اذكار  ، 
🍧 | زخارف  ، 
🥧 | كت  ، 
🚲 | اسال  ، 
🎪 | خيروك  ، 
🏭 | صور  ، 
🔓 | انمي  ، 
📐 | متحركه  ، 
⚱️| تلاوة  ، 
🗃️ | اقتباس  ، 
♻️ | هيدرا  ، 
🦺 | افاتار بنات  ، 

╚━━━※𝙎𝙊𝙐𝙍𝘾𝙀 𝘼𝙑𝘼𝙏𝘼𝙍※━━╝"""
    await m.message.reply_text(abrag_text, reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^tslyaaa3 (\\d+)$"))
async def bnat1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    abrag_text = """╼═════⦗ ᥲ️᥎ᥲ️ƚᥲ️ᖇ ⦘═════╾
👕 | صور شباب  ، 
🧣| سوره  ، 
🪡 | النقشبندي  ، 
🎰 | عبدالباسط عبدالصمد  ، 
🎛️ | استوري  ، 
🧵 | كتبات  ، 
⚡ | نكته  ، 
🌧️ |  صراحه  ، 
🎮 | العاب  ، 
🌖 | بنك  ، 
🌗 | الصاعدين  ، 
🐺 | المطور  ، 
🌠 | نادي المطور  ، 
🪐 | احسب  ، 
╼═════⦗ ᥲ️᥎ᥲ️ƚᥲ️ᖇ ⦘═════╾"""
    await m.message.reply_text(abrag_text, reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^tahsehh1 (\\d+)$"))
async def asmaa1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    abrag_text = """  ╼═════⦗ ᥲ️᥎ᥲ️ƚᥲ️ᖇ ⦘═════╾

ᚔᚔᚔ᚜ اوامر الرفع والتنزيل ᚛ᚔᚔᚔ

 | نمله
| المرفعوين نمل 
| رقاصه
| صرصار
| رقاصه 
| متناك
| نجس
| عره
| بقره
| قرد
| قلبي
| خدام
| معرص
| ارمله 
╼═════⦗ ᥲ️᥎ᥲ️ƚᥲ️ᖇ ⦘═════╾."""
    await m.message.reply_text(abrag_text, reply_to_message_id=mid)
    
    
@app.on_callback_query(filters.regex("^tahshh2 (\\d+)$"))
async def asmaa1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    abrag_text = """ ╼═════⦗ ᥲ️᥎ᥲ️ƚᥲ️ᖇ ⦘═════╾

ᚔᚔᚔ᚜ اوامر الرفع والتنزيل ᚛ᚔᚔᚔ

| مزه
| ابني 
| خاينه
| بنتي
| خاين
| خول 
| حمار
| غبي
| مراتي
| زبال
| خدامه
| كلبه
| طيز 
|حرامي
╼═════⦗ ᥲ️᥎ᥲ️ƚᥲ️ᖇ ⦘═════╾"""
    await m.message.reply_text(abrag_text, reply_to_message_id=mid)    
    
    
@app.on_callback_query(filters.regex("^bankkky (\\d+)$"))
async def asmaa1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    abrag_text = """━━━▰☛ 𝙎𝙊𝙐𝙍𝘾𝙀 𝘼𝙑𝘼𝙏𝘼𝙍 ☚▰━━━

🏦 اوامر لعبه البنك ⇊

👮‍♂️ « المطور » ⇊
━━━▰☛ 𝙎𝙊𝙐𝙍𝘾𝙀 𝘼𝙑𝘼𝙏𝘼𝙍 ☚▰━━━
➕╖ اضف فلوس + المبلغ «» ❬ بالرد علي الشخص المراد اضافه الفلوس له ❭
🗑╢ حذف حسابه «» ❬ بالرد علي الشخص المراد حذف حسابه ❭
❌╢ حذف حساب + اليوزر «» ❬ لحذف حساب الشخص ❭
😵╜ تصفير البنك «» ❬ لمسح كل الحسابات ❭

👨‍🦳 « الاعضاء » ⇊
━━━▰☛ 𝙎𝙊𝙐𝙍𝘾𝙀 𝘼𝙑𝘼𝙏𝘼𝙍 ☚▰━━━
📑╖ انشاء «» فتح حساب بنكي
🤑╢ فلوسي «» اموالي
💸╢ فلوسه «» امواله ❬ بالرد علي الشخص ❭
🏦╢ بنكي «» حسابي
💰╢ بنكه «» حسابه ❬ بالرد علي الشخص ❭
♻️╢ تحويل + المبلغ
☠️╢ كنز
🤖╢ استثمار + المبلغ
🍃╢ حظ + المبلغ
⏫╢ مضاعفه «» مضاربه + المبلغ
🎯╢ عجله الحظ
🤞╢ رشوه
🥺╢ بقشيش
⏳╢ راتب
📎╢ سرقه «» اسرق ❬ بالرد علي الشخص ❭
🚔╢ شرطه «» شرطة ❬ بالرد علي الشخص ❭
⭐️╢ حمايه اموالي «» ❬ لحمايه اموالك من السرقه ❭
👮╢ شرطه + اليوزر
💂‍♀️╢ توب الحراميه «» توب السرقه
⤴️╜ توب الفلوس «» توب فلوس


━━━▰☛ 𝙎𝙊𝙐𝙍𝘾𝙀 𝘼𝙑𝘼𝙏𝘼𝙍 ☚▰━━━"""
    await m.message.reply_text(abrag_text, reply_to_message_id=mid)