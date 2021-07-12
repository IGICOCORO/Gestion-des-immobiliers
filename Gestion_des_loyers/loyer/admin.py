from django.contrib import admin
from .models import *


class ImmeubleAdmin(admin.ModelAdmin):
    fields = ['etage', 'address', 'nbre_bureau']
admin.site.register(Immeuble, ImmeubleAdmin)

class OfficeAdmin(admin.ModelAdmin):
    pass

    # fields = ['num', 'picture', 'rent_amount', 'is_available', 'price']
admin.site.register(Office, OfficeAdmin)

class LocataireAdmin(admin.ModelAdmin):
    pass
    # fields = ['user', 'office', 'start_rent_date', 'end_rent_date', 'deposit_by_renter', 'pay_inadvance', 'amount_inadvance', 'Paid_for_mounths']
admin.site.register(Locataire, LocataireAdmin)
class CalenderAdmin(admin.ModelAdmin):
    pass
    # fields = ['user', 'office', 'start_rent_date', 'end_rent_date', 'deposit_by_renter', 'pay_inadvance', 'amount_inadvance', 'Paid_for_mounths']
admin.site.register(Calender, CalenderAdmin)
