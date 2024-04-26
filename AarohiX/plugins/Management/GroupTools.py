from pyrogram import enums
from pyrogram.enums import ChatType
from pyrogram import filters, Client
from AarohiX import app
from config import OWNER_ID
from pyrogram.types import Message
from AarohiX.utils.admin_check import admin_filter
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton



# ------------------------------------------------------------------------------- #


@app.on_message(filters.command(["المشرفين","الاشراف"], "")) & admin_filter)
async def pin(_, message):
    replied = message.reply_to_message
    chat_title = message.chat.title
    chat_id = message.chat.id
    user_id = message.from_user.id
    name = message.from_user.mention
    
    if message.chat.type == enums.ChatType.PRIVATE:
        await message.reply_text("**الامر في الجروبات بس**")
    elif not replied:
        await message.reply_text("**ريب علي الرساله ال عاوز تثبتها**")
    else:
        user_stats = await app.get_chat_member(chat_id, user_id)
        if user_stats.privileges.can_pin_messages and message.reply_to_message:
            try:
                await message.reply_to_message.pin()
                await message.reply_text(f"**◍ تم تثبيت الرساله\n**بواسطة:** {name}", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(" 📝 الرساله ", url=replied.link)]]))
            except Exception as e:
                await message.reply_text(str(e))


@app.on_message(filters.command(["التثبيت","المثبت"], ""))
async def pinned(_, message):
    chat = await app.get_chat(message.chat.id)
    if not chat.pinned_message:
        return await message.reply_text("**لا يوجد رسايل مثبته**")
    try:        
        await message.reply_text("الرسال المثبته مأخرا",reply_markup=
        InlineKeyboardMarkup([[InlineKeyboardButton(text="📝 اظهار الرساله",url=chat.pinned_message.link)]]))  
    except Exception as er:
        await message.reply_text(er)


# ------------------------------------------------------------------------------- #

@app.on_message(filters.command(["الغاء تثبيت","الغي تثبيت"], "")) & admin_filter)
async def unpin(_, message):
    replied = message.reply_to_message
    chat_title = message.chat.title
    chat_id = message.chat.id
    user_id = message.from_user.id
    name = message.from_user.mention
    
    if message.chat.type == enums.ChatType.PRIVATE:
        await message.reply_text("**الامر في الجروبات بس !**")
    elif not replied:
        await message.reply_text("**ريب علي الرساله ال عاوز تشيلها م التثبيت!**")
    else:
        user_stats = await app.get_chat_member(chat_id, user_id)
        if user_stats.privileges.can_pin_messages and message.reply_to_message:
            try:
                await message.reply_to_message.unpin()
                await message.reply_text(f"** تم الغاء تثبيت الرساله\n**بواسطة:** {name}", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(" 📝 اظهار الرساله ", url=replied.link)]]))
            except Exception as e:
                await message.reply_text(str(e))




# --------------------------------------------------------------------------------- #

@app.on_message(filters.command(["حذف صوره","ازاله صورة"], "")) & admin_filter)
async def deletechatphoto(_, message):
      
      chat_id = message.chat.id
      user_id = message.from_user.id
      msg = await message.reply_text("**جاري التحميل...**")
      admin_check = await app.get_chat_member(chat_id, user_id)
      if message.chat.type == enums.ChatType.PRIVATE:
           await msg.edit("**الامر في الجروبات بس! !**") 
      try:
         if admin_check.privileges.can_change_info:
             await app.delete_chat_photo(chat_id)
             await msg.edit("**تم حذف الصوره\nبواسطة** {}".format(message.from_user.mention))    
      except:
          await msg.edit("**❀ البوت ليس لديه صلاحيه تغيير المعلومات !**")


# --------------------------------------------------------------------------------- #

@app.on_message(filters.command(["وضع صوره","وضع صورة"], "")) & admin_filter)
async def setchatphoto(_, message):
      reply = message.reply_to_message
      chat_id = message.chat.id
      user_id = message.from_user.id
      msg = await message.reply_text("جاري التحميل...")
      admin_check = await app.get_chat_member(chat_id, user_id)
      if message.chat.type == enums.ChatType.PRIVATE:
           await msg.edit("`الامر في الجروبات بس!`") 
      elif not reply:
           await msg.edit("**❀ ريب علي الصوره لوضعها للجروب**")
      elif reply:
          try:
             if admin_check.privileges.can_change_info:
                photo = await reply.download()
                await message.chat.set_photo(photo=photo)
                await msg.edit_text("**تم وضع الصوره\nبواسطة** {}".format(message.from_user.mention))
             else:
                await msg.edit("**جرب صوره تانيه لقد حدث خطا!**")
     
          except:
              await msg.edit("**❀ البوت ليس لديه صلاحيه تغيير المعلومات**")


# --------------------------------------------------------------------------------- #

@app.on_message(filters.command(["وضع اسم","تغيير اسم"], "")) & admin_filter)
async def setgrouptitle(_, message):
    reply = message.reply_to_message
    chat_id = message.chat.id
    user_id = message.from_user.id
    msg = await message.reply_text("جاري التحميل...")
    if message.chat.type == enums.ChatType.PRIVATE:
          await msg.edit("**الامر في الجروبات بس !**")
    elif reply:
          try:
            title = message.reply_to_message.text
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_change_info:
               await message.chat.set_title(title)
               await msg.edit("**❀تم وضع الاسم بنجاح\nبواسطة** {}".format(message.from_user.mention))
          except AttributeError:
                await msg.edit("**❀ البوت ليس لديه صلاحيه تغيير المعلومات!**")   
    elif len(message.command) >1:
        try:
            title = message.text.split(None, 1)[1]
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_change_info:
               await message.chat.set_title(title)
               await msg.edit("**❀تم وضع الاسم بنجاح\nبواسطة** {}".format(message.from_user.mention))
        except AttributeError:
               await msg.edit("*❀ البوت ليس لديه صلاحيه تغيير المعلومات**")
          

    else:
       await msg.edit("**اعمل ريب علي الاسم ال عاوز تحطه**")


# --------------------------------------------------------------------------------- #



@app.on_message(filters.command(["وضع بايو","تغيير بايو"], "")) & admin_filter)
async def setg_discription(_, message):
    reply = message.reply_to_message
    chat_id = message.chat.id
    user_id = message.from_user.id
    msg = await message.reply_text("**جاري التحميل...**")
    if message.chat.type == enums.ChatType.PRIVATE:
        await msg.edit("**الامر في الجروبات بس !**")
    elif reply:
        try:
            discription = message.reply_to_message.text
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_change_info:
                await message.chat.set_description(discription)
                await msg.edit("**sᴜᴄᴄᴇssғᴜʟʟʏ ɴᴇᴡ ɢʀᴏᴜᴘ ᴅɪsᴄʀɪᴘᴛɪᴏɴ ɪɴsᴇʀᴛ!**\nʙʏ {}".format(message.from_user.mention))
        except AttributeError:
            await msg.edit("**❀ البوت ليس لديه صلاحيه تغيير المعلومات**")   
    elif len(message.command) > 1:
        try:
            discription = message.text.split(None, 1)[1]
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_change_info:
                await message.chat.set_description(discription)
                await msg.edit("**❀تم وضع البايو بنجاح\nبواسطة** {}".format(message.from_user.mention))
        except AttributeError:
            await msg.edit("**❀ البوت ليس لديه صلاحيه تغيير المعلومات**")
    else:
        await msg.edit("**اعمل ريب علي البايو ال عاوز تحطه للبار**")


# --------------------------------------------------------------------------------- #

@app.on_message(filters.command(["مغادرة","غادر"], ""))& filters.user(OWNER_ID))
async def bot_leave(_, message):
    chat_id = message.chat.id
    text = "**تم المغارده !!.**"
    await message.reply_text(text)
    await app.leave_chat(chat_id=chat_id, delete=True)


# --------------------------------------------------------------------------------- #
