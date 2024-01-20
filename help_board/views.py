from django.shortcuts import render
from django.views import generic
from .models import Query

# Create your views here.


class QueryList(generic.ListView):
    queryset = Query.objects.filter(status=1).order_by("created_on")
    template_name = "qna_list.html"
