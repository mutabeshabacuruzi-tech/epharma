import django_filters
from . import models

class Filter_Produit(django_filters.FilterSet):
    class Meta:
        model = models.produits
        fields = "__all__"

class Filter_Categorie(django_filters.FilterSet):
    class Meta:
        model = models.Categories
        fields = "__all__"