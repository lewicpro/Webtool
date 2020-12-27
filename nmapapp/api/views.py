
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
import nmap

class SearchedDomainNmapView(APIView):
    queryset = NmapRequests.objects.all()
    # serializer_class = SearchedDomainsSerializer
    # permission_classes = [IsAuthenticated]


    def get(self, request, format=None):
 
        passed = self.request.GET.get('nmap', None)

        print('here 2', passed )

        nm = nmap.PortScanner()   
        datas=nm.all_hosts()
        sing = [datas]
        print('obtained : ', sing)

        context={
            'scaned':nm.scan(passed, '22-443'),
            'commandline':nm.command_line(),
            # 'info':nm.scaninfo(),
            'all_hosts_scanned':nm.all_hosts()[0],
            'hostname':nm[nm.all_hosts()[0]].hostname(),
            'hostnames':nm[nm.all_hosts()[0]].hostnames(),
            'get_state':nm[nm.all_hosts()[0]].state(),
            'protocols':nm[nm.all_hosts()[0]].all_protocols(),
            'sctp':nm[nm.all_hosts()[0]].all_sctp(),
            'tcp':nm[nm.all_hosts()[0]].all_tcp(),
            'udp':nm[nm.all_hosts()[0]].all_udp(),
            'has_tcp':nm[nm.all_hosts()[0]].has_tcp(22),
            'has_tcp_state':nm[nm.all_hosts()[0]]['tcp'][22]['state'] ,
            'nifo_port':nm[nm.all_hosts()[0]]['tcp'],
          
          
          
        }
        return Response(context, status=HTTP_200_OK)

