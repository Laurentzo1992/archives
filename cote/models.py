from django.db import models


class Site(models.Model):
    site = models.CharField(max_length=100, null=True, blank=True)
    
    
    def __str__(self):
        return self.site
    
    
    
    
class Salle(models.Model):
    code = models.CharField(max_length=100, null=True, blank=True)
    salle = models.CharField(max_length=100, null=True, blank=True)
    site = models.ForeignKey(Site, null=True, blank=True, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.salle
    
    
    
class Travee(models.Model):
    travee = models.IntegerField(null=True, blank=True)
    salle = models.ForeignKey(Salle, null=True, blank=True, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return str(self.travee)
    
    
    
    
class Rayon(models.Model):
    rayon = models.CharField(null=True, blank=True, max_length=5)
    travee = models.ForeignKey(Travee, null=True, blank=True, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.rayon
    
    
    
    
class Boite(models.Model):
    boite = models.IntegerField(null=True, blank=True)
    rayon = models.ForeignKey(Rayon, null=True, blank=True, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return str(self.boite)