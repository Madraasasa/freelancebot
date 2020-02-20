from telethon.sync import TelegramClient
from telethon import functions, types


name = 'madrid'
api_hash = 'c379b803cad89a8946812bafd806c561'

from telethon.sync import TelegramClient, events
with TelegramClient('name', 999772, api_hash) as client:
    client.send_message('me', 'Hello, myself!')
    print(client.download_profile_photo('me'))
    @client.on(events.NewMessage(pattern='(?i).*Hello'))
    async def handler(event):
        await event.reply('Hey!')
client.run_until_disconnected()
