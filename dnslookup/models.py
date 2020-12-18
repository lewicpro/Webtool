from django.db import models

# Create your models here.


class Requests(models.Model):
    name = models.CharField(max_length=120, blank=True, null=True)
    link = models.CharField(max_length=120, blank=True, null=True)
    country = models.CharField(max_length=120, blank=True, null=True)
    phone = models.CharField(max_length=120, blank=True, null=True)
    email = models.CharField(max_length=120, blank=True, null=True)
    whatsapp = models.CharField(max_length=120, blank=True, null=True)
    twitter = models.CharField(max_length=120, blank=True, null=True)
    instagram = models.CharField(max_length=120, blank=True, null=True)
    Descriptions = models.CharField(max_length=120, blank=True, null=True)
    options = models.CharField(max_length=120, blank=True, null=True)


class SearchedDomains(models.Model):
    name=models.CharField(max_length=50, blank=False, null=True)

