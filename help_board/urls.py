from . import views
from django.urls import path

urlpatterns = [
    path('help_board/', views.QueryList.as_view(), name='home'),
]