from django import forms
from django.core.validators import RegexValidator
from django.db import models
from paramettre.models import Provenance, Document_type, Archive_type, Archive_statuts
from fond.models import Serie, Sous_serie, Sous_sous_Serie
from cote.models import Site, Salle, Travee, Rayon, Boite
from gestion.models import Tache, Fichier, Descripteur
from datetime import datetime


### FORM CONTRAT ###

class TacheForm(forms.ModelForm):
    

    analyse = forms.CharField(
        label='Analyse',
        widget=forms.TextInput(attrs={'placeholder': 'analyse'})
    )
    current_year = datetime.now().year
    year_choices = [(str(year), str(year)) for year in range(1900, current_year + 1)]
    date_extrem = forms.ChoiceField(choices=year_choices, label='Année', initial=str(current_year))

    
    def clean_year_field(self):
        year = self.cleaned_data['date_extrem']
        return year

    class Meta:
        model = Tache
        fields = '__all__'
        
        
        
class FichierForm(forms.ModelForm):
    
    fichier = forms.FileField(
        label='Fichier',
        widget=forms.TextInput(attrs={'placeholder': 'Fichier'})
    )
    
    class  Meta:
        model = Fichier
        fields = '__all__'
        
        
        
        
class DescripteurForm(forms.ModelForm):
    
    descripteur = forms.CharField(
        label='Descripteur',
        widget=forms.TextInput(attrs={'placeholder': 'Descripteur'})
    )
    
    class  Meta:
        model = Descripteur
        fields = '__all__'
        






