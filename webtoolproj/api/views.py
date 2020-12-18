
from rest_framework import routers, serializers, viewsets
from rest_framework import generics
from .serializers import *
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from django.conf import settings
from rest_framework.views import APIView
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.authtoken.models import Token
# ViewSets define the view behavior.
import whois

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(request, self):
        print(request.user)
        token = Token.objects.get(user=request.user)
        print(token.key)
        return User.objects.get(User=request.user)


class RequestView(generics.ListCreateAPIView):
    queryset = Requests.objects.all()
    serializer_class = RequestSerializer
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        return Response('content')


class SearchedDomainView(APIView):
    queryset = Requests.objects.all()
    serializer_class = SearchedDomainsSerializer
    # permission_classes = [IsAuthenticated]


    def get(self, request, format=None):
        print('here1' )
        passed = self.request.GET.get('domain', None)

        print('here 2', passed )

        domaine = whois.query(passed)       
        context={
            'domain':domaine.name,
            'info':domaine.__dict__
        }
        return Response(context, status=HTTP_200_OK)




class CreateUserView(generics.CreateAPIView):
    model = get_user_model()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
