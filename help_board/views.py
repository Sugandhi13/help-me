from django.shortcuts import render
from django.views import generic
from .models import Query

# Create your views here.


class QueryList(generic.ListView):
    queryset = Query.objects.all().order_by("created_on")
    template_name = "qna_board/index.html"
    paginate_by = 2
