import datetime
from django.urls import path
from .import Controllers
from . import views
urlpatterns = [
    path('', views.seConnecter, name='connect'),
    path('ac', views.home, name='acc'),
    path('controllerConnection', Controllers.LoginController, name='connectController'),
    path('MonCompte', views.creerCompte, name='compte'),
    path('controllerCompte', Controllers.CompteController, name='nouveau compte'),
    path('aproposs', views.aProposDenous, name='apropos'),
    path('produit', views.produit, name='produit'),
    path('ajouter_le_produit', views.ajouter_un_produit, name='viewAjoutProduit'),
    path('modifierProduit/<Produits>', views.modifierProduit, name='viewModifierProduit'),
    path('controllerAjoutProduit', Controllers.AjoutProduit_controller, name='ControllerAjoutProduit'),
    path('controllerModifierProduit/<Produits>', Controllers.ModifierProduit_controller, name='ControllerModifierProduit'),
    path('controllerSupprimer/<Produits>', Controllers.EffacerProduit_controller, name='supprimerProduit'),
    path('ajouterCateg', views.ajouterCategorie, name=' ajouterCat'),
    path('modifierCategorie/<categories>', views.modifierCategorie, name='modifier'),
    path('AjouterCategorie', Controllers.AjoutCategorie_controller, name='mod22 ajouter'),
    path('EffacerCategorie/<categorie>', Controllers.EffacerCategorie_controller, name='supprimer'),
    path('ModifierCategorie/<categories>', Controllers.ModifierCatedorie_Controller, name='modifierCatego'),
    path('ajoutVente', views.venteProduit, name='venteVue'),
    path('controllerAjoutVente', Controllers.VenteController, name='venteController'),
    path('EffacerVente/<vente>', Controllers.EffacerVente_controller, name='supprimerVente'),
    path('approvisionner2/<id>', views.approvisionnerProduit2, name='approvisionner2'),
    path('approvi2/<id>', Controllers.approviController2, name='approvisionnement2'),
    path('facture1/<id>', views.showFacture1, name='facture1'),
    path('facture2/<id>', Controllers.showFacture2, name='show2'),












    # path('recherche', views.recherche, name='recherche'),
    # path('rechercheProduitController', Controllers.rechercheProduit_controller, name= 'recherchePcontroller'),

























]
