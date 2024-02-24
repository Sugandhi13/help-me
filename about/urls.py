# Importing libraries required to build url patterns

from django.urls import path
from . import views

# url configuration for about app

urlpatterns = [
    path('view_profile/', views.view_profile, name='view_profile'),
    path('add_profile/', views.add_profile, name='add_profile'),
    path('contact/', views.contact, name='contact'),
    path('', views.about_me, name='about'),
]
