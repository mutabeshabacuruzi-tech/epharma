import datetime, django_filters
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import models, formulaires, Controllers, filters, modules_externes
from django.shortcuts import redirect, get_object_or_404
from django.core.paginator import Paginator

# Create your views here.

@modules_externes.verification_de_session()
def produit(request):
    user = request.session['user']
    produits = models.produits.objects.all().order_by('name')
    categories = models.Categories.objects.all().order_by('name')

    filter_produits = filters.Filter_Produit(request.GET, queryset=produits)
    filter_categories = filters.Filter_Categorie(request.GET, queryset=categories)

    result_produits = filter_produits.qs
    result_categories = filter_categories.qs

    paginator_produit = Paginator(result_produits, 6)
    paginator_categories = Paginator(result_categories, 6)

    page_number_produit = request.GET.get('page_produits')
    page_number_categories = request.GET.get('page_categories')

    page_obj_produit = paginator_produit.get_page(page_number_produit)
    page_obj_categories = paginator_categories.get_page(page_number_categories)

    form_produit = []
    form_categorie = []

    for produit in page_obj_produit:
        form = formulaires.Ajouter_Un_Produit(instance=produit)
        form_produit.append((produit.id, form ))
    for categorie in page_obj_categories:
        form = formulaires.Ajouter_Categorie(instance=categorie)
        form_categorie.append((categorie.id, form, len(models.produits.objects.filter(categories=categorie.id)) ))
    
    context = {
        'user': user,
        'produits': page_obj_produit,
        'categories': page_obj_categories,

        'nbr_produits': len(models.produits.objects.all()),
        'nbr_categorie': len(models.Categories.objects.all()),

        'form_modifier_produits': form_produit,
        'form_modifier_categorie': form_categorie,

        'form_ajouter_produit': formulaires.Ajouter_Un_Produit,
        'form_ajouter_categorie': formulaires.Ajouter_Categorie,
    }
    return render(request, 'produitcontenu.html', context)

def home(request):
    return render(request, 'home.html')
def ajouter_un_produit(request):
    context = {
        'form': formulaires.Ajouter_Un_Produit()
    }
    return render(request, 'templates/ajouter_un_produit.html', context=context)
def ajouterCategorie(request):
    catergorie = models.Categories.objects.all()
    context = {
        'form': formulaires.Ajouter_Categorie,
        'categories': catergorie,
    }
    return render(request, 'templates/ajouterCategorie.html', context=context)
def modifierProduit(request, Produits):
    produit = models.produits.objects.get(id=Produits)
    form = formulaires.Ajouter_Un_Produit(instance=produit)
    context = {
        'form': form,
        'produit': produit,
    }
    return render(request, 'templates/modifierUnProduit.html', context=context)
def modifierCategorie(request, categories):
    categories = models.Categories.objects.get(id=categories)
    form = formulaires.Ajouter_Categorie(instance=categories)
    context = {
        'form': form,
        'Categorie': categories,
    }
    return render(request, 'templates/modifierCategorie.html', context=context)
def approvisionnerProduit2(request, id):
    produit = models.produits.objects.get(id=id)
    form = formulaires.ApproForm()
    context = {
        'form': form,
        'produit': produit,
    }
    return render(request, 'templates/approvisionner.html', context=context)
def venteProduit(request):
    ventes = models.produitVente.objects.all()
    form = formulaires.Vente
    context = {
        'ventes': ventes,
        'form': form,
    }
    return render(request, 'templates/vente_produit.html', context=context)
def showFacture1(request, id):
    sale = models.produitVente.objects.get(id=id)
    form = formulaires.Facture()
    context = {
        'sale': sale,
        'form': form,
    }
    return render(request, 'templates/facture.html', context=context)
def voirClients(request):
    clients = models.customer.objects.all()
    context = {
        'clients': clients,
    }
    return render(request, 'templates/listeClients.html', context=context)





def seConnecter(request):
    form = formulaires.ConnectForm()
    context = {
        'form': form,
    }
    return render(request, 'templates/pageConnexion.html', context=context)

def aProposDenous(request):
    return render(request, 'templates/aPropo.html')
def creerCompte(request):
    form = formulaires.compteForm()
    context = {
        'form': form,
    }
    return render(request, 'templates/comptes.html', context=context)
