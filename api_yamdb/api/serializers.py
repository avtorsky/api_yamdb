from django.shortcuts import get_object_or_404
from rest_framework.validators import UniqueValidator
from rest_framework import serializers

from reviews.models import User, Category, Genre, Title, Review, Comment


class UserRegistrSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True,
        validators=[
            UniqueValidator(queryset=User.objects.all())]
    )
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    class Meta:
        model = User
        fields = ['username', 'email',]
    
    def validate_username(self, user):
        if user.lower() == 'me':
            raise serializers.ValidationError('username не может быть  "me".')
        return user


class TokenSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    confirmation_code = serializers.CharField()
    
    class Meta:
        model = User
        fields = (
            'confirmation_code',
            'username'
        )


class UserEditSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("username", "email", "first_name",
                  "last_name", "bio", "role")
        model = User
        read_only_fields = ('role',)

    def validate_username(self, user):
        if user.lower() == 'me':
            raise serializers.ValidationError('username не может быть  "me".')
        return user