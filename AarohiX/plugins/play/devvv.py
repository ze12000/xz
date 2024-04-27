import json
from pyrogram import Client, filters
from pyrogram.enums import ChatMembersFilter
from pyrogram import enums
import json
from pyrogram import Client, filters


#############               #####                         ###                      ###
      ###                   ##         ##                     ###  ##             ##  ###
      ###                 ##             ##                   ###    ##         ##    ###
      ###               ##                 ##                 ###      ##     ##      ###
      ###                 ##             ##                   ###        ####         ###
      ###                   ##        ##                      ###                       ###
      ###                      #####                          ###                      ###



@app.on_message(filters.command("رفع مطور", ""))
def promote_devs(client, message):
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user_id = str(target)
    elif message.reply_to_message is None:
        target = message.text.split()[2]
        user = app.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            message.reply_text("لا يمكن العثور على المستخدم")
            return
    else:
        target = message.text.split()[1].strip("@")
        user = app.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            message.reply_text("لا يمكن العثور على المستخدم")
            return

    tom_devs = load_tom_devs()

    if (not TOM(client, message, message) and not basic_dev(client, message, message) and not OWNER_ID(client, message, message)):
        message.reply_text("""◍ انت لست المطور الثانوي
√""")
        return

    if user_id in tom_devs['devs']:
        message.reply_text("""◍ هذا المستخدم مطور بالفعل
√""")
    else:
        tom_devs['devs'][user_id] = True
        dump_tom_devs(tom_devs)
        message.reply_text("""◍ تم رفع المستخدم ليصبح مطور
√""")



@app.on_message(filters.command("المطورين", ""))
def get_devs(client, message):
    chat_id = str(message.chat.id)
    tom_devs = load_tom_devs()
    if (not TOM(client, message, message) and not basic_dev(client, message, message) and not OWNER_ID(client, message, message) and not dev(client, message, message)):
        message.reply_text("""◍ انت لست المطور
√""")
        return

    if 'devs' not in tom_devs:
        message.reply_text("لا يوجد مطورين حتى الأن")
        return

    admins = tom_devs['devs']
    if not admins:
        message.reply_text("لا يوجد مطورين حتى الأن")
    else:
        admin_names = []
        for admin_id in admins:
            user = app.get_users(int(admin_id))
            if user:
                admin_names.append(f"[{user.first_name}](tg://user?id={user.id})")

        if admin_names:
            admin_list = "\n".join(admin_names)
            message.reply_text(f"◍ قائمة المطورين:\n\n{admin_list}")
        else:
            message.reply_text("تعذر العثور على معلومات المطورين")



@app.on_message(filters.command("تنزيل مطور", ""))
def demote_devs(client, message):
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user_id = str(target)
    elif message.reply_to_message is None:
        target = message.text.split()[2]
        user = app.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            message.reply_text("لا يمكن العثور على المستخدم")
            return
    else:
        target = message.text.split()[1].strip("@")
        user = app.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            message.reply_text("لا يمكن العثور على المستخدم")
            return
    chat_id = str(message.chat.id)

    tom_devs = load_tom_devs()
    if (not TOM(client, message, message) and not basic_dev(client, message, message) and not OWNER_ID(client, message, message)):
        message.reply_text("""◍ انت لست المطور الثانوي
√""")
        return

    if user_id not in tom_devs['devs']:
        message.reply_text("""◍ هذا المستخدم ليس مطور لتنزيله
√""")
    else:
        del tom_devs['devs'][user_id]
        dump_tom_devs(tom_devs)
        message.reply_text("""◍ تم تنزيل المستخدم من المطورين بنجاح
√""")

@app.on_message(filters.command("مسح المطورين", ""))
def clear_devs(client, message):
    chat_id = str(message.chat.id)
    tom_devs = load_tom_devs()
    if (not TOM(client, message, message) and not basic_dev(client, message, message) and not OWNER_ID(client, message, message)):
        message.reply_text("""◍ انت لست المطور الثانوي
√""")
        return

    if 'devs' in tom_devs:
        tom_devs['devs'] = {}
        dump_tom_devs(tom_devs)
        message.reply_text("""◍ تم مسح المطورين بنجاح
√""")
    else:
        message.reply_text("لا يوجد مطورين ليتم مسحهم")

#############               #####                         ###                      ###
      ###                   ##         ##                     ###  ##             ##  ###
      ###                 ##             ##                   ###    ##         ##    ###
      ###               ##                 ##                 ###      ##     ##      ###
      ###                 ##             ##                   ###        ####         ###
      ###                   ##        ##                      ###                       ###
      ###                      #####                          ###                      ###