from django.db import models
from datetime import datetime

class Serie(models.Model):
    serie = models.CharField(max_length=5, null=True, blank=True)
    entite = models.CharField(max_length=200, null=True, blank=True)
    create_at = models.DateField(auto_now_add=True, null=True)
    modified_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.serie

class Sous_serie(models.Model):
    sousserie = models.CharField(max_length=5, null=True, blank=True)
    entite = models.CharField(max_length=200, null=True, blank=True)
    serie = models.ForeignKey(Serie, null=True, blank=True, on_delete=models.CASCADE)
    duree = models.IntegerField()
    sort_final = models.CharField(max_length=200, null=True, blank=True)
    create_at = models.DateField(auto_now_add=True, null=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.sousserie


class Sous_sous_Serie(models.Model):
    soussousserie = models.CharField(max_length=5, null=True, blank=True)
    entite = models.CharField(max_length=200, null=True, blank=True)
    sousserie = models.ForeignKey(Sous_serie, null=True, blank=True, on_delete=models.CASCADE)
    duree = models.IntegerField()
    sort_final = models.CharField(max_length=200, null=True, blank=True)
    create_at = models.DateField(auto_now_add=True, null=True)
    modified_at = models.DateTimeField(auto_now_add=True)  
    
    def __str__(self):
        return self.soussousserie