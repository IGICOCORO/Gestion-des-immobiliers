from django.urls import path
from loyer.views import *


urlpatterns = [
    path('', home, name='home')
]