from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from ..models import *
from django.db.models import Q
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model



class NmapRequestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NmapRequests
        fields = ['name', 'link', 'country', 'phone', 'email', 'whatsapp', 'twitter', 'instagram', 'options','Descriptions']


# class SearchedDomainsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SearchedDomains
#         fields = ['name']



