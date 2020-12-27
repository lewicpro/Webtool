from .views import *
from django.urls import path, include
# from rest_framework impauth_tokenort routers, viewsets
from rest_framework.authtoken.views import obtain_auth_token

# Additionally, we include login URLs for the browsable API.

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

urlpatterns = [
    # path('nmap', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls')),
    # path('Requests/', RequestView.as_view(), name='requestst'),
    # path('login/', obtain_auth_token, name='login'),
    # path('Register/', CreateUserView.as_view(), name='nubergen'),
    path('nmap/', SearchedDomainNmapView.as_view(), name='nmap'),
    # path('Domains/:<str:passed>/', SearchedDomainView.as_view(), name='domain'),
]
