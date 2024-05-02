from channels.generic.websocket import AsyncWebsocketConsumer
import json

from Benchmark.settings import channel_name_mapping


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user_id = "asim"
        channel_name_mapping[self.user_id] = self.channel_name
        print(f"Connected: {self.channel_name}")
        await self.accept()

    async def disconnect(self, close_code):
        if self.user_id in channel_name_mapping:
            print(f"Disconnected: {self.channel_name}")
            del channel_name_mapping[self.user_id]

    async def receive(self, text_data):
        print(f"Received: {text_data}")

    async def send_alert(self, message):
        print("INSIDE SEND ALERT", message)
        await self.send(text_data=json.dumps({
            'alert': message
        }))
