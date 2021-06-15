from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class OfficeForm(forms.ModelForm):
	class Meta:
		model = Office
		fields = ('immeuble','num', 'picture','picture1','picture2', 'rent_amount','bordereaU','is_available')
		


class LocataireForm(forms.ModelForm):
	class Meta:
		model = Locataire
		fields = ('first_name','last_name', 'phone', 'address','contract')
		


class CalenderForm(forms.ModelForm):
	class Meta:
		model = Calender
		fields = ('locataire','office', 'pay_inadvance','amount_inadvance', 'Paid_for_mounths')
		



