from telethon import TelegramClient
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN, STRING

client = TelegramClient(
    "telethonbot",
    API_ID,
    API_HASH
)

app = Client(
    "pyrogrambot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

userbot = None

if STRING:
    userbot = Client(
        "4gbbot",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING
    )


async def start_client():

    if not client.is_connected():
        await client.start(bot_token=BOT_TOKEN)
        print("✓ Telethon Started")

    if userbot:
        try:
            await userbot.start()
            print("✓ Userbot Started")
        except Exception as e:
            raise RuntimeError(
                f"Invalid or expired STRING session: {e}"
            )

    if not app.is_connected:
        await app.start()
        print("✓ Pyrogram Started")

    return client, app, userbot


async def stop_client():

    try:
        if userbot and userbot.is_connected:
            await userbot.stop()
    except:
        pass

    try:
        if app.is_connected:
            await app.stop()
    except:
        pass

    try:
        if client.is_connected():
            await client.disconnect()
    except:
        pass
