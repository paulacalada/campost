from django.core import validators
from django import forms
#from .models import User
from .models import Client,Compte

#class ClientRegistration(forms.ModelForm):
 #   class Meta:
  #      model = User
   #     fields = ['name', 'telephone', 'email', 'password']
    #    widgets = {
    #       'name': forms.TextInput(attrs={'class': 'form-control'}),
    #        'telephone': forms.TextInput(attrs={'class': 'form-control'}),
    #       'email': forms.EmailInput(attrs={'class': 'form-control'}),
    #       'password': forms.PasswordInput(attrs={'class': 'form-control'}),
    #    }

class ClientStore(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['nom', 'prenom', 'adresse', 'telephone']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'adresse': forms.TextInput(attrs={'class': 'form-control','placeholder':'Adresse physique du client'}),
        }    
        
class CompteGestion(forms.ModelForm):
    class Meta:
        model = Compte
        fields = ['numero', 'client', 'solde', 'jour']
        widgets = {
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'client': forms.Select(attrs={'class': 'form-control'}),
            'solde': forms.FloatField(),
            'jour': forms.DateField(),
        }
        
            