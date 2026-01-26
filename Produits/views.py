import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import models, formulaires, Controllers
from django.shortcuts import redirect, get_object_or_404
# Create your views here.
def produit(request):
    donnees = models.produits.objects.all()
    context = {
        'donnees': donnees,
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
