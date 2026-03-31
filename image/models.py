from django.db import models
from user.models import User  # your custom User model


class Farm(models.Model):
    farmer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='farms'
    )
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('farmer', 'name')

    def __str__(self):
        return f"{self.name} ({self.farmer.name})"


class FarmPoint(models.Model):
    farm = models.ForeignKey(
        Farm,
        on_delete=models.CASCADE,
        related_name='points'
    )
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"Point ({self.latitude}, {self.longitude}) for {self.farm.name}"
