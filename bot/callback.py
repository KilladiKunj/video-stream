# Copyright (C) 2021 By VeezMusicProject

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import Veez


@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""__❓ HOW TO USE THIS BOT:

1.) first, add me to your group.
2.) then promote me as admin and give all permissions except anonymous admin.
3.) add @{Veez.ASSISTANT_NAME } to your group.
4.) turn on the voice chat first before start to stream video.
5.) type /play (reply to video) to start streaming.
6.) type /stop to end the video streaming.__
    ⚠️𝗖𝗮𝗻'𝘁 𝗣𝗹𝗮𝘆 𝗙𝗶𝗹𝗲𝘀 𝗠𝗼𝗿𝗲 𝗧𝗵𝗮𝗻 20 𝗺𝗶𝗻𝘂𝘁𝗲𝘀⚠️

📝 **note: stream & stop command can only be executed by group admin only!**

**⚡ __Powered by @Arun_TG__ ⚡**""",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    "🏡 Go Back", callback_data="cbstart")
            ]]
        ))


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"✨ **Hello there, I am a telegram group video streaming bot.**\n\n💭 **I was created to stream videos in group "
        f"video chats easily.**\n\n❔ **To find out how to use me, please press the help button below** 👇🏻",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    "➕ Add me to your Group ➕", url=f"https://t.me/{Veez.BOT_USERNAME}?startgroup=true")
            ], [
                InlineKeyboardButton(
                    "❔ HOW TO USE THIS BOT", callback_data="cbguide")
            ], [
                InlineKeyboardButton(
                    "🌐 Terms & Condition", callback_data="cbinfo")
            ], [
                InlineKeyboardButton(
                    "📣 Channel 1", url=f"https://t.me/CinemaCIub"),
                InlineKeyboardButton(
                    "📣 Channel 2", url=f"https://t.me/unknown_leech_mirror")
            ], [
                InlineKeyboardButton(
                    "🧙🏻‍♂️ Owner", url=f"https://t.me/Arun_TG")
            ], [
                InlineKeyboardButton(
                    "📚 All Command List", callback_data="cblist")
            ]]
        ))


@Client.on_callback_query(filters.regex("cbinfo"))
async def cbinfo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🌐 **bot information !**

🤖 __This bot was created to stream video in telegram group video chats using several methods from WebRTC.__

💡 __Powered by PyTgcalls the Async client API for the Telegram Group Calls, and Pyrogram the telegram MTProto API 
Client Library and Framework in Pure Python for Users and Bots.__

__This bot licensed under GNU-GPL 3.0 License__""",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    "🏡 Go Back", callback_data="cbstart")
            ]]
        ),
        disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex("cblist"))
async def cblist(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**📚 All Command List:**

__➪ /play (reply to video or yt/live url) - to stream video
➪ /stop - stop the video streaming
➪ /song (song name) - download song from YT
➪ /vsong (video name) - download video from YT
➪ /lyric (song name) - lyric scrapper
➪ /join - invite assistant join to your group
➪ /leave - order assistant leave from your group__

   ⚠️𝗖𝗮𝗻'𝘁 𝗣𝗹𝗮𝘆 𝗙𝗶𝗹𝗲𝘀 𝗠𝗼𝗿𝗲 𝗧𝗵𝗮𝗻 20 𝗺𝗶𝗻𝘂𝘁𝗲𝘀⚠️

**🔰 EXTRA CMD:**

__➪ /tts (reply to text) - text to speech
➪ /alive - check bot alive status
➪ /ping - check bot ping status
➪ /uptime - check bot uptime status
➪ /sysinfo - check bot system information__

**💡 OWNER ONLY:**

__➪ /rmd - remove all downloaded files
➪ /rmw - remove all downloaded raw files
➪ /leaveall - order assistant leave from all group__

**⚡ __Powered by @Arun_TG__ ⚡**""",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    "🏡 Go Back", callback_data="cbstart")
            ]]
        ))


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    await query.message.delete()
