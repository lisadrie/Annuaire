from django.core.management.base import BaseCommand
from faker import Faker
from MyAnnuaire.models import Salarie, Site, Service
import random

class Command(BaseCommand):
    help = 'Génère un nombre spécifié de faux salariés'

    def add_arguments(self, parser):
        parser.add_argument('nombre', type=int, help='Nombre de faux salariés à générer')

    def handle(self, *args, **options):
        nombre = options['nombre']
        fake = Faker('fr_FR')  

        sites = list(Site.objects.all())
        services = list(Service.objects.all())

        if not sites or not services:
            self.stdout.write(self.style.WARNING('Veuillez créer au moins un site et un service avant de générer des salariés.'))
            return

        for _ in range(nombre):
            nom = fake.last_name()
            prenom = fake.first_name()
            telephone_fixe = fake.phone_number() if random.choice([True, False]) else None
            telephone_portable = fake.phone_number()
            email = fake.email()
            service = random.choice(services)
            site = random.choice(sites)

            Salarie.objects.create(
                nom=nom,
                prenom=prenom,
                telephone_fixe=telephone_fixe,
                telephone_portable=telephone_portable,
                email=email,
                service=service,
                site=site
            )

        self.stdout.write(self.style.SUCCESS(f'{nombre} faux salariés ont été générés avec succès.'))