import json
from time import timezone
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
     self.room_name = ...
     self.room_group_name = f"chat_{self.room_name}"

     if self.scope["user"].is_authenticated:
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()
        print(f"WebSocket connected for user: {self.scope['user']}")
     else:
        await self.close()

    async def disconnect(self, close_code):
        # Remove this channel from the room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
     print("Received data:", text_data)
     data = json.loads(text_data)
     message = data['message']
     receiver_id = data['receiver_id']

    # Log saving the message
     print(f"Saving message: {message} to receiver {receiver_id}")
     await self.save_message(message, receiver_id)

    # Log broadcasting
     await self.channel_layer.group_send(
         self.room_group_name,
         {
            'type': 'chat_message',
            'message': message,
            'sender_id': self.scope['user'].id,
            'receiver_id': receiver_id,
        }
     )

    async def chat_message(self, event):
        # Send the message to WebSocket
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'sender_id': event['sender_id'],
            'receiver_id': event['receiver_id'],
        }))

   
    @database_sync_to_async
    def save_message(self, message, receiver_id):
      from .models import Message
      from django.contrib.auth.models import User

      try:
        receiver = User.objects.get(id=receiver_id)
        saved_message = Message.objects.create(
            sender=self.scope['user'],
            receiver=receiver,
            content=message
        )
        print(f"Message saved: {saved_message.content}")
      except Exception as e:
        print(f"Error saving message: {e}")

