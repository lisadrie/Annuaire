from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_salaries, name='liste_salaries'),
    path('salarie/<int:pk>/', views.detail_salarie, name='detail_salarie'),
    path('recherche/nom/', views.recherche_par_nom, name='recherche_par_nom'),
    path('site/', views.liste_sites, name='liste_sites'),
    path('site/<str:ville>/salaries/', views.salaries_par_site, name='salaries_par_site'),
    path('service/', views.liste_services, name='liste_services'),
    path('service/<str:nom>/salaries/', views.salaries_par_service, name='salaries_par_service'),
]