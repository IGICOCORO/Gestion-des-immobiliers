from django.urls import path, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'authenticate'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('loyer/', include("loyer.urls")),
    path('', include('authenticate.urls')),# namespace='authenticate')),
    
]

urlpatterns += staticfiles_urlpatterns()
