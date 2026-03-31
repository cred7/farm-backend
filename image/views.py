from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Farm, FarmPoint
from .serializers import FarmSerializer, FarmPointSerializer
from .services.area import polygon_area_geodesic
from .services.image import get_coordinates
from rest_framework.parsers import MultiPartParser, FormParser


class FarmViewSet(viewsets.ModelViewSet):
    """
    CRUD for Farms and nested actions
    """
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Return farms only for the logged-in farmer
        return self.queryset.filter(farmer=self.request.user)

    def perform_create(self, serializer):
        # Link the farm to the logged-in farmer
        serializer.save(farmer=self.request.user)

    @action(detail=True, methods=['get'])
    def area(self, request, pk=None):
        """
        Returns farm area calculated from points
        """
        try:
            farm = self.get_queryset().get(pk=pk)
        except Farm.DoesNotExist:
            return Response({"error": "Farm not found"}, status=status.HTTP_404_NOT_FOUND)

        points = farm.points.all()
        coords = [(p.latitude, p.longitude) for p in points]

        if len(coords) < 3:
            return Response({"error": "Not enough points to calculate area"}, status=status.HTTP_400_BAD_REQUEST)

        area_m2 = polygon_area_geodesic(coords)
        return Response({
            "coord": coords,
            "area_m2": area_m2,
            "hectares": area_m2 / 10000,
            "acres": area_m2 * 0.000247105,
        })


class FarmPointUploadView(viewsets.ViewSet):
    """
    Upload image and create FarmPoint
    """
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    @action(detail=False, methods=['post'])
    def upload_image(self, request):
        image = request.FILES.get("image")
        farm_id = request.data.get("farm_id")
        print(image, farm_id)
        if not image:
            return Response({"error": "No image provided"}, status=status.HTTP_400_BAD_REQUEST)

        coords = get_coordinates(image)
        if not coords:
            return Response({"error": "No GPS data found in image"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            farm = Farm.objects.get(pk=farm_id, farmer=request.user)
        except Farm.DoesNotExist:
            return Response({"error": "Farm not found"}, status=status.HTTP_404_NOT_FOUND)

        point = FarmPoint.objects.create(
            farm=farm,
            latitude=coords[0],
            longitude=coords[1]
        )

        serializer = FarmPointSerializer(point)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
