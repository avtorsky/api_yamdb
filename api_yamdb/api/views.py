from operator import imod
from django.shortcuts import get_object_or_404
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.decorators import api_view  
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken

from .serializers import TokenSerializer, UserRegistrSerializer
from reviews.models import User

CONF_CODE = 1234

@api_view(['POST',])
def regist(request):
    serializer = UserRegistrSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    user = get_object_or_404(
        User,
        username=serializer.validated_data["username"]
    )
    confirmation_code = default_token_generator.make_token(user)
    send_mail(
        subject='YaMDb регистрация',
        message=f'Ваш код подтверждения: {confirmation_code}',
        from_email=None,
        recipient_list=[user.email],
        fail_silently=True
    )
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST',])
def get_jwt_token(request):
    serializer = TokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = get_object_or_404(
        User,
        username=serializer.validated_data['username']
    )
    print(serializer.validated_data['confirmation_code'])
    if default_token_generator.check_token(
        user, serializer.validated_data['confirmation_code']
    ):
        token = AccessToken.for_user(user)
        return Response({'token': str(token)}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
