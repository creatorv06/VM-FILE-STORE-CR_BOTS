import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "27344784"))
  API_HASH = os.environ.get("API_HASH", "a12613f54c74d00bfb76cf8f0688c2ee")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "8056573673:AAHEnwKW1qGG1_twU7AUyDBTzUsECkLVRQs")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "VM_FILE_STORE_BOT")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002056408106"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "papajiurl.com")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "be436003d5e3c576b9753a6613d255f13484f7e0")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "6899191648"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://alibaba0:alibaba0@alibaba0.61vkq.mongodb.net/?retryWrites=true&w=majority")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001811300784")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002540488913"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ 💡FɪʟᴇSᴛᴏʀᴇBᴏᴛ💡]────⍟
│
├🤖 My Name: [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├📝 Language: [Python 3](https://www.python.org)
│
├🧰 Library: [Pyrogram](https://docs.pyrogram.org)
│
╰──────[ 🥰 ]───────────⍟
"""
  ABOUT_DEV_TEXT = f"""
👨‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [VISHWA](https://t.me/iTS_ViSHWA14)
 
 I am Super noob Please Support My Hard Work.

[Donate Me](https://t.me/Developerltr_bot)
"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

👨‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿:- VISHWA

ℹ️ How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.
"""
