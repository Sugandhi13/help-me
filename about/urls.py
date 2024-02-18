from . import views
from django.urls import path

urlpatterns = [
    path('view_profile/', views.view_profile, name='view_profile'),
    path('add_profile/', views.add_profile, name='add_profile'),
    path('contact/', views.contact, name='contact'),
    path('', views.about_me, name='about'),
]
