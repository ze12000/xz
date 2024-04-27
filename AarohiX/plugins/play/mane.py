import asyncio
from pyrogram import Client, filters
from datetime import datetime
from pyrogram import enums
from pyrogram.types import (Message,InlineKeyboardButton,InlineKeyboardMarkup,CallbackQuery,ChatPrivileges)
from AarohiX import app
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import ChatPermissions, ChatPrivileges
from config import *
from pyrogram.enums import ChatMembersFilter

welcome_enabled = True


@app.on_chat_member_updated()
async def welcome(client, chat_member_updated):
    if not welcome_enabled:
        return
    
    if chat_member_updated.new_chat_member.status == ChatMemberStatus.BANNED:
        kicked_by = chat_member_updated.new_chat_member.restricted_by
        user = chat_member_updated.new_chat_member.user
        
        if kicked_by is not None and kicked_by.is_self:
            messagee = f"• المستخدم {user.username} ({user.first_name}) تم طرده من الدردشة بواسطة البوت"
        else:
            if kicked_by is not None:
                message = f"• المستخدم [{user.first_name}](tg://user?id={user.id}) \n• تم طرده من الدردشة بواسطة [{kicked_by.first_name}](tg://user?id={kicked_by.id})\n• ولقد طردته بسبب هذا"
                try:
                    await client.ban_chat_member(chat_member_updated.chat.id, kicked_by.id)
                except Exception as e:
                    message += f"\n\nعذرًا، لم استطع حظر الإداري بسبب: {str(e)}"
            else:
                message = f"• المستخدم {user.username} ({user.first_name}) تم طرده من الدردشة"
            
            
        
        await client.send_message(chat_member_updated.chat.id, message)



@app.on_message(filters.command("رفع مشرف", "") & filters.channel)
async def tasfaya(client, message):
  ask = await app.ask(message.chat.id, "ارسل ايدي الان", timeout=300)
  ZOMBIE = ask.text
  chat_id = message.chat.id
  await app.promote_chat_member(
    chat_id=chat_id,
    user_id=ZOMBIE,
    privileges=ChatPrivileges(
    can_promote_members=False,
	can_manage_video_chats=True,
	can_post_messages=True,
	can_invite_users=True,
	can_edit_messages=True,
	can_delete_messages=True,
	can_change_info=False))
  await message.reply("تم رفع العضو مشرف بنجاح")


@app.on_message(filters.command("رفع مشرف", "") & filters.group)
async def tasfaya(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
    ahmed = await client.get_chat(message.from_user.id)
    zombie = ahmed.first_name
    usr = await client.get_users(message.reply_to_message.from_user.id)
    name = usr.first_name
    user_id = message.reply_to_message.from_user.id
    chat_id = message.chat.id
    await app.promote_chat_member(
    chat_id=chat_id,
    user_id=user_id,
    privileges=ChatPrivileges(
    can_promote_members=False,
	can_manage_video_chats=True,
	can_pin_messages=True,
	can_invite_users=True,
	can_restrict_members=True,
	can_delete_messages=True,
	can_change_info=True))
    await message.reply_text(f"• تم رفع العضو {name} \n※ بواسطه {zombie}")
