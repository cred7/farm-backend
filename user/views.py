from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import RegisterSerializer, CustomTokenSerializer, UserDetailSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# Register endpoint


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        print(serializer)
        try:
            serializer.is_valid(raise_exception=True)
            if serializer.is_valid():
                serializer.save()
            return Response({"message": "User created"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Login endpoint


class CustomTokenView(TokenObtainPairView):
    serializer_class = CustomTokenSerializer

# Example protected view


class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserDetailSerializer(request.user)
        return Response(serializer.data)
