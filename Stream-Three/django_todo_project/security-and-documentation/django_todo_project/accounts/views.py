from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import RegistrationSerializer


class RegistrationView(APIView):

    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

        data = serializer.data

        user = User.objects.create(username=data['username'])
        user.set_password(data['password'])
        user.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
