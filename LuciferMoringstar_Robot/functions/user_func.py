 
from pyrogram.types import Message
from typing import Union

def extract_user(update: Message) -> Union[int, str]:
    """extracts the user from a message"""
    # https://github.com/SpEcHiDe/PyroGramBot/blob/f30e2cca12002121bad1982f68cd0ff9814ce027/pyrobot/helper_functions/extract_user.py#L7
    user_id = None
    user_first_name = None
    if update.reply_to_message:
        user_id = update.reply_to_message.from_user.id
        user_first_name = update.reply_to_message.from_user.first_name

    elif len(update.command) > 1:
        if (
            len(update.entities) > 1 and
            update.entities[1].type == "text_mention"
        ):
           
            required_entity = update.entities[1]
            user_id = required_entity.user.id
            user_first_name = required_entity.user.first_name
        else:
            user_id = update.command[1]
            # don't want to make a request -_-
            user_first_name = user_id
        try:
            user_id = int(user_id)
        except ValueError:
            pass
    else:
        user_id = update.from_user.id
        user_first_name = update.from_user.first_name
    return (user_id, user_first_name)
