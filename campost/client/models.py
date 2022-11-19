from django.db import models

# Create your models here.
#class User(models.Model):
 #   name =  models.CharField(max_length=70)
 #  telephone =  models.CharField(max_length=100)
 #   email =  models.CharField(max_length=100)
 #   password =  models.CharField(max_length=100)
    
class Client(models.Model):
    nom = models.CharField(max_length=70)
    prenom = models.CharField(max_length=70)
    telephone = models.IntegerField(max_length=70)
    adresse = models.CharField(max_length=70)
    
    def __str__(self) -> str:
        return "{} {}".format(self.nom,self.prenom)
    
class Compte(models.Model):
    client = models.ForeignKey(Client, null=True,verbose_name=u"Proprietaire du compte", on_delete=models.SET_NULL)
    numero = models.IntegerField(max_length=11,verbose_name=u"Numero de compte")
    solde = models.FloatField(default=0,verbose_name=u"Solde initial du compte")
    jour = models.DateTimeField(null=True,verbose_name=u"Date de creation")
    
    def __str__(self) -> str:
        return "{}".format(self.numero)


   
   
     