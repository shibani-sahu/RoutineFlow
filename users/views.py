from rest_framework import generics, status
from django.contrib.auth.models import User
from rest_framework.response import Response
from .serializers import RegisterSerializer, LoginSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data= request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]

        return Response({
            "message" : "Login Successful",
            "username": user.username, 
            "email": user.email
        }, status = status.HTTP_200_OK)