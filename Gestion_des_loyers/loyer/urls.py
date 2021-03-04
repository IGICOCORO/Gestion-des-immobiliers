from django.urls import path
from . import views

urlpatterns = [
    path('',views.login, name="login"),
    path('home/',views.home, name='home'),
    path('office/',views.office, name='office'),
    path('tenant/',views.tenant, name='tenant'),
    path('calendar/',views.calendar, name='calendar')
]	