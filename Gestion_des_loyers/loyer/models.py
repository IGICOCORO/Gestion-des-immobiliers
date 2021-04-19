from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Paiement(models.Model):
	montant_payé = models.CharField(max_length=40)

	
	def __str__(self):
		return  {self.montant_payé}

class Bureau(models.Model):
	num = models.PositiveIntegerField(default=1)
	prix = models.PositiveIntegerField()
	disponible = models.BooleanField()

	def __str__(self):
		return f'{self.num} {self.prix}'
class Immeuble(models.Model):
	address = models.CharField(max_length=40)
	bureau = models.OneToOneField(Bureau,on_delete=models.CASCADE)
	nbre_bureau = models.PositiveIntegerField()
	def __str__(self):
		return self.address


class Proprietaire(models.Model):
	user = models.OneToOneField(User,on_delete= models.CASCADE)
	immeuble = models.OneToOneField(Immeuble,on_delete= models.PROTECT)
	tel = models.PositiveIntegerField()


	def __str__(self):
		return f"{self.user.first_name} {self.user.last_name}"

class Locataire(models.Model):
	user = models.OneToOneField(User,on_delete= models.CASCADE)
	bureau = models.OneToOneField(Bureau,on_delete= models.CASCADE)
	tel = models.PositiveIntegerField()
	contrat = models.FileField()


	def __str__(self):
		return f"{self.user.first_name} {self.user.last_name}"


