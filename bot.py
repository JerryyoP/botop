import os
import sys
from datetime import datetime
from os import execl
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateProfileRequest
from Config import STRING, SUDO, BIO_MESSAGE, API_ID, API_HASH, STRING2
import asyncio
a = API_ID
b = API_HASH
c = STRING
d = STRING2
f = "1793755076:AAEFNio23JQ8i4hcXf2I3TFe9cF4nKoDFs0"
if c:
    session_name = str(c)
    print("String 1 Found")
    idk = TelegramClient(StringSession(session_name), a, b)
    try:
        print("Booting Up The Client 1")
        idk.start()
    except Exception as e:
        print(e)
        pass
else:
    print("Session 1 not Found")
    pass
   
if d:
    session_name = str(d)
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
async def ping(e):
    if e.sender_id in SUDO:
        start = datetime.now()
        xxx = "PINGING..."
        event = await e.reply(xxx, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"**PONG**: **{ms}**")




@idk.on(events.NewMessage(incoming=True, pattern=".restart"))
async def restart(e):
    if e.sender_id in SUDO:
        text = "RESTARTED, CHECK ME AFTER 2 MINUTES"
        await e.reply(text, parse_mode=None, link_preview=None )
        await idk.disconnect()
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()

@idk.on(events.NewMessage(incoming=True, pattern=".help"))
async def help(e):
    if e.sender_id in SUDO:
       text = "Available Commands\n.spam\n.dspam\n.mspam\n.restart\n.ping"
       await e.reply(text, parse_mode=None, link_preview=None )
 
print("started sucessfully")
if len(sys.argv) not in (1, 3, 4):
    idk.disconnect()
else:
    idk.run_until_disconnected()

