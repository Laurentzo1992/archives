from django.db import models
from paramettre.models import *
from fond.models import *
from cote.models import *
from datetime import datetime



class Fichier(models.Model):
    fichier = models.FileField(upload_to='archives', null=True, blank=True)
    create_at = models.DateField(auto_now_add=True, null=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.fichier
    
    
    
    @property
    def fileURL(self):
        try:
            url = self.fichier.url
        except:
            url = ''
        return url
    
    
    
    
class Descripteur(models.Model):
    descripteur = models.CharField(max_length=250, null=True, blank=True)
    create_at = models.DateField(auto_now_add=True, null=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.descripteur


class Tache(models.Model):
    provenance = models.ForeignKey(Provenance, null=True, blank=True, on_delete=models.CASCADE)
    analyse = models.TextField()
    date_extrem = models.CharField(max_length=10, null=True, blank=True)
    type_doc = models.ForeignKey(Document_type, null=True, blank=True, on_delete=models.CASCADE)
    doc_manquant = models.TextField()
    type_archive = models.ForeignKey(Archive_type, null=True, blank=True, on_delete=models.CASCADE)
    status_archive = models.ForeignKey(Archive_statuts, null=True, blank=True, on_delete=models.CASCADE)
    
    serie = models.ForeignKey(Serie, null=True, blank=True, on_delete=models.CASCADE)
    sous_serie = models.ForeignKey(Sous_serie, null=True, blank=True, on_delete=models.CASCADE)
    sous_sous_serie = models.ForeignKey(Sous_sous_Serie, null=True, blank=True, on_delete=models.CASCADE)
    
    site = models.ForeignKey(Site, null=True, blank=True, on_delete=models.CASCADE)
    salle = models.ForeignKey(Salle, null=True, blank=True, on_delete=models.CASCADE)
    travee = models.ForeignKey(Travee, null=True, blank=True, on_delete=models.CASCADE)
    rayon = models.ForeignKey(Rayon, null=True, blank=True, on_delete=models.CASCADE)
    boite = models.ForeignKey(Boite, null=True, blank=True, on_delete=models.CASCADE)
    cote = models.CharField(max_length=200, null=True, blank=True)
    fichier = models.ManyToManyField(Fichier, through='FichierArchive')
    descripteur = models.ManyToManyField(Descripteur, through='DescripteurArchive')
    create_at = models.DateField(auto_now_add=True, null=True)
    modified_at = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return self.analyse
    
    
    
class FichierArchive(models.Model):
    archive = models.ForeignKey(Tache, null=True, blank=True, on_delete=models.CASCADE)
    fichier = models.ForeignKey(Fichier, null=True, blank=True, on_delete=models.CASCADE)
    create_at = models.DateField(auto_now_add=True, null=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.archive





class DescripteurArchive(models.Model):
    archive = models.ForeignKey(Tache, null=True, blank=True, on_delete=models.CASCADE)
    descripteur = models.ForeignKey(Descripteur, null=True, blank=True, on_delete=models.CASCADE)
    create_at = models.DateField(auto_now_add=True, null=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.archive
    
    
    
