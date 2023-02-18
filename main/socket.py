from channels.generic.websocket import AsyncWebsocketConsumer
import json


class Consumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('event', self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard('event', self.channel_name)

    async def message_send(self, event):
        await self.send(json.dumps(
            {
                'type': 'message.send',
                'object': event['object'],
                'action': event['action'],
                'data': event['data'],
            }
        ))
