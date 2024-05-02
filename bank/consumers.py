from channels.generic.websocket import AsyncWebsocketConsumer
import json

from bank.views import channel_name_mapping


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # self.user_id = self.scope["user"].id  # Assuming 'user' is authenticated
        self.user_id = "asim"
        # Register user's channel with global mapping
        channel_name_mapping[self.user_id] = self.channel_name
        await self.accept()

    async def disconnect(self, close_code):
        # Remove user's channel from the mapping when they disconnect
        if self.user_id in channel_name_mapping:
            del channel_name_mapping[self.user_id]

    async def receive(self, text_data):
        # Handle incoming message if necessary
        pass

    async def send_alert(self, message):
        await self.send(text_data=json.dumps({
            'alert': message
        }))
