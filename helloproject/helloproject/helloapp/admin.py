from django.contrib import admin

from . models import Place
from django.contrib.sites.models import Site

# Register your models here.
admin.site.register(Place)
