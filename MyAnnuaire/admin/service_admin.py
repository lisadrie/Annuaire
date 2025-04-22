from django.contrib import admin
from ..models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ('nom',)