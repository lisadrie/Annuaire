from django.contrib import admin
from ..models import Site

@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ('ville',)
    search_fields = ('ville',)