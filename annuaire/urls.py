"""
URL configuration for annuaire project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from MyAnnuaire import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.liste_salaries, name='liste_salaries'),
    # path('salarie/<int:pk>/', views.detail_salarie, name='detail_salarie'),
    # path('recherche/nom/', views.recherche_par_nom, name='recherche_par_nom'),
    # path('recherche/site/<str:ville>/', views.salaries_par_site, name='salaries_par_site'),
    # path('recherche/service/<str:nom>/', views.salaries_par_service, name='salaries_par_service'),
]

