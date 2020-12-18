from django.contrib import admin
from .models import *

# Register your models here.


class RequestsAdmin(admin.ModelAdmin):
    list_display = ['name', 'link', 'country', 'phone', 'email', 'whatsapp', 'twitter', 'instagram', 'Descriptions', 'options']
    
class SearchedDomainsAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Requests, RequestsAdmin)
admin.site.register(SearchedDomains, SearchedDomainsAdmin)
