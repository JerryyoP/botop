import os
import sys
from datetime import datetime
from os import execl
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateProfileRequest
from Config import STRING, SUDO, BIO_MESSAGE, API_ID, API_HASH, STRING2, STRING3, STRING4 ,STRING5, STRING6, STRING7, STRING8 ,STRING9, STRING10
import asyncio
import telethon.utils
a = API_ID
b = API_HASH
smex = STRING
smexx = STRING2
smexxx = STRING3
smexxxx = STRING4
smexxxxx = STRING5
sixth = STRING6
seven = STRING7
eight = STRING8
ninth = STRING9
tenth = STRING10


SMEX_USERS = []
SMEX_USERS.append(SUDO)


if smex:
    session_name = str(smex)
    print("String 1 Found")
    idk = TelegramClient(StringSession(session_name), a, b)
    try:
        print("Booting Up The Client 1")
        idk.start()
        botme = idk.get_me()
        botid = telethon.utils.get_peer_id(botme)
        SMEX_USERS.append(botid)
    except Exception as e:
        idk = "smex"
        print(e)
        pass
else:
    print("Session 1 not Found")
    session_name = "startup"
    idk = TelegramClient(session_name, a, b)
    try:
        idk.start()
    except Exception as e:
        pass
   
if smexx:
    session_name = str(smexx)
    print("String 2 Found")
    ydk = TelegramClient(StringSession(session_name), a, b)
    try:
        print("Booting Up The Client 2")
        ydk.start()
        botme = await ydk.get_me()
        botid = telethon.utils.get_peer_id(botme)
        SMEX_USERS.append(botid)
    except Exception as e:
        print(e)
        pass
else:
    print("Session 2 not Found")
    pass
    session_name = "startup"
    ydk = TelegramClient(session_name, a, b)
    try:
        ydk.start()
    except Exception as e:
        pass

if smexxx:
    session_name = str(smexxx)
    print("String 3 Found")
    wdk = TelegramClient(StringSession(session_name), a, b)
    try:
        print("Booting Up The Client 3")
        wdk.start()
        botme = await wdk.get_me()
        botid = telethon.utils.get_peer_id(botme)
        SMEX_USERS.append(botid)
    except Exception as e:
        print(e)
        pass
else:
    print("Session 3 not Found")
    pass
    session_name = "startup"
    wdk = TelegramClient(session_name, a, b)
    try:
        wdk.start()
    except Exception as e:
        pass

if smexxxx:
    session_name = str(smexxxx)
    print("String 4 Found")
    hdk = TelegramClient(StringSession(session_name), a, b)
    try:
        print("Booting Up The Client 4")
        hdk.start()
        botme = await hdk.get_me()
        botid = telethon.utils.get_peer_id(botme)
        SMEX_USERS.append(botid)
    except Exception as e:
        print(e)
        pass
else:
    print("Session 4 not Found")
    pass
    session_name = "startup"
    hdk = TelegramClient(session_name, a, b)
    try:
        hdk.start()
    except Exception as e:
        pass

if smexxxxx:
    session_name = str(smexxxxx)
    print("String 5 Found")
    sdk = TelegramClient(StringSession(session_name), a, b)
    try:
        print("Booting Up The Client 5")
        sdk.start()
        botme = await sdk.get_me()
        botid = telethon.utils.get_peer_id(botme)
        SMEX_USERS.append(botid)
    except Exception as e:
        print(e)
        pass
else:
    print("Session 5 not Found")
    pass
    session_name = "startup"
    sdk = TelegramClient(session_name, a, b)
    try:
        sdk.start()
    except Exception as e:
        pass
                  
if sixth:
    session_name = str(sixth)
    print("String 6 Found")
    sdk = TelegramClient(StringSession(session_name), a, b)
    try:
        print("Booting Up The Client 6")
        adk.start()
        botme = await adk.get_me()
        botid = telethon.utils.get_peer_id(botme)
        SMEX_USERS.append(botid)
    except Exception as e:
        print(e)
        pass
else:
    print("Session 6 not Found")
    pass
    session_name = "startup"
    adk = TelegramClient(session_name, a, b)
    try:
        adk.start()
    except Exception as e:
        pass

if seven:
    session_name = str(seven)
    print("String 7 Found")
    sdk = TelegramClient(StringSession(session_name), a, b)
    try:
        print("Booting Up The Client 7")
        bdk.start()
        botme = await bdk.get_me()
        botid = telethon.utils.get_peer_id(botme)
        SMEX_USERS.append(botid)
    except Exception as e:
        print(e)
        pass
else:
    print("Session 7 not Found")
    pass
    session_name = "startup"
    bdk = TelegramClient(session_name, a, b)
    try:
        bdk.start()
    except Exception as e:
        pass    
    
    
if eight:
    session_name = str(eight)
    print("String 8 Found")
    sdk = TelegramClient(StringSession(session_name), a, b)
    try:
        print("Booting Up The Client 8")
        cdk.start()
        botme = await cdk.get_me()
        botid = telethon.utils.get_peer_id(botme)
        SMEX_USERS.append(botid)
    except Exception as e:
        print(e)
        pass
else:
    print("Session 8 not Found")
    pass
    session_name = "startup"
    cdk = TelegramClient(session_name, a, b)
    try:
        cdk.start()
    except Exception as e:
        pass   
    
    
if ninth:
    session_name = str(ninth)
    print("String 9 Found")
    sdk = TelegramClient(StringSession(session_name), a, b)
    try:
        print("Booting Up The Client 9")
        ddk.start()
        botme = await ddk.get_me()
        botid = telethon.utils.get_peer_id(botme)
        SMEX_USERS.append(botid)
    except Exception as e:
        print(e)
        pass
else:
    print("Session 9 not Found")
    pass
    session_name = "startup"
    ddk = TelegramClient(session_name, a, b)
    try:
        ddk.start()
    except Exception as e:
        pass   
    
  
if tenth:
    session_name = str(tenth)
    print("String 10 Found")
    sdk = TelegramClient(StringSession(session_name), a, b)
    try:
        print("Booting Up The Client 10")
        edk.start()
        botme = await edk.get_me()
        botid = telethon.utils.get_peer_id(botme)
        SMEX_USERS.append(botid)
    except Exception as e:
        print(e)
        pass
else:
    print("Session 10 not Found")
    pass
    session_name = "startup"
    edk = TelegramClient(session_name, a, b)
    try:
        edk.start()
    except Exception as e:
        pass 
    
    
@idk.on(events.NewMessage(incoming=True, pattern=".bio (.*)"))
@ydk.on(events.NewMessage(incoming=True, pattern=".bio (.*)"))
@wdk.on(events.NewMessage(incoming=True, pattern=".bio (.*)"))
@hdk.on(events.NewMessage(incoming=True, pattern=".bio (.*)"))
@sdk.on(events.NewMessage(incoming=True, pattern=".bio (.*)"))
@sixth.on(events.NewMessage(incoming=True, pattern=".bio (.*)"))
@seven.on(events.NewMessage(incoming=True, pattern=".bio (.*)"))
@eight.on(events.NewMessage(incoming=True, pattern=".bio (.*)"))
@ninth.on(events.NewMessage(incoming=True, pattern=".bio (.*)"))
@tenth.on(events.NewMessage(incoming=True, pattern=".bio (.*)"))        
async def _(event):
    if event.fwd_from:
        return
    if event.sender_id not in SMEX_USERS:
        return
    bio = event.pattern_match.group(1)
    await event.delete()
    event = await edit_or_reply(event, "Trying")
    try:
        await event.client(functions.account.UpdateProfileRequest(about=bio))
        await event.edit("Succesfully changed my profile bio")
    except Exception as e:
        await event.edit(str(e))        
        
        
        
        
        
        
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
@sixth.on(events.NewMessage(incoming=True, pattern=".ping"))
@seven.on(events.NewMessage(incoming=True, pattern=".ping"))
@eight.on(events.NewMessage(incoming=True, pattern=".ping"))
@ninth.on(events.NewMessage(incoming=True, pattern=".ping"))
@tenth.on(events.NewMessage(incoming=True, pattern=".ping"))
async def ping(e):
    if e.sender_id in SMEX_USERS:
        event = await edit_or_reply(event, "Pong!")
        start = datetime.now()
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"🤖 𝗣𝗼𝗻𝗴!\n`{ms} 𝗺𝘀")




@idk.on(events.NewMessage(incoming=True, pattern=".restart"))
@ydk.on(events.NewMessage(incoming=True, pattern=".restart"))
@wdk.on(events.NewMessage(incoming=True, pattern=".restart"))
@hdk.on(events.NewMessage(incoming=True, pattern=".restart"))
@sdk.on(events.NewMessage(incoming=True, pattern=".restart"))
async def restart(e):
    if e.sender_id in SUDO:
        text = "**__Restart__**\n\nRestarted the clients... Please wait till it reboots..."
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
    
if len(sys.argv) not in (1, 3, 4):
    try:
        idk.disconnect()
    except Exception as e:
        pass
    try:
        ydk.disconnect()
    except Exception as e:
        pass
    try:
        wdk.disconnect()
    except Exception as e:
        pass
    try:
        hdk.disconnect()
    except Exception as e:
        pass
    try:
        sdk.disconnect()
    except Exception as e:
        pass
else:
    try:
        idk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        ydk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        wdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        hdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        sdk.run_until_disconnected()
    except Exception as e:
        pass
