import os
import sys
from datetime import datetime
from os import execl
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateProfileRequest
from Config import STRING, SUDO, BIO_MESSAGE, API_ID, API_HASH, STRING2, STRING3, STRING4 ,STRING5
import asyncio
from pyrogram import idle
a = API_ID
b = API_HASH
smex = STRING
smexx = STRING2
smexxx = STRING3
smexxxx = STRING4
smexxxxx = STRING5

if smex:
    session_name = str(smex)
    print("String 1 Found")
    idk = TelegramClient(StringSession(session_name), a, b)
    try:
        print("Booting Up The Client 1")
        idk.start()
    except Exception as e:
        idk = 1
        print(e)
        pass
else:
    print("Session 1 not Found")
    idk = 1
    pass
   
if smexx:
    session_name = str(smexx)
    print("String 2 Found")
    ydk = TelegramClient(StringSession(session_name), a, b)
    try:
        print("Booting Up The Client 2")
        ydk.start()
    except Exception as e:
        
        print(e)
        pass
else:
    print("Session 2 not Found")
    pass

if smexxx:
    session_name = str(smexxx)
    print("String 3 Found")
    wdk = TelegramClient(StringSession(session_name), a, b)
    try:
        print("Booting Up The Client 3")
        wdk.start()
    except Exception as e:
        print(e)
        pass
else:
    print("Session 3 not Found")
    pass

if smexxxx:
    session_name = str(smexxxx)
    print("String 4 Found")
    hdk = TelegramClient(StringSession(session_name), a, b)
    try:
        print("Booting Up The Client 4")
        hdk.start()
    except Exception as e:
        print(e)
        pass
else:
    print("Session 4 not Found")
    pass

if smexxxxx:
    session_name = str(smexxxxx)
    print("String 5 Found")
    sdk = TelegramClient(StringSession(session_name), a, b)
    try:
        print("Booting Up The Client 5")
        sdk.start()
    except Exception as e:
        print(e)
        pass
else:
    print("Session 5 not Found")
    pass
          
@idk.on(events.NewMessage(incoming=True, pattern=".bio"))
async def biook(e):
    if e.sender_id in SUDO:
        text = "Bio Applied Successfully"
        await e.reply(text, parse_mode=None, link_preview=None )
        await idk(UpdateProfileRequest(
            about=f'{BIO_MESSAGE}'
        ))

@idk.on(events.NewMessage(incoming=True, pattern=".spam"))
async def spam(e):
    if e.sender_id in SUDO:
        if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
            idk = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
            message = str(idk[1])
            counter = int(idk[0])
            chut=  await asyncio.wait([e.respond(message) for i in range(counter)])
            await e.delete()



@idk.on(events.NewMessage(incoming=True, pattern=".dspam"))
async def dspam(e):
    if e.sender_id in SUDO:
        input_str = "".join(e.text.split(maxsplit=1)[1:])
        spamDelay = float(input_str.split(" ", 2)[0])
        counter = int(input_str.split(" ", 2)[1])
        spam_message = str(input_str.split(" ", 2)[2])
        for _ in range(counter):
            await e.respond(spam_message)
            await asyncio.sleep(spamDelay)


@idk.on(events.NewMessage(incoming=True, pattern=".mspam"))
async def mspam(e):
    if e.sender_id in SUDO:
        input_str = "".join(e.text.split(maxsplit=1)[1:])
        counter = int(input_str.split(" ", 2)[0])
        reply_message = await e.get_reply_message()
        bro = reply_message.media
        for i in range(1, counter):
            await e.client.send_file(e.chat_id, bro)



@idk.on(events.NewMessage(incoming=True, pattern=".ping"))
@ydk.on(events.NewMessage(incoming=True, pattern=".ping"))
@wdk.on(events.NewMessage(incoming=True, pattern=".ping"))
@hdk.on(events.NewMessage(incoming=True, pattern=".ping"))
@sdk.on(events.NewMessage(incoming=True, pattern=".ping"))
async def ping(e):
    if e.sender_id in SUDO:
        start = datetime.now()
        xxx = "PINGING..."
        event = await e.reply(xxx, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"**PONG**: **{ms}**")




@idk.on(events.NewMessage(incoming=True, pattern=".restart"))
@ydk.on(events.NewMessage(incoming=True, pattern=".restart"))
@wdk.on(events.NewMessage(incoming=True, pattern=".restart"))
@hdk.on(events.NewMessage(incoming=True, pattern=".restart"))
@sdk.on(events.NewMessage(incoming=True, pattern=".restart"))
async def restart(e):
    if e.sender_id in SUDO:
        text = "**__Restart__**\n\Restarted the clients... Please wait till it reboots..."
        await e.reply(text, parse_mode=None, link_preview=None )
        try:
            await idk.disconnect()
        except Exception as e:
            print(e)
            pass
        try:
            await ydk.disconnect()
        except Exception as e:
            pass
        try:
            await wdk.disconnect()
        except Exception as e:
            pass
        try:
            await hdk.disconnect()
        except Exception as e:
            pass
        try:
            await sdk.disconnect()
        except Exception as e:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()

@idk.on(events.NewMessage(incoming=True, pattern=".help"))
async def help(e):
    if e.sender_id in SUDO:
       text = "Available Commands\n.spam\n.dspam\n.mspam\n.restart\n.ping"
       await e.reply(text, parse_mode=None, link_preview=None )
 
print("Started sucessfully")
    
idle()
