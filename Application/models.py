from django.db import models
class Categories(models.Model):
    name = models.CharField(max_length=250, unique=True, primary_key=False)
    def __str__(self):
        return self.name
class produits(models.Model):
    name = models.CharField(max_length=100, unique=True, primary_key=False)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantite = models.PositiveIntegerField(default=0)
    description = models.TextField()
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_expiration = models.DateField()
    def __str__(self):
        return self.name
class Meta:
    ordering = ['-date_ajout']

class customer(models.Model):
    name = models.CharField(max_length=100)
    adresse = models.CharField(default='none', max_length=100)
    def __str__(self):
        return self.name
class produitVente(models.Model):
        produit = models.ForeignKey(produits, on_delete=models.CASCADE)
        sale_Date = models.DateTimeField(auto_now_add=True)
        quantite = models.PositiveIntegerField()
        customer = models.CharField(max_length=100)
        total_amount = models.DecimalField(max_digits=10, decimal_places=2)
        def __str__(self):
            return self.produit
# class approvisionnement(models.Model):
#     produit = models.ForeignKey(produits, on_delete=models.CASCADE)
#     quantite = models.PositiveIntegerField()
#     def __str__(self):
#         return self.produit
# class Meta:
#     ordering = ['sale_date']

class login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=10)
    def __str__(self):
         return 'le username est{}'.format(self.username)
class compteUtilisateur(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=10)
    password_confirm = models.CharField(max_length=10)
    def __str__(self):
         return "utilisateur : {} username : {} email: {} password ".format(self.username, self.email, self.password)



# class Facture(models.Model):
#     client = models.ForeignKey(customer, on_delete=models.CASCADE)
#     date_facture = models.DateTimeField(auto_now_add=True)
#     ventes = models.ManyToManyField(produitVente, related_name="factures")
#     total = models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
#
# def calculer_total(self):
#         total = sum(
#             vente.quantite * vente.prix_unitaire
#             for vente in self.ventes.all()
#         )
#         self.total = total
#         self.save()
#
# def str(self):
#         return f"Facture #{self.id} pour {self.client.nom}"
#

