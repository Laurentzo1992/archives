from django import forms
from paramettre.models import Archive_statuts, Archive_type, Document_type, Provenance
from django.core.validators import RegexValidator



class Archive_statutsForm(forms.ModelForm):
    
    libelle = forms.CharField(
        label='Libelle',
        widget=forms.TextInput(attrs={'placeholder': 'Libelle'})
    )
    
    class  Meta:
        model = Archive_statuts
        fields = '__all__'
        
        
        
class Archive_typeForm(forms.ModelForm):
    
    libelle = forms.CharField(
        label='Libelle',
        widget=forms.TextInput(attrs={'placeholder': 'Libelle'})
    )
    
    class  Meta:
        model = Archive_type
        fields = '__all__'
        
        
        
        
class Document_typeForm(forms.ModelForm):
    
    libelle = forms.CharField(
        label='Libelle',
        widget=forms.TextInput(attrs={'placeholder': 'Libelle'})
    )
    
    class  Meta:
        model = Document_type
        fields = '__all__'
        
        
        
        
class ProvenanceForm(forms.ModelForm):
    
    sigle = forms.CharField(
        label='Sigle',
        widget=forms.TextInput(attrs={'placeholder': 'Sigle'})
    )
    
    nom = forms.CharField(
        label='Nom',
        widget=forms.TextInput(attrs={'placeholder': 'Nom'})
    )
    
    class  Meta:
        model = Provenance
        fields = '__all__'
        

### FORM CONTRAT ###

""" class ClientForm(forms.ModelForm):
    

    nom = forms.CharField(
        label='Nom',
        widget=forms.TextInput(attrs={'placeholder': 'Nom du client'})
    )
    
    prenom = forms.CharField(
        label='Prenom',
        widget=forms.TextInput(attrs={'placeholder': 'Prenom du client'})
    )
    
    telephone = forms.CharField(
        label='telephone',
        widget=forms.TextInput(attrs={'placeholder': 'Telephone du client'})
    )
    
    
    avcar = forms.CharField(
        label='Carrure avant',
        widget=forms.TextInput(attrs={'placeholder': 'Carrure avant'})
    )
     
    arcar = forms.CharField(
        label='Carrure arrière',
        widget=forms.TextInput(attrs={'placeholder': 'Carrure arrière'})
    )


    class Meta:
        model = Client
        fields = '__all__'
        
         """
        

        
        
""" class TenueForm(forms.ModelForm):
    
    libelle = forms.CharField(
        label='Nom de la tenue',
        widget=forms.TextInput(attrs={'placeholder': 'Nom de la tenue'})
    )
    
    price = forms.FloatField(
        label='Prix',
        widget=forms.TextInput(attrs={'placeholder': 'Prix'})
    )
    
    class  Meta:
        model = Tenue
        fields = '__all__'
        



class ModelTenueForm(forms.ModelForm):
    
    libelle = forms.CharField(
        label='Model',
        widget=forms.TextInput(attrs={'placeholder': 'Model'})
    )
    
    class  Meta:
        model = ModelTenue
        fields = '__all__'
        


class PostForm(forms.ModelForm):
    
    libelle = forms.CharField(
        label='Post',
        widget=forms.TextInput(attrs={'placeholder': 'Post'})
    )
    
    class  Meta:
        model = Post
        fields = '__all__'
        
        
        
class CouturierForm(forms.ModelForm):
    
    class  Meta:
        model = Couturier
        fields = '__all__'
        
         """