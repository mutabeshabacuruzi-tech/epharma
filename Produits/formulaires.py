from django import forms
from  django.forms import widgets
from . import models
from django.contrib.auth.forms import AuthenticationForm
class Ajouter_Un_Produit(forms.ModelForm):
    class Meta:
        model = models.produits
        fields = "__all__"
        widgets = {
            'date_expiration': widgets.Input(attrs={
                'type': 'date',
                'class': 'form-control form-control-sm'
            }),
            'name': widgets.Input(
                attrs={
                    'class': 'form-control form-control-sm',
                }
            ),
            'description': widgets.Textarea(
                attrs={
                    'rows': 2,
                }
            )
        }

class Ajouter_Categorie(forms.ModelForm):
    class Meta:
        model = models.Categories
        fields = "__all__"
class Vente(forms.ModelForm):
    class Meta:
        model = models.produitVente
        fields = "__all__"
        exclude = ["total_amount"]
class ApproForm(forms.ModelForm):
    class Meta:
        model = models.produits
        fields = ['quantite']
class Facture(forms.ModelForm):
    class Meta:
        model = models.produitVente
        fields = '__all__'

class SearchForm(forms.Form):
    query = forms.CharField(
        label='', max_length=100, required=False,
        widget=forms.TextInput(attrs={'placeholder': 'rechercher un produit', 'class': 'form-control'})
    )
class ConnectForm(forms.ModelForm):
    class Meta:
        model = models.login
        fields = '__all__'
class compteForm(forms.ModelForm):
    class Meta:
        model = models.compteUtilisateur
        fields= '__all__'

#


