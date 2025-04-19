from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio

# Auto delete incoming or bot-sent video messages after 60 seconds
@Client.on_message(filters.video & (filters.private | filters.group))
async def auto_delete_incoming_video(client: Client, message: Message):
    try:
        await asyncio.sleep(60)
        await message.delete()
    except Exception as e:
        print(f"Failed to delete incoming video: {e}")

@Client.on_message(filters.video & filters.me)
async def auto_delete_sent_video(client: Client, message: Message):
    try:
        await asyncio.sleep(60)
        await message.delete()
    except Exception as e:
        print(f"Failed to delete bot-sent video: {e}")
