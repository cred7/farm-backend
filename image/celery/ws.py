from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


def push_farm_update(history):
    channel_layer = get_channel_layer()

    async_to_sync(channel_layer.group_send)(
        f"farm_{history.farm.id}",
        {
            "type": "farm.update",
            "data": {
                "history_id": history.id,
                "status": history.status,
                "ml_result": history.ml_result,
            }
        }
    )
