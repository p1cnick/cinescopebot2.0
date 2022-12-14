import asyncio 
from pyrogram import Client as lucifermoringstar_robot, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import UserIsBlocked, PeerIdInvalid, UserNotParticipant, MessageNotModified
from LuciferMoringstar_Robot import temp, CUSTOM_FILE_CAPTION, AUTH_CHANNEL, SUPPORT, CREATOR_NAME, CREATOR_USERNAME, SAVE_FILES, GET_FILECHANNEL, ADMINS, START_MESSAGE
from LuciferMoringstar_Robot.functions import get_size, get_settings, save_group_settings, is_subscribed
from LuciferMoringstar_Robot.modules import autofilter_text, modeles_text, spellcheck_text, welcome_text, misc_text, filecaption_text
from LuciferMoringstar_Robot.modules.fonts import stylishtext
from LuciferMoringstar_Robot.translation import HELP_MESSAGE, ABOUT_MESSAGE, STATUS_MESSAGE, GETFILE_TEXT, USAGE_MESSAGE, NOT_SUB
from database.connections_mdb import active_connection, all_connections, delete_connection, if_active, make_active, make_inactive
from database.autofilter_mdb import Media, get_file_details
from database.chats_users_mdb import db

@lucifermoringstar_robot.on_callback_query()
async def cb_handler(bot, update):

    try:
        userID = update.message.reply_to_message.from_user.id
    except:
        userID = update.from_user.id

    if userID == update.from_user.id:        

        if update.data == "close":
            await update.message.delete()

        elif update.data.startswith("nextgroup"):
            mrk, index, keyword = update.data.split("_")
            try:
                data = temp.BUTTONS[keyword]
            except KeyError:
                await update.answer("ππ·πΈπ πΌπ πΎπ»π³ πΌπ΄πππ°πΆπ΄ ππΎ πΏπ»π΄π°ππ΄ ππ΄πππ΄ππ π°πΆπ°πΈπ½ π",show_alert=True)
                return

            if int(index) == int(data["total"]) - 2:
                buttons = data['buttons'][int(index)+1].copy()
                buttons.append(
                    [InlineKeyboardButton("π", callback_data=f"backgroup_{int(index)+1}_{keyword}"),
                     InlineKeyboardButton(f"π {int(index)+2}/{data['total']}", callback_data="pages"),
                     InlineKeyboardButton("ποΈ", callback_data="close")]
                )
                buttons.append(
                    [InlineKeyboardButton(text="π€ π²π·π΄π²πΊ πΌπ πΏπΌ π€", url=f"https://telegram.dog/{temp.Bot_Username}")]
                )
                await update.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return
            else:
                buttons = data['buttons'][int(index)+1].copy()
                buttons.append(
                    [InlineKeyboardButton("π", callback_data=f"backgroup_{int(index)+1}_{keyword}"),
                     InlineKeyboardButton(f"π {int(index)+2}/{data['total']}", callback_data="pages"),
                     InlineKeyboardButton("ποΈ", callback_data="close"),
                     InlineKeyboardButton("β‘", callback_data=f"nextgroup_{int(index)+1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(text="π€ π²π·π΄π²πΊ πΌπ πΏπΌ π€", url=f"https://telegram.dog/{temp.Bot_Username}")]
                )
                await update.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))                
                return
        
        elif update.data.startswith("backgroup"):
            mrk, index, keyword = update.data.split("_")
            try:
                data = temp.BUTTONS[keyword]
            except KeyError:
                await update.answer("ππ·πΈπ πΌπ πΎπ»π³ πΌπ΄πππ°πΆπ΄ ππΎ πΏπ»π΄π°ππ΄ ππ΄πππ΄ππ π°πΆπ°πΈπ½ π",show_alert=True)
                return
            if int(index) == 1:
                buttons = data['buttons'][int(index)-1].copy()
                buttons.append(
                    [InlineKeyboardButton(f"π {int(index)}/{data['total']}", callback_data="pages"),
                     InlineKeyboardButton("ποΈ", callback_data="close"),
                     InlineKeyboardButton("β‘", callback_data=f"nextgroup_{int(index)-1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(text="π€ π²π·π΄π²πΊ πΌπ πΏπΌ π€", url=f"https://telegram.dog/{temp.Bot_Username}")]
                )
                await update.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))                
                return   
            else:
                buttons = data['buttons'][int(index)-1].copy()
                buttons.append(
                    [InlineKeyboardButton("π", callback_data=f"backgroup_{int(index)-1}_{keyword}"),
                     InlineKeyboardButton(f"π {int(index)}/{data['total']}", callback_data="pages"),
                     InlineKeyboardButton("ποΈ", callback_data="close"),
                     InlineKeyboardButton("β‘", callback_data=f"nextgroup_{int(index)-1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(text="π€ π²π·π΄π²πΊ πΌπ πΏπΌ π€", url=f"https://telegram.dog/{temp.Bot_Username}")]
                )
                await update.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))                
                return

        elif update.data.startswith("nextbot"):
            mrk, index, keyword = update.data.split("_")
            try:
                data = temp.BUTTONS[keyword]
            except KeyError:
                await update.answer("ππ·πΈπ πΌπ πΎπ»π³ πΌπ΄πππ°πΆπ΄ ππΎ πΏπ»π΄π°ππ΄ ππ΄πππ΄ππ π°πΆπ°πΈπ½ π",show_alert=True)
                return
            if int(index) == int(data["total"]) - 2:
                buttons = data['buttons'][int(index)+1].copy()
                buttons.append(
                    [InlineKeyboardButton("π", callback_data=f"backbot_{int(index)+1}_{keyword}"),
                     InlineKeyboardButton(f"π {int(index)+2}/{data['total']}", callback_data="pages"),
                     InlineKeyboardButton("ποΈ", callback_data="close")]
                )

                await update.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))                
                return
            else:
                buttons = data['buttons'][int(index)+1].copy()
                buttons.append(
                    [InlineKeyboardButton("π", callback_data=f"backbot_{int(index)+1}_{keyword}"),
                     InlineKeyboardButton(f"π {int(index)+2}/{data['total']}", callback_data="pages"),
                     InlineKeyboardButton("ποΈ", callback_data="close"),
                     InlineKeyboardButton("β‘", callback_data=f"nextbot_{int(index)+1}_{keyword}")]
                )

                await update.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))                
                return

        elif update.data.startswith("backbot"):
            mrk, index, keyword = update.data.split("_")
            try:
                data = temp.BUTTONS[keyword]
            except KeyError:
                await update.answer("ππ·πΈπ πΌπ πΎπ»π³ πΌπ΄πππ°πΆπ΄ ππΎ πΏπ»π΄π°ππ΄ ππ΄πππ΄ππ π°πΆπ°πΈπ½ π",show_alert=True)
                return
            if int(index) == 1:
                buttons = data['buttons'][int(index)-1].copy()
                buttons.append(
                    [InlineKeyboardButton(f"π {int(index)}/{data['total']}", callback_data="pages"),
                     InlineKeyboardButton("ποΈ", callback_data="close"),
                     InlineKeyboardButton("β‘", callback_data=f"nextbot_{int(index)-1}_{keyword}")]
                )

                await update.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))                
                return   
            else:
                buttons = data['buttons'][int(index)-1].copy()
                buttons.append(
                    [InlineKeyboardButton("π", callback_data=f"backbot_{int(index)-1}_{keyword}"),
                     InlineKeyboardButton(f"π {int(index)}/{data['total']}", callback_data="pages"),
                     InlineKeyboardButton("ποΈ", callback_data="close"),
                     InlineKeyboardButton("β‘", callback_data=f"nextbot_{int(index)-1}_{keyword}")]
                )
                await update.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))                
                return

        elif update.data.startswith("settings"):
            mrk, set_type, status, grp_id = update.data.split("#")
            grpid = await active_connection(str(update.from_user.id))
            if str(grp_id) != str(grpid):
                await update.message.edit("πΈπ°πΌ π½πΎπ π²πΎπ½π½π΄π²ππ΄π³ π°π½π πΆππΎππΏ..!\n   πππ΄ ππ·πΈπ π²πΎπΌπΌπ°π½π³ /connect π°π½π³ π²πΎπ½π½π΄π²π ππΎππ π²π·π°π")
            if status == "True":
                await save_group_settings(grpid, set_type, False)
            else:
                await save_group_settings(grpid, set_type, True)
            settings = await get_settings(grpid)
            if settings is not None:
                pr0fess0r_99 = [[
                 InlineKeyboardButton('π΅πΈπ»ππ΄π π±ππππΎπ½', callback_data=f'settings#button#{settings["button"]}#{str(grp_id)}'),        
                 InlineKeyboardButton('ππΈπ½πΆπ»π΄' if settings["button"] else 'π³πΎππ±π»π΄', callback_data=f'settings#button#{settings["button"]}#{str(grp_id)}')
                 ],[
                 InlineKeyboardButton('ππ΄π»π²πΎπΌπ΄ πΌππΆ', callback_data=f'settings#welcome#{settings["welcome"]}#{str(grp_id)}'),
                 InlineKeyboardButton('πΎπ½' if settings["welcome"] else 'πΎπ΅π΅', callback_data=f'settings#welcome#{settings["welcome"]}#{str(grp_id)}')           
                 ],[  
                 InlineKeyboardButton('ππΏπ΄π»π» π²π·π΄π²πΊ', callback_data=f'settings#spellmode#{settings["spellmode"]}#{str(grp_id)}'),
                 InlineKeyboardButton('πΎπ½' if settings["spellmode"] else 'πΎπ΅π΅', callback_data=f'settings#spellmode#{settings["spellmode"]}#{str(grp_id)}')           
                 ],[
                 InlineKeyboardButton('π±πΎπ πΏπΎπππ΄π', callback_data=f'settings#photo#{settings["photo"]}#{str(grp_id)}'),
                 InlineKeyboardButton('πΎπ½' if settings["photo"] else 'πΎπ΅π΅', callback_data=f'settings#photo#{settings["photo"]}#{str(grp_id)}')           
                 ],[
                 InlineKeyboardButton('ππ°ππ΄ π΅πΈπ»π΄π', callback_data=f'settings#savefiles#{settings["savefiles"]}#{str(grp_id)}'),
                 InlineKeyboardButton('πΎπ½' if settings["savefiles"] else 'πΎπ΅π΅', callback_data=f'settings#savefiles#{settings["savefiles"]}#{str(grp_id)}')           
                 ],[
                 InlineKeyboardButton('π΅πΈπ»π΄ πΌπΎπ³π΄', callback_data=f'settings#filemode#{settings["filemode"]}#{str(grp_id)}'),
                 InlineKeyboardButton('πΏπΌ' if settings["filemode"] else 'π²π·π°π½π½π΄π»', callback_data=f'settings#filemode#{settings["filemode"]}#{str(grp_id)}')           
                 ]]
                pr0fess0r_99 = InlineKeyboardMarkup(pr0fess0r_99)
                await update.message.edit_reply_markup(reply_markup=pr0fess0r_99)

        elif update.data.startswith("luciferGP"):
            mrk, file_id = update.data.split("#")
            file_details_pr0fess0r99 = await get_file_details(file_id)
            settings = await get_settings(update.message.chat.id)
            if not file_details_pr0fess0r99:
                return await update.answer('π΅πΈπ»π΄ π½πΎπ π΅πΎππ½π³...!')
            files = file_details_pr0fess0r99[0]
            title = files.file_name
            size = get_size(files.file_size)

            if not await db.is_user_exist(update.from_user.id):
                dellogs=await update.message.reply_text(f"""<b>π·π΄π {update.from_user.mention} ππΎππ ππ΄πππ΄ππ π΅πΈπ»π΄ πΈπ ππ΄π°π³π<b>\n\nβ’ **ππΈππ»π΄** : <code>{title}</code>\n\nβ’ **ππΈππ΄** : {size} """, reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("π²π»πΈπ²πΊ π·π΄ππ΄", url=f"https://telegram.dog/{temp.Bot_Username}?start=muhammedrk-mo-tech-group-{file_id}") ]] ))
                await asyncio.sleep(30)
                await dellogs.delete()
                return
            if AUTH_CHANNEL and not await is_subscribed(bot, update):
                dellogs=await update.message.reply_text(f"""<b>π·π΄π {update.from_user.mention} ππΎππ ππ΄πππ΄ππ π΅πΈπ»π΄ πΈπ ππ΄π°π³π<b>\n\nβ’ **ππΈππ»π΄** : <code>{title}</code>\n\nβ’ **ππΈππ΄** : {size} """, reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("π²π»πΈπ²πΊ π·π΄ππ΄", url=f"https://telegram.dog/{temp.Bot_Username}?start=muhammedrk-mo-tech-group-{file_id}") ]] ))
                await asyncio.sleep(30)
                await dellogs.delete()
                return

            FILE_CAPTION = settings["caption"]
            caption = FILE_CAPTION.format(mention=update.from_user.mention, file_name=title, size=size, caption=files.caption)
            buttons = [[ InlineKeyboardButton("βοΈ ππ·π°ππ΄ πΌπ΄ ππΈππ· ππΎππ π΅ππΈπ΄π½π³π βοΈ", url=f"https://t.me/share/url?url=Best%20AutoFilter%20Bot%20%0A%40LuciferMoringstar_Robot%0A@{temp.Bot_Username}") ]]
            if settings["savefiles"]:
                protect_content = True
            else:
                protect_content = False

            try:
                if settings["filemode"]:
                    try:
                        await bot.send_cached_media(chat_id=update.from_user.id, file_id=file_id, caption=caption, reply_markup=InlineKeyboardMarkup(buttons), protect_content=protect_content)
                        await update.answer("""π²π·π΄π²πΊ πΏπΌ, πΈ π·π°ππ΄ ππ΄π½π π΅πΈπ»π΄π πΈπ½ πΏπΌ\nπ²π»πΈπ²πΊ π²π·π΄π²πΊ πΏπΌ π±ππππΎπ½""", show_alert=True)   
                    except Exception as e:
                        await update.message.reply(f"{e}")                  
                        dellogs=await update.message.reply_text(f"""<b>π·π΄π {update.from_user.mention} ππΎππ ππ΄πππ΄ππ π΅πΈπ»π΄ πΈπ ππ΄π°π³π<b>\n\nβ’ **ππΈππ»π΄** : <code>{title}</code>\n\nβ’ **ππΈππ΄** : {size} """, reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("π²π»πΈπ²πΊ π·π΄ππ΄", url=f"https://telegram.dog/{temp.Bot_Username}?start=muhammedrk-mo-tech-group-{file_id}") ]] ))
                        await asyncio.sleep(30)
                        await dellogs.delete()
                else:
                    try:
                        invite_link = await bot.create_chat_invite_link(GET_FILECHANNEL)      
                        dlFile = await bot.send_cached_media(chat_id=GET_FILECHANNEL, file_id=file_id, caption=caption, reply_markup=InlineKeyboardMarkup(buttons))
                        dlReply = await update.message.reply_text(GETFILE_TEXT.format(mention=update.from_user.mention, file_name=title, file_size=size), reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("π₯ π³οΈπΎοΈποΈπ½οΈπ»οΈπΎοΈπ°οΈπ³οΈ π₯", url=dlFile.link) ],[ InlineKeyboardButton("β οΈπ²πΎπ½'π π°π²π²π΄ππ π²π»πΈπ²πΊ π·π΄ππ΄β οΈ", url=invite_link.invite_link) ]] ))
                        await asyncio.sleep(1000)
                        await dlFile.delete()
                        await dlReply.delete()
                    except Exception as e:
                        await update.message.reply(f"**(1)**Β» {e}")
                        dellogs=await update.message.reply_text(f"""<b>π·π΄π {update.from_user.mention} ππΎππ ππ΄πππ΄ππ π΅πΈπ»π΄ πΈπ ππ΄π°π³π<b>\n\nβ’ **ππΈππ»π΄** : <code>{title}</code>\n\nβ’ **ππΈππ΄** : {size} """, reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("π²π»πΈπ²πΊ π·π΄ππ΄", url=f"https://telegram.dog/{temp.Bot_Username}?start=muhammedrk-mo-tech-group-{file_id}") ]] ))
                        await asyncio.sleep(30)
                        await dellogs.delete()
            except UserIsBlocked:
                await update.answer('Unblock the bot mahn !', show_alert=True)
            except PeerIdInvalid:
                dellogs=await update.message.reply_text(f"""<b>π·π΄π {update.from_user.mention} ππΎππ ππ΄πππ΄ππ π΅πΈπ»π΄ πΈπ ππ΄π°π³π<b>\n\nβ’ **ππΈππ»π΄** : <code>{title}</code>\n\nβ’ **ππΈππ΄** : {size} """, reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("π²π»πΈπ²πΊ π·π΄ππ΄", url=f"https://telegram.dog/{temp.Bot_Username}?start=muhammedrk-mo-tech-group-{file_id}") ]] ))
                await asyncio.sleep(30)
                await dellogs.delete()
            except Exception as e:
                await update.message.reply(f"**(2)**Β» {e}")
                dellogs=await update.message.reply_text(f"""<b>π·π΄π {update.from_user.mention} ππΎππ ππ΄πππ΄ππ π΅πΈπ»π΄ πΈπ ππ΄π°π³π<b>\n\nβ’ **ππΈππ»π΄** : <code>{title}</code>\n\nβ’ **ππΈππ΄** : {size} """, reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("π²π»πΈπ²πΊ π·π΄ππ΄", url=f"https://telegram.dog/{temp.Bot_Username}?start=muhammedrk-mo-tech-group-{file_id}") ]] ))
                await asyncio.sleep(30)
                await dellogs.delete()
                
        elif update.data.startswith("luciferPM"):
            mrk, file_id = update.data.split("#")
            # if not await db.is_user_exist(update.from_user.id):
                # dellogs=await update.message.reply_text(f"""<b>π·π΄π {update.from_user.id} ππΎππ ππ΄πππ΄ππ π΅πΈπ»π΄ πΈπ ππ΄π°π³π<b>\n\nβ’ **ππΈππ»π΄** : <code>{title}</code>\n\nβ’ **ππΈππ΄** : {size} """, reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("π²π»πΈπ²πΊ π·π΄ππ΄", url=f"https://telegram.dog/{temp.Bot_Username}?start=muhammedrk-mo-tech-group-{file_id}") ]] ))
                # await asyncio.sleep(30)
                # await dellogs.delete()
                # return
            if AUTH_CHANNEL and not await is_subscribed(bot, update):
                await update.answer(NOT_SUB, show_alert=True)
                # dellogs=await update.message.reply_text(f"""<b>π·π΄π {update.from_user.id} ππΎππ ππ΄πππ΄ππ π΅πΈπ»π΄ πΈπ ππ΄π°π³π<b>\n\nβ’ **ππΈππ»π΄** : <code>{title}</code>\n\nβ’ **ππΈππ΄** : {size} """, reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("π²π»πΈπ²πΊ π·π΄ππ΄", url=f"https://telegram.dog/{temp.Bot_Username}?start=muhammedrk-mo-tech-group-{file_id}") ]] ))
                # await asyncio.sleep(30)
                # await dellogs.delete()
                return
            file_details_pr0fess0r99 = await get_file_details(file_id)
            if not file_details_pr0fess0r99:
                return await update.answer('π΅πΈπ»π΄ π½πΎπ π΅πΎππ½π³...!')
            files = file_details_pr0fess0r99[0]
            title = files.file_name
            size = get_size(files.file_size)
            caption = CUSTOM_FILE_CAPTION.format(mention=update.from_user.mention, file_name=title, size=size, caption=files.caption)
            buttons = [[ InlineKeyboardButton("βοΈ ππ·π°ππ΄ πΌπ΄ ππΈππ· ππΎππ π΅ππΈπ΄π½π³π βοΈ", url=f"https://t.me/share/url?url=Best%20AutoFilter%20Bot%20%0A%40LuciferMoringstar_Robot%0A@{temp.Bot_Username}") ]]
            try:
                await bot.send_cached_media(chat_id=update.from_user.id, file_id=file_id, caption=caption, reply_markup=InlineKeyboardMarkup(buttons), protect_content=SAVE_FILES)            
            except Exception as e:
                print(f"{e}")
                dellogs=await update.message.reply_text(f"""<b>π·π΄π {update.from_user.id} ππΎππ ππ΄πππ΄ππ π΅πΈπ»π΄ πΈπ ππ΄π°π³π<b>\n\nβ’ **ππΈππ»π΄** : <code>{title}</code>\n\nβ’ **ππΈππ΄** : {size} """, reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("π²π»πΈπ²πΊ π·π΄ππ΄", url=f"https://telegram.dog/{temp.Bot_Username}?start=muhammedrk-mo-tech-group-{file_id}") ]] ))
                await asyncio.sleep(30)
                await dellogs.delete()
                return
              
        elif update.data == "start":
            buttons = [[ InlineKeyboardButton("Γ π°π³π³ πΌπ΄ ππΎ ππΎππ πΆππΎππΏ Γ", url=f"http://t.me/{temp.Bot_Username}?startgroup=true") ],
                      [ InlineKeyboardButton("πππΏπΏπΎππ π¬", url=f"t.me/{SUPPORT}"), InlineKeyboardButton("ππΏπ³π°ππ΄π π’", url="t.me/Mo_Tech_YT") ],
                      [ InlineKeyboardButton("βΉοΈ π·π΄π»πΏ", callback_data="help"), InlineKeyboardButton("π°π±πΎππ π€ ", callback_data="about") ]] 
            await update.message.edit(START_MESSAGE.format(mention=update.from_user.mention, name=temp.Bot_Name, username=temp.Bot_Username), reply_markup=InlineKeyboardMarkup(buttons))

        elif update.data == "help":
            try:
                buttons = [[
                 InlineKeyboardButton("AutoFilter", callback_data="autofilter"),
                 InlineKeyboardButton("FileStore", callback_data="filestore"),
                 InlineKeyboardButton("Misc", callback_data="misc")
                 ],[
                 InlineKeyboardButton("Connections", callback_data="connection"),
                 InlineKeyboardButton("SpellCheck", callback_data="spellcheck"),
                 InlineKeyboardButton("Via", callback_data="inlinecb")
                 ],[
                 InlineKeyboardButton("Welcome", callback_data="welcome"),
                 InlineKeyboardButton("Caption", callback_data="filecaption"),
                 InlineKeyboardButton("Fun", callback_data="funcb")
                 ],[
                 InlineKeyboardButton("Font", callback_data="fontcb"),
                 InlineKeyboardButton("ShareText", callback_data="sharetextcb"),
                 InlineKeyboardButton("TTs", callback_data="ttscb")
                 ],[
                 InlineKeyboardButton("Status", callback_data="status"),
                 InlineKeyboardButton("Home", callback_data="start")
                 ]]                     
                await update.message.edit(HELP_MESSAGE.format(mention=update.from_user.mention, name=temp.Bot_Name, username=temp.Bot_Username), reply_markup=InlineKeyboardMarkup(buttons))
            except MessageNotModified:
                pass
        elif update.data == "about":
            try:
                buttons = [ [ InlineKeyboardButton("π·πΎπΌπ΄", callback_data="start"), InlineKeyboardButton("π·πΎπ ππΎ πππ΄", callback_data="usage"), InlineKeyboardButton("π²π»πΎππ΄", callback_data="close") ]]                     
                await update.message.edit(ABOUT_MESSAGE.format(name=CREATOR_NAME, username=CREATOR_USERNAME, py3_version=temp.PY3_VERSION, pyro_version=temp.PYRO_VERSION, version=temp.BOT_VERSION), reply_markup=InlineKeyboardMarkup(buttons))
            except MessageNotModified:
                pass
        elif update.data == "usage":
            try:
                buttons = [[ InlineKeyboardButton("β π±π°π²πΊ β", callback_data="about") ]]
                await update.message.edit(USAGE_MESSAGE.format(CREATOR_NAME, CREATOR_USERNAME), reply_markup=InlineKeyboardMarkup(buttons))
            except MessageNotModified:
                pass
        elif update.data == "status":
            try:
                files = await Media.count_documents()
                users = await db.total_users_count()
                chats = await db.total_chat_count()
                buttons = [[ InlineKeyboardButton("β π±π°π²πΊ", callback_data="help"), InlineKeyboardButton("ππ΄π΅ππ΄ππ·", callback_data="status"), InlineKeyboardButton("π²π»πΎππ΄ Γ", callback_data="close") ]]                                 
                await update.message.edit(STATUS_MESSAGE.format(bot_name=temp.Bot_Name, users=users, files=files, chats=chats), reply_markup=InlineKeyboardMarkup(buttons))
            except MessageNotModified:
                pass

        elif update.data == "files_delete":
            await Media.collection.drop()
            try:
                await update.message.edit('πππ²π²π΄ππ΅ππ»π»π π³π΄π»π΄ππ΄π³ π°π»π» ππ·π΄ πΈπ½π³π΄ππ΄π³ π΅πΈπ»π΄π..')
            except MessageNotModified:
                pass        
        elif update.data == "autofilter":
            try:
                await update.message.edit(autofilter_text, reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("β Back To Menu β", callback_data="help") ]] ))
            except MessageNotModified:
                pass
        elif update.data == "connection":
            try:
                await update.message.edit(modeles_text.connection_text, reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("β Back To Menu β", callback_data="help") ]] ))
            except MessageNotModified:
                pass
        elif update.data == "spellcheck":
            try:
                await update.message.edit(spellcheck_text, reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("β Back To Menu β", callback_data="help") ]] ))
            except MessageNotModified:
                pass
        elif update.data == "welcome":
            try:
                await update.message.edit(welcome_text, reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("β Back To Menu β", callback_data="help") ]] ))
            except MessageNotModified:
                pass
        elif update.data == "misc":
            try:
                await update.message.edit(misc_text, reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("β Back To Menu β", callback_data="help") ]] ))
            except MessageNotModified:
                pass
        elif update.data == "filecaption":
            try:
                await update.message.edit(filecaption_text, reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("β Back To Menu β", callback_data="help") ]] ))
            except MessageNotModified:
                pass
        elif update.data == "filestore":
            try:
                await update.message.edit(modeles_text.filestore_text, reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("β Back To Menu β", callback_data="help") ]] ))
            except MessageNotModified:
                pass
        elif update.data == "inlinecb":
            try:
                await update.message.edit(modeles_text.inline_text, reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton('π Search Here π', switch_inline_query_current_chat="") ],[ InlineKeyboardButton("β Back To Menu β", callback_data="help") ]] ))
            except MessageNotModified:
                pass
        elif update.data == "funcb":
            try:
                await update.message.edit(modeles_text.fun_text, reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("β Back To Menu β", callback_data="help") ]] ))
            except MessageNotModified:
                pass
        elif update.data == "fontcb":
            try:
                await update.message.edit(modeles_text.font_text, reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("β Back To Menu β", callback_data="help") ]] ))
            except MessageNotModified:
                pass
        elif update.data == "sharetextcb":
            try:
                await update.message.edit(modeles_text.sharetext_text, reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("β Back To Menu β", callback_data="help") ]] ))
            except MessageNotModified:
                pass
        elif update.data == "ttscb":
            try:
                await update.message.edit(modeles_text.tts_text, reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("β Back To Menu β", callback_data="help") ]] ))
            except MessageNotModified:
                pass

        elif "style" in update.data:
            cmd, style = update.data.split('+')
            await stylishtext(bot, update, style) # StylishText CallbackQuery

        elif update.data == "backcb":
            await update.answer()
            userid = update.from_user.id
            groupids = await all_connections(str(userid))
            if groupids is None:
                await update.message.edit("ππ·π΄ππ΄ π°ππ΄ π½πΎ π°π²ππΈππ΄ π²πΎπ½π½π΄π²ππΈπΎπ½π..! π²πΎπ½π½π΄π²π ππΎ ππ°πΌπ΄ πΆππΎππΏπ π΅πΈπππ")
            return await update.answer('Piracy Is Crime')
            buttons = []
            for groupid in groupids:
                try:
                    mrk = await bot.get_chat(int(groupid))
                    title = mrk.title
                    active = await if_active(str(userid), str(groupid))
                    act = " - ACTIVE" if active else ""
                    buttons.append([InlineKeyboardButton(f"{title}{act}", callback_data=f"groupcb:{groupid}:{act}")])                
                except:
                    pass
            if buttons:
                await update.message.edit("""ππΎππ π²πΎπ½π½π΄π²ππ΄π³ πΆππΎππΏ π³π΄ππ°πΈπ»π:\n\n""", reply_markup=InlineKeyboardMarkup(buttons))
            
        elif "deletecb" in update.data:
            await update.answer()
            user_id = update.from_user.id
            group_id = update.data.split(":")[1]
            delcon = await delete_connection(str(user_id), str(group_id))
            if delcon:
                await update.message.edit("πππ²π²π΄πππ΅ππ»π»π π³π΄π»π΄ππ΄π³ π²πΎπ½π½π΄π²ππΈπΎπ½")           
            else:
                await update.message.edit(f"ππΎπΌπ΄ π΄πππΎπ πΎπ²π²ππππ΄π³..!")
            return 

        elif "disconnect" in update.data:
            await update.answer()
            group_id = update.data.split(":")[1]
            mrk = await bot.get_chat(int(group_id))
            title = mrk.title
            user_id = update.from_user.id
            mkinact = await make_inactive(str(user_id))
            if mkinact:
                await update.message.edit(f"π³πΈππ²πΎπ½π½π΄π²ππ΄π³ π΅ππΎπΌ **{title}**")
            else:
                await update.message.edit(f"ππΎπΌπ΄ π΄πππΎπ πΎπ²π²ππππ΄π³..!")
            
        elif "connectcb" in update.data:
            await update.answer()
            group_id = update.data.split(":")[1]
            mrk = await bot.get_chat(int(group_id))
            title = mrk.title
            user_id = update.from_user.id
            mkact = await make_active(str(user_id), str(group_id))
            if mkact:
                await update.message.edit(f"π²πΎπ½π½π΄π²ππ΄π³ ππΎ **{title}**")            
            else:
                await update.message.edit_text('Some error occurred!!')
            return

        elif "groupcb" in update.data:
            await update.answer()
            group_id = update.data.split(":")[1]
            act = update.data.split(":")[2]
            mrk = await bot.get_chat(int(group_id))
            title = mrk.title
            user_id = update.from_user.id

            if act == "":
                stat = "π²οΈπΎοΈπ½οΈπ½οΈπ΄οΈπ²οΈποΈ"
                cb = "connectcb"
            else:
                stat = "π³οΈπΈοΈποΈπ²οΈπΎοΈπ½οΈπ½οΈπ΄οΈπ²οΈποΈ"
                cb = "disconnect"

            pr0fess0r_99 = [[ InlineKeyboardButton(f"{stat}", callback_data=f"{cb}:{group_id}") ],
                            [ InlineKeyboardButton("π³π΄π»π΄ππ΄", callback_data=f"deletecb:{group_id}"), InlineKeyboardButton("π±π°π²πΊ", callback_data="backcb") ]]         
            pr0fess0r_99 = InlineKeyboardMarkup(pr0fess0r_99)
            await update.message.edit("""πΆππΎππΏ π½π°πΌπ΄: **{title}**\n πΆππΎππΏ πΈπ³: `{group_id}`""", reply_markup=pr0fess0r_99)        
            return

        elif update.data == "delallconfirm":
            userid = update.from_user.id
            chat_type = update.message.chat.type
            if chat_type == enums.ChatType.PRIVATE:
                grpid = await active_connection(str(userid))
                if grpid is not None:
                    grp_id = grpid
                    try:
                        chat = await bot.get_chat(grpid)
                        title = chat.title
                    except:
                        await update.message.edit("πΌπ°πΊπ΄ ππππ΄ πΈ'πΌ πΏππ΄ππ΄π½π πΈπ½ ππΎππ πΆππΎππΏ..!", quote=True)
                        return 
                else:
                    await update.message.edit("πΈπ°πΌ π½πΎπ π²πΎπ½π½π΄π²ππ΄π³ ππΎ π°π½π πΆππΎππΏ..!\n π²π·π΄π²πΊ /connections πΎπ π²πΎπ½π½π΄π²π ππΎ π°π½π πΆππΎππΏπ", quote=True)
                    return
            elif chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
                grp_id = update.message.chat.id
                title = update.message.chat.title
            else:
                return
            st = await bot.get_chat_member(grp_id, userid)
            if (st.status == enums.ChatMemberStatus.OWNER) or (str(userid) in ADMINS):
                await del_all(update.message, grp_id, title)
            else:
                await update.answer("ππΎπ π½π΄π΄π³ ππΎ π±π΄ πΆππΎππΏ πΎππ½π΄π πΎπ π°π½ π°π³πΌπΈπ½π ππΎ π³πΎ ππ·π°π.!", show_alert=True)

        elif update.data == "delallcancel":
            userid = update.from_user.id
            chat_type = update.message.chat.type
            if chat_type == enums.ChatType.PRIVATE:
                await update.message.reply_to_message.delete()
                await update.message.delete()
            elif chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
                grp_id = update.message.chat.id
                st = await bot.get_chat_member(grp_id, userid)
                if (st.status == enums.ChatMemberStatus.OWNER) or (str(userid) in ADMINS):
                    await update.message.delete()
                    try:
                        await update.message.reply_to_message.delete()
                    except:
                        pass
                else:
                    await update.answer("ππ·π°ππ'π π½πΎπ π΅πΎπ ππΎπ..!", show_alert=True)
    else:
        await update.answer("ππ·π°ππ'π π½πΎπ π΅πΎπ ππΎπ..!", show_alert=True)


