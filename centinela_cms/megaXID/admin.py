from django.contrib import admin
from .models import Artist
from django.conf import settings
from bs4 import BeautifulSoup
from django.utils.translation import ugettext_lazy as _


class ArtistAdmin(admin.ModelAdmin):
    model = Artist
    list_display = ['first_name', 'last_name', 'id_number', 'created_date', 'gender', 'email']
    list_filter = ['created_date', 'gender']
    search_fields = ['first_name', 'last_name', 'id_number', 'email', 'payment']
admin.site.register(Artist, ArtistAdmin)