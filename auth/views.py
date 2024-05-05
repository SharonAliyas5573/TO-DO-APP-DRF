from rest_framework import permissions, views, status
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth import authenticate
from rest_framework import permissions, views, status
from rest_framework.response import Response
from jose import jwt 
import datetime
import time
from TO_DO_DRF import settings
from .models import Token
from .authenticate import JwtTokensAuthentication


class RegisterView(views.APIView):

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

class LoginView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            payload = {
                'user_id': user.id,
                'exp': int(time.time()) + int(settings.JWT_SETTINGS['EXP_DELTA_SECONDS'].total_seconds())
            }
            token = jwt.encode(payload, settings.JWT_SETTINGS['SECRET_KEY'], algorithm=settings.JWT_SETTINGS['ALGORITHM'])
            Token.objects.create(user=user, token=token, expires_at=datetime.datetime.fromtimestamp(payload['exp']))
            return Response({"access_token": token})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)
        
class TestView(views.APIView):
    authentication_classes = [JwtTokensAuthentication]
    def get(self, request, *args, **kwargs):
        return Response({"message": "Hello, World!"})