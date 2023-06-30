from django.db import models
from datetime import datetime

class Archive_statuts(models.Model):
    libelle = models.CharField(max_length=200, null=True, blank=True)
    create_at = models.DateField(auto_now_add=True, null=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.libelle
    
    
    
class Archive_type(models.Model):
    libelle = models.CharField(max_length=200, null=True, blank=True)
    create_at = models.DateField(auto_now_add=True, null=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.libelle



class Document_type(models.Model):
    libelle = models.CharField(max_length=200, null=True, blank=True)
    create_at = models.DateField(auto_now_add=True, null=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.libelle
    
    
    
class Provenance(models.Model):
    sigle = models.CharField(max_length=50, null=True, blank=True)
    nom = models.CharField(max_length=200, null=True, blank=True)
    create_at = models.DateField(auto_now_add=True, null=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.sigle
