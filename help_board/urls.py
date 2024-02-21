# Importing libraries required to build url patterns for views to work with html pages

from . import views
from django.urls import path

# url configuration for help_board app

urlpatterns = [
    path('', views.CategoryList.as_view(), name='home'),
    path('ask_query/', views.ask_query, name='ask_query'),
    path('<slug:slug>/', views.queries, name='queries'),
    path('<slug:slug>/queries', views.query_detail, name='query_detail'),
    path('<slug:slug>/edit_answer/<int:answer_id>', views.answer_edit, name='answer_edit'),
    path('<slug:slug>/delete_answer/<int:answer_id>', views.answer_delete, name='answer_delete'),
    path('<slug:slug>/delete_query/<int:query_id>', views.query_delete, name='query_delete'),
]