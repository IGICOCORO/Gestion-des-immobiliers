from django import forms
from .models import *





class OfficeForm(forms.ModelForm):
	class Meta:
		model = Office
		fields = ('immeuble','etage','num', 'picture','picture1','picture2', 'rent_amount','bordereau','is_available')
		


class LocataireForm(forms.ModelForm):
	class Meta:
		model = Locataire
		fields = ('user','phone', 'address','contract')
		


class CalenderForm(forms.ModelForm):
	class Meta:
		model = Calender
		fields = ('locataire','office', 'pay_inadvance','amount_inadvance', 'Paid_for_mounths')
		



