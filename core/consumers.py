import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import UserSession
from uuid import UUID
from urllib.parse import parse_qs

class RadioConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.frequency = self.scope["url_route"]["kwargs"]["frequency"]
        self.room_group_name = f"channel_{self.frequency}"

        # Parse query string instead of header
        query_string = self.scope.get("query_string", b"").decode()
        query_params = parse_qs(query_string)
        token_list = query_params.get("token", [])
        token = token_list[0] if token_list else None

        try:
            UUID(token)
            self.user = await self.get_user(token)
            if self.user is None:
                await self.close()
                return
        except Exception:
            await self.close()
            return

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "radio_message",
                "message": data.get("message"),
                "callsign": self.user.callsign if self.user else "Unknown"
            }
        )

    async def radio_message(self, event):
        await self.send(text_data=json.dumps({
            "callsign": event["callsign"],
            "message": event["message"]
        }))

    @database_sync_to_async
    def get_user(self, session_id):
        try:
            return UserSession.objects.get(session_id=session_id)
        except UserSession.DoesNotExist:
            return None
