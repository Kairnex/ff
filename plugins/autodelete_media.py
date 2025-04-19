from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio

# Filter for video messages (sent by bot or incoming replies)
@Client.on_message(filters.video & (filters.private | filters.group))
async def auto_delete_video(client: Client, message: Message):
    try:
        # Optional: You can add more checks here
        await asyncio.sleep(60)
        await message.delete()
    except Exception as e:
        print(f"Failed to delete message: {e}")
