from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio

# Helper to check for video-like documents
async def is_video_document(msg: Message):
    return msg.document and msg.document.mime_type and msg.document.mime_type.startswith("video")

# Auto delete incoming video messages
@Client.on_message((filters.video | filters.document) & (filters.private | filters.group))
async def auto_delete_incoming_video(client: Client, message: Message):
    try:
        if message.video or await is_video_document(message):
            print("[Autodelete] Video message detected. Waiting 60s...")
            await asyncio.sleep(60)
            await message.delete()
    except Exception as e:
        print(f"Failed to delete incoming video: {e}")

# Auto delete videos sent by the bot itself
@Client.on_message((filters.video | filters.document) & filters.outgoing)
async def auto_delete_sent_video(client: Client, message: Message):
    try:
        if message.video or await is_video_document(message):
            print("[Autodelete] Bot sent video. Waiting 60s...")
            await asyncio.sleep(60)
            await message.delete()
    except Exception as e:
        print(f"Failed to delete bot-sent video: {e}")
