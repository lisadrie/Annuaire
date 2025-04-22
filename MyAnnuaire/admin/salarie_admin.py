from django.contrib import admin
from ..models import  Salarie

@admin.register(Salarie)
class SalarieAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'telephone_portable', 'email', 'service', 'site')
    list_filter = ('service', 'site')
    search_fields = ('nom', 'prenom', 'email', 'telephone_portable', 'telephone_fixe')
    autocomplete_fields = ('service', 'site')
    fieldsets = (
        ('Informations Personnelles', {
            'fields': ('nom', 'prenom', 'email')
        }),
        ('Contact', {
            'fields': ('telephone_fixe', 'telephone_portable')
        }),
        ('Informations Professionnelles', {
            'fields': ('service', 'site')
        }),
    )