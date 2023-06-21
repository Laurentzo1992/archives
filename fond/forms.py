from django import forms
from fond.models import *
from django.core.validators import RegexValidator



class SerieForm(forms.ModelForm):
    
    serie = forms.CharField(
        label='Serie',
        widget=forms.TextInput(attrs={'placeholder': 'Serie'})
    )
    
    entite = forms.CharField(
        label='Entité',
        widget=forms.TextInput(attrs={'placeholder': 'Entité'})
    )
    
    class  Meta:
        model = Serie
        fields = '__all__'
        
        
        
class Sous_serieForm(forms.ModelForm):
    
    sousserie = forms.CharField(
        label='Sous Serie',
        widget=forms.TextInput(attrs={'placeholder': 'Sous Serie'})
    )
    entite = forms.CharField(
        label='Entité',
        widget=forms.TextInput(attrs={'placeholder': 'Entité'})
    )
    duree = forms.IntegerField(
        label='Durée(ans)',
        widget=forms.TextInput(attrs={'placeholder': 'Duree'})
    )
    
    sort_final = forms.CharField(
        label='Sort final',
        widget=forms.TextInput(attrs={'placeholder': 'Sort final'})
    )
    
    class  Meta:
        model = Sous_serie
        fields = '__all__'
        
        
        
        
class Sous_sous_SerieForm(forms.ModelForm):
    
    soussousserie = forms.CharField(
        label='Sous Sous Serie',
        widget=forms.TextInput(attrs={'placeholder': 'Sous Sous Serie'})
    )
    entite = forms.CharField(
        label='Entité',
        widget=forms.TextInput(attrs={'placeholder': 'Entité'})
    )
    duree = forms.IntegerField(
        label='Durée(ans)',
        widget=forms.TextInput(attrs={'placeholder': 'Duree'})
    )
    
    sort_final = forms.CharField(
        label='Sort final',
        widget=forms.TextInput(attrs={'placeholder': 'Sort final'})
    )
    class  Meta:
        model = Sous_sous_Serie
        fields = '__all__'
        
        
        
        