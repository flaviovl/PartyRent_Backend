from django.contrib.auth.models import Group
from .models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'is_administrator',
            'phone_number',
            'birth_date',
            'email',
            'password',
            'picture'
        ]

        def create(self, validated_data):
            user = User(
                name=validated_data.get('name', None),
                email=validated_data.get('email', None),
            )
            user.set_password(validated_data.get('password', None))
            user.save()
            return user

        def update(self, instance, validated_data):
            for field in validated_data:
                if field == 'password':
                    instance.set_password(validated_data.get(field))
                else:
                    instance.__setattr__(field, validated_data.get(field))
            instance.save()
            return instance
