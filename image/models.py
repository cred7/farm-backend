from django.db import models
from user.models import User


class Farm(models.Model):
    farmer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="farms")
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    crop_type = models.CharField(max_length=100, blank=True)
    expected_yield = models.FloatField(null=True, blank=True)

    class Meta:
        unique_together = ("farmer", "name")

    def __str__(self):
        return f"{self.name} ({self.farmer})"


class FarmPoint(models.Model):
    farm = models.ForeignKey(
        Farm, on_delete=models.CASCADE, related_name="points")
    latitude = models.FloatField()
    longitude = models.FloatField()
    is_boundary = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.latitude}, {self.longitude} - {self.farm.name}"


class FarmHistory(models.Model):
    ACTIVITY_TYPES = [
        ("PLANTING", "Planting"),
        ("SPRAYING", "Spraying"),
        ("HARVEST", "Harvest"),
        ("FERTILIZING", "Fertilizing"),
        ("OTHER", "Other"),
    ]

    farm = models.ForeignKey(
        Farm, on_delete=models.CASCADE, related_name="history"
    )

    activity_type = models.CharField(max_length=50, choices=ACTIVITY_TYPES)
    description = models.TextField(blank=True)

    date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    image = models.ImageField(
        upload_to="activity_images/", null=True, blank=True
    )

    status = models.CharField(
        max_length=20,
        default="PENDING"
    )

    ml_result = models.JSONField(null=True, blank=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.activity_type} - {self.farm.name}"
