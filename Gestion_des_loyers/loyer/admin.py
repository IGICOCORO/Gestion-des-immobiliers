from django.contrib import admin
from .models import *

@admin.register(Paiement)
class PaiementAdmin(admin.ModelAdmin):
	list_display = "montant_payé",
	list_filter = "montant_payé",
	search_field = "montant_payé", 
	ordering = "montant_payé", 

	select_related = True

@admin.register(Bureau)
class BureauAdmin(admin.ModelAdmin):
	list_display = "num", "prix"
	list_filter = "num", "prix"
	search_field = "num", "prix"
	ordering = "num", "prix"

@admin.register(Immeuble)
class ImmeubleAdmin(admin.ModelAdmin):
	list_display = "address", "bureau"
	list_filter = "address", "bureau",
	search_field = "address", "bureau"
	ordering = "address", "bureau"

	select_related = True

@admin.register(Proprietaire)
class ProprietaireAdmin(admin.ModelAdmin):
	list_display = "tel", "user"
	list_filter = "tel", "user"
	search_field = "tel", "user"
	ordering = "tel",

@admin.register(Locataire)
class LocataireAdmin(admin.ModelAdmin):
	list_display = "tel", "user"
	list_filter = "tel","user" 
	search_field = "tel", "user"
	ordering = "tel", 

	select_related = True