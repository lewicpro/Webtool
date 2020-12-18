from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from ..models import *
from django.db.models import Q
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model



class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requests
        fields = ['name', 'link', 'country', 'phone', 'email', 'whatsapp', 'twitter', 'instagram', 'options','Descriptions']


class SearchedDomainsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchedDomains
        fields = ['name']





class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True, label="Confirm pasword")

    class Meta:
        model =User
        fields = [
            'username',
            'password',
            'password2',
            'email'
           ]

    def create(self, validated_data):
        user = get_user_model().objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
            

        )
        user.set_password(validated_data['password'])
        user.save()
        return user



    def validate_password2(self, value):
        data = self.get_initial()
        password = data.get("password")
        # username = data.get("username", None)
        password2 = value
        if password != password2:
            raise ValidationError('passwords must be the same')
        return value


