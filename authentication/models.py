from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    PUBLIC = 'PUBLIC'
    ARCHIVISTE = 'ARCHIVISTE'
    ADMINISTRATEUR = 'ADMINISTRATEUR'
    
    ROLE_CHOICES = (
    (PUBLIC, 'Public'),
    (ARCHIVISTE, 'Archiviste'),
    (ADMINISTRATEUR, 'Administrateur')
    )
    photo = models.ImageField(upload_to='users_img/', null=True, blank=True)
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Rôle')
    
    @property
    def fileURL(self):
        try:
            url = self.photo.url
        except:
            url = ''
        return url