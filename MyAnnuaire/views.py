from django.shortcuts import render, get_object_or_404
from .models import Salarie, Site, Service
from django.db.models import Q

def liste_salaries(request):
    salaries = Salarie.objects.all()
    sites = Site.objects.all()
    services = Service.objects.all()
    return render(request, 'MyAnnuaire/liste_salaries.html', {'salaries': salaries, 'sites': sites, 'services': services})

def detail_salarie(request, pk):
    salarie = get_object_or_404(Salarie, pk=pk)
    return render(request, 'MyAnnuaire/detail_salarie.html', {'salarie': salarie})

def recherche_par_nom(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        if query:
            salaries = Salarie.objects.filter(
                Q(nom__icontains=query) | Q(prenom__icontains=query)
            )
            sites = Site.objects.all()
            services = Service.objects.all()
            return render(request, 'MyAnnuaire/liste_salaries.html', {'salaries': salaries, 'sites': sites, 'services': services, 'recherche_term': query})
        else:
            return render(request, 'MyAnnuaire/recherche_nom_form.html')
    return render(request, 'MyAnnuaire/recherche_nom_form.html')

def liste_sites(request):
    sites = Site.objects.all()
    return render(request, 'MyAnnuaire/liste_sites.html', {'sites': sites})

def salaries_par_site(request, ville):
    site = get_object_or_404(Site, ville=ville)
    salaries = Salarie.objects.filter(site=site)
    return render(request, 'MyAnnuaire/liste_salaries.html', {'salaries': salaries, 'titre': f"Salariés du site de {ville}"})

def liste_services(request):
    services = Service.objects.all()
    return render(request, 'MyAnnuaire/liste_services.html', {'services': services})

def salaries_par_service(request, nom):
    service = get_object_or_404(Service, nom=nom)
    salaries = Salarie.objects.filter(service=service)
    return render(request, 'MyAnnuaire/liste_salaries.html', {'salaries': salaries, 'titre': f"Salariés du service {nom}"})