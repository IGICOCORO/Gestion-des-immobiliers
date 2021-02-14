from django.urls import path
from loyer.views import *
from django.views.generic.base import TemplateView 


urlpatterns = [
    path('', TemplateView.as_view(template_name='loyer/login.html'), name='login'),
]	