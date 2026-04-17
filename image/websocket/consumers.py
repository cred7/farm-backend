import json
from channels.generic.websocket import AsyncWebsocketConsumer


class FarmConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.farm_id = self.scope["url_route"]["kwargs"]["farm_id"]
        self.group_name = f"farm_{self.farm_id}"

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def farm_update(self, event):
        await self.send(text_data=json.dumps(event["data"]))
