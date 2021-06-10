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



class Proprietaire(models.Model):
	user = models.OneToOneField(User,on_delete= models.CASCADE, related_name = 'proprietaires')
	tel = models.PositiveIntegerField()
	address = models.CharField(max_length=200)
	
	def __str__(self):
		return f"{self.user.first_name} {self.user.last_name}"

class Immeuble(models.Model):
	Proprietaire = models.ForeignKey(Proprietaire, on_delete= models.PROTECT)
	address = models.CharField(max_length=40)
	nbre_bureau = models.PositiveIntegerField()
	image = models.ImageField(upload_to='imeuble/')


	def __str__(self):
		return self.Proprietaire.user.username

class Office(models.Model):
	immeuble = models.ForeignKey(Immeuble, on_delete=models.CASCADE)
	num = models.PositiveIntegerField(default=1)
	picture = models.ImageField(upload_to='bureau/')	
	picture1 = models.ImageField(upload_to='bureau/')
	picture2 = models.ImageField(upload_to='bureau/')	
	Houseownerjoinedthesite = models.DateTimeField(default=datetime.now,editable=True, blank=True)
	rent_amount  = models.PositiveIntegerField(default=0)
	is_available = models.BooleanField(default = False)

	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.Houseownerjoinedthesite <= now
	
	

	def __str__(self):
		return f'{self.num}'

	

class Locataire(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	phone = models.CharField(max_length=200)
	address = models.CharField(max_length = 200)

	def __str__(self):
		return f"{self.first_name} {self.last_name}"

class Calender(models.Model):
	locataire = models.ForeignKey(Locataire, on_delete=models.CASCADE)
	office = models.ForeignKey(Office, on_delete=models.CASCADE)
	start_rent_date = models.DateField('Agreement started', default=datetime.now,editable=True, blank=True)
	end_rent_date = models.DateField('Agreement Ended', default=datetime.now,editable=True, blank=True)
	deposit_by_renter = models.PositiveIntegerField(default=0, editable=True)
	pay_inadvance = models.BooleanField()
	amount_inadvance = models.PositiveIntegerField()
	Paid_for_mounths = MultiSelectField(choices=Months_year)

	def __str__(self):
		return f'{self.locataire.first_name} {self.locataire.last_name}'
