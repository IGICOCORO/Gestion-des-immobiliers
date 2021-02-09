from django.db import models

# Create your models here.
class Bureau(models.Model):
	number_bureau = models.PositiveIntegerField()


	def __str__(self):
		return self.number_bureau

