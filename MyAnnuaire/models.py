from django.db import models

class Site(models.Model):
    ville = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.ville
    
    class Meta:
        db_table = 'site'

class Service(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom
    class Meta:
        db_table = 'service'

class Salarie(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    telephone_fixe = models.CharField(max_length=20, blank=True, null=True)
    telephone_portable = models.CharField(max_length=20)
    email = models.EmailField()
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True)
    site = models.ForeignKey(Site, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"
    class Meta:
        db_table = 'salarie'