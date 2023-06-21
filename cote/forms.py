from django import forms
from cote.models import Site, Salle, Travee, Rayon, Boite
from django.core.validators import RegexValidator



class SiteForm(forms.ModelForm):
    
    site = forms.CharField(
        label='Site',
        widget=forms.TextInput(attrs={'placeholder': 'Site'})
    )
    
    class  Meta:
        model = Site
        fields = '__all__'
        
        
        
class SalleForm(forms.ModelForm):
    
    code = forms.CharField(
        label='Code',
        widget=forms.TextInput(attrs={'placeholder': 'code'})
    )
    salle = forms.CharField(
        label='Salle',
        widget=forms.TextInput(attrs={'placeholder': 'salle'})
    )
    
    class  Meta:
        model = Salle
        fields = '__all__'
        
        
        
        
class TraveeForm(forms.ModelForm):
    
    travee = forms.IntegerField(
        label='Travee',
        widget=forms.TextInput(attrs={'placeholder': 'travee'})
    )
    
    class  Meta:
        model = Travee
        fields = '__all__'
        
        
        
        
class RayonForm(forms.ModelForm):
    
    rayon = forms.CharField(
        label='Rayon',
        widget=forms.TextInput(attrs={'placeholder': 'Rayon'})
    )
    
    
    class  Meta:
        model = Rayon
        fields = '__all__'
        


class BoiteForm(forms.ModelForm):
    
    boite = forms.IntegerField(
        label='Boite',
        widget=forms.TextInput(attrs={'placeholder': 'Boite'})
    )
    
    
    class  Meta:
        model = Boite
        fields = '__all__'