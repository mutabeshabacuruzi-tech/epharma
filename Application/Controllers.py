import re
from .views import *
from . import models, views
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate
from django.contrib.auth.validators import validators
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db.models import Q
def AjoutProduit_controller(request):
    if request.method == 'POST':
        le_formulaire = formulaires.Ajouter_Un_Produit(data=request.POST)
        if le_formulaire.is_valid():
            le_formulaire.save()
            return redirect('produit')
        else:
            return HttpResponse(le_formulaire.errors)
    else:
        return redirect(home)
def AjoutCategorie_controller(request):
        if request.method == 'POST':
            le_formulaire = formulaires.Ajouter_Categorie(data=request.POST)
            if le_formulaire.is_valid():
                le_formulaire.save()
                messages.success(request, "La categorie {} a ete ajoutee".format(request.POST['name']))
                return redirect(request.META['HTTP_REFERER'])
            else:
                return HttpResponse(le_formulaire.errors)
        else:
            return redirect(home)
def EffacerProduit_controller(request, Produits):
    produit = models.produits.objects.get(id=Produits)
    produit.delete()
    # produit = get_object_or_404(models.produits, id=Produits)
    # produit.delete()
    messages.success(request, "La produit {} a ete supprimee".format(produit.name))
    return redirect(request.META['HTTP_REFERER'])
def EffacerCategorie_controller(request, categorie):
    categorie = models.Categories.objects.get(id=categorie)
    categorie.delete()
    messages.success(request, "La categorie {} a ete supprimee".format(categorie.name))
    return redirect(request.META['HTTP_REFERER'])
def EffacerVente_controller(request, vente):
    models.produitVente.objects.get(id=vente).delete()
    return redirect(venteProduit)
def ModifierProduit_controller(request, Produits):
    if request.method == 'POST':
        produit = models.produits.objects.get(id=Produits)
        form = formulaires.Ajouter_Un_Produit(data=request.POST, instance=produit)
        if form.is_valid():
            form.save()
            return redirect('produit')
        else:
            return HttpResponse(form.errors)
    else:
        return redirect(home)
def approviController2(request,id):
    if request.method == 'POST':
        produit = get_object_or_404(models.produits, id=id)
        form = formulaires.ApproForm(data=request.POST)
        if form.is_valid():
            quantite = form.cleaned_data['quantite']
        if produit.quantite < 0:
             form.add_error('quantite', 'quantite insuffisante.')
        else:
             produit.quantite += quantite
             models.produits.save(self=produit)
        return redirect('produit')
def showFacture2(request, id):
    if request.method == 'POST':
        sale = get_object_or_404(models.produitVente, id=id)
        form = formulaires.Facture(data=request.POST)
        if form.is_valid():
            quantite = form.cleaned_data['quantite']
        if produit.quantite < 0:
            form.add_error('quantite', 'quantite insuffisante.')
        else:
            produit.quantite += quantite
            models.produitVente.save(self=sale)
        return redirect(venteProduit)

# def creerFacture(request):
#     if request.method == 'POST':
#         factureF = formulaires.factureForm(request.POST)
#         elemetFactureF=formulaires.elementFactureForm(request.POST, request.FILES)
#         if factureF.is_valid()and elemetFactureF.is_valid():
#             facture=factureF.save()

def ModifierCatedorie_Controller(request, categories):
    if request.method == 'POST':
        categories = models.Categories.objects.get(id=categories)
        form = formulaires.Ajouter_Categorie(data=request.POST, instance=categories)
        if form.is_valid():
            form.save()
            return redirect(ajouterCategorie)
        else:
            return HttpResponse(form.errors)
    else:
        return redirect(home)
def VenteController(request):
    if request.method == 'POST':
        produit = get_object_or_404(models.produits, id=request.POST['produit'])
        form = formulaires.Vente(data=request.POST)
        if form.is_valid():
            quantite = form.cleaned_data['quantite']
            customer = request.POST.get('customer')
            if quantite >=produit.quantite+5:
                form.add_error('quantite', 'Quantité demandée supérieure au stock disponible.')
            else:
                total_amount = quantite * produit.price
                vente = models.produitVente(
                    produit=produit,
                    customer=customer,
                    quantite=quantite,
                    total_amount=total_amount,
                )
                vente.save()
                produit.quantite -= quantite
                models.produits.save(self=produit)
            return redirect(venteProduit)
def LoginController(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        utilisateur = authenticate(request, username=username, password=password)
        if utilisateur is not None:
            login(request, utilisateur)
            # comme le login est correcte a ce niveau, il vaut mieux creer une variable de session
            # afin d'identifier a tout moment qui vient de se connection
            request.session['user'] = utilisateur.username
            return redirect('acc')
        else:
            messages.error(request, 'nom utilisateur incorect ou mot de passe incorect.')
            return redirect(seConnecter)
    else:
        messages.error(request, 'attention vous avez pas de compte')
        return redirect(seConnecter)
def CompteController(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
#verification de la confirmation du mot de passe
        if password != password_confirm:
            messages.error(request, 'les mots de passe ne sont pa identiques')
            return redirect(creerCompte)
#verification de la longueur et des caracteres du mot de passe
        if len(password) < 8 or not re.search(r'[A-za-z]', password) or not re.search(r'\d', password) or not re.search(r'[!@$%(){}'',.?:<>|]', password):
            messages.error(request, ' le mot de passe doit contenir plus de 8 chiffres des lettres chiffres et caracteres.')
            return redirect(creerCompte)
#verification du format de l'adresse mail
        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, 'adresse mail invalide')
            return redirect(creerCompte)
#verification de l'existance de l'utilisateur
        if User.objects.filter(username=username).exists():
            messages.error('cet utilisateur existe deja')
            return redirect(creerCompte)
        if User.objects.filter(email=email).exists():
            messages.error('ce mail existe deja')
            return redirect(creerCompte)
        if User.objects.filter(password=password).exists():
            messages.error('ce mot de passe existe deja')
            return redirect(creerCompte)
#creation de l'utiliateur
        User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, 'utilisateur creee avec succes')
        return redirect(seConnecter)


#Calvin AWA MUSAFIRI
def logoutControler(request):
    try:
        del request.session['user']
    except Exception:
        messages.error(request, "Une erreur s'est produite ")
    finally:
        return redirect(views.seConnecter)












