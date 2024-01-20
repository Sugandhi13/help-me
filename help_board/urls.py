from . import views
from django.urls import path

urlpatterns = [
    path('', views.QueryList.as_view(), name='home'),
]