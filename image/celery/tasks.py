from celery import shared_task
from ..models import FarmHistory
from ..ml.analyzer import analyze_image
from .ws import push_farm_update


@shared_task(bind=True)
def analyze_farm_image_task(self, history_id):
    history = FarmHistory.objects.get(id=history_id)

    history.status = "PROCESSING"
    history.save()
    print(f"Processing image for activity {history.id}...")
    try:
        # ML inference (image is in media/activity_images/)
        result = analyze_image(history.image.path)
        print(f"ML result for activity {history.id}: {result}")
        history.ml_result = result
        history.status = "DONE"
        history.save()

        push_farm_update(history)

    except Exception as e:
        history.status = "FAILED"
        history.save()
        raise e
