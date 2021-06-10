from django.urls import path
from . import views

urlpatterns = [
    path("register", views.register_request, name="register"),
    path("", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),

    # path('',views.login, name="login"),
    path('home/',views.home, name='home'),
    path('office/',views.office, name='office'),
    path('tenant/',views.tenant, name='tenant'),
    path('calendar/',views.calendar, name='calendar'),

    path('new', views.office_create, name='office_new'),
    path('add', views.tenant_create, name='tenant_new'),
    path('create', views.calender_create, name='calender_new'),

    path('view/<int:id>', views.office_update,name='office_detail'), 
    path('edit_office/<int:id>', views.office_update,name='edit_office'), 
    path('delete_office/<int:id>', views.office_destroy,name='delete_office'),
    
    path('edit/<int:id>', views.calender_update,name='edit_calender'), 
    path('delete/<int:id>', views.calender_destroy,name='delete_calender'),
    
    path('edit_tenant/<int:id>', views.tenant_update,name='edit_tenant'), 
    path('delete_tenant/<int:id>', views.tenant_destroy,name='delete_tenant'),
]