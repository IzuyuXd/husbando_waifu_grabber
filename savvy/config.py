import os
from dotenv import load_dotenv

env = load_dotenv("config.env")

if env:
    OWNER_ID = os.environ.get("OWNER_ID")
    sudo_users = list(map(int, os.environ.get("sudo_users", "").split()))
    GROUP_ID = os.environ.get("GROUP_ID")
    TOKEN = os.environ.get("TOKEN")
    mongo_url = os.environ.get("MONGODB_URL")
    if os.environ.get("PHOTO_URL") != None:
        PHOTO_URL = os.environ.get("PHOTO_URL") 
    else:
        PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT")
    UPDATE_CHAT = os.environ.get("UPDATE_CHAT")
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
    CHARA_CHANNEL_ID = os.environ.get("CHARA_CHANNEL_ID")
    api_id = os.environ.get("api_id")
    api_hash = os.environ.get("api_hash")
else:
    OWNER_ID = 7200052671
    sudo_users = ["7200052671"]
    GROUP_ID = -1002219450332
    TOKEN = "7257328725:AAF4dynU4pOVdDfipgysNldqVZZT62f9NGw"
    mongo_url = "mongodb+srv://MayuraSan:MayuraSan@cluster0.cconah4.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "WaifuCatcherSupport"
    UPDATE_CHAT = "waifucatcherupdate"
    BOT_USERNAME = "waifucatcherrobot"
    CHARA_CHANNEL_ID = -1002247616568
    api_id = 16136051
    api_hash = "0f558cfd8541ededbd14e0b22768af5d"
