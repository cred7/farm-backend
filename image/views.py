from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

from .models import Farm, FarmPoint, FarmHistory
from .serializers import FarmSerializer, FarmPointSerializer, FarmHistorySerializer
from .services.area import polygon_area_geodesic
from .services.image import get_coordinates


class FarmViewSet(viewsets.ModelViewSet):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(farmer=self.request.user)

    def perform_create(self, serializer):
        serializer.save(farmer=self.request.user)

    @action(detail=True, methods=["get"])
    def area(self, request, pk=None):
        farm = get_object_or_404(Farm, pk=pk, farmer=request.user)

        coords = [(p.latitude, p.longitude) for p in farm.points.all()]

        if len(coords) < 3:
            return Response({"error": "Not enough points"}, status=400)

        area_m2 = polygon_area_geodesic(coords)

        return Response({
            "area_m2": round(area_m2, 2),
            "hectares": round(area_m2 / 10000, 2),
            "acres": round(area_m2 / 4046.856, 2),
        })

    @action(detail=True, methods=["get"])
    def summary(self, request, pk=None):
        farm = get_object_or_404(Farm, pk=pk, farmer=request.user)

        coords = [(p.latitude, p.longitude) for p in farm.points.all()]
        area = polygon_area_geodesic(coords) if len(coords) >= 3 else 0

        return Response({
            "id": farm.id,
            "name": farm.name,
            "crop_type": farm.crop_type,
            "expected_yield": farm.expected_yield,
            "points_count": farm.points.count(),
            "area_m2": round(area, 2),
            "hectares": round(area / 10000, 2),
            "acres": round(area / 4046.856, 2),
            "activities": FarmHistorySerializer(
                farm.history.all(),
                many=True,
                context={"request": request}
            ).data
        })

    @action(detail=True, methods=["post"], parser_classes=[MultiPartParser, FormParser])
    def add_activity(self, request, pk=None):
        farm = get_object_or_404(Farm, pk=pk, farmer=request.user)

        activity_type = request.data.get("activity_type")
        if not activity_type:
            return Response({"error": "activity_type required"}, status=400)

        history = FarmHistory.objects.create(
            farm=farm,
            activity_type=activity_type,
            description=request.data.get("description", ""),
            image=request.data.get("image"),
        )

        return Response(
            FarmHistorySerializer(history, context={"request": request}).data
        )

    @action(detail=True, methods=["patch"])
    def update_activity(self, request, pk=None):
        farm = get_object_or_404(Farm, pk=pk, farmer=request.user)

        activity = get_object_or_404(
            FarmHistory,
            id=request.data.get("activity_id"),
            farm=farm
        )

        activity.activity_type = request.data.get(
            "activity_type", activity.activity_type)
        activity.description = request.data.get(
            "description", activity.description)
        activity.save()

        return Response(
            FarmHistorySerializer(activity, context={"request": request}).data
        )

    @action(detail=True, methods=["delete"])
    def delete_activity(self, request, pk=None):
        farm = get_object_or_404(Farm, pk=pk, farmer=request.user)

        activity = get_object_or_404(
            FarmHistory,
            id=request.data.get("activity_id"),
            farm=farm
        )

        activity.delete()
        return Response({"success": True})


class FarmPointViewSet(viewsets.ModelViewSet):
    queryset = FarmPoint.objects.all()
    serializer_class = FarmPointSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get_queryset(self):
        return self.queryset.filter(farm__farmer=self.request.user)

    def create(self, request, *args, **kwargs):
        farm = get_object_or_404(
            Farm,
            id=request.data.get("farm_id"),
            farmer=request.user
        )

        image = request.data.get("image")

        if not image:
            return Response({"error": "image required"}, status=400)

        lat, lng = get_coordinates(image)

        point = FarmPoint.objects.create(
            farm=farm,
            latitude=lat,
            longitude=lng,
            is_boundary=request.data.get("is_boundary", True),
        )

        return Response({
            "id": point.id,
            "lat": point.latitude,
            "lng": point.longitude
        })

    @action(detail=False, methods=["post"], url_path="upload_image")
    def upload_image(self, request):
        farm_id = request.data.get("farm_id")
        lat = request.data.get("lat")
        lng = request.data.get("lng")

        farm = get_object_or_404(Farm, id=farm_id, farmer=request.user)

        point = FarmPoint.objects.create(
            farm=farm,
            latitude=lat,
            longitude=lng,
            is_boundary=request.data.get("is_boundary", True),
        )

        return Response({
            "id": point.id,
            "lat": point.latitude,
            "lng": point.longitude
        }, status=201)
