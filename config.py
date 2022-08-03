# MIT License
# Copyright (c) 2022 Muhammed
import os, re
search = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


# Creator
CREATOR_NAME = os.environ.get("CREATOR_NAME", "Unknown(n1ck)")
CREATOR_USERNAME = os.environ.get("CREATOR_USERNAME", "BotFather")

# Account
API_HASH = os.environ.get("API_HASH", "7faeee7a2f3cc706f3502bf6a2a62276")
API_ID = os.environ.get("API_ID", "15117137")
# About Bot
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5589728506:AAHD1skSo5P0XC8BRa1Ab4s01NBI2KfhVOw")
PICS = os.environ.get("PICS", "https://telegra.ph/file/a7279d08e76fd6d405c42.jpg https://telegra.ph/file/b4b08bbd9424b6c89f84e.jpg")
# Database
DATABASE_NAME = os.environ.get("DATABASE_NAME", "new-mv-bot")
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://PN:PN@cluster0.kqqcs.mongodb.net/?retryWrites=true&w=majority")
# Chats & Users
ADMINS = os.environ.get("ADMINS", "959619649")
SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", "CineScopeGrp")
AUTH_CHANNEL = os.environ.get("AUTH_CHANNEL", "-1001745791083")
CHANNELS = [int(ch) if search.search(ch) else ch for ch in os.environ.get("CHANNELS", "-1001745791083").split()]
LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1001690739792")
GET_FILECHANNEL = os.environ.get("GET_FILECHANNEL", "-1001521887840")
FILTER_DEL_SECOND = int(os.environ.get("FILTER_DEL_SECOND", "600"))

# AutoFilter
AUTH_GROUPS = os.environ.get("AUTH_GROUPS", "-1001664531310")
AUTH_USERS = [int(user) if search.search(user) else user for user in os.environ.get('AUTH_USERS', '').split()]
FILTER_BUTTONS = os.environ.get("FILTER_BUTTONS", "10")
PROTECT_FILES = is_enabled((os.environ.get('PROTECT_FILES', "True")), True) 
