import random, asyncio
from pyrogram import Client as lucifermoringstar_robot , filters, enums
from LuciferMoringstar_Robot import temp, SUPPORT, PICS, ADMINS, CREATOR_USERNAME, CREATOR_NAME, AUTH_CHANNEL, CUSTOM_FILE_CAPTION, SAVE_FILES, START_MESSAGE
from LuciferMoringstar_Robot.translation import SETTINGS_MESSAGE, ADMIN_CMD_MESSAGE, ABOUT_MESSAGE, USAGE_MESSAGE
from LuciferMoringstar_Robot.functions import get_settings, save_group_settings
from LuciferMoringstar_Robot.admins.broadcast import send_broadcast
from LuciferMoringstar_Robot.functions import send_msg
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserNotParticipant
from database.connections_mdb import active_connection
from database.chats_users_mdb import db
from database.autofilter_mdb import get_file_details
from LuciferMoringstar_Robot.functions import get_size

@lucifermoringstar_robot.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot: lucifermoringstar_robot, update):

    if not await db.is_user_exist(update.from_user.id):
        await db.add_user(update.from_user.id)

    if update.text.startswith("/start muhammedrk"):
        if AUTH_CHANNEL:
            invite_link = await bot.create_chat_invite_link(int(AUTH_CHANNEL))
            try:
                user = await bot.get_chat_member(int(AUTH_CHANNEL), update.from_user.id)
                if user.status == enums.ChatMemberStatus.RESTRICTED:
                    await bot.send_message(chat_id=update.from_user.id, text="""ππΎπππ ππΈπ, ππΎπ π°ππ΄ π±π°π½π½π΄π³ ππΎ πππ΄ πΌπ΄""", disable_web_page_preview=True)                  
                    return
            except UserNotParticipant:
                mrk, file_id = update.text.split("-mo-tech-group-")
                FORCES = ["https://telegra.ph/file/b2acb2586995d0e107760.jpg"]
                invite_link = await bot.create_chat_invite_link(int(AUTH_CHANNEL))
                pr0fess0r_99 = [[ InlineKeyboardButton("π° πΉπΎπΈπ½ πΌπ π²π·π°π½π½π΄π» π°", url=invite_link.invite_link) ],
                                [ InlineKeyboardButton("π πππ π°πΆπ°πΈπ½ π", callback_data=f"luciferPM#{file_id}") ]]
                pr0fess0r_99 = InlineKeyboardMarkup(pr0fess0r_99)
                await update.reply_photo(photo=random.choice(FORCES), caption=f"""<i><b>π·π΄π»π»πΎ {update.from_user.mention}. \n ππΎπ π·π°ππ΄ <a href="{invite_link.invite_link}"> π½πΎπ πππ±ππ²ππΈπ±π΄π³</a> ππΎ <a href="{invite_link.invite_link}">πΌπ ππΏπ³π°ππ΄ π²π·π°π½π½π΄π»</a>.ππΎ ππΎπ π³πΎ π½πΎπ πΆπ΄π ππ·π΄ π΅πΈπ»π΄π πΎπ½ π±πΎπ πΏπΌ πΎπ πΆππΎππΏ (π΅πΈπ»ππ΄π)</i></b>""", reply_markup=pr0fess0r_99)                
                return
        try:
            mrk, file_id = update.text.split("-mo-tech-group-")
            file_details_pr0fess0r99 = await get_file_details(file_id)
            for mrk in file_details_pr0fess0r99:
                title = mrk.file_name
                size = get_size(mrk.file_size)
                await bot.send_cached_media(chat_id=update.from_user.id, file_id=file_id, caption=CUSTOM_FILE_CAPTION.format(mention=update.from_user.mention, file_name=title, size=size, caption=mrk.caption), protect_content=SAVE_FILES)
        except Exception as error:
            await update.reply_text(f"ππΎπΌπ΄ππ·πΈπ½πΆ ππ΄π½π πππΎπ½πΆ.!\n\nπ΄πππΎπ:`{error}`")

    if len(update.command) ==2 and update.command[1] in ["subscribe"]:
        FORCES = ["https://telegra.ph/file/b2acb2586995d0e107760.jpg"]
        invite_link = await bot.create_chat_invite_link(int(AUTH_CHANNEL))
        pr0fess0r_99 = [[ InlineKeyboardButton("π SUBSCRIBE π", url=invite_link.invite_link) ]]
        pr0fess0r_99 = InlineKeyboardMarkup(pr0fess0r_99)
        await update.reply_photo(photo=random.choice(FORCES), caption=f"""<i><b>π·π΄π»π»πΎ {update.from_user.mention}. \n ππΎπ π·π°ππ΄ <a href="{invite_link.invite_link}"> π½πΎπ πππ±ππ²ππΈπ±π΄π³</a> ππΎ <a href="{invite_link.invite_link}">πΌπ ππΏπ³π°ππ΄ π²π·π°π½π½π΄π»</a>.ππΎ ππΎπ π³πΎ π½πΎπ πΆπ΄π ππ·π΄ π΅πΈπ»π΄π πΎπ½ π±πΎπ πΏπΌ, ππΈπ° π°π½π³ πΆππΎππΏ (π΅πΈπ»ππ΄π)</i></b>""", reply_markup=pr0fess0r_99)
        return

    if len(update.command) != 2:
        pr0fess0r_99 = [[ InlineKeyboardButton("Γ π°π³π³ πΌπ΄ ππΎ ππΎππ πΆππΎππΏ Γ", url=f"http://t.me/{temp.Bot_Username}?startgroup=true") ],
                        [ InlineKeyboardButton("πππΏπΏπΎππ π¬", url=f"t.me/{SUPPORT}"), InlineKeyboardButton("ππΏπ³π°ππ΄π π’", url="t.me/Mo_Tech_YT") ],
                        [ InlineKeyboardButton("βΉοΈ π·π΄π»πΏ", callback_data="help"), InlineKeyboardButton("π°π±πΎππ π€ ", callback_data="about") ]] 
        await bot.send_photo(photo=random.choice(PICS), chat_id=update.chat.id, caption=START_MESSAGE.format(mention=update.from_user.mention, name=temp.Bot_Name, username=temp.Bot_Username), reply_markup=InlineKeyboardMarkup(pr0fess0r_99))

@lucifermoringstar_robot.on_message(filters.command(["admin", "admins"]) & filters.user(ADMINS) & filters.private, group=2)
async def admin(bot: lucifermoringstar_robot, update):
    await bot.send_photo(photo=random.choice(PICS), chat_id=update.chat.id, caption=ADMIN_CMD_MESSAGE, reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("Γ π²π»πΎππ΄ Γ", callback_data="close") ]] ))

@lucifermoringstar_robot.on_message(filters.command(["about"]) & filters.private, group=3)
async def about(bot: lucifermoringstar_robot, update):
    pr0fess0r_99 = [[ InlineKeyboardButton("π·πΎπΌπ΄", callback_data="start"), InlineKeyboardButton("π·πΎπ ππΎ πππ΄", callback_data="usage"), InlineKeyboardButton("π²π»πΎππ΄", callback_data="close") ]]                     
    await bot.send_photo(photo=random.choice(PICS), chat_id=update.chat.id, caption=ABOUT_MESSAGE.format(name = CREATOR_NAME, username = CREATOR_USERNAME, py3_version = temp.PY3_VERSION, pyro_version = temp.PYRO_VERSION, version = temp.BOT_VERSION), reply_markup=InlineKeyboardMarkup(pr0fess0r_99))

@lucifermoringstar_robot.on_message(filters.command(["usage"]) & filters.private, group=4)
async def usage(bot: lucifermoringstar_robot, update):
    pr0fess0r_99 = [[ InlineKeyboardButton("ποΈ π³π΄π»π΄ππ΄ ποΈ", callback_data="close") ]]
    await bot.send_photo(photo=random.choice(PICS), chat_id=update.chat.id, caption=USAGE_MESSAGE.format(CREATOR_NAME, CREATOR_USERNAME), reply_markup=InlineKeyboardMarkup(pr0fess0r_99))

@lucifermoringstar_robot.on_message(filters.command(["broadcast"]) & filters.user(ADMINS) & filters.private, group=5)
async def broadcast(bot: lucifermoringstar_robot, update):
    await send_broadcast(bot, update, db, send_msg, temp)

@lucifermoringstar_robot.on_message((filters.private | filters.group) & filters.command('settings'), group=5)
async def settings(bot, update):
    userid = update.from_user.id if update.from_user else None
    if not userid:
        return await update.reply_text(f"ππΎππ π°ππ΄ π°π½πΎπ½ππΌπΎππ π°π³πΌπΈπ½. /connect {update.chat.id} πΈπ½ πΏπΌ")
    chat_type = update.chat.type
    if chat_type == enums.ChatType.PRIVATE:
        grpid = await active_connection(str(userid))
        if grpid is not None:
            grp_id = grpid
            try:
                chat = await bot.get_chat(grpid)
                title = chat.title
            except:
                await update.reply_text("πΌπ°πΊπ΄ ππππ΄ πΈπ°πΌ πΏππ΄ππ΄π½π πΈπ½ ππΎππ πΆππΎππΏ..!", quote=True)
                return
        else:
            await update.reply_text("πΈπ°πΌ π½πΎπ π²πΎπ½π½π΄π²ππ΄π³ π°π½π πΆππΎππΏ..!", quote=True)
            return

    elif chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        grp_id = update.chat.id
        title = update.chat.title
    else:
        return

    mrk = await bot.get_chat_member(grp_id, userid)
    if (mrk.status != enums.ChatMemberStatus.ADMINISTRATOR and mrk.status != enums.ChatMemberStatus.OWNER and userid not in ADMINS):
        return

    settings = await get_settings(grp_id)

    if settings is not None:
        buttons = [[ InlineKeyboardButton('π΅πΈπ»ππ΄π π±ππππΎπ½', callback_data=f'settings#button#{settings["button"]}#{grp_id}'), InlineKeyboardButton('ππΈπ½πΆπ»π΄' if settings["button"] else 'π³πΎππ±π»π΄', callback_data=f'settings#button#{settings["button"]}#{grp_id}') ],
                   [ InlineKeyboardButton('ππ΄π»π²πΎπΌπ΄ πΌππΆ', callback_data=f'settings#welcome#{settings["welcome"]}#{grp_id}'), InlineKeyboardButton('πΎπ½' if settings["welcome"] else 'πΎπ΅π΅', callback_data=f'settings#welcome#{settings["welcome"]}#{grp_id}') ],         
                   [ InlineKeyboardButton('ππΏπ΄π»π» π²π·π΄π²πΊ', callback_data=f'settings#spellmode#{settings["spellmode"]}#{grp_id}'), InlineKeyboardButton('πΎπ½' if settings["spellmode"] else 'πΎπ΅π΅', callback_data=f'settings#spellmode#{settings["spellmode"]}#{grp_id}') ],          
                   [ InlineKeyboardButton('π±πΎπ πΏπΎπππ΄π', callback_data=f'settings#photo#{settings["photo"]}#{grp_id}'), InlineKeyboardButton('πΎπ½' if settings["photo"] else 'πΎπ΅π΅', callback_data=f'settings#photo#{settings["photo"]}#{grp_id}') ],
                   [ InlineKeyboardButton('ππ°ππ΄ π΅πΈπ»π΄π', callback_data=f'settings#savefiles#{settings["savefiles"]}#{grp_id}'), InlineKeyboardButton('πΎπ½' if settings["savefiles"] else 'πΎπ΅π΅', callback_data=f'settings#savefiles#{settings["savefiles"]}#{grp_id}') ],
                   [ InlineKeyboardButton('π΅πΈπ»π΄ πΌπΎπ³π΄', callback_data=f'settings#filemode#{settings["filemode"]}#{grp_id}'), InlineKeyboardButton('πΏπΌ' if settings["filemode"] else 'π²π·π°π½π½π΄π»', callback_data=f'settings#filemode#{settings["filemode"]}#{grp_id}') ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await update.reply_text(text=SETTINGS_MESSAGE.format(title=title), reply_markup=reply_markup, disable_web_page_preview=True, reply_to_message_id=update.id)
        
@lucifermoringstar_robot.on_message((filters.private | filters.group) & filters.command('set_temp'), group=6)
async def save_template(bot, update):
    sts = await update.reply_text("β³οΈ")
    await asyncio.sleep(0.3)
    userid = update.from_user.id if update.from_user else None
    if not userid:
        return await update.reply_text(f"ππΎππ π°ππ΄ π°π½πΎπ½ππΌπΎππ π°π³πΌπΈπ½. /connect {update.chat.id} πΈπ½ πΏπΌ")
    chat_type = update.chat.type
    if chat_type == enums.ChatType.PRIVATE:
        grpid = await active_connection(str(userid))
        if grpid is not None:
            grp_id = grpid
            try:
                chat = await bot.get_chat(grpid)
                title = chat.title
            except:
                await update.reply_text("πΌπ°πΊπ΄ ππππ΄ πΈπ°πΌ πΏππ΄ππ΄π½π πΈπ½ ππΎππ πΆππΎππΏ..!", quote=True)
                return
        else:
            await update.reply_text("πΈπ°πΌ π½πΎπ π²πΎπ½π½π΄π²ππ΄π³ π°π½π πΆππΎππΏ..!", quote=True)
            return

    elif chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        grp_id = update.chat.id
        title = update.chat.title
    else:
        return

    motechyt = await bot.get_chat_member(grp_id, userid)
    if (motechyt.status != enums.ChatMemberStatus.ADMINISTRATOR and motechyt.status != enums.ChatMemberStatus.OWNER and userid not in ADMINS):
        return

    if len(update.command) < 2:
        return await sts.edit("π·πΎπ ππΎ πππ΄ ππ·πΈπ π²πΎπΌπΌπ°π½π³..!", reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("π²π»πΈπ²πΊ π·π΄ππ΄", callback_data="autofilter") ]] ))

    pr0fess0r_99 = update.text.split(" ", 1)[1]
    await save_group_settings(grp_id, 'template', pr0fess0r_99)
    await sts.edit(f"""πππ²π²π΄πππ΅ππ»π»π π²π·π°π½πΆπ΄π³ ππ΄πΌπΏπ»π°ππ΄ (π°πππΎπ΅πΈπ»ππ΄π ππ΄πΌπΏ) π΅πΎπ {title} ππΎ\n\n{pr0fess0r_99}""", reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("Γ π²π»πΎππ΄ Γ", callback_data="close") ]] ))

@lucifermoringstar_robot.on_message((filters.private | filters.group) & filters.command('setwelcome'), group=7)
async def setwelcome(client, message):
    sts = await message.reply("β³οΈ")
    await asyncio.sleep(0.3)
    userid = message.from_user.id if message.from_user else None
    if not userid:
        return await message.reply(f" ππΎππ π°ππ΄ π°π½πΎπ½ππΌπΎππ π°π³πΌπΈπ½. /connect {message.chat.id} πΈπ½ πΏπΌ")
    chat_type = message.chat.type
    if chat_type == enums.ChatType.PRIVATE:
        grpid = await active_connection(str(userid))
        if grpid is not None:
            grp_id = grpid
            try:
                chat = await client.get_chat(grpid)
                title = chat.title
            except:
                await message.reply_text("πΌπ°πΊπ΄ ππππ΄ πΈπ°πΌ πΏππ΄ππ΄π½π πΈπ½ ππΎππ πΆππΎππΏ..!", quote=True)
                return
        else:
            await message.reply_text("πΈπ°πΌ π½πΎπ π²πΎπ½π½π΄π²ππ΄π³ π°π½π πΆππΎππΏ..!", quote=True)
            return

    elif chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        grp_id = message.chat.id
        title = message.chat.title

    else:
        return

    member = await client.get_chat_member(grp_id, userid)
    if (member.status != enums.ChatMemberStatus.ADMINISTRATOR and member.status != enums.ChatMemberStatus.OWNER and userid not in ADMINS):
        return

    if len(message.command) < 2:
        return await sts.edit("π·πΎπ ππΎ πππ΄ ππ·πΈπ π²πΎπΌπΌπ°π½π³..!", reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("π²π»πΈπ²πΊ π·π΄ππ΄", callback_data="welcome") ]] ))

    pr0fess0r_99 = message.text.split(" ", 1)[1]
    await save_group_settings(grp_id, 'welcometext', pr0fess0r_99)
    await sts.edit(f"""πππ²π²π΄πππ΅ππ»π»π π²π·π°π½πΆπ΄π³ ππ΄π»π²πΎπΌπ΄ πΌπ΄πππ°πΆπ΄ π΅πΎπ {title} ππΎ\n\n{pr0fess0r_99}""", reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("Γ π²π»πΎππ΄ Γ", callback_data="close") ]] ))


@lucifermoringstar_robot.on_message((filters.private | filters.group) & filters.command('setspell'), group=8)
async def setspell(client, message):
    sts = await message.reply("β³οΈ")
    await asyncio.sleep(0.3)
    userid = message.from_user.id if message.from_user else None
    if not userid:
        return await message.reply(f" ππΎππ π°ππ΄ π°π½πΎπ½ππΌπΎππ π°π³πΌπΈπ½. /connect {message.chat.id} πΈπ½ πΏπΌ")
    chat_type = message.chat.type
    if chat_type == enums.ChatType.PRIVATE:
        grpid = await active_connection(str(userid))
        if grpid is not None:
            grp_id = grpid
            try:
                chat = await client.get_chat(grpid)
                title = chat.title
            except:
                await message.reply_text("πΌπ°πΊπ΄ ππππ΄ πΈπ°πΌ πΏππ΄ππ΄π½π πΈπ½ ππΎππ πΆππΎππΏ..!", quote=True)
                return
        else:
            await message.reply_text("πΈπ°πΌ π½πΎπ π²πΎπ½π½π΄π²ππ΄π³ π°π½π πΆππΎππΏ..!", quote=True)
            return

    elif chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        grp_id = message.chat.id
        title = message.chat.title

    else:
        return

    member = await client.get_chat_member(grp_id, userid)
    if (
            member.status != enums.ChatMemberStatus.ADMINISTRATOR
            and member.status != enums.ChatMemberStatus.OWNER
            and userid not in ADMINS
    ):
        return

    if len(message.command) < 2:
        return await sts.edit("π·πΎπ ππΎ πππ΄ ππ·πΈπ π²πΎπΌπΌπ°π½π³..!", reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("π²π»πΈπ²πΊ π·π΄ππ΄", callback_data="spellcheck") ]] ))

    pr0fess0r_99 = message.text.split(" ", 1)[1]
    await save_group_settings(grp_id, 'spelltext', pr0fess0r_99)
    await sts.edit(f"""πππ²π²π΄πππ΅ππ»π»π π²π·π°π½πΆπ΄π³ ππ΄π ππΏπ΄π»π» π²π·π΄π²πΊ π΅πΎπ {title} ππΎ\n\n{pr0fess0r_99}""", reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("Γ π²π»πΎππ΄ Γ", callback_data="close") ]] ))

@lucifermoringstar_robot.on_message((filters.private | filters.group) & filters.command('setcaption'), group=9)
async def filecap(client, message):
    sts = await message.reply("β³οΈ")
    await asyncio.sleep(0.3)
    userid = message.from_user.id if message.from_user else None
    if not userid:
        return await message.reply(f" ππΎππ π°ππ΄ π°π½πΎπ½ππΌπΎππ π°π³πΌπΈπ½. /connect {message.chat.id} πΈπ½ πΏπΌ")
    chat_type = message.chat.type
    if chat_type == enums.ChatType.PRIVATE:
        grpid = await active_connection(str(userid))
        if grpid is not None:
            grp_id = grpid
            try:
                chat = await client.get_chat(grpid)
                title = chat.title
            except:
                await message.reply_text("πΌπ°πΊπ΄ ππππ΄ πΈπ°πΌ πΏππ΄ππ΄π½π πΈπ½ ππΎππ πΆππΎππΏ..!", quote=True)
                return
        else:
            await message.reply_text("πΈπ°πΌ π½πΎπ π²πΎπ½π½π΄π²ππ΄π³ π°π½π πΆππΎππΏ..!", quote=True)
            return

    elif chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        grp_id = message.chat.id
        title = message.chat.title

    else:
        return

    member = await client.get_chat_member(grp_id, userid)
    if (
            member.status != enums.ChatMemberStatus.ADMINISTRATOR
            and member.status != enums.ChatMemberStatus.OWNER
            and userid not in ADMINS
    ):
        return

    if len(message.command) < 2:
        return await sts.edit("π·πΎπ ππΎ πππ΄ ππ·πΈπ π²πΎπΌπΌπ°π½π³..!", reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("π²π»πΈπ²πΊ π·π΄ππ΄", callback_data="filecaption") ]] ))

    pr0fess0r_99 = message.text.split(" ", 1)[1]
    await save_group_settings(grp_id, 'caption', pr0fess0r_99)
    await sts.edit(f"""πππ²π²π΄πππ΅ππ»π»π π²π·π°π½πΆπ΄π³ π΅πΈπ»π΄ π²π°πΏππΈπΎπ½ π΅πΎπ {title} ππΎ\n\n{pr0fess0r_99}""", reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("Γ π²π»πΎππ΄ Γ", callback_data="close") ]] ))
