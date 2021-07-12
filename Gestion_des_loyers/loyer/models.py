from datetime import datetime
from django.utils import timezone
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

# Create your models here.
Months_year = ( 
				('Jan', 'January'),  
				('Feb', 'February'),   
				('Mar', 'March'),        
				('Apr', 'April'),    
				('May', 'May'),   
				('Jun', 'June'),       
				('Jul', 'July'),     
				('Aug', 'August'),  
				('Sep', 'September'),   
				('Oct', 'October'),    
				('Nov', 'November'), 
				('Dec', 'December')
			)  

niveau = (
			('1ere niveau', '1ere niveau'),
			('2eme niveau', '2eme niveau'),
			('3eme niveau', '3eme niveau'),
			('4eme niveau', '4eme niveau'),
	)



# def ca
class Immeuble(models.Model): 
	address = models.CharField(max_length=40)
	nbre_bureau = models.PositiveIntegerField()
	image = models.ImageField(upload_to='imeuble/')

# intrgrer le niveau de chaque bureau
	def __str__(self):
		return self.address

class Office(models.Model):
	
	immeuble = models.ForeignKey(Immeuble, on_delete=models.CASCADE)
	etage = models.CharField(max_length=20, choices = niveau)
	picture = models.ImageField(upload_to='bureau/')	
	num = models.PositiveIntegerField(default=1, unique = True)
	picture1 = models.ImageField(upload_to='bureau/')
	picture2 = models.ImageField(upload_to='bureau/')	
	Houseownerjoinedthesite = models.DateTimeField(default=datetime.now, blank=True)
	rent_amount  = models.PositiveIntegerField(default=0)
	bordereau = models.ImageField(upload_to='bordeau/')
	is_available = models.BooleanField(default = True)

	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.Houseownerjoinedthesite <= now
	
	

	def __str__(self):
		return f'{self.num}'


	# defne nbre_bureau_notif au nombre

	

class Locataire(models.Model):
	profile = models.OneToOneField(User, on_delete=models.CASCADE)
	phone = models.CharField(max_length=200)
	address = models.CharField(max_length = 200)
	contract = models.FileField(upload_to = 'contrat/')


	class Meta:

		ordering=('-profile',)


	def __str__(self):
		return f"{self.profile.first_name} {self.profile.last_name}"

class Calender(models.Model):
	locataire = models.ForeignKey(Locataire, on_delete=models.CASCADE)
	office = models.OneToOneField(Office, on_delete=models.CASCADE)
	start_rent_date = models.DateField('Agreement started', default=datetime.now,editable=True, blank=True)
	end_rent_date = models.DateField('Agreement Ended', default=datetime.now,editable=True, blank=True)
	deposit_by_renter = models.PositiveIntegerField(default=0, editable=True)
	pay_inadvance = models.BooleanField(default=False)
	amount_inadvance = models.PositiveIntegerField()
	Paid_for_mounths = MultiSelectField(choices=Months_year)

	def __str__(self):
		return f'{self.locataire.user.first_name} {self.locataire.user.last_name}'


	class Meta:
		ordering = ('-office',)
	# relation a payer entre le montant mensuel(deposit_by_renter) et l\'avance (amount_inadvance)

	def get_montant(self):
		pass

	# def notification(self):
	# 	if self.Paid_for_mounths.days -


# CMS acces au locateurs

# notification suivant les jrs restants par rapport au periode de location 5jrs