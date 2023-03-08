from telethon import TelegramClient, events

api_id = '22878300'
api_hash = '1ae533d7273bd5824e6a5a29c46cfc8f'

ENTRY_LINK = 'https://t.me/canaltestee0'

with TelegramClient('name', api_id, api_hash) as client:
    id_cloned_channel = '1542598247'

    @client.on(events.NewMessage(pattern='(?i).*'))
    async def handler(event):
        destiny_channel = await client.get_entity(ENTRY_LINK)

        if (str(event.message.peer_id.channel_id) == id_cloned_channel):
            message = event.message.message
            await client.send_message(entity=destiny_channel, message=message)

    client.run_until_disconnected()