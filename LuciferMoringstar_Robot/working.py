from pyrogram import Client as lucifermoringstar_robot, filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from LuciferMoringstar_Robot.modules import group_filters, pm_filters
from LuciferMoringstar_Robot import AUTH_GROUPS, AUTH_USERS, LOG_CHANNEL, temp, COMMANDS, AUTH_CHANNEL
from LuciferMoringstar_Robot.translation import CHAT_LOGS_MESSAGE
from database.chats_users_mdb import db


@lucifermoringstar_robot.on_message(filters.text & filters.private & filters.incoming & ~filters.command(COMMANDS) & filters.user(AUTH_USERS) if AUTH_USERS else filters.text & filters.private & filters.incoming & ~filters.command(COMMANDS))
async def pmbot_filters(client, update):
    if not await db.is_user_exist(update.from_user.id):
        await db.add_user(update.from_user.id)

    if AUTH_CHANNEL:
        invite_link = await client.create_chat_invite_link(int(AUTH_CHANNEL))
        try:
            user = await client.get_chat_member(int(AUTH_CHANNEL), update.from_user.id)
            if user.status == enums.ChatMemberStatus.RESTRICTED:
                await client.send_message(chat_id=update.from_user.id, text="Sorry Sir, You are Banned to use me.", disable_web_page_preview=True)
                return
        except UserNotParticipant:
            await client.send_message(chat_id=update.from_user.id, text="**πΏπ»π΄π°ππ΄ πΉπΎπΈπ½ πΌπ ππΏπ³π°ππ΄ π²π·π°π½π½π΄π» ππΎ πππ΄ ππ·πΈπ π±πΎπ..!**", reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("π’ πΉπΎπΈπ½ πΌπ ππΏπ³π°ππ΄ π²π·π°π½π½π΄π» π’", url=invite_link.invite_link) ]] ))           
            return

    if update.chat.id in temp.PMAF_OFF:
        return
    else:
        await pm_filters(client, update)

@lucifermoringstar_robot.on_message(filters.text & filters.group & filters.incoming & filters.chat(AUTH_GROUPS) if AUTH_GROUPS else filters.text & filters.group & filters.incoming)
async def groupfilters(client, update):
    if not await db.get_chat(update.chat.id):
        try:
            invite_link = await client.create_chat_invite_link(update.chat.id)
            join = f"{invite_link.invite_link}"
        except:
            join = "Error"
        await client.send_message(chat_id=LOG_CHANNEL, text=CHAT_LOGS_MESSAGE.format(title=update.chat.title, id=update.chat.id, join=join), disable_web_page_preview=True) 
        await db.add_chat(update.chat.id, update.chat.title)
    await group_filters(client, update)

