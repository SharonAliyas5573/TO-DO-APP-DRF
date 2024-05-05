
from rest_framework import authentication
from rest_framework import exceptions
from .models import Token
from django.utils import timezone
import datetime
from rest_framework.exceptions import AuthenticationFailed
import jwt
from django.conf import settings
import time

class JwtTokensAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token_id = request.headers.get("Authorization", "")
        try:
            print(token_id)
            payload = jwt.decode(token_id, settings.JWT_SETTINGS['SECRET_KEY'], algorithms=[settings.JWT_SETTINGS['ALGORITHM']])
            print(payload)
            token_obj = Token.objects.get(token=token_id)
            if token_obj.expires_at < timezone.now():
                raise AuthenticationFailed('Token has expired')

            return payload, None
        except Exception as e:
            print(e)
            raise exceptions.AuthenticationFailed(
                detail={"code": 401, "message": "Expired or Invalid Token"}
            )