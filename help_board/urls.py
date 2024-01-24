from . import views
from django.urls import path

urlpatterns = [
    path('', views.QueryList.as_view(), name='home'),
    path('<slug:slug>/', views.query_detail, name='query_detail'),
]