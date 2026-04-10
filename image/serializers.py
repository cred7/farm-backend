from rest_framework import serializers
from .models import Farm, FarmPoint, FarmHistory


class FarmPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmPoint
        fields = ["id", "latitude", "longitude", "is_boundary"]


class FarmHistorySerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = FarmHistory
        fields = [
            "id",
            "activity_type",
            "description",
            "date",
            "created_at",
            "updated_at",
            "image",
        ]

    def get_image(self, obj):
        if not obj.image:
            return None

        request = self.context.get("request")
        if request:
            return request.build_absolute_uri(obj.image.url)

        return obj.image.url


class FarmSerializer(serializers.ModelSerializer):
    points = FarmPointSerializer(many=True, read_only=True)
    history = FarmHistorySerializer(many=True, read_only=True)

    class Meta:
        model = Farm
        fields = [
            "id",
            "name",
            "created_at",
            "crop_type",
            "expected_yield",
            "points",
            "history",
        ]
