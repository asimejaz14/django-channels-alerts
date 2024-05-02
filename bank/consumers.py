# consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from urllib.parse import parse_qs
import jwt
from django.conf import settings
from channels.db import database_sync_to_async
from django.contrib.auth.models import User


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Extract and verify JWT token from the query string
        # query_string = parse_qs(self.scope['query_string'].decode())
        # token = query_string.get('token', [None])[0]
        # user = await self.get_user_from_token(token)
        user = 'Asim'

        if user is not None:
            self.room_name = f"user_{user}"  # Create a unique room name for the user
            self.room_group_name = f"notification_{self.room_name}"

            # Join room group
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )
            await self.accept()
        else:
            await self.close()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'notification_message',  # this is the method name which sends the data to socket
                'message': message
            }
        )

    async def notification_message(self, event):
        message = event['message']
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))

    @database_sync_to_async
    def get_user_from_token(self, token):
        try:
            decoded_data = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user = User.objects.get(id=decoded_data['user_id'])
            return user
        except:
            return None
